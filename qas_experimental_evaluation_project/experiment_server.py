from qas_experimental_evaluation_project.utils import \
    execute_command, wait, log_info, kill
import os, sys

attackers_ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"

def start():
    commands = {
        "server": {
            "cmd": ['server'],
            "process": None
        },
        "monitoring": {
            "cmd": ['monitoring'],
            "process": None
        },
        "malware_client": {
            "cmd": ['malware_client', f"http://{attackers_ip}:8000/"],
            "process": None
        },
        "ransomware": {
            "cmd": ['ransomware'],
            "process": None
        }
    }
    log_info("[starting monitoring main]", os.getpid())
    
    execute_command(commands, "server")
    wait(seconds=5)
    execute_command(commands, "monitoring")
    wait(seconds=15)
    kill(commands, "monitoring")
    wait(seconds=5)
    kill(commands, "server")

    # process.wait() esperar em todos os processos?
    log_info("[killing monitoring main]", os.getpid())
