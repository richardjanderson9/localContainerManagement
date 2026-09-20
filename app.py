import datetime

def main():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from the Vultr container! Current time is {current_time}")

if __name__ == "__main__":
    main()