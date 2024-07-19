import subprocess
import time
import platform
import os
import socket


def logo():
    print("  _________  __                                       __                        ")
    print(" /   _____/_/  |_   ____  ___  __  ____  _______     |__|_____   ___  _______   ")
    print(" \\_____  \\ \\   __\\_/ __ \\ \\  \\/ /_/ __ \\ \\_  __ \\    |  |\\__  \\  \\  \\/ /\\__  \\  ")
    print(" /        \\ |  |  \\  ___/  \\   / \\  ___/  |  | \\/    |  | / __ \\_ \\   /  / __ \\_")
    print("/_______  / |__|   \\___  >  \\_/   \\___  > |__|   /\\__|  |(____  /  \\_/  (____  /")
    print("        \\/             \\/             \\/         \\______|     \\/             \\/ ")


def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("Please submit a request on GitHub with your system information and a screenshot of the error!")


print("Welcome to \"Minecraft-Server-Launch\", a script that automatically launches Minecraft servers!\n You ready?")
# 询问用户是否开始
parameter = input("[y/n]")
if parameter == "y":
    pass
else:
    exit()

logo()

print("Now we are examining your computer system and its architecture.")  # 告知用户检测信息
System = platform.system() + " " + platform.version()
Users = os.getlogin()
Hostname = socket.gethostname()

for parameter in range(4):
    time.sleep(0.5)
    print("... ", end="")
print("... ")
time.sleep(2)

print("Your operating system is", System, ".")
print("The current user is", Users, ".")
print("The current host is", Hostname, ".")

for parameter in range(4):
    time.sleep(0.5)
    print("... ", end="")
print("... ")
time.sleep(2)

if os.name == 'posix':
    command = 'ifconfig'
elif os.name == 'darwin':
    command = 'ifconfig'
elif os.name == 'nt':
    command = 'ipconfig /all'
else:
    raise Exception('Unsupported operating system')

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()

output = output.strip()
print(output.decode('cp936'))

print("Checking licensing agreement status...")

file_path = 'eula.txt'
expected_content = "eula=true"
expected_content_bug = "#eula=true"
if os.path.exists(file_path):
    print("Detected licensing agreement file!")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            content = content.lower()
    except FileNotFoundError:
        print("Unable to read file")
        exit()
    except IOError as e:
        print("File operation error:", e)
        exit()

    print("Checking file integrity...")

    if expected_content_bug in content:
        try:
            with open(file_path, 'w') as file:
                file.write('eula=true')
                print("The agreement information has been amended!")
        except IOError as e:
            print("File operation error:", e)
            exit()
    elif expected_content in content:
        print("The agreement agrees that the information is complete!")
    else:
        while True:
            Boolean = input("Do you agree to the EULA?(y/n)\n（https://account.mojang.com/documents/minecraft_eula）")
            if Boolean.lower() == "y":
                Boolean = "true"
                break
            elif Boolean.lower() == "n":
                Boolean = "false"
                print("Note: If you do not agree to the EULA, you will not be able to open the server!")
                break
            else:
                print("Invalid input, please re-enter (y/n)")

        try:
            with open(file_path, 'w') as file:
                file.write('eula=' + Boolean)
                print("The agreement information has been amended!")
        except IOError as e:
            print("File operation error:", e)

else:
    print("No license file detected!")
    while True:
        Boolean = input("Do you agree to the EULA?(y/n)\n（https://account.mojang.com/documents/minecraft_eula）")
        if Boolean.lower() == "y":
            Boolean = "true"
            break
        elif Boolean.lower() == "n":
            Boolean = "false"
            print("Note: If you do not agree to the EULA, you will not be able to open the server!")
            break
        else:
            print("Invalid input, please re-enter (y/n)")
    try:
        with open(file_path, 'w') as file:
            file.write("eula=" + Boolean)
            print("The agreement information has been amended!")
    except IOError as e:
        print("File operation error:", e)

