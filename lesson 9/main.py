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
    for process in get_processes():
        if process['status'] == 'sleeping':
            sleeping += 1
    return sleeping


def get_running():
    running = 0
    for process in get_processes():
        if process['status'] == 'running':
            running += 1
    return running


def get_threads():
    threads = 0
    for process in get_processes():
        threads += process['n_threads']
    return threads


avgload1, avgload2, avgload3 = get_loadavg()
bytes_sent, bytes_recv, pcks_sent, pcks_recv, a, b, c, d = psutil.net_io_counters()


def info():
    print(f'Processes: {len(get_processes())} total, {get_running()} running, {get_sleeping()} sleeping, '
          f'{get_threads()} threads.\nLoad Avg: {avgload1:.2f} {avgload2:.2f} {avgload3:.2f} CPU usage: '
          f'{psutil.cpu_percent()}% \nNetwork packets: {pcks_sent} sent, {pcks_recv} received, {bytes_sent} sent, '
          f'{bytes_recv} received.\n')


def table():
    i = 0
    print("|{:^8}|{:25}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format('pid', 'name', 'cores', 'cpu_usage',
                                                                            'status', 'nice', 'n_threads', 'user'))
    for process in get_processes():
        if i == 30:
            break
        else:
            print("|{:^8}|{:^25}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(process['pid'],
                                                                                    process['name'], process['cores'],
                                                                                    process['cpu_usage'],
                                                                                    process['status'], process['nice'],
                                                                                    process['n_threads'],
                                                                                    process['user']))
            i += 1


def show():
    info()
    table()


show()