import datetime
import os
import platform

def main():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 50)
    print(f"🚀 Hello from the Vultr container!")
    print(f"⏰ Current time: {current_time}")
    print(f"💻 Operating System: {platform.system()} {platform.release()}")
    print(f"🐍 Python Version: {platform.python_version()}")
    print(f"👤 Running as User: {os.getenv('USER', 'appuser')}")
    print("=" * 50)

if __name__ == "__main__":
    main()