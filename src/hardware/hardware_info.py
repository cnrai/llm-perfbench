import platform
import psutil

try:
    import cpuinfo
except ImportError:
    cpuinfo = None

def get_system_info():
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return info

def get_cpu_info():
    info = {}

    # If cpuinfo is available, include additional details
    if cpuinfo:
        cpu_details = cpuinfo.get_cpu_info()
        info['Brand'] = cpu_details.get("brand_raw", "N/A")
        info['Arch'] = cpu_details.get("arch", "N/A")
        info['Bits'] = cpu_details.get("bits", "N/A")
    else:
        info['Brand'] = platform.processor()

    # CPU core counts
    info['Physical cores'] = psutil.cpu_count(logical=False)
    info['Total cores'] = psutil.cpu_count(logical=True)

    # CPU frequency (in MHz)
    freq = psutil.cpu_freq()
    info['Max Frequency'] = f"{freq.max:.2f} MHz" if freq else "N/A"
    info['Min Frequency'] = f"{freq.min:.2f} MHz" if freq else "N/A"
    info['Current Frequency'] = f"{freq.current:.2f} MHz" if freq else "N/A"

    return info

def get_memory_info():
    mem = psutil.virtual_memory()
    info = {
        "Total Memory": f"{mem.total/1e9:.2f} GB",
        "Available Memory": f"{mem.available/1e9:.2f} GB",
        "Used Memory": f"{mem.used/1e9:.2f} GB",
        "Memory Usage (%)": f"{mem.percent}%",
    }
    return info

def get_disk_info():
    disk = psutil.disk_usage('/')
    info = {
        "Total Disk Space": f"{disk.total/1e9:.2f} GB",
        "Used Disk Space": f"{disk.used/1e9:.2f} GB",
        "Free Disk Space": f"{disk.free/1e9:.2f} GB",
        "Disk Usage (%)": f"{disk.percent}%",
    }
    return info

def main():
    print("=== System Information ===")
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\n=== CPU Information ===")
    cpu_info = get_cpu_info()
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

    print("\n=== Memory Information ===")
    memory_info = get_memory_info()
    for key, value in memory_info.items():
        print(f"{key}: {value}")

    print("\n=== Disk Information ===")
    disk_info = get_disk_info()
    for key, value in disk_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()