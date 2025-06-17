import psutil

def monitor_cpu(threshold):
    print("Monitoring CPU usage...")

    try:
        while True:
            # Get CPU usage over 1 second interval
            usage = psutil.cpu_percent(interval=1)

            if usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {usage}%")
            
    except KeyboardInterrupt:
        #user can press CTRL+C to interept inifinite loop running script
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set threshold to 80%
    monitor_cpu(threshold=80)
