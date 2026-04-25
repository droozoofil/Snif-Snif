import socket
import threading
import ipaddress
import tkinter as tk
from tkinter import scrolledtext

COMMON_PORTS = [21, 22, 23, 80, 443, 8080]

def scan_port(ip, port, output):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((str(ip), port))
        if result == 0:
            output.insert(tk.END, f"[OPEN] {ip}:{port}\n")
        s.close()
    except:
        pass

def scan_host(ip, output):
    output.insert(tk.END, f"\n[+] Scanning host: {ip}\n")
    for port in COMMON_PORTS:
        scan_port(ip, port, output)
    output.insert(tk.END, "[✓] Done\n")

def scan_network(network, output):
    output.insert(tk.END, f"\n[+] Scanning network: {network}\n")
    try:
        net = ipaddress.ip_network(network, strict=False)
        for ip in net.hosts():
            for port in COMMON_PORTS:
                scan_port(ip, port, output)
        output.insert(tk.END, "[✓] Done\n")
    except:
        output.insert(tk.END, "[-] Invalid network format\n")

def start_scan():
    target = entry.get()
    mode = var.get()

    output.delete(1.0, tk.END)

    if mode == "host":
        threading.Thread(target=scan_host, args=(target, output)).start()
    else:
        threading.Thread(target=scan_network, args=(target, output)).start()

# GUI setup
root = tk.Tk()
root.title("Python Port Scanner")

tk.Label(root, text="Target (IP or Network):").pack()
entry = tk.Entry(root, width=30)
entry.pack()

var = tk.StringVar(value="host")
tk.Radiobutton(root, text="Single Host", variable=var, value="host").pack()
tk.Radiobutton(root, text="Network", variable=var, value="network").pack()

tk.Button(root, text="Start Scan", command=start_scan).pack()

output = scrolledtext.ScrolledText(root, width=60, height=20)
output.pack()

root.mainloop()
