"""
Python script to read data from Arduino serial ports and save it to a JSON file.

This script reads data from Arduino serial ports and saves it to a JSON file.
It takes command line arguments for mouse ID and condition. The script continuously
reads data from the serial ports and appends it to a data list. When a specific end session
message is received, the script stops reading data, saves the data to a JSON file, and exits.

Usage:
    python arduino_serial.py -ids <mouse_ids> -c <condition>

Example:
    python arduino_serial.py -id mouse1 -c condition
"""

import argparse
import json
import time
from datetime import datetime
from os.path import join

import serial
from serial_comm import SerialComm as sc


def main():
    """
    Main function that reads data from Arduino serial ports and saves it to a JSON file.

    Args:
        None

    Returns:
        None
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-id", "--mouse_id", required=True, help="id of the mouse")
    ap.add_argument(
        "-c",
        "--condition",
        required=True,
        help="Condition",
    )

    args = ap.parse_args()
    mouse_id = args.mouse_id.split(",")
    cond = args.condition
    port = '/dev/ttyUSB1'

    # Global variables
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d_%H-%M-%S")
    end_session_message = "Session has ended"
    session_ended = False  # Flag to indicate the end of the session
    file_name = "_".join(mouse_id) + f"_{formatted_date_time}.json"

    data_list = {mouse_id: []}

    header = {
        "mouse_id": mouse_id,
        "condition": cond,
        "port": port,
        "Start_time": formatted_date_time,
    }
    # Initialize serial communication
    comms = (mouse_id, sc(port, 115200))
    time.sleep(2)

    try:
        while True:
            mouse_id = comms[0]
            comm = comms[1]
            data = comm.read()
            if data is not None and "error" not in data:
                print(f"{mouse_id}: {data}")
                data_json = {
                    "message": data,
                    "mouse_id": mouse_id,
                    "port": comm.port,
                    "absolute_time": datetime.now().strftime(
                        "%Y-%m-%d_%H-%M-%S.%f"
                    ),
                }
                data_list[mouse_id].append(data_json)
                if end_session_message in data_json.get("message", ""):
                    end_message = {
                        "message": data,
                        "absolute_time": datetime.now().strftime(
                            "%Y-%m-%d_%H-%M-%S.%f"
                        ),
                    }
                    # adding the end session message to all the mice
                    data_list[mouse_id].append(end_message)
                    print("Session has ended, closing file and exiting...")
                    session_ended = True
                    break
            elif data is not None and "error" in data:
                print(f"Non-JSON data: {data}")
            if session_ended:
                comm.close()
                break  # Exit the while loop

    except serial.SerialException as e:
        print(f"Serial port error: {e}")
    except KeyboardInterrupt:
        keyboard_interrupt = {
            "message": "KeyboardInterrupt",
            "absolute_time": datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f"),
        }
        data_list[mouse_id].append(keyboard_interrupt)
        print("KeyboardInterrupt detected. Saving data to file...")

    with open(join("data", file_name), "w", encoding="utf-8") as f:
        json.dump({"header": header, "data": data_list}, f, indent=4)
        print(f"Data saved to {file_name}")
    # Time for cleaning up
    time.sleep(2)


if __name__ == "__main__":
    main()
