import os
from proc_killer import *
import multi
import datetime
import time
CURRENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(CURRENT_DIR, "results.txt"), "a", encoding="utf-8") as wf:
    wf.write(f"[{datetime.datetime.now()}] ===============Старт=============\n")
    wf.close()

def read_data_file():
    rd = open(os.path.join(CURRENT_DIR, "config.json"), "r")
    read_conf = json.loads(rd.read())
    rd.close()
    return read_conf

def modify_data_file(write_key):
    rd = read_data_file()
    rd["kill_processes"] = write_key
    wd = open(os.path.join(CURRENT_DIR, "config.json"), "w")
    wd.write(json.dumps(rd, indent=4))
    wd.close()
    pass


READ_CONFIG = read_data_file()
if READ_CONFIG["orchestrate_processes"]:
    modify_data_file(True)
    orchestrate_process()
EXAMPLES_COUNT = READ_CONFIG["examples_count"]
print(f"Привет Димон! Для того чтобы поиграть в компьютер тебе надо решить {EXAMPLES_COUNT} примеров, погнали!")
i = 1
fails = 0
successed = 0
while i <= EXAMPLES_COUNT:
    print(f"Пример {i} из {EXAMPLES_COUNT}")
    if i % 2 == 0:
        check_res = multi.MathematicalExamples().multiplication()
    else:
        check_res = multi.MathematicalExamples().division()
    if check_res:
        successed += 1
    else:
        fails += 1
    i += 1
print(f"\nВсего было дано {successed} правильных и {fails} неправильных ответов.")
with open(os.path.join(CURRENT_DIR, "results.txt"), "a", encoding="utf-8") as wf:
    wf.write(f"[{datetime.datetime.now()}] решено примеров {EXAMPLES_COUNT}, правильно {successed}, неправильно {fails}\n")
    wf.write(f"[{datetime.datetime.now()}] ===============Конец=============\n")
    wf.close()
if READ_CONFIG["orchestrate_processes"]:
    modify_data_file(False)
time.sleep(5)
