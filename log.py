# pylint: disable=all
from datetime import datetime

lf = None
lf_suppress = False

def setup(lfile):
    global lf
    with open(lfile, 'w') as f:
        f.write('')
    lf = lfile
    

def log(msg, type=None):
    global lf
        
    current_time = datetime.now()
    time = current_time.strftime("%d/%m/%Y %H:%M:%S") + f".{current_time.microsecond // 1000}"
    
    if lf is None and lf_suppress == False: 
        print(f"\033[35m[{time}] FATAL: No log file specified \033[0m")
         
  
    if type == 0:
        print(f"[{time}]: {msg}")
        if lf is not None:
            with open(lf, "a") as file:
                file.write(f"\n[{time}]: {msg}")
        
    if type == 1:
        print(f"\033[32m[{time}] SUCCESS: {msg} \033[0m")
        if lf is not None:
            with open(lf, "a") as file:
                file.write(f"\n[{time}] SUCCESS: {msg}")
            
            
    if type == 2:
        print(f"\033[33m[{time}] WARNING: {msg} \033[0m")
        if lf is not None:
            with open(lf, "a") as file:
                file.write(f"\n[{time}] WARNING: {msg}")
 
    if type == 3:
        print(f"\033[31m[{time}] ERROR: {msg} \033[0m")
        if lf is not None:
            with open(lf, "a") as file:
                file.write(f"\n[{time}] ERROR: {msg}")
        
    if type == 4:
        print(f"\033[35m[{time}] FATAL: {msg} \033[0m")
        if lf is not None:
            with open(lf, "a") as file:
                file.write(f"\n[{time}] FATAL: {msg}")
    
    elif type == None:
        print(f"\033[34m[{time}] DEBUG: {msg}\033[0m")
        if lf is not None:
            with open(lf, "a") as file:
                file.write(f"\n[{time}] DEBUG: {msg}")