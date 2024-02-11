import psutil


def get_processes():
    processes = []
    for process in psutil.process_iter():
        with process.oneshot():
            pid = process.pid
            name = process.name()
            cores = len(process.cpu_affinity())
            cpu_usage = process.cpu_percent()
            status = process.status()
            nice = int(process.nice())
            n_threads = process.num_threads()
            user = process.username()

        processes.append({
            "pid": pid, "name": name, 'cores': cores, "cpu_usage": cpu_usage,
            "status": status, 'nice': nice,
            'n_threads': n_threads, 'user': user,
        })

    return processes


def get_loadavg():
    avgload = psutil.getloadavg()
    return avgload


def get_sleeping():
    sleeping = 0
    for process in processes:
        if process['status'] == 'sleeping':
            sleeping += 1
    return sleeping


def get_running():
    running = 0
    for process in processes:
        if process['status'] == 'running':
            running += 1
    return running


def get_threads():
    threads = 0
    for process in processes:
        threads += process['n_threads']
    return threads


processes = get_processes()
avgload1, avgload2, avgload3 = get_loadavg()
bytes_sent, bytes_recv, pcks_sent, pcks_recv, a, b, c, d = psutil.net_io_counters()


def info():
    info = (f' Processes: {len(processes)} total, {get_running()} running, {get_sleeping()} sleeping,'
            f' {get_threads()} threads.\n Load Avg: {round(avgload1, 2)} {round(avgload2, 2)} {round(avgload3, 2)}'
            f' CPU usage: {psutil.cpu_percent()}%\n Networks packets: {pcks_sent} sent, {pcks_recv} received, '
            f'{bytes_sent} bytes sent, {bytes_recv} bytes received.')
    return info


print(info())


print("|{:^8}|{:^40}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^30}|".format('pid', 'name', 'cores', 'cpu_usage',
                                                                        'status', 'nice', 'n_threads', 'user'))
for process in processes:
    for k, v in process.items():
        # pid, name, cores, cpu_usage, status, nice, n_threads, user = v
        # print(pid, name, cores, cpu_usage, status, nice, n_threads, user)
        proc = [process['pid'], process['name'], process['cores'], process['cpu_usage'], process['status'],
                process['nice'], process['n_threads'], process['user']]
        print("|{:^8}|{:^40}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^30}|".format(*proc))
