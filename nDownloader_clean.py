# nDownloader_clean  -  https://github.com/r4v10l1

try:
    import os, requests, base64, random, string, sys, time
    from colorama import Fore, Style
except Exception:
    print()
    print(" [!] There was an error importing the necesary modules: os, requests, base64, random, string, sys, time, colorama")
    print()
    exit(1)

############ EDIT ME ############
operative_system = "win"        #  << Put here win or lin
useTorProxy = False             #  << Put here True or False
#################################

def banner():
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}         _____                        __                 __             ")
    print(f"{Fore.RED} .-----.{Fore.WHITE}|     \\.-----.--.--.--.-----.|  |.-----.---.-.--|  |.-----.----.")
    print(f"{Fore.RED} |     |{Fore.WHITE}|  --  |  _  |  |  |  |     ||  ||  _  |  _  |  _  ||  -__|   _|")
    print(f"{Fore.RED} |__|__|{Fore.WHITE}|_____/|_____|________|__|__||__||_____|___._|_____||_____|__|  {Style.RESET_ALL}\n")

def main():

    try:
        banner()
        start_program = input(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE} [i] Welcome to nDownloader! Press any key to start...{Style.RESET_ALL} ")
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}     Starting at{Style.RESET_ALL}{Fore.BLUE} " + time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()) + f"{Style.RESET_ALL} ")
        with open("nDownloaded.log", "a") as nLog:  # Append to the log file
            nLog.write("[%s] User started.\n" % time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
        print()
    except KeyboardInterrupt:
        print()
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} Detected Ctrl+C. Shutting down...{Style.RESET_ALL} ")
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} Stopped at{Style.RESET_ALL}{Fore.RED} "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()) + f"{Style.RESET_ALL} ")
        with open("nDownloaded.log", "a") as nLog:  # Append to the log file
            nLog.write("[%s] User stopped.\n" % time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
        print()
        exit(1)

    if useTorProxy == False:
        proxies = ""
    elif useTorProxy == True:
        proxies = {
            'http': 'socks5://127.0.0.1:9150',
            'https': 'socks5://127.0.0.1:9150'
        }
    else:
        print()
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} [!] Error. Invalid proxy. Exiting...{Style.RESET_ALL} ")
        print()
        exit(1)

    if not os.path.isfile(os.path.realpath(__file__) + "\\nDownloads"):
        os.makedirs(os.path.realpath(__file__) + "\\nDownloads")

    has_ended = True
    first_time = True

    try:
        while True:
            if has_ended == True:
                nID = "".join(random.choice(string.digits) for i in range(6))
                nID = "1%s" % nID
                pageNumber = 1
            nURL = "https://i.nhentai.net/galleries/" + nID + "/" + str(pageNumber) + ".jpg"
            try:
                r = requests.get(nURL, proxies=proxies, allow_redirects=True)
                images = {"image/jpeg"}
                if r.headers["content-type"] not in images:
                    if first_time:
                        sys.stdout.write(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE} [{Fore.RED}-{Fore.WHITE}] Request for ")
                        first_time = False
                    sys.stdout.write(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED}{nID}" + f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE} is bad.")
                    sys.stdout.write('\b'*15)
                    sys.stdout.flush()
                    has_ended = True
                elif r.headers["content-type"] in images:
                    has_ended = False
                    if operative_system == "win":
                        os.system("echo.> nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg")  # Create the empty file on windows
                    elif operative_system == "lin":
                        os.system("touch nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg")  # Create the empty file on linux
                    else:
                    	exit(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} Operative system error. Exiting...{Style.RESET_ALL} ")
                    PATH = "nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg"
                    open(str(PATH), "wb").write(r.content)  # Write the request content (Image) into the empty file
                    if pageNumber == 1:
                        if not first_time:
                            print()
                        sys.stdout.write('\b'*50)
                        sys.stdout.flush()
                        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE} [{Fore.GREEN}+{Fore.WHITE}] Request for{Fore.GREEN} " + str(nID) + f"{Fore.WHITE} is good.{Style.RESET_ALL} ")
                        with open("nDownloaded.log", "a") as nLog:  # Append to the log file
                            nLog.write("[%s] Dowloading: %s" % (time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()), nID))  # Write the date and the ID downloaded.
                            nLog.write("\n")
                        first_time = True
                    pageNumber += 1
            except Exception as e:
                print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} [!] An error ocurred:{Style.RESET_ALL} {e}")
                print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} Stopped at{Style.RESET_ALL}{Fore.RED} "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()) + f"{Style.RESET_ALL} ")
                with open("nDownloaded.log", "a") as nLog:  # Append to the log file
                    nLog.write("[%s] Exception: %s \n" % (time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()), e))
                print()
                exit(1)
    except KeyboardInterrupt:
        sys.stdout.write('\b'*15)
        sys.stdout.flush()
        print()
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} Detected Ctrl+C. Shutting down...{Style.RESET_ALL} ")
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} Stopped at{Style.RESET_ALL}{Fore.RED} "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()) + f"{Style.RESET_ALL} ")
        with open("nDownloaded.log", "a") as nLog:  # Append to the log file
            nLog.write("[%s] User stopped.\n" % time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
        print()
        exit(1)

main()
