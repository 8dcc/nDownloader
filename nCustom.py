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

except KeyboardInterrupt:  # Detects if user ctrl + c while checking the os
    print()
    print(" Detected Ctrl+C. Shutting down...")
    print()
    exit(1)

try:
    if operative_system == "win":
        pass  # I'm too lazy to check if the folder exists
    elif operative_system == "lin":
        os.system("rm -r nDownloads")  # Remove the folder
        os.system("mkdir nDownloads")  # Make the folder
    print()
    nID = input(" [?] Write here your image ID: ")  # The image ID, not the sauce. See README.md to see what I mean
    if len(nID) != 7:  # Check if the ID length is 7
        print()
        print(" [!] Invalid ID. Length must be 7 . Exiting...")
        print()
        exit(1)
    pageNumber = 1  # Start by trying to download page 1 before the loop adds more pages
    while True:
        nURL = "https://i.nhentai.net/galleries/" + nID + "/" + str(pageNumber) + ".jpg"  # Base URL + ID + number.jpg
        try:
            r = requests.get(nURL, allow_redirects=True)
            images = {"image/jpeg"}  # Check if the request gives a image (AKA the id is correct and there are no erros)
            if r.headers["content-type"] not in images:  # Check if we did not get an image from the request
                if pageNumber == 1:  # If the request did not get an image and the page is 1.
#                                      That means it didnt download a single page, so the id is wrong.
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
                os.system("echo.> nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg")  # ID + _ + number.jpg  -->  1233212_5.jpg
                PATH = "nDownloads/" + str(nID) + "_" + str(pageNumber) + ".jpg"  # Same as above
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