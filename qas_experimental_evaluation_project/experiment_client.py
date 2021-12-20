from qas_experimental_evaluation_project.utils import execute_command, wait, log_info, kill
import os, sys

victims_ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"

def start():
    commands = {
        "client": {
            "cmd": ['client', f'http://{victims_ip}:8000/'],
            "process": None
        },
        "malware_server": {
            "cmd": ['malware_server'],
            "process": None
        },
        "dos": {
            "cmd": ['dos', f'{victims_ip}'],
            "process": None
        }
    }
    log_info("[starting monitoring main]", os.getpid())
    
    execute_command(commands, "client")
    wait(minutes= 15, seconds=10)
    execute_command(commands, "malware_server")
    wait(minutes= 15, seconds=10)
    kill(commands, "malware_server")
    wait(minutes= 45, seconds=10) # 14 normal + 15 ransomware + 15 normal
    execute_command(commands, "dos")
    wait(seconds=15)
    kill(commands, "dos")
    wait(seconds=5)
    kill(commands, "client")

    # process.wait() esperar em todos os processos?
    log_info("[killing monitoring main]", os.getpid())
