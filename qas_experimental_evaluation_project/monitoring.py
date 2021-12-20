import signal, subprocess, os, datetime

def start():
    args = ['collectl', '--all', '-f', 'data_collection/dataset', '-P', '--options', '2']
    print(f"[starting monitoring main] pid({os.getpid()}) at {datetime.datetime.now()}")
    process = subprocess.Popen(args)
    print(f"[starting monitoring children] pid({process.pid}) at {datetime.datetime.now()}")
    def kill_child(signum, frame):
        print(f"[killing monitoring children] pid({process.pid}) at {datetime.datetime.now()}")
        process.send_signal(signal.SIGTERM)

    signal.signal(signal.SIGINT, kill_child)
    signal.signal(signal.SIGTERM, kill_child)

    process.wait()
    print(f"[killing monitoring main] pid({os.getpid()}) at {datetime.datetime.now()}")
