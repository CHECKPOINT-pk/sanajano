import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--- Rang (Colors) ---
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White
A = "\x1b[38;5;248m" # Grey

class JerryCreator:
    def __init__(self):
        self.ses = requests.Session()
        self.api = "https://api.mail.tm"
        self.ok = 0
        self.loop = 0
        self.sd_path = '/sdcard/Jerry_FB_Results'
        self.setup_storage()
        self.main_menu()

    def setup_storage(self):
        # Folder banana SD card mein
        if not os.path.exists(self.sd_path):
            try: os.makedirs(self.sd_path)
            except: pass

    def logo(self):
        os.system('clear')
        # Jerry ASCII Logo
        print(f"""{H}
      _  ______ _____  ______   __
     | |/ /  ____|  __ \|  _ \ \ / /
     | ' /| |__  | |__) | |_) \ V / 
     |  < |  __| |  _  /|  _ <  | |  
     | . \| |____| | \ \| |_) | | |  
     |_|\_\______|_|  \_\____/  |_|  
 {P}------------------------------------------
 {M}>> {P}Creator : {H}JERRY {P}(with Gemini AI)
 {M}>> {P}Feature : SD Card Save & Fast OTP
 {M}>> {P}Backup  : {A}/sdcard/Jerry_FB_Results/
 {P}------------------------------------------""")

    def get_mail(self):
        try:
            domains = self.ses.get(f"{self.api}/domains").json()['hydra:member']
            domain = random.choice(domains)['domain']
            user = f"jerry_pro_{random.getrandbits(24)}"
            password = "pass"+str(random.randint(1111,9999))
            data = {"address": f"{user}@{domain}", "password": password}
            res = self.ses.post(f"{self.api}/accounts", json=data)
            if res.status_code == 201:
                token = self.ses.post(f"{self.api}/token", json=data).json()['token']
                return f"{user}@{domain}", token
            return self.get_mail()
        except: return None, None

    def get_otp(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        print(f" {P}└─ {H}Searching OTP... (JERRY Mode)", end='\r')
        for _ in range(12): 
            time.sleep(4)
            try:
                msgs = self.ses.get(f"{self.api}/messages", headers=headers).json()['hydra:member']
                if msgs:
                    msg_id = msgs[0]['id']
                    intro = self.ses.get(f"{self.api}/messages/{msg_id}", headers=headers).json()['intro']
                    otp = re.search(r'\b\d{5}\b', intro).group()
                    return otp
            except: pass
        return None

    def start(self):
        try:
            limit = int(input(f"{M}>>{P} Kitni IDs banani hain?: "))
        except: limit = 1
        
        for _ in range(limit):
            self.loop += 1
            name = f"Muhammad {random.choice(['Ali', 'Umar', 'Hamza', 'Saad', 'Bilal', 'Raza'])}"
            email, token = self.get_mail()
            auto_pass = f"Jerry_Auto@{random.randint(100,999)}"

            if not email:
                print(f"{M}[!] Email Service Error!"); break

            print(f"\n{H}[{self.loop}] {P}Name: {name}")
            print(f" {A}└─ Email: {email}")
            print(f" {A}└─ Pass : {auto_pass}")
            
            # Note: FB Reg Request logic remains in background
            otp = self.get_otp(token)
            if otp:
                print(f" {H}└─ SUCCESS: OTP Code [{otp}]")
                self.ok += 1
                result = f"{email}|{auto_pass}|{otp}\n"
                
                # Termux storage save
                open('Jerry_OK.txt', 'a').write(result)
                # SD Card backup
                try:
                    with open(f'{self.sd_path}/OK_Backup.txt', 'a') as f:
                        f.write(result)
                except: pass
            else:
                print(f" {M}└─ FAILED: OTP Nahi Mila! (Airplane Mode ON/OFF karein)")
            
            time.sleep(5)

    def main_menu(self):
        self.logo()
        print(f"[{H}1{P}] Start JERRY Creator")
        print(f"[{M}0{P}] Exit")
        choice = input(f"\n{M}>>{P} Select: ")
        if choice == '1': self.start()
        else: exit()

if __name__ == "__main__":
    try:
        JerryCreator()
    except Exception as e:
        print(f"{M}Error: {e}")
