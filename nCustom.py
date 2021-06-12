import os, requests, base64, random, string, sys, time
from colorama import Fore, Style
from bs4 import BeautifulSoup

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

    elif operative_system == "lin":  # Same as before but with colorama.
        print(Style.RESET_ALL, Style.BRIGHT, Fore.WHITE)
        banner()
        print(Style.RESET_ALL, Fore.MAGENTA)
        print(str(base64.b64decode(sig)))
        print(Style.RESET_ALL)
    else:
        print(" [!] Error. Invalid operative system, exiting...")  # If operative_system is not win or lin
        exit(1)
    print("     Starting at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))

except KeyboardInterrupt:
    print()
    print(" Detected Ctrl+C. Shutting down...")
    print()
    exit(1)

try:
    if operative_system == "lin":
        os.system("rm -r nDownloads")
        os.system("mkdir nDownloads")
    print()
    nID = input(" [?] Write here your sauce/image ID: ")
    if len(nID) != 6 and len(nID) != 7:
        print()
        print(" [!] Invalid ID. Length must be 7 . Exiting...")
        print()
        exit(1)
    pageNumber = 1
    if len(nID) == 6:  # Get the image id from the sauce page
        URL = "https://nhentai.net/g/" + nID + "/1/"
        r = requests.get(URL)
        souped = BeautifulSoup(r.text, 'html.parser')
        try:
            nID = souped.findAll('img')[1].get('src').split("/")[4]
        except Exception as e:
            print(" ID error. Check nCustom_debug.log for details.")
            with open("nCustom_debug.log", "w") as nLog:
                nLog.write(e)
            exit(1)
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
                    print(" [+] Done downloading. Exiting...")  # Once we dont get more images, the download is done and we can exit
                    print(" Stopped at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))  # Display when the program stopped
                    exit(1)
            elif r.headers["content-type"] in images:
                if operative_system == "win":
                    os.system("echo.> nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg")  # Create the empty file on windows
                elif operative_system == "lin":
                    os.system("touch nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg")  # Create the empty file on linux
                else:
                    exit(" Operative system error. Exiting...")
                PATH = "nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg"  # Store the path in a variable
                open(str(PATH), "wb").write(r.content)  # Write the contents on the files
                if pageNumber == 1:  # If the page we are downloading is the first one (AKA this will execute once per id)
                    print()
                    print(" [i] Request for " + str(nID) + " is good. Downloading in " + PATH)  # Display that all went good
                pageNumber += 1  # Adds a page number which will be downloaded in the loop
        except Exception as e:  # If there is an error
            print(" [!] An error ocurred: %s" % (e))
            print(" Stopped at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))  # Display when the program stopped
            print()
            exit(1)
except KeyboardInterrupt:  # If the user ctrl + c during the loop / download
    print()
    print(" Detected Ctrl+C. Shutting down...")
    print(" Stopped at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))  # Display when the program stopped
    print()
    exit(1)

exit(1)
