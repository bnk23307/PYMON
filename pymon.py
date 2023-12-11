#!/usr/bin/python3
from multiprocessing import Process
import subprocess
import os,signal
import sys
import time


glob = ''
f_name = sys.argv[1]
procs = []
pipes = []

def tt():
    subprocess.run(['python3',f_name])

def Quit():
    inp = input("")
    if(inp=="q" or inp=="quit" or inp == "exit"):
        for _ in  pipes:
            _.kill()

def main():
    run = 1
    while True:
        if run==1:
            with open(f_name,'r') as infile:
                data = infile.read()
                glob = data
                infile.close()
            run+=1
            pipe = subprocess.Popen(['python3',f_name])
            pipes.append(pipe)
        else:
            try:
                with open(f_name,'r') as inf:
                    text = inf.read()
                    if(text!=glob):
                        if len(pipes)>0:
                            for p in pipes:
                                p.kill()
                                pipes.remove(p)
                        pipe = subprocess.Popen(['python3',f_name])
                        pipes.append(pipe)
                        glob = text
                    inf.close()
            except:
                pass

if __name__ == '__main__':
    main_proc = Process(target=main,args=())
    main_proc.start()
