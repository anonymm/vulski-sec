import requests
import sys

def banner():
    print("""
  _____ _                 _  _           _         
 |  ___| | ___  _   _  __| || |__   ___ | |___ ___ 
 | |_  | |/ _ \| | | |/ _` || '_ \ / _ \| / __/ __|
 |  _| | | (_) | |_| | (_| || | | | (_) | \__ \__ \\
 |_|   |_|\___/ \__,_|\__,_||_| |_|\___/|_|___/___/
            by Vulski (Android + Termux)
    """)

def finder(url, wordlist):
    with open(wordlist, "r") as f:
        for line in f:
            path = line.strip()
            full_url = f"{url}/{path}"
            try:
                r = requests.get(full_url)
                if r.status_code == 200:
                    print(f"[+] Found: {full_url}")
                elif r.status_code == 403:
                    print(f"[-] Forbidden: {full_url}")
            except requests.RequestException:
                continue

if __name__ == "__main__":
    banner()
    if len(sys.argv) != 3:
        print("Usage: python dirfinder.py https://target.com wordlist.txt")
        sys.exit(1)

    target_url = sys.argv[1]
    wordlist_file = sys.argv[2]
    finder(target_url, wordlist_file)
