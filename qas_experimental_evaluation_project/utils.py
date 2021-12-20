import os, time, datetime, subprocess, signal


def log_info(task, pid):
    print(f"{task} pid({pid}) at {datetime.datetime.now()}")

def get_total_time_str(minutes=0, seconds=0):
    seconds_waited_str = f"{seconds} seconds"
    minutes_waited_str = f"{minutes} minutes"
    if minutes and seconds:
        return "". join([minutes_waited_str, " and ", seconds_waited_str])
    elif minutes:
        return minutes_waited_str
    else:
        return seconds_waited_str

def wait(minutes=0, seconds=0):
    wait_time_str = get_total_time_str(minutes, seconds)
    total_seconds_to_wait = (minutes * 60) + seconds
    print(f"pid({os.getpid()}) waiting for {wait_time_str} at {datetime.datetime.now()}")
    for seconds_remaining in range(total_seconds_to_wait, 0, -1):
        print(f"{seconds_remaining} seconds remaining...")
        time.sleep(1)
    print(f"pid({os.getpid()}) resumed for {wait_time_str} at {datetime.datetime.now()}")

def run(server_args):
    return subprocess.Popen(server_args)

def kill(process, name):
    process_obj = process[name]["process"]
    log_info(f"[killing {name} child]", process_obj.pid)
    process_obj.send_signal(signal.SIGTERM)

def run_and_log(server_cmd, process_name):
    log_info(f"[starting {process_name} main]", os.getpid())
    process = run(server_cmd)
    log_info(f"[starting {process_name} child]", process.pid)
    return process

def execute_command(commands, name):
    commands[name]['process'] = run_and_log(commands[name]['cmd'], name)
