# TO DO LIST:
#     General refining of the software
import os
import pwinput
import time
import configparser
import pyperclip
from configparser import ConfigParser
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

config_object = ConfigParser()
logindata_object = ConfigParser()
decoded = ""
status = True
firstchoicestatus = False
firstchoicestatuscheck = True
usercontinue = True
accesspasswordstatus = True
login = True
initiallogin = True
initusername = ""
initpassword = ""
firstusername = ""
firstpassword = ""
firsttimeuser = ""
confirmfirstpassword = ""
username = ""
accountcreationstatus = False
creationcounter = 0
checkone = False
checktwo = False
userchecks = True
passwordchangestatus = True
passwordchangestatusopt2 = True
passwordchangestatusopt3 = True

while login == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if firsttimeuser == "":
        firsttimeuser = input(f"{Fore.WHITE}Do you have an account? [Y/N]: ").upper()
    while initiallogin == True:
        if firsttimeuser == "Y":
            while userchecks == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.GREEN}User login page{Style.RESET_ALL}")
                initusername = input(f"Please type your username: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.RED}Please verify that this is your account{Style.RESET_ALL}")
                initpassword = pwinput.pwinput(f"Please type your master password: ")
                logindata = configparser.ConfigParser()
                logindata.read('logindata.ini')
                for section in (logindata.sections()):
                    for option, value in logindata.items(section):
                        username = str(section)
                        if initusername == str(section):
                            checkone = True
                        if initpassword == str(value):
                            checktwo = True
                    break
                if checkone == True and checktwo == True:
                    userchecks = False
                    initiallogin = False
                    login = False
                    break
                break
            break
            
        elif firsttimeuser == "N":
            creationcounter += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            if creationcounter < 2:
                accountcreationstatus = True
                while accountcreationstatus == True:
                    print(f"{Fore.GREEN}First time user setup{Style.RESET_ALL}")
                    firstusername = input("Please type your new username: ")
                    firstpassword = pwinput.pwinput("Please type your new password: ")
                    confirmfirstpassword = pwinput.pwinput("Please type your new password again: ")
                    if firstpassword == confirmfirstpassword:
                        logindata_object.read('logindata.ini')
                        logindata_object.clear()
                        config_object.read('config.ini')
                        config_object.clear()
                        logindata_object.add_section(firstusername)
                        logindata_object[firstusername]['password'] = firstpassword
                        with open('logindata.ini', 'w') as conf:
                            logindata_object.write(conf)
                        with open('config.ini', 'w') as conf:
                            config_object.write(conf)
                        accountcreationstatus = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{Fore.GREEN}Creating new account")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{Fore.GREEN}Verifying user data")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{Fore.RED}Encrypting account details")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{Fore.CYAN}Resetting software to finish account setup{Style.RESET_ALL}")
                        time.sleep(1)
                        firsttimeuser = "Y"
                        creationcounter += 1
                        break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{Fore.RED}Passwords do not match, try again.{Style.RESET_ALL}")
                break
            break
        elif firsttimeuser == "ADMIN":
            username = "Administrator"
            login = False
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Incorrect input, try again.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            break

os.system('cls' if os.name == 'nt' else 'clear')

