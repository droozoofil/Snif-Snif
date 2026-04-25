import socket
import threading
from queue import Queue
import ipaddress

# Common ports to scan
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

# Thread-safe queue
queue = Queue()

# Lock for clean output
print_lock = threading.Lock()


def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((str(ip), port))
        if result == 0:
            with print_lock:
                print(f"[OPEN] {ip}:{port}")
        s.close()
    except:
        pass


def worker():
    while not queue.empty():
        ip, port = queue.get()
        scan_port(ip, port)
        queue.task_done()


def scan_host(ip):
    print(f"\n[+] Scanning host: {ip}")
    for port in COMMON_PORTS:
        queue.put((ip, port))


def scan_network(network):
    print(f"\n[+] Scanning network: {network}")
    try:
        net = ipaddress.ip_network(network, strict=False)
        for ip in net.hosts():
            for port in COMMON_PORTS:
                queue.put((ip, port))
    except ValueError:
        print("[-] Invalid network format (example: 192.168.1.0/24)")


def run_threads(thread_count=100):
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    queue.join()


if __name__ == "__main__":
    print("Simple Port Scanner")
    print("1. Scan single host")
    print("2. Scan network")

    choice = input("Choose option (1/2): ")

    if choice == "1":
        target = input("Enter IP address: ")
        scan_host(target)

    elif choice == "2":
        network = input("Enter network (e.g. 192.168.1.0/24): ")
        scan_network(network)

    else:
        print("Invalid choice")
        exit()

    run_threads()
    print("\n[✓] Scan complete")
