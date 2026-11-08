#!/usr/bin/env python3
"""Fixed twelve-state experiment transport. Models/ranking/evaluation are native.
No optimizer or host inference. Defective cases intentionally produce Test FAIL.
"""
import argparse, hashlib, json, os, subprocess, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
COMMON=Path(subprocess.check_output(['git','rev-parse','--path-format=absolute','--git-common-dir'],cwd=ROOT,text=True).strip())
FAMILY=COMMON.parent.parent
BIN=FAMILY/'mncs-language/target/debug/mncs'
OUT=ROOT/'outputs/first-guidance'
EXP=ROOT/'experiments/first_guidance'
ENV=dict(os.environ, MNCS_NATIVE_APPLICATION_CACHE_DIR=str(COMMON/'mncs-native-application-cache'/hashlib.sha256(str(BIN.resolve()).encode()).hexdigest()[:16]))
LIBS=['--library','src','--library','experiments/first_guidance','--library',str(FAMILY/'mncs-test/native'),'--library',str(FAMILY/'mncs-language/library')]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def save(name,value):
 p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,indent=2)+'\n');return p
def decode(v):
 if 'record' in v:return {k:decode(x) for k,x in v['record']['fields']}
 if 'sequence' in v:return [decode(x) for x in v['sequence']['values']]
 if 'finite' in v:return v['finite']['variant_identity'].split('::')[-1]
 for k in ['integer','boolean']: 
  if k in v:return v[k]['value']
 raise ValueError(v)
def n(x):return {'integer':{'value':x}}
def b(x):return {'boolean':{'value':x}}
def seq(x):return {'sequence':{'values':x}}
def rec(**x):return {'record':{'fields':x}}
def enum(x):return {'finite':{'variant':x}}
def host(v):
 if 'record' in v:return rec(**{k:host(x) for k,x in v['record']['fields']})
 if 'sequence' in v:return seq([host(x) for x in v['sequence']['values']])
 if 'finite' in v:return enum(v['finite']['variant_identity'].split('::')[-1])
 for k in ['integer','boolean']:
  if k in v:return {k:{'value':v[k]['value']}}
 raise ValueError(v)
def call(function,args,label,module='guidance'):
 if (OUT/(label+'.json')).exists():raise SystemExit('Preserve existing result: '+label)
 path=save(label+'.args.json',args);result=OUT/(label+'.json')
 command=[str(BIN),'call',str(EXP/(module+'.mncs')),'--module','study.'+module,'--function',function,'--args',str(path),*LIBS,'--step-budget','3000000','--result',str(result)]
 start=time.time_ns()//1000000;t=time.monotonic();p=subprocess.run(command,cwd=ROOT,env=ENV,capture_output=True,text=True,timeout=180)
 if p.returncode or not result.exists():raise SystemExit(p.stdout+p.stderr)
 d=load(result)
 if d.get('status')!='returned' or d['call']['status']!='returned':raise SystemExit(str(d))
 save(label+'-cost.json',{'command':command,'started_at':start,'finished_at':time.time_ns()//1000000,'wall_seconds':time.monotonic()-t,'vm_steps':d['call']['steps'],'argument_sha256':sha(path),'result_sha256':sha(result)})
 return d['call']['returned'][0]
def test(label,part,selector=None):
 p=OUT/(label+'.json')
 if not p.exists():
  command=[str(BIN),'test',str(EXP/(part+'_tests.mncs')),*LIBS,'--step-budget','3000000','--format','text','--result',str(p)]
  if selector:command+=['--filter',selector]
  start=time.time_ns()//1000000;t=time.monotonic();r=subprocess.run(command,cwd=ROOT,env=ENV,capture_output=True,text=True,timeout=180)
  (OUT/(label+'.log')).write_text(r.stdout+r.stderr)
  if not p.exists():raise SystemExit(r.stdout+r.stderr)
  save(label+'-execution.json',{'started_at':start,'finished_at':time.time_ns()//1000000,'wall_seconds':time.monotonic()-t,'exit_code':r.returncode,'command':command})
 d=load(p)
 if not d['execution']['canonical_path'] or d['execution']['fallback']:raise SystemExit('Noncanonical execution')
 for k in ['compile_failures','runtime_failures','setup_failures','timeout_failures','infrastructure_failures','unsupported','skipped']:
  if d['native_suite_summary'][k]:raise SystemExit('Not an assertion outcome: '+k)
 return d

REGIONS={'net':'Net','surcharge':'Surcharge','cap_condition':'CapCondition','urgent_condition':'UrgentCondition','floor_body':'FloorBody','cap_body':'CapBody','floor_condition':'FloorCondition','new_branch':'NewBranch'}
def feature_rows(region,traces,history):
 # Only ABI encoding remains here; the fixed source-owner projection is native.
 label='projection-'+region+'-'+'-'.join(map(str,history))
 p=decode(call('project',[enum(REGIONS[region]),seq([n(x) for x in history])],label,'reference'))
 return [x['values'][:4] for x in p['signals']]

def main():
 global OUT
 parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['develop']);parser.add_argument('--output-root',default='outputs/first-guidance');args=parser.parse_args();OUT=ROOT/args.output_root;OUT.mkdir(parents=True,exist_ok=True)
 if (OUT/'development.json').exists():raise SystemExit('Development already recorded')
 reference=test('reference','reference')
 if reference['summary']['passed'] != 3:raise SystemExit('Clean reference must pass all three probes')
 traces=decode(call('traces',[],'reference-traces','reference'))
 protocol=load(EXP/'protocol.json');history=[0,0,0];groups=[]
 for c in protocol['cases']:
  if c['partition']!='development':continue
  x=feature_rows(c['changed_region'],traces,history)
  d=test(c['id'],'development',c['id']+'_')
  tests=sorted(d['tests'],key=lambda t:t['entry']);assert len(tests)==3;verdicts=[t['native_result']['verdict'] for t in tests]
  groups.append({'id':c['id'],'features':x,'history_before':list(history),'verdicts':verdicts,'native_ids':[t['id'] for t in tests],'costs':[t['execution']['steps'] for t in tests],'result_sha256':sha(OUT/(c['id']+'.json'))})
  for i,v in enumerate(verdicts):history[i]+=int(v=='FAIL')
  print(c['id'],verdicts,flush=True)
 save('development.json',{'groups':groups,'history_after':history,'reference_traces':traces,'chronology_limit':'First two pilot features are retrospective development reconstruction from the immutable clean reference; they are not historical decision-time captures. Subsequent/final feature snapshots precede their target executions.','observed_at':time.time_ns()//1000000})
if __name__=='__main__':main()
