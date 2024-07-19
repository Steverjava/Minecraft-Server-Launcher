import subprocess
import os

# 启动服务器脚本
'''
Xms = input("Xms")
Xmx = input("Xmx")
jar_name = input("jar_name")
jar_file = os.getcwd() + "\\" + jar_name

output = 'java -Xms' + Xms + ' -Xmx' + Xmx + f' -jar {jar_file}'

pi = subprocess.Popen(output, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

for i in pi.stdout:
    i = i.strip()
    print(i.decode('cp936'))
'''

# IP查询
'''
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
'''

# logo
'''
print("  _________  __                                       __                        ")
print(" /   _____/_/  |_   ____  ___  __  ____  _______     |__|_____   ___  _______   ")
print(" \\_____  \\ \\   __\\_/ __ \\ \\  \\/ /_/ __ \\ \\_  __ \\    |  |\\__  \\  \\  \\/ /\\__  \\  ")
print(" /        \\ |  |  \\  ___/  \\   / \\  ___/  |  | \\/    |  | / __ \\_ \\   /  / __ \\_")
print("/_______  / |__|   \\___  >  \\_/   \\___  > |__|   /\\__|  |(____  /  \\_/  (____  /")
print("        \\/             \\/             \\/         \\______|     \\/             \\/ ")
'''

# EULA
'''
file_path = 'eula.txt'
expected_content = "eula=true"
expected_content_bug = "#eula=true"
if os.path.exists(file_path):
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

    if expected_content_bug in content:
        try:
            with open(file_path, 'w') as file:
                file.write('eula=true')
        except IOError as e:
            print("File operation error:", e)
            exit()
    elif expected_content in content:
        pass
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
        except IOError as e:
            print("File operation error:", e)

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
                file.write("eula=" + Boolean)
        except IOError as e:
            print("File operation error:", e)
'''

# 认证库 库
library = []

path = str(input(""))

