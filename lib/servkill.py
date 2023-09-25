import os
import time

# Set the process name to be terminated
process_name = "msedge.exe"

# Set the time limit in seconds (1 hour = 3600 seconds)
time_limit = 3600

# Check if the process is running
def is_process_running(name):
    try:
        # Run 'tasklist' command and check if the process name is in the output
        output = os.popen('tasklist /FI "IMAGENAME eq {}"'.format(name)).read()
        return name.lower() in output.lower()
    except Exception as e:
        print("Error:", e)
        return False

if is_process_running(process_name):
    print(f"{process_name} is running. Waiting for {time_limit} seconds...")
    time.sleep(time_limit)

    if is_process_running(process_name):
        print(f"{process_name} is still running after {time_limit} seconds. Terminating...")

        try:
            # Terminate the process using 'taskkill' command
            os.system('taskkill /F /IM {}'.format(process_name))
            print(f"{process_name} has been terminated.")
        except Exception as e:
            print("Error:", e)
    else:
        print(f"{process_name} has already terminated before the time limit.")
else:
    print(f"{process_name} is not currently running.")
