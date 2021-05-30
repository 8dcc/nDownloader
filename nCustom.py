import os, requests, base64, random, string, sys, time
from colorama import Fore, Style

############ EDIT ME ############
operative_system = "win"        #  << Put here win or lin
#################################

def banner():
    print("         _____                        __                 __             ")
    print(" .-----.|     \\.-----.--.--.--.-----.|  |.-----.---.-.--|  |.-----.----.")
    print(" |     ||  --  |  _  |  |  |  |     ||  ||  _  |  _  |  _  ||  -__|   _|")
    print(" |__|__||_____/|_____|________|__|__||__||_____|___._|_____||_____|__|  ")

try:
    if operative_system == "win"    :
        print()
        banner()
        print()

    elif operative_system == lin:
        print(Style.RESET_ALL, Style.BRIGHT, Fore.WHITE)
        banner()
        print(Style.RESET_ALL, Fore.MAGENTA)
        print(Style.RESET_ALL)
    else:
        print(" [!] Error. Invalid operative system, exiting...")
        exit(1)
    print("     Starting at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
    print()
except KeyboardInterrupt:
    print()
    print(" Detected Ctrl+C. Shutting down...")
    print()
    exit(1)

try:
    if operative_system == "win":
        pass
    elif operative_system == "lin":
        os.system("rm -r nDownloads")
        os.system("mkdir nDownloads")
    else:
        print()
        print(" [!] Error. Invalid operative system, exiting...")
        print()
    nID = input(" [?] Write here your image ID: ")
    if len(nID) != 7:
        print()
        print(" [!] Invalid ID. Length must be 7 . Exiting...")
        print()
        exit(1)
    pageNumber = 1
    while True:
        nURL = "https://i.nhentai.net/galleries/" + nID + "/" + str(pageNumber) + ".jpg"
        try:
            r = requests.get(nURL, allow_redirects=True)
            images = {"image/jpeg"}
            if r.headers["content-type"] not in images:
                if pageNumber == 1:
                    print()
                    print(" [!] Error. ID not found. Exiting...")
                    print()
                    exit(1)
                else:
                    print()
                    print(" [+] Done downloading. Exiting...")
                    print()
                    exit(1)
            elif r.headers["content-type"] in images:
                os.system("echo.> nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg")
                PATH = "nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg"
                open(str(PATH), "wb").write(r.content)
                if pageNumber == 1:
                    print()
                    print(" [i] Request for " + str(nID) + " is good. Downloading in " + PATH)
                pageNumber += 1
        except Exception as e:
            print(" %s%s[!] An error ocurred: %s%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL, e))
            print(" Stopped at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
            print()
            exit(1)
except KeyboardInterrupt:
    print()
    print(" Detected Ctrl+C. Shutting down...")
    print(" Stopped at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
    print()
    exit(1)

exit(1)