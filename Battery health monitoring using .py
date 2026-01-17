import psutil  # This library lets us talk to the computer hardware
import time    # We need this to create a delay (so we don't crash the PC)

def check_my_system():
    print("--- 🖥️  Checking System Health ---")

    # 1. Let's check the Battery first
    # We use 'try' because desktop PCs don't have batteries, and we don't want errors.
    try:
        battery = psutil.sensors_battery()
        plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
        print(f"🔋 Battery: {battery.percent}% | {plugged}")
    except:
        print("🔋 Battery: Not Found (Are you on a desktop?)")

    # 2. Check CPU Usage
    # We wait 1 second to get an accurate reading of what the CPU is doing right now.
    print("⏳ Measuring CPU work...", end="\r")
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"🧠 CPU Usage: {cpu_usage}%       ")  # The spaces clear the previous text

    # 3. Check Memory (RAM)
    # Computers store memory in bytes. We divide by (1024*1024*1024) to get Gigabytes (GB).
    memory = psutil.virtual_memory()
    total_gb = memory.total / (1024 ** 3)
    used_gb = memory.used / (1024 ** 3)
    
    # I'm formatting this to 2 decimal places so it looks clean (e.g., "8.45 GB")
    print(f"💾 RAM Used: {used_gb:.2f} GB / {total_gb:.2f} GB")

    # 4. A simple warning system
    if cpu_usage > 80:
        print("⚠️  WARNING: Your CPU is working very hard!")
    else:
        print("✅ System is running smoothly.")

if __name__ == "__main__":
    # Run this check every 5 seconds forever
    try:
        while True:
            check_my_system()
            print("\nUpdating in 5 seconds... (Press Ctrl+C to stop)")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n🛑 Monitor Stopped.")
