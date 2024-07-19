import subprocess
import time
import platform
import os
import socket
import re


def timed():
    for i in range(4):
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


def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("Please submit a request on GitHub with your system information and a screenshot of the error!")


def main_menu(authlib_injector):
    clear()  #清屏

    #设置标准变量
    variable_authentication_menu = '1'
    variable_more_settings_menus = '2'
    variable_minecraft_game_menu = '3'
    variable_minecraft_settings_menu = '4'
    variable_server_restart_menu = '5'
    variable_exit = '6'

    #打印选项
    print("***** Main Menu *****")
    print("1.Authentication menu"
          "\n2.More settings menus"
          "\n3.Minecraft Game Menu"
          "\n4.Minecraft Settings menu"
          "\n5.Server restart menu"
          "\n6.Exit")

    #用户输入选项
    variable = str(input("Please select the menu:"))

    #进行判断
    if variable == variable_authentication_menu:  #转到认证菜单
        print("Please wait...")
        authentication_menu(authlib_injector)
    elif variable == variable_more_settings_menus:  #转到更多设置菜单
        print("Please wait...")
        more_settings_menus()
    elif variable == variable_minecraft_game_menu:  #转到Minecraft Game菜单
        print("Please wait...")
        minecraft_game_menu()
    elif variable == variable_minecraft_settings_menu:  #转到Minecraft Setting菜单
        print("Please wait...")
        minecraft_settings_menu()
    elif variable == variable_server_restart_menu:  #转到服务器重启菜单
        print("Please wait...")
        server_restart_menu()
    elif variable == variable_exit:  #退出
        exit()
    else:  #错误输入
        print("Invalid input!")
        main_menu(authlib_injector)


#认证菜单
def authentication_menu(authlib_injector):
    clear()  #清屏

    #设置标准变量
    variable_return_to_main_menu = "0"
    variable_open_authentication = "a"
    variable_close_authentication = "b"

    #打印选项
    print("***** Authentication Menu *****")
    print("0.Return to main menu"
          "\na.Open authentication"
          "\nb.Close authentication")

    #用户输入选项
    variable = str(input("Please select the menu:"))

    #进行判断
    if variable == variable_return_to_main_menu:  #返回主菜单
        print("Please wait...")
        main_menu(authlib_injector)
    elif variable == variable_open_authentication:  #开启认证菜单
        print("Please wait...")
        open_authentication(authlib_injector)
    elif variable == variable_close_authentication:  #关闭认证菜单
        print("Please wait...")
        close_authentication()
    else:  #错误输入
        print("Invalid input!")
        authentication_menu(authlib_injector)

    # 开启认证菜单


def open_authentication(authlib_injector):
    clear()  # 清屏

    library = []  # 创建认证库 库

    # 设置标准变量
    variable_back_to_authentication_menu = "0"
    variable_set_up_the_authentication_library = "a"
    variable_set_the_default_authentication_library = "b"

    variable_add_authentication_library = "1"
    variable_management_certification_library = "2"

    default_authentication_library = ""

    # 打印选项
    print("***** Open Authentication *****")
    print("0.Authentication Menu"
          "\na.Set up the authentication library"
          "\nb.Set the default authentication library")

    # 用户输入选项
    variable = str(input("Please choose:"))

    # 进行判断
    if variable == variable_back_to_authentication_menu:  # 返回认证菜单
        print("Please wait...")
        authentication_menu(authlib_injector)
    elif variable == variable_set_up_the_authentication_library:  # 设置认证库
        print("Please wait...")

        clear()

        print("0.Return"
              "\n1.Add authentication library"
              "\n2.Management certification library")

        variable = str(input("Please choose:"))

        if variable == variable_add_authentication_library:
            print("Please wait...")

            add_authentication_library(authlib_injector, library)

        elif variable == variable_management_certification_library:
            print("Please wait...")

            management_certification_library(authlib_injector, library)
        else:  # 错误输入
            print("Invalid input!")
            open_authentication(authlib_injector)


    elif variable == variable_set_the_default_authentication_library:  # 设置默认认证库
        print("Please wait...")

        for index, item in enumerate(library):
            print(f"[{index + 1}] {item}")


    elif not variable:

        clear()


def add_authentication_library(authlib_injector, library):
    clear()

    default_authentication_library = ""

    # 用户输入认证库
    authentication_library = str(input("Please enter your certification library: (should be URL)"))

    # 判断是否为网址
    if re.match(r'https?://', authentication_library):
        pass
    else:
        print("Invalid input!")
        open_authentication(authlib_injector)

    # 判断输入认证库是否是新库
    if authentication_library in library:  # 不为新库
        print("The authentication library has been started!")
        command = "-javaagent:" + authlib_injector + authentication_library  # 启动认证命令
    elif not authentication_library:  # 输入enter
        print("Default authentication library enabled!")
        command = "-javaagent:" + authlib_injector + default_authentication_library  # 启动认证命令（默认库）
    else:  # 为新库
        # 是否添加到认证库 库
        print("Detected as a new library."
              "\nIs the library added to the authentication library?[y/n]")

        variable = str(input(""))

        # 进行判断
        if variable == "y":  # 添加
            library.append(authentication_library)
            print("Added!")
        elif variable == "n":  # 不添加
            print("ok,don't!")
        else:  # 错误输入
            print("Invalid input!")
            open_authentication(authlib_injector)

        # 是否设置成默认库
        print("Is it set as the default library?[y/n]")

        variable = str(input(""))

        # 进行判断
        if variable == "y":  # 设置
            default_authentication_library = authentication_library
            command = "-javaagent:" + authlib_injector + authentication_library  # 启动认证命令
        elif variable == "n":  # 不设置
            command = "-javaagent:" + authlib_injector + authentication_library  # 启动认证命令
        else:  # 错误输入
            print("Invalid input!")
            open_authentication(authlib_injector)


def management_certification_library(authlib_injector, library):
    clear()

    long = str(len(library))
    if long == "0":
        print("The authentication library is empty!"
              "\nPlease go to Add authentication library to add library.")
        open_authentication(authlib_injector)
    else:
        for index, item in enumerate(library):
            print(f"[{index + 1}] {item}")


def close_authentication():
    clear()

    variable_back_to_authentication_menu = "0"
    variable_clear_the_authentication_library = "a"


def more_settings_menus():
    clear()


def minecraft_game_menu():
    clear()


def minecraft_settings_menu():
    clear()


def server_restart_menu():
    clear()


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

timed()

print("Your operating system is", System, ".")
print("The current user is", Users, ".")
print("The current host is", Hostname, ".")

timed()

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

