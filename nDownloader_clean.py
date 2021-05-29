import os, requests, base64, random, string, sys
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
        print(str(base64.b64decode(sig)))
        print(Style.RESET_ALL)
    else:
        print(" [!] Error. Invalid operative system, exiting...")
        exit(1)
    URL = input(" [i] Welcome to nDownloader! Press any key to start... ")
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
    has_ended = True
    sys.stdout.write(" [-] Request for ")
    while True:
        if has_ended == True:
            nID = "".join(random.choice(string.digits) for i in range(7))
            pageNumber = 1
        nURL = "https://i.nhentai.net/galleries/" + nID + "/" + str(pageNumber) + ".jpg"
        try:
            r = requests.get(nURL, allow_redirects=True)
            images = {"image/jpeg"}
            if r.headers["content-type"] not in images:
                sys.stdout.write(nID + " is bad.")
                sys.stdout.write('\b'*15)
                sys.stdout.flush()
                has_ended = True
            elif r.headers["content-type"] in images:
                has_ended = False
                os.system("echo.> nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg")
                PATH = "nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg"
                open(str(PATH), "wb").write(r.content)
                if pageNumber == 1:
                    print()
                    sys.stdout.write('\b'*50)
                    sys.stdout.flush()
                    print(" [+] Request for " + str(nID) + " is good.")
                    sys.stdout.write(" [-] Request for ")
                pageNumber += 1
        except Exception as e:
            print(" %s%s[!] An error ocurred: %s%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL, e))
            print()
            exit(1)
except KeyboardInterrupt:
    print()
    print(" Detected Ctrl+C. Shutting down...")
    print()
    exit(1)

exit(1)