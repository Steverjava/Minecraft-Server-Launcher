import subprocess
import time
import platform
import os
import socket
import requests


def timed():
    for a in range(4):
        time.sleep(0.5)
        print("... ", end="")
    print("... ")
    time.sleep(2)


def logo():
    print("  _________  __                                       __                        ")
    print(" /   _____/_/  |_   ____  ___  __  ____  _______     |__|_____   ___  _______   ")
    print(" \\_____  \\ \\   __\\_/ __ \\ \\  \\/ /_/ __ \\ \\_  __ \\    |  |\\__  \\  \\  \\/ /\\__  \\  ")
    print(" /        \\ |  |  \\  ___/  \\   / \\  ___/  |  | \\/    |  | / __ \\_ \\   /  / __ \\_")
    print("/_______  / |__|   \\___  >  \\_/   \\___  > |__|   /\\__|  |(____  /  \\_/  (____  /")
    print("        \\/             \\/             \\/         \\______|     \\/             \\/ ")


print("欢迎来到 Minecraft-Server-Launch, 一个帮助开服的程序\n 你准备好了吗?")
# 询问用户是否开始
parameter = input("[y/n]")
if parameter.lower() == "y":
    pass
else:
    exit()

logo()

print("现在我们将测你的设备信息")  # 告知用户检测信息
System = platform.system() + " " + platform.version()
Users = os.getlogin()
Hostname = socket.gethostname()

timed()

print("你的系统为：", System, ".")
print("当前用户为：", Users, ".")
print("当前主机为：", Hostname, ".")

timed()

if os.name == 'posix':
    command = 'ifconfig'
elif os.name == 'darwin':
    command = 'ifconfig'
elif os.name == 'nt':
    command = 'ipconfig /all'
else:
    raise Exception('不支持的类型')

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()

output = output.strip()
print(output.decode('cp936'))

command = ""
print("你是否要启动认证？")
variable = str(input("[y/n]")).lower()
if variable == "y":
    file_name = "authlib-injector-1.2.5.jar"
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)
    if os.path.exists(file_path):
        pass
    else:
        print("正在下载所需内容……")
        url = "https://authlib-injector.yushi.moe/artifact/53/authlib-injector-1.2.5.jar"
        response = requests.get(url)
        if response.status_code == 200:
            with open("authlib-injector-1.2.5.jar", "wb") as file:
                file.write(response.content)
            command = " -javaagent:authlib-injector-1.2.5.jar=https://littleskin.cn/api/yggdrasil"
        else:
            print("下载失败", response.status_code)
else:
    pass

file_path = 'eula.txt'
expected_content = "eula=true"
expected_content_bug = "#eula=true"
if os.path.exists(file_path):
    print("检测到许可协议文件！")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            content = content.lower()
    except FileNotFoundError:
        print("无法读取文件")
        exit()
    except IOError as e:
        print("文件操作错误：", e)
        exit()

    print("检查文件完整性…")

    if expected_content_bug in content:
        try:
            with open(file_path, 'w') as file:
                file.write('eula=true')
                print("协议信息已修改！")
        except IOError as e:
            print("文件操作错误：", e)
            exit()
    elif expected_content in content:
        print("协议同意资料齐全！")
    else:
        while True:
            Boolean = input("你是否同意EULA？(y/n)\n（https://account.mojang.com/documents/minecraft_eula）").lower()
            if Boolean.lower() == "y":
                Boolean = "true"
                break
            elif Boolean.lower() == "n":
                Boolean = "false"
                print("注意：如果您不同意EULA，您将无法打开服务器！")
                break
            else:
                print("输入无效，请重新输入")

        try:
            with open(file_path, 'w') as file:
                file.write('eula=' + Boolean)
                print("协议信息已修改！")
        except IOError as e:
            print("文件操作错误：", e)

else:
    print("未检测到许可证文件！!")
    while True:
        Boolean = input("你是否同意EULA?(y/n)\n（https://account.mojang.com/documents/minecraft_eula）").lower()
        if Boolean.lower() == "y":
            Boolean = "true"
            break
        elif Boolean.lower() == "n":
            Boolean = "false"
            print("注意：如果您不同意EULA，您将无法打开服务器！")
            break
        else:
            print("输入无效，请重新输入")
    try:
        with open(file_path, 'w') as file:
            file.write("eula=" + Boolean)
            print("协议信息已修改！")
    except IOError as e:
        print("文件操作错误：", e)

print("正在启动服务器")
Xms = input("Xms:")
Xmx = input("Xmx:")
jar_name = input("jar_name(包含.jar)")
jar_file = os.getcwd() + "\\" + jar_name

output = 'java -Xms' + Xms + ' -Xmx' + Xmx + command + f' -jar {jar_file}'

pi = subprocess.Popen(output, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

for i in pi.stdout:
    i = i.strip()
    print(i.decode('cp936'))

while True:
    print("检测到服务器崩溃/崩溃，是否重启？")
    variable = str(input("[y/n]"))
    if variable == "y":
        pi = subprocess.Popen(output, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        for i in pi.stdout:
            i = i.strip()
            print(i.decode('cp936'))
    else:
        exit()
