"""Module for serial communication with Arduino.
maintainer: @gergelyturi"""
import json
import logging
import time

import serial
from tqdm import tqdm


class SerialComm:
    """
    A class for serial communication.

    Attributes:
    port (str): The port to connect to.
    baudrate (int): The baudrate to use for the connection.
    ser (serial.Serial): The serial connection object.
    """

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate, timeout=10)
        self.ser.flush()

    def __enter__(self):
        """
        Opens the serial connection and returns the object itself as the context manager.
        """
        if not self.ser.is_open:
            self.ser.open()
        self.ser.flush()
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback):
        """
        Closes the serial connection.
        """
        self.ser.close()

    def read(self):
        """
        Reads a line from the serial connection.

        Returns:
        str: The line read from the serial connection.
        """
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode("utf-8").rstrip()
            # print(line)
            return line
        else:
            return None

    def write(self, data):
        """
        Writes data to the serial connection.

        Args:
        data (str): The data to write to the serial connection.
        """
        self.ser.write(data.encode("utf-8"))

    def close(self):
        """
        Closes the serial connection.
        """
        self.ser.close()

    def read_json(self):
        """
        Reads a line from the serial connection and returns it as a JSON object.

        Returns:
        dict: The JSON object read from the serial connection.
        """
        line = self.read()
        if line is not None:
            try:
                return json.loads(
                    {
                        "message": line,
                    }
                )
            except json.JSONDecodeError:
                print(f"JSONDecodeError: {line}")
                return {"error": "JSONDecodeError", "data": line}
        else:
            return None

    def write_json(self, data):
        """
        Writes a JSON object to the serial connection.

        Args:
        data (dict): The JSON object to write to the serial connection.
        """
        self.write(json.dumps(data))

    def is_connected(self):
        """
        Checks if the serial connection is open.

        Returns:
        bool: True if the serial connection is open, False otherwise.
        """
        return self.ser.is_open if self.ser else False

    def listen_for_ttl_pulse(self):
        """Listen for TTL pulse from Arduino."""
        logging.info("Listening for TTL pulse...")
        while True:
            # print(f"Waiting for TTL pulse on port {self.port}...")
            line = self.read()
            print(f"Received: {line}")
            if line is not None:
                logging.info(f"Received: {line}")
                if "Session has started" in line:
                    logging.info("TTL received")
                    return True


class VisualEnhancemnets:
    @staticmethod
    def progress_bar(seconds):
        for i in tqdm(range(seconds), desc="Processing", unit="s", ncols=100):
            time.sleep(1)
