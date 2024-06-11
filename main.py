# main.py

from Call_API_Relay import control_relay
import time

# Example usage
ip = '192.168.1.250'
username = 'user'
password = 'password'

try:
    while True:
        # Call API with state 1
        response = control_relay(ip, 1, username, password)
        print("Response for state 1:", response)
        time.sleep(0.1)  # Delay for 100 milliseconds

        # Call API with state 0
        response = control_relay(ip, 0, username, password)
        print("Response for state 0:", response)
        time.sleep(0.1)  # Delay for 100 milliseconds

except KeyboardInterrupt:
    print("Exiting the loop gracefully.")
