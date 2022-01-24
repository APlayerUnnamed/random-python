import base64, os, colorama, shutil, logging, sys
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s [%(levelname)s] %(message)s",handlers=[logging.FileHandler("debug.log")])
print(f"{colorama.Fore.YELLOW}The Developer:\nAPlayerUnnamed\nhttps://github.com/APlayerUnnamed/random-python{colorama.Fore.RESET}")
def isFile():
    theInput = input(f"{colorama.Fore.MAGENTA}\nDo you want to encode a file (y/n){colorama.Fore.YELLOW}\n>>> {colorama.Fore.RESET}")
    if theInput.lower() == "y": return True
    else:
        if theInput.lower() != "n":
            print(f"{colorama.Fore.RED}Please enter a valid answer AKA (y/n){colorama.Fore.RESET}")
            isFile()
        else: return False
if isFile():
    import pyperclip
    pyperclip.copy(os.getcwd())
    TheDir = None
    def fileGet():
        try:
            TheDir = input(f"{colorama.Fore.MAGENTA}Copied {os.getcwd()} to the clipboard\nPlease enter a directory (e.g. {os.getcwd().lower()}\\dataToEncode.txt){colorama.Fore.YELLOW}\n>>> {colorama.Fore.RESET}")
            try:
                file = open(f"{TheDir}", "r")
                data = file.readlines()
            except:
                try:
                    if os.path.exists(TheDir):
                        shutil.copy(TheDir,f"{TheDir}.txt")
                        file = open(f"{TheDir}.txt", "r")
                        logging.log(file.readlines())
                        data = file.readlines()
                except:
                    try:
                        print(f"{colorama.Fore.YELLOW}That file can not be encoded to Base64!{colorama.Fore.RESET}")
                        file.close()
                        os.remove(f"{TheDir}.txt")
                        raise Exception("13531")
                    except BaseException as e:
                        if "13531" in str(e): raise Exception("13531")
                        print(f"A Error Occurred\nDetails: \n{e}\nSee debug.log for traceback")
                        logging.exception()
                        raise Exception("13531")
            string1=""
            urlSafeEncodedBytes = base64.urlsafe_b64encode(string1.join(data).encode("utf-8"))
            urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
            file.close()
            print(f"{colorama.Fore.YELLOW}Encoded Data:{colorama.Fore.BLUE} {urlSafeEncodedStr} {colorama.Fore.RESET}")
            try: os.remove(f"{os.getcwd()}\\encoded.encode.txt")
            except: pass
            def export():
                theInputExport = input(f"{colorama.Fore.MAGENTA}Do you want to export the results to a file (y/n){colorama.Fore.YELLOW}\n>>> {colorama.Fore.RESET}")
                if theInputExport.lower() == "y": return True
                else:
                    if theInputExport.lower() != "n":
                        print(f"{colorama.Fore.RED}Please enter a valid answer AKA (y/n){colorama.Fore.RESET}")
                        export()
                    else: return False
            if export():
                try: os.remove(f"{os.getcwd()}\\encode.txt")
                except: pass
                file = file = open(f"{os.getcwd()}\\encode.txt", "a")  
                file.write(urlSafeEncodedStr)
                file.close()
                print(f"{colorama.Fore.MAGENTA}Exported results to {os.getcwd()}\\encode.txt{colorama.Fore.RESET}")
            import pyperclip
            pyperclip.copy(urlSafeEncodedStr)
            clip = pyperclip.paste()
            print(f"{colorama.Fore.MAGENTA}Copied results to the clipboard{colorama.Fore.RESET}")
            if os.path.exists(f"{TheDir}.txt"): os.remove(f"{TheDir}.txt")
        except BaseException as e:
            if "13531" in str(e): sys.exit()
            logging.error(f"{e}")
            print(f"{colorama.Fore.RED}Please enter a valid directory (e.g. {os.getcwd()}\\file.txt){colorama.Fore.RESET}")
            fileGet()
    fileGet()
else:
    data = input(f"{colorama.Fore.MAGENTA}Please enter a string (e.g. \"This program converts the users input to Base64\"){colorama.Fore.YELLOW}\n>>> {colorama.Fore.RESET}")
    urlSafeEncodedBytes = base64.urlsafe_b64encode(data.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
    print(f"{colorama.Fore.YELLOW}Encoded Data:{colorama.Fore.BLUE} {urlSafeEncodedStr} {colorama.Fore.RESET}")
    try: os.remove(f"{os.getcwd()}\\encoded.encode.txt")
    except: pass
    def export():
        theInputExport = input(f"{colorama.Fore.MAGENTA}Do you want to export the results to a file (y/n){colorama.Fore.YELLOW}\n>>> {colorama.Fore.RESET}")
        if theInputExport.lower() == "y": return True
        else:
            if theInputExport.lower() != "n":
                print(f"{colorama.Fore.RED}Please enter a valid answer (y/n){colorama.Fore.RESET}")
                export()
            else: return False
    if export():
        try: os.remove(f"{os.getcwd()}\\encode.txt")
        except: pass
        file = file = open(f"{os.getcwd()}\\encode.txt", "a")
        file.write(urlSafeEncodedStr)
        file.close()
        print(f"{colorama.Fore.MAGENTA}Exported results to {os.getcwd()}\\encode.txt{colorama.Fore.RESET}")
    import pyperclip
    pyperclip.copy(urlSafeEncodedStr)
    clip = pyperclip.paste()
    print(f"{colorama.Fore.MAGENTA}Copied results to the clipboard{colorama.Fore.RESET}")
def exitP():
    var = input(f"{colorama.Fore.MAGENTA}Press ENTER to exit...{colorama.Fore.YELLOW}\n>>> {colorama.Fore.RESET}")
    sys.exit()
logging.shutdown()
try: os.remove(f"{os.getcwd()}\\debug.log")
except: pass
exitP()
