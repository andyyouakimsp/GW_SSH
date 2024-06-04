import requests
import hashlib
import json

def main():
    # Get user input for Gateway IP and mode
    gw_ip = input("Please enter Gateway IP: ")
    mode = input("Mode (0 for disable, 1 for enable): ")

    try:
        mode = int(mode)
        if mode not in [0, 1]:
            raise ValueError("Mode must be 0 or 1.")
    except ValueError as e:
        print(f"Invalid mode: {e}")
        return

    # Generate MD5 hash key
    key = hashlib.md5((gw_ip + "admin").encode()).hexdigest()

    # Prepare data payload
    data = {
        "key": key,
        "enableSsh": mode
    }

    # Convert data to JSON
    json_data = json.dumps(data)

    # Prepare files for POST request
    files = {
        'data': json_data
    }

    # Send POST request to the server
    try:
        response = requests.post(f'http://{gw_ip}/api/v2/gw/sshd', files=files)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())
    except requests.RequestException as e:
        print(f"Request failed: {e}")

    input("Press Enter to close...")

if __name__ == "__main__":
    main()
