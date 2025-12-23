import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--- Colors ---
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White
A = "\x1b[38;5;248m" # Grey

class JerryUltra:
    def __init__(self):
        self.ses = requests.Session()
        # Nayi aur fast API services ka backup list
        self.apis = ["https://api.mail.tm", "https://api.mail.gw"]
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
 {M}>> {P}Developer : {H}JERRY (Ultra Fix)
 {M}>> {P}Task      : {H}Multi-Mail & Number Mode
 {M}>> {P}Status    : {H}2026 Updated Logic
 {P}------------------------------------------""")

    def get_private_mail(self):
        # Service rotator taake agar ek block ho to doosri chale
        api = random.choice(self.apis)
        try:
            dom_res = self.ses.get(f"{api}/domains", timeout=10).json()
            # Sabse naya domain uthana
            domain = dom_res['hydra:member'][-1]['domain']
            user = f"jerry_pro_{random.getrandbits(32)}"
            password = "jerry_auto_pass"
            
            data = {"address": f"{user}@{domain}", "password": password}
            res = self.ses.post(f"{api}/accounts", json=data)
            
            if res.status_code == 201:
                token = self.ses.post(f"{api}/token", json=data).json()['token']
                return f"{user}@{domain}", token, api
            return self.get_private_mail()
        except: return None, None, None

    def fast_otp_fetcher(self, token, api):
        headers = {"Authorization": f"Bearer {token}"}
        print(f" {P}└─ {H}JERRY Waiting for Code (Auto-Refresh)... ", end='\r')
        
        for _ in range(20): # 80 seconds wait
            time.sleep(4)
            try:
                msgs = self.ses.get(f"{api}/messages", headers=headers).json()['hydra:member']
                if msgs:
                    m_id = msgs[0]['id']
                    msg_data = self.ses.get(f"{api}/messages/{m_id}", headers=headers).json()
                    body = msg_data['intro']
                    otp = re.search(r'\b\d{5}\b', body).group()
                    return otp
            except: pass
        return None

    def start_creation(self):
        limit = int(input(f"{M}>>{P} Kitni IDs banani hain?: "))
        for _ in range(limit):
            self.loop += 1
            name = f"Muhammad {random.choice(['Ali', 'Hamza', 'Umar', 'Usman', 'Waqas', 'Bilal'])}"
            email, token, active_api = self.get_private_mail()
            pwd = f"Jerry_Auto@{random.randint(11,99)}#"

            if not email:
                print(f"{M}[!] API Response Nahi De Rahi. Airplane Mode ON/OFF!"); break

            print(f"\n{H}[{self.loop}] {P}Creating: {name}")
            print(f" {A}└─ Email: {email}")
            print(f" {A}└─ Pass : {pwd}")

            otp = self.fast_otp_fetcher(token, active_api)
            
            if otp:
                print(f" {H}└─ OTP SUCCESS: {otp}")
                self.ok += 1
                result = f"{email}|{pwd}|{otp}\n"
                open('Jerry_Verified.txt', 'a').write(result)
                with open(f'{self.sd_path}/Success_IDs.txt', 'a') as f: f.write(result)
            else:
                print(f" {M}└─ OTP FAILED: Facebook ne code nahi bheja.")
            
            time.sleep(5)

    def main_menu(self):
        self.logo()
        print(f"[{H}1{P}] Start Auto Account (New Private Mail)")
        print(f"[{H}2{P}] USA/Country Number Mode (Format Only)")
        print(f"[{M}0{P}] Exit")
        
        opt = input(f"\n{M}>>{P} Select: ")
        if opt == '1': self.start_creation()
        elif opt == '2':
            print(f"\n{M}[!] {P}Note: Number creation ke liye apko SMS API keys chahiye hongi.")
            print(f"{A}USA Numbers Format: +1 (XXX) XXX-XXXX")
            time.sleep(3); self.main_menu()
        else: exit()

if __name__ == "__main__":
    JerryUltra()
