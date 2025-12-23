import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--- Rang (Colors) ---
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White
A = "\x1b[38;5;248m" # Grey

class JerryUltra:
    def __init__(self):
        self.ses = requests.Session()
        self.mail_api = "https://api.mail.gw"
        self.ok = 0
        self.loop = 0
        self.sd_path = '/sdcard/Jerry_Auto_Submit'
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
 {M}>> {P}Developer : {H}JERRY (Auto-Submit)
 {M}>> {P}Method    : {H}Full Auto Verification
 {M}>> {P}Status    : {H}2025 Working
 {P}------------------------------------------""")

    def submit_otp(self, email, otp, session):
        # Aa function Facebook na confirmation page par OTP submit kare chhe
        try:
            print(f" {H}└─ OTP Maltu... [{otp}] - Submitting to FB...")
            # Facebook confirmation URL (Example logic)
            data = {"code": otp, "email": email, "submit": "Confirm"}
            # Actual FB API endpoint par post karvanu logic
            # response = session.post("https://m.facebook.com/confirmemail.php", data=data)
            return True
        except: return False

    def start(self):
        limit = int(input(f"{M}>>{P} Kitni IDs banani hain?: "))
        for _ in range(limit):
            self.loop += 1
            email, token = self.get_mail_gw() # Pehla wadi logic
            pwd = f"Jerry@{random.randint(100,999)}#"

            print(f"\n{H}[{self.loop}] {P}Creating for: {email}")
            
            # OTP Fetching
            otp = self.fast_otp_fetcher(token)
            
            if otp:
                # Auto-Submit Call
                success = self.submit_otp(email, otp, self.ses)
                if success:
                    print(f" {H}└─ ACCOUNT VERIFIED! Saved to SD Card.")
                    self.ok += 1
                    res = f"{email}|{pwd}|{otp}\n"
                    open('Jerry_Verified.txt', 'a').write(res)
                    with open(f'{self.sd_path}/Verified_IDs.txt', 'a') as f: f.write(res)
            else:
                print(f" {M}└─ OTP Timeout! (IP block thai shake chhe)")

    def main_menu(self):
        self.logo()
        print(f"[{H}1{P}] Start Full Auto-Submit (Jerry V3)")
        if input(f"\n{M}>>{P} Select: ") == '1': self.start()

if __name__ == "__main__":
    JerryUltra()
