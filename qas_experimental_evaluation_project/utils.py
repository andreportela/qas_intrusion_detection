import os, time, datetime

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
