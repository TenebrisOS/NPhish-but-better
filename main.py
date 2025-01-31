import os, sys, time, socket, argparse, json
from os import popen, system
from time import sleep
from subprocess import run
from server import requirements

version = "TenebrisOS edition"
# ANSI COLOURS
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
wr="\x1b[93;99;95m"

root= popen("cd $HOME && pwd").read().strip()

# SYMBOLS
ask = green + '[' + white + '?' + green + '] '+ blue
success = yellow + '[' + white + '√' + yellow + '] '+green
error = blue + '[' + white + '!' + blue + '] '+red
info= yellow + '[' + white + '+' + yellow + '] '+ cyan
info2= green + '[' + white + '•' + green + '] '+ purple
nrml=white

sites=[]
files=os.listdir("sites/")
for file in files:
    if file.endswith(".json"):
        sites.append(file)
# print(sites)

# Website chooser
def options(list):
    print("\n"+ask+"Choose one of the following sites :\n"+nrml)
    i=0
    for site in list:
        i+=1
        print(blue+str(i)+nrml+" "+site.partition(".")[0].capitalize())

    choice=list[int(input("\n"+info2+"#user> "+nrml))-1]
    # print(choice)
    return choice

# socket.setdefaulttimeout(30)
def check_intr(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"No internet!")
        time.sleep(2)
        check_intr()


# MAIN FUNCTION
def main(port, mode):
    while True:
        if os.path.exists(root+"/.site"):
            system("rm -rf $HOME/.site && cd $HOME && mkdir .site")
            break
        else:
            system("cd $HOME && mkdir .site")
            break
    while True:
        choice=options(sites)
        if choice != None or " " or "":
            try:
                with open("sites/"+choice) as phs:
                    json_phis=json.load(phs)
                choicesnbr=[]
                for choice0 in json_phis:
                    choicesnbr.append(choice0)
                choices=[]
                for choice00 in choicesnbr:
                    choices.append(json_phis[choice00])
                choice1=options(choicesnbr)
                # print(choice0)
                # print(choicesnbr)
                # print(choice1)
                # print(json_phis[choice1])
                requirements(folder=json_phis[choice1], port=port, mode=mode)
            except:
                print("\n"+error+"Wrong input!"+nrml)
                main(port, mode)
        else:
            print("\n"+error+"Wrong input"+nrml)
            main(port, mode)

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        print("No port mentioned, launch with port argument at the end")
        exit()
    try:
        args2=str(sys.argv[2])
        if args2 == "cloudflare":
            mode=1
            from ngrock_cloudflare import cld_ngr_install
            cld_ngr_install()
        elif args2 != "cloudflare":
            print("Unknown command! Check out the Github page for usage.")
            exit()
    except:
        mode=0
    print("Version: ", version)
    print("Main creator: CodingSangh")
    print("Editor: TenebrisOS")
    main(port, mode)