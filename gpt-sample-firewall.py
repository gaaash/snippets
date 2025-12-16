import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from scapy.all import sniff
import threading

# List to store blocked IPs
blocked_ips = set()

def block_ip(ip):
    """Block an IP using iptables"""
    if ip and ip not in blocked_ips:
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
        blocked_ips.add(ip)
        log_message(f"✅ Blocked IP: {ip}")
    else:
        messagebox.showwarning("Warning", "Invalid or already blocked IP")

def unblock_ip(ip):
    """Unblock an IP using iptables"""
    if ip in blocked_ips:
        os.system(f"sudo iptables -D INPUT -s {ip} -j DROP")
        blocked_ips.remove(ip)
        log_message(f"❌ Unblocked IP: {ip}")
    else:
        messagebox.showwarning("Warning", "IP not found in blocked list")

def log_message(message):
    """Log messages to the GUI"""
    log_box.insert(tk.END, message + "\n")
    log_box.yview(tk.END)

def packet_callback(packet):
    """Capture network packets and display in GUI"""
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        log_message(f"🌐 Packet from {src_ip}")

def start_sniffing():
    """Start packet sniffing in a separate thread"""
    sniff_thread = threading.Thread(target=lambda: sniff(prn=packet_callback, store=False, filter="ip", count=0))
    sniff_thread.daemon = True
    sniff_thread.start()

# GUI Setup
root = tk.Tk()
root.title("Basic Firewall")
root.geometry("520x570")
root.configure(bg="#2C3E50")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=5)

frame_title = tk.Frame(root, bg="#2C3E50")
frame_title.pack(pady=10)

icon_label = tk.Label(frame_title, text="🛡️", font=("Arial", 32), fg="white", bg="#2C3E50")
icon_label.pack(side=tk.LEFT, padx=10)

tk.Label(frame_title, text="Firewall Control", font=("Arial", 20, "bold"), fg="white", bg="#2C3E50").pack(side=tk.LEFT)

log_box = scrolledtext.ScrolledText(root, width=62, height=15, bg="#ECF0F1", fg="black", font=("Arial", 10))
log_box.pack(pady=5, padx=10)

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=10)

tk.Label(frame, text="🔍 IP Address:", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50").grid(row=0, column=0, padx=5)
ip_entry = tk.Entry(frame, width=25, font=("Arial", 12))
ip_entry.grid(row=0, column=1, padx=5)

frame_buttons = tk.Frame(root, bg="#2C3E50")
frame_buttons.pack(pady=10)

ttk.Button(frame_buttons, text="🚫 Block IP", command=lambda: block_ip(ip_entry.get()), style="TButton").grid(row=0, column=0, padx=10)
ttk.Button(frame_buttons, text="✅ Unblock IP", command=lambda: unblock_ip(ip_entry.get()), style="TButton").grid(row=0, column=1, padx=10)

ttk.Button(root, text="🔄 Start Sniffing", command=start_sniffing, style="TButton").pack(pady=10)

root.mainloop()
