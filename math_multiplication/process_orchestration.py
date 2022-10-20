from multiprocessing.connection import wait
import os
import time
import subprocess

class ProcessOrchestration:
    def kill_processes(self, name):
        os.system(f"taskkill /f /im {name}")
    
    def start_processes(self, name):
        # os.system(f"{name}")
        subprocess.call(f"start {name}", shell=True)

if __name__ == "__main__":
    proc_name = "taskmgr.exe"
    ProcessOrchestration().start_processes(proc_name)
    time.sleep(2)
    ProcessOrchestration().kill_processes(proc_name)