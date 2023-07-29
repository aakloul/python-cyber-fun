import os
import psutil
from pprint import pp


def look_process():
    pp(psutil.users())
    print(psutil.pids())
    # print(psutil.net_connections(kind="inet4"))

    for proc in psutil.process_iter(["pid", "name", "username"]):
        pp(proc.info)

    pid = 69693

    p = psutil.Process(pid=pid)
    with p.oneshot():
        print(f"Name:\t{p.name()}")
        print(f"CPU times:\t{p.cpu_times()}")
        print(f"CPU %:\t{p.cpu_percent()}")
        print(f"Create time:\t{p.create_time()}")
        print(f"PPID:\t{p.ppid()}")
        print(f"Status:\t{p.status()}")


def look_cpu():
    print(f"CPU times:\t{psutil.cpu_times()}")
    print(f"CPU %:\t{psutil.cpu_percent(interval=.1)}%")
    print(f"Memory in use:\t{psutil.virtual_memory().percent}%")
    pp(f"Disk Usage:\t{psutil.disk_usage(path='/')}")
    print(f"Disk Used:\t{psutil.disk_usage(path='/').used / (1024**3)} GB")
    print(f"Disk Free:\t{psutil.disk_usage(path='/').free / (1024**3)} GB")
    print(f"Disk Total:\t{psutil.disk_usage(path='/').total / (1024**3)} GB")
    print(f"Disk %:\t{psutil.disk_usage(path='/').percent}%")
    pp(psutil.disk_partitions())
    print(psutil.boot_time())


def find_procs_by_name(name):
    ls = []
    for p in psutil.process_iter(["exe", "name", "cmdline"]):
        try:
            if (
                (name == p.name())
                or (p.exe() and os.path.basename(p.exe()) == name)
                or (p.cmdline() and p.cmdline()[0] == name)
            ):
                ls.append(p)
        except psutil.AccessDenied:
            pass
    return ls


if __name__ == "__main__":
    # look_cpu()
    pp(find_procs_by_name("Brave Browser Helper"))
