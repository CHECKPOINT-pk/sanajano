import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--- Colors ---
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White
A = "\x1b[38;5;248m" # Grey

class JerryPro:
    def __init__(self):
        self.ses = requests.Session()
        self.mail_api = "https://api.mail.gw" # Sabse fast service 2025 ki
        self.ok = 0
        self.loop = 0
        self.sd_path = '/sdcard/Jerry_Verified_IDs'
        self.setup_env()
        self.main_menu()

    def setup_env(self):
        if not os.path.exists(self.sd_path):
            try: os.makedirs(self.sd_path)
            except: pass

    def logo(self):
        os.system('clear')
        print(f"""{H}
      _ ______ _____  ______     __
     | |  ____|  __ \|  _ \ \   / /
     | | |__  | |__) | |_) \ \_/ / 
 _   | |  __| |  _  /|  _ < \   /  
| |__| | |____| | \ \| |_) | | |   
 \____/|______|_|  \_\____/  |_|   
 {P}------------------------------------------
 {M}>> {P}Developer : {H}JERRY (Power Mode)
 {M}>> {P}Feature   : {H}Auto-OTP Submission
 {M}>> {P}Mail      : {H}Mail.gw (High Success)
 {P}------------------------------------------""")

    def get_mail_gw(self):
        try:
            # Domain nikalna
            dom_res = self.ses.get(f"{self.mail_api}/domains").json()
            domain = dom_res['hydra:member'][0]['domain']
            user = f"jerry_{random.randint(111111,999999)}"
            password = "jerry_auto_pass"
            
            # Account banana
            data = {"address": f"{user}@{domain}", "password": password}
            res = self.ses.post(f"{self.mail_api}/accounts", json=data)
            
            if res.status_code == 201:
                # Token lena verification ke liye
                token = self.ses.post(f"{self.mail_api}/token", json=data).json()['token']
                return f"{user}@{domain}", token
            return self.get_mail_gw()
        except: return None, None

    def fast_otp_fetcher(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        print(f" {P}└─ {H}JERRY Checking Inbox... ", end='\r')
        
        # 10 martaba check karega har 4 second baad
        for _ in range(15):
            time.sleep(4)
            try:
                msgs = self.ses.get(f"{self.mail_api}/messages", headers=headers).json()['hydra:member']
                if msgs:
                    m_id = msgs[0]['id']
                    # Pura message download karna
                    msg_data = self.ses.get(f"{self.mail_api}/messages/{m_id}", headers=headers).json()
                    body = msg_data['intro']
                    # 5 digit FB code find karna
                    otp = re.search(r'\b\d{5}\b', body).group()
                    return otp
            except: pass
        return None

    def start(self):
        limit = int(input(f"{M}>>{P} Kitni IDs banani hain?: "))
        for _ in range(limit):
            self.loop += 1
            name = f"Muhammad {random.choice(['Ali', 'Hamza', 'Umar', 'Usman', 'Waqas'])}"
            email, token = self.get_mail_gw()
            pwd = f"Jerry@{random.randint(100,999)}#"

            if not email:
                print(f"{M}[!] Mail service block hai. Airplane mode ON karein."); break

            print(f"\n{H}[{self.loop}] {P}Target: {name}")
            print(f" {A}└─ Email: {email}")
            print(f" {A}└─ Password: {pwd}")

            # --- AUTO OTP FETCH ---
            otp = self.fast_otp_fetcher(token)
            
            if otp:
                print(f" {H}└─ OTP SUCCESS: {otp} (Applying...)")
                self.ok += 1
                result = f"{email}|{pwd}|{otp}\n"
                # Saving
                open('Jerry_Live.txt', 'a').write(result)
                with open(f'{self.sd_path}/Success_IDs.txt', 'a') as f:
                    f.write(result)
                print(f" {H}└─ ID Saved to SD Card!")
            else:
                print(f" {M}└─ OTP FAILED: Code nahi aaya.")
            
            time.sleep(5)

    def main_menu(self):
        self.logo()
        print(f"[{H}1{P}] Start Auto-Creation (JERRY V2)")
        print(f"[{M}0{P}] Exit")
        if input(f"\n{M}>>{P} Select: ") == '1': self.start()

if __name__ == "__main__":
    JerryPro()
