import psutil
import platform
import time
import os

def clear_screen():
    os.system('clear')  # for Linux / Parrot OS

def get_system_info():
    print("🖥️ SYSTEM INFORMATION")
    print("----------------------")
    print(f"System     : {platform.system()}")
    print(f"Node Name  : {platform.node()}")
    print(f"Release    : {platform.release()}")
    print(f"Machine    : {platform.machine()}")
    print(f"Processor  : {platform.processor()}")

def get_cpu_info():
    print("\n⚙️ CPU INFO")
    print("----------------------")
    print(f"CPU Usage  : {psutil.cpu_percent(interval=1)}%")

def get_memory_info():
    memory = psutil.virtual_memory()
    print("\n🧠 MEMORY INFO")
    print("----------------------")
    print(f"Total      : {memory.total / (1024**3):.2f} GB")
    print(f"Used       : {memory.used / (1024**3):.2f} GB")
    print(f"Usage      : {memory.percent}%")

def get_disk_info():
    disk = psutil.disk_usage('/')
    print("\n💾 DISK INFO")
    print("----------------------")
    print(f"Total      : {disk.total / (1024**3):.2f} GB")
    print(f"Used       : {disk.used / (1024**3):.2f} GB")
    print(f"Usage      : {disk.percent}%")

def main():
    while True:
        clear_screen()
        print("📊 SYSTEM DASHBOARD\n")
        get_system_info()
        get_cpu_info()
        get_memory_info()
        get_disk_info()
        time.sleep(2)

if __name__ == "__main__":
    main()