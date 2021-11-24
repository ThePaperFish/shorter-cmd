import os, signal
from subprocess import Popen, PIPE
import yaml

def get_config():
    with open('config.yaml', 'r') as fid:
        return yaml.safe_load(fid)

def run_process(cmd, gpus=None, wait=True):
    if gpus != None:
        gpu_env = {"CUDA_VISIBLE_DEVICES": gpus}
        proc = Popen(cmd, stdout=PIPE, env=dict(os.environ, **gpu_env))
    else:
        proc = Popen(cmd, stdout=PIPE)

    if not wait:
        return proc
        
    flush_me = []
    for line in iter(proc.stdout.readline, b''):
        line = line.decode('utf-8')
        flush_me.append(line)
        print(line, end='')
    
    return ''.join(flush_me)

def kill_process(pid):
    os.kill(pid, signal.SIGSTOP)