import os
import time

print("Welcome to NEXUS.")
name = input("How should I call you?: ")
print(f"Welcome {name}!")
time.sleep(2)
print("Welcome to NEXUS. Please wait while we boot up the system...")
time.sleep(2)
os.system('cls')
print("""
╔══════════════════════════════════════╗
║          NEXUS TERMINAL v1.0         ║
║          SYSTEM INITIALIZED          ║
╚══════════════════════════════════════╝ \n""")
time.sleep(1)
print("[+] Initializing terminal...")
time.sleep(1)
print("[+] Loading modules...")
time.sleep(2)
print("[+] Connecting to simulation server...\n")
time.sleep(1)
print("ACCESS GRANTED")

print("\nType 'exit' to close the terminal.")
while True:
    command = input(f"{name}@NEXUS:~$ ")
    if command.lower() == "exit":
        print("Exiting NEXUS terminal...")
        time.sleep(1)
        break
    else:
        print(f"Executing command: {command}")
        time.sleep(1)
        print(f"Command '{command}' executed successfully.\n")
