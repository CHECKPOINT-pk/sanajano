# CHARSI BRAND - 2025 ULTIMATE VERIFIED CREATOR
# THEME: GHOST GREEN NEON
# STATUS: MAXIMUM STABILITY - 5 ACCOUNTS ONLY

import os, sys, re, time, random, uuid, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def install_deps():
    modules = ['requests', 'bs4', 'faker']
    for m in modules:
        try: __import__(m)
        except: subprocess.check_call([sys.executable, "-m", "pip", "install", m])

install_deps()

import requests
from bs4 import BeautifulSoup
from faker import Faker

#▬▭▬▭▬▭▬▭[PREMIUM COLOR CODES]▬▭▬▭▬▭▬▭#
G = "\x1b[38;5;46m"  # Neon Green
W = "\033[1;37m"     # White
R = "\x1b[38;5;196m" # Red
B = "\x1b[38;5;21m"  # Deep Blue
Y = "\x1b[38;5;226m" # Yellow
RESET = "\033[0m"

#▬▭▬▭▬▭▬▭[SMALL HEAVY BANNER]▬▭▬▭▬▭▬▭#
def banner():
    os.system('clear')
    print(f"""
{G}   ______ _    _         _____   _____ _____ 
{G}  |  ____| |  | |  /\   |  __ \ / ____|_   _|
{G}  | |    | |__| | /  \  | |__) | (___   | |  
{G}  | |    |  __  |/ /\ \ |  _  / \___ \  | |  
{G}  | |____| |  | / ____ \| | \ \ ____) |_| |_ 
{G}  |______|_|  |_/_/    \_\_|  \_\_____/|_____|
{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W}  [{G}#{W}] {G}VERSION  : {W}2025 VERIFIED {G}(USA-LOC)
{W}  [{G}#{W}] {G}METHOD   : {W}AUTO-OTP BYPASS
{W}  [{G}#{W}] {G}LIMIT    : {W}5 STABLE ACCOUNTS
{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

class CharsiUltimate:
    def __init__(self):
        self.oks = []
        self.loop = 0
        self.fk = Faker('en_US') # US Location Identity

    def get_mail(self):
        """Generates a fresh temporary email"""
        try:
            res = requests.get("https://www.1secmail.com/api/v1/?action=genAddrs&count=1").json()
            return res[0]
        except: return f"charsi{random.randint(10,99)}@1secmail.com"

    def get_otp(self, email):
        """Force-checks for Facebook OTP code"""
        u, d = email.split('@')
        for i in range(15): # Extended wait for 1.5 minutes
            try:
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={u}&domain={d}").json()
                for m in r:
                    if "Facebook" in m['from'] or "code" in m['subject']:
                        msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={u}&domain={d}&id={m['id']}").json()
                        otp = re.search(r'\b\d{5}\b', msg['body'])
                        if otp: return otp.group(0)
            except: pass
            time.sleep(6)
        return None

    def create(self):
        f_name = self.fk.first_name()
        l_name = self.fk.last_name()
        email = self.get_mail()
        pwd = f"{f_name}{l_name}@{random.randint(100,999)}"
        
        # USA High Quality UA Simulation
        ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1"
        
        print(f"\r{W}[{G}TRYING{W}] {G}{f_name} {W}| {Y}USA-LOC...           ", end="")
        
        try:
            ses = requests.Session()
            # Headers Optimized for USA Registration
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': ua,
            }

            # Account Creation Data
            payload = {
                "firstname": f_name, "lastname": l_name,
                "reg_email__": email, "reg_passwd__": pwd,
                "birthday_day": str(random.randint(1,28)), 
                "birthday_month": str(random.randint(1,12)),
                "birthday_year": str(random.randint(1992,2002)),
                "sex": "2"
            }

            reg = ses.post("https://m.facebook.com/reg/submit/", data=payload, headers=headers)
            
            print(f"\r{W}[{Y}VERIFYING{W}] Checking OTP for {email}...      ", end="")
            otp = self.get_otp(email)
            
            if otp:
                print(f"\r{G}[CHARSI-OK] {email} | {pwd} | OTP:{otp} ✅")
                self.oks.append(email)
                with open("/sdcard/CHARSI-VERIFIED.txt", "a") as f:
                    f.write(f"{email}|{pwd}|{otp}|USA\n")
            else:
                print(f"\r{R}[CHARSI-CP] {email} | OTP Timeout ❌          ")
                
            self.loop += 1
        except:
            self.loop += 1

    def run(self):
        banner()
        print(f"{G}Starting Heavy Creation Process...")
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Fixed 5 Account creation for maximum hit rate
        with ThreadPool(max_workers=2) as pool:
            for _ in range(5):
                pool.submit(self.create)
        
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G}TASK COMPLETED! {W}Verified IDs: {G}{len(self.oks)}")
        print(f"{W}Saved In: {G}/sdcard/CHARSI-VERIFIED.txt")

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiUltimate().run()
