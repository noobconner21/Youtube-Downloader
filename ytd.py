from pytube import YouTube
from time import sleep
import os
import time



def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(.01)
        
        
r='\033[1;31m' 
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m' 

os.system('clear')
# def main() :
print ('\n')
printLow(f"""\n{y}                  █▄█ █▀█ █░█ ▀█▀ █░█ █▄▄ █▀▀          
                  ░█░ █▄█ █▄█ ░█░ █▄█ █▄█ ██▄""")
print("\n ")
printLow(f"""\n{g}          
          █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
          █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄""")
printLow(f"""\n\n   {r}                   Project SSLaB LK™""")
    
print('\n')   
link = input(f'\n\n{g}[?] {y}Link{r}- {w}')
if "https://" not in link :
    printLow(f"\n{g}[-] {r}Enter Youtube link or Video")
    link = input(f'\n\n{g}[?] {y}Enter Link{r}- {w}')
kir = YouTube(link)


printLow(f"""\n{y}Info:
    {g}[+] {y}Video Name : {w}({kir.title})
    {g}[+] {y}Video Views : {w}({kir.views})
    {g}[+] {y}Video Length (sec): {w}({kir.length})
""")



x = input(f'\n{g}[?] {r}You want a Download (Y/n) {y}- {w}')
if x.lower() == "y" :
    printLow(f"\n{g}[+] {y}Downloading...\n")
    ys = kir.streams.get_highest_resolution()
    ys.download()
    printLow(f"{g}[+] {y}Completed !\n")
elif x.lower() == "n" :
    printLow(f"\n{g}[-] {r}Abort !\n")
else:
    printLow(f"{r}Errorأ!\n")
    
    
        # time.sleep(2)
        # exit(1337)
    
    # print (main)
    
# print (main)
import time
time.sleep(2)
exit(1337)

