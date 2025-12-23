import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--- Colors ---
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White
A = "\x1b[38;5;248m" # Grey

class JerryAutoOnly:
    def __init__(self):
        self.ses = requests.Session()
        self.ok = 0
        self.loop = 0
        self.sd_path = '/sdcard/Jerry_Created_IDs'
        self.setup_folder()
        self.main_menu()

    def setup_folder(self):
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
 {M}>> {P}Developer : {H}JERRY (Auto-Mode)
 {M}>> {P}Task      : {H}Facebook Account Creator
 {M}>> {P}Storage   : {H}/sdcard/Jerry_Created_IDs/
 {P}------------------------------------------""")

    def get_mail(self):
        # Best Mail API for 2025
        try:
            api_list = ["https://api.mail.tm", "https://api.mail.gw"]
            api = random.choice(api_list)
            dom_res = self.ses.get(f"{api}/domains").json()
            domain = random.choice(dom_res['hydra:member'])['domain']
            user = f"jerry_{random.randint(111111,999999)}"
            password = "jerry_pass_123"
            data = {"address": f"{user}@{domain}", "password": password}
            res = self.ses.post(f"{api}/accounts", json=data)
            if res.status_code == 201:
                token = self.ses.post(f"{api}/token", json=data).json()['token']
                return f"{user}@{domain}", token, api
            return self.get_mail()
        except: return None, None, None

    def fetch_otp(self, token, api):
        headers = {"Authorization": f"Bearer {token}"}
        print(f" {P}└─ {H}JERRY is waiting for OTP...", end='\r')
        for _ in range(15):
            time.sleep(4)
            try:
                msgs = self.ses.get(f"{api}/messages", headers=headers).json()['hydra:member']
                if msgs:
                    m_id = msgs[0]['id']
                    msg_content = self.ses.get(f"{api}/messages/{m_id}", headers=headers).json()['intro']
                    otp = re.search(r'\b\d{5}\b', msg_content).group()
                    return otp
            except: pass
        return None

    def start(self):
        self.logo()
        try:
            limit = int(input(f" {M}>> {P}How many IDs?: "))
        except: limit = 1
        
        for _ in range(limit):
            self.loop += 1
            name = f"Muhammad {random.choice(['Ali', 'Hamza', 'Saad', 'Usman', 'Waqas'])}"
            email, token, active_api = self.get_mail()
            pwd = f"Jerry@{random.randint(11,99)}Pak"

            if not email:
                print(f"{M}[!] Mail API error. Use Airplane Mode."); break

            print(f"\n{H}[{self.loop}] {P}Target: {name}")
            print(f" {A}└─ Email: {email}")
            print(f" {A}└─ Pass : {pwd}")

            otp = self.fetch_otp(token, active_api)
            if otp:
                print(f" {H}└─ SUCCESS: OTP IS {otp}")
                self.ok += 1
                info = f"{email}|{pwd}|{otp}\n"
                open('Jerry_OK.txt', 'a').write(info)
                with open(f'{self.sd_path}/Verified.txt', 'a') as f: f.write(info)
            else:
                print(f" {M}└─ FAILED: OTP not received.")
            
            time.sleep(5)

    def main_menu(self):
        self.logo()
        print(f" [{H}1{P}] Start Auto Account Creator")
        print(f" [{M}0{P}] Exit")
        if input(f"\n {M}>> {P}Select: ") == '1': self.start()

if __name__ == "__main__":
    JerryAutoOnly()
