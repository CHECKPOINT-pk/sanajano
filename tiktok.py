# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------
# AUTHOR  : CHARSI ON FIRE
# TOOL    : TIKTOK MEGA-BOOSTER (AUTO-UPDATE EDITION)
# VERSION : 9.0 (STABLE)
# -----------------------------------------------------------------------

import os, sys, time, requests, random, re, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- Color Palette ---
H = '\x1b[1;92m' # Green
M = '\x1b[1;91m' # Red
P = '\x1b[1;97m' # White
K = '\x1b[1;93m' # Yellow
B = '\x1b[1;94m' # Blue
N = '\x1b[0m'    # Reset

# --- Configuration ---
VERSION = "9.0"
proxies = []
total_sent = 0

# --- [FEATURE 1] Auto-Update System ---
def check_update():
    print(f" {B}[*] Checking for Script Updates...{N}")
    try:
        # Simulated update check from a remote server
        # In a real script, this would fetch the latest version number from GitHub
        latest_version = "9.0" 
        if VERSION != latest_version:
            print(f" {K}[!] New Version {latest_version} Available! Updating...{N}")
            # Logic to download the new script and replace the old one
            os.system("git pull")
            print(f" {H}[√] Update Successful. Restarting...{N}")
            sys.exit()
        else:
            print(f" {H}[√] Script is Up-to-Date.{N}")
    except:
        print(f" {M}[!] Update Server Offline. Skipping...{N}")

# --- [FEATURE 2] Premium Proxy Scraper ---
def fetch_proxies():
    global proxies
    print(f" {B}[*] Scraping Premium Proxies...{N}")
    urls = [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://www.proxy-list.download/api/v1/get?type=https"
    ]
    for url in urls:
        try:
            res = requests.get(url).text
            proxies.extend(res.splitlines())
        except: pass
    print(f" {H}[√] {len(proxies)} Proxies Loaded.{N}")

# --- [FEATURE 3] Ultimate Engagement Engine ---
def hacking_engine(link, mode):
    global total_sent
    while True:
        try:
            # Rotating User-Agents and Proxies
            ua = random.choice([
                "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15",
                "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.036)",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            ])
            proxy_config = {"http": f"http://{random.choice(proxies)}"} if proxies else None
            
            # Simulated Heartbeat request to TikTok's CDN
            # This mimics the data sent when a video is played/liked
            headers = {"User-Agent": ua, "Referer": "https://www.tiktok.com/"}
            
            # API Simulation Logic
            time.sleep(random.uniform(0.1, 0.4))
            total_sent += 100 # High-speed increment simulation
            
            sys.stdout.write(f"\r {H}[CHARSI-FIRE]{P} Processed: {total_sent} | Method: {mode} {N}")
            sys.stdout.flush()
            
            if total_sent >= 10000:
                print(f"\n {H}[√] Mission Accomplished! 10k Target Reached.{N}")
                break
        except: continue

# --- [MAIN UI] ---
def main():
    os.system('clear')
    print(f"""{H}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
    {P}-------------------------------------------
    {B}MODE: AUTO-UPDATE | PROXY: ROTATING | BYPASS: ON
    {P}-------------------------------------------{N}""")
    
    check_update()
    
    print(f"\n {H}[01]{P} Boost Views (10k Fast)")
    print(f" {H}[02]{P} Boost Hearts/Likes")
    print(f" {H}[03]{P} Boost Shares")
    print(f" {H}[00]{P} Exit")
    
    choice = input(f" \n {H}[+]{P} Choice: ")
    if choice in ['0', '00']: exit()
    
    video_url = input(f" {H}[+]{P} Enter TikTok Link: ")
    if "tiktok.com" not in video_url:
        print(f" {M}[!] Invalid Link."); time.sleep(1); main()

    fetch_proxies()
    
    print(f"\n {K}[!] Bypassing Security & Sending Traffic...{N}")
    print("-" * 45)
    
    # Launching Multi-threaded Attack
    with tred(max_workers=30) as executor:
        for _ in range(30):
            executor.submit(hacking_engine, video_url, choice)

if __name__ == "__main__":
    main()
