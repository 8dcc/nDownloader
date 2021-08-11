import os, requests, base64, random, string, sys, time
from colorama import Fore, Style
from bs4 import BeautifulSoup

############ EDIT ME ############
operative_system = "win"        #  << Put here win or lin
#################################

def ask_text(text):
    return input(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE} [?] {text}{Style.RESET_ALL}")
def info_text(text):
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE} [i] {text}{Style.RESET_ALL}")
def error_text(text):
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED} [!] {text}{Style.RESET_ALL}")
def success_text(text):
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN} [+] {text}{Style.RESET_ALL}")

def start_time():
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}        Starting at {Style.RESET_ALL}{Fore.RED}" + time.strftime(f"%d %b %Y {Style.BRIGHT}{Fore.WHITE}-{Style.RESET_ALL}{Fore.RED} %H:%M:%S{Style.RESET_ALL}", time.gmtime()))
def stop_time():
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}     Stopped at {Style.RESET_ALL}{Fore.GREEN}" + time.strftime(f"%d %b %Y {Style.BRIGHT}{Fore.WHITE}-{Style.RESET_ALL}{Fore.GREEN} %H:%M:%S{Style.RESET_ALL}", time.gmtime()))
def stop_time_bad():
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}     Stopped at {Style.RESET_ALL}{Fore.RED}" + time.strftime(f"%d %b %Y {Style.BRIGHT}{Fore.WHITE}-{Style.RESET_ALL}{Fore.RED} %H:%M:%S{Style.RESET_ALL}", time.gmtime()))

def banner():
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}         _____                        __                 __             ")
    print(f"{Fore.RED} .-----.{Fore.WHITE}|     \\.-----.--.--.--.-----.|  |.-----.---.-.--|  |.-----.----.")
    print(f"{Fore.RED} |     |{Fore.WHITE}|  --  |  _  |  |  |  |     ||  ||  _  |  _  |  _  ||  -__|   _|")
    print(f"{Fore.RED} |__|__|{Fore.WHITE}|_____/|_____|________|__|__||__||_____|___._|_____||_____|__|  {Style.RESET_ALL}")
    start_time()
    print()

def main():
    banner()

    if not os.path.exists(os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/nDownloads"):
        os.makedirs(os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/nDownloads")

    pageNumber = 1

    try:
        nID = ask_text("Write here your sauce/image ID: ")
        user_sauce = nID  # This will be used to make the folder

        try:
            int(nID)
        except ValueError:
            error_text("Invalid ID type, must be a number. Exiting...")
            print()
            exit(1)

        if len(nID) != 6 and len(nID) != 7:
            error_text("Invalid ID lenght, must be 6 or 7. Exiting...")
            print()
            exit(1)

        if len(nID) == 6:  # Get the image id from the sauce page
            URL = "https://nhentai.net/g/" + nID + "/1/"
            r = requests.get(URL)
            souped = BeautifulSoup(r.text, 'html.parser')
            try:
                nID = souped.findAll('img')[1].get('src').split("/")[4]
            except Exception as e:
                error_text("ID error. Check nCustom_debug.log for details.")
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
                        error_text("ID not found. Exiting...")
                        print()
                        exit(1)
                    else:
                        success_text("Done downloading. Exiting...")  # Once we dont get more images, the download is done and we can exit
                        stop_time()
                        exit(1)
                elif r.headers["content-type"] in images:
                    if pageNumber == 1:  # If the page we are downloading is the first one (AKA this will execute once per id)
                        if not os.path.exists(os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/nDownloads/" + str(user_sauce)):
                            os.makedirs(os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/nDownloads/" + str(user_sauce))
                        info_text(f"[{str(user_sauce)}] Request for {str(nID)} is good. Downloading in \'/nDownloads/{str(user_sauce)}/\'") # Display that all went good

                    PATH = "nDownloads/" + str(user_sauce) + "/" + str(user_sauce) + "_" + str(pageNumber) + ".jpg"  # Store the path in a variable
                    open(str(PATH), "wb").write(r.content)  # Write the contents on the files


                    pageNumber += 1  # Adds a page number which will be downloaded in the loop
            except Exception as e:  # If there is an error
                error_text("An error ocurred: %s" % (e))
                stop_time_bad()
                print()
                exit(1)
    except KeyboardInterrupt:  # If the user ctrl + c during the loop / download
        error_text("Detected Ctrl+C. Shutting down...")
        stop_time_bad()
        print()
        exit(1)

main()