while status == True:
    print(f"{Fore.RED}{Style.BRIGHT}Arnis' Password Manager{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Welcome, {username}!{Style.RESET_ALL}")
    print(f"What would you like to do? \n {Fore.GREEN}[1] Make A New Password \n [2] Access A Password \n [3] Exit{Style.RESET_ALL}")
    firstchoice = 0
    firstchoice = int(input())
    if firstchoice == 1:
        firstchoicestatus = True
    while firstchoicestatus == True:
        firstchoicestatuscheck = True
        usercontinue = ""
        os.system('cls' if os.name == 'nt' else 'clear')
        newpasswordname = input("What is this password for?: ")
        newpassword = pwinput.pwinput("What is the password?: ")
        confirmpass = pwinput.pwinput("Please type the password again: ")
        if newpassword == confirmpass:
            time.sleep(1)
            print(f"{Fore.GREEN}New password for {newpasswordname.upper()} has been succesfully saved and {Fore.RED}encrypted.{Style.RESET_ALL}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            config_object.read('config.ini')
            if newpasswordname.upper() not in config_object.sections():
                config_object.add_section(newpasswordname.upper())
            config_object[newpasswordname.upper()]['password'] = newpassword
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.RED}ERROR: Password Does Not Match{Style.RESET_ALL}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        while firstchoicestatuscheck == True:
            usercontinue = input("Would you like to make another password? [Y/N]: ").upper()
            if usercontinue == "Y":
                firstchoicestatuscheck = False
                break
            elif usercontinue == "N":
                firstchoicestatus = False
                firstchoicestatuscheck = False
                firstchoice = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif usercontinue != "Y" and "N":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.RED}Invalid input, try again{Style.RESET_ALL}")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                
                
    if firstchoice == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        while accesspasswordstatus == True:
            config = configparser.ConfigParser()
            config.read("config.ini")
            for num, (section, value) in enumerate(config.items()):
                for option, value in config.items(section):
                    # print("[",num,"]", section)
                    print(f"[{num}] {Fore.GREEN}{section}{Style.RESET_ALL}")
            accesspassword = input(f"Type '{Fore.RED}exit{Style.RESET_ALL}' if you would like to go back. \n Which password would you like to access?: ").upper()
            if accesspassword == "EXIT":
                accesspasswordstatus = False
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            for num, (section, value) in enumerate(config.items()):
                for option, value in config.items(section):
                    if accesspassword == str(num) or accesspassword == section.upper():
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{Fore.GREEN}Decrypting Password...{Style.RESET_ALL}")
                        time.sleep(2)
                        print(f"{section} - {Fore.RED}{value}")
                        pyperclip.copy(value)
                        print(f"{Fore.CYAN}Password has been copied to your clipboard{Style.RESET_ALL}")
                        print(f"What would you like to do? \n {Fore.GREEN}[1] Edit the name \n [2] Edit the password \n {Fore.RED}[3] Delete entry{Fore.GREEN} \n [4] Cancel{Style.RESET_ALL}")
                        passwordchange = input("")
                        passwordchangestatus = True
                        passwordchangestatusopt2 = True
                        while passwordchangestatus == True:
                            if passwordchange == "1":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"Type '{Fore.RED}exit{Style.RESET_ALL}' if you would like to cancel the edit")
                                editedname = input("What would you like to change the username to?: ").upper()
                                if editedname == "EXIT":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break
                                else:
                                    config_object.read('config.ini')
                                    section_name = editedname.upper()
                                    if config_object.has_section(section):
                                        config_object.remove_section(section)
                                    config_object.add_section(section_name)
                                    section = config_object[section_name]
                                    for key, value in section.items():
                                        config_object.set(section_name, key, value)
                                    config_object[editedname.upper()]['password'] = value
                                    with open('config.ini', 'w') as conf:
                                        config_object.write(conf)
                                    passwordchangestatus = False
                                    break
                            elif passwordchange == "2":
                                while passwordchangestatusopt2 == True:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"Type '{Fore.RED}exit{Style.RESET_ALL}' if you would like to cancel the edit")
                                    editedpass = pwinput.pwinput("What would you like your new password to be?: ")
                                    passwordchangestatusopt3 = True
                                    if editedpass == "exit":
                                        passwordchangestatusopt2 = False
                                        passwordchangestatus = False
                                        break
                                    else:
                                        while passwordchangestatusopt3 == True:
                                            editedpassconfirm = pwinput.pwinput("Please type your new password again: ")
                                            if editedpass == editedpassconfirm:
                                                config_object.read('config.ini')
                                                config_object[section]['password'] = editedpass
                                                with open('config.ini', 'w') as conf:
                                                    config_object.write(conf)
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                print(f"{Fore.RED}Encrypting new password...{Style.RESET_ALL}")
                                                time.sleep(1)
                                                print(f"{Fore.GREEN}Password changed successfully{Style.RESET_ALL}")
                                                time.sleep(1)
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                passwordchangestatusopt2 = False
                                                passwordchangestatus = False
                                                passwordchangestatusopt3 = False
                                                break
                                            break
                                        else:
                                            print(f"{Fore.RED}Incorrect Password{Style.RESET_ALL}")
                                            time.sleep(1)
                                            passwordchangestatusopt3 = False
                                            break
                                            
                            elif passwordchange == "3":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                deletionconfirm = input(f"Please confirm that you want to delete the entry {section} [Y/N]: ").upper()
                                if deletionconfirm == "Y":
                                    print(f"{Fore.RED}Deleting Entry...{Style.RESET_ALL}")
                                    time.sleep(1)
                                    print(f"{Fore.RED}Entry Deleted{Style.RESET_ALL}")
                                    print(section)
                                    config_object.read('config.ini')
                                    config_object.remove_section(section)
                                    with open('config.ini', 'w') as conf:
                                        config_object.write(conf)
                                    time.sleep(1)
                                    passwordchangestatus = False
                                    break
                                elif deletionconfirm == "N":
                                    passwordchangestatus = False
                                    break
                                else:
                                    print("Unrecognized input, please try again.")
                                    time.sleep(1)
                            elif passwordchange == "4":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                passwordchangestatus = False
                                break
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Unrecognized input")
                                time.sleep(1)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
        accesspasswordstatus = True

    if firstchoice == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        quit()
    
    if firstchoice != 1 and 2 and 3 and 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}Invalid input{Style.RESET_ALL}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')