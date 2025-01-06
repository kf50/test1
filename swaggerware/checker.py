import random
import string
import requests
import threading
from colorama import Fore, Style





def display_banner():
    banner = """
   ███████╗██╗    ██╗ █████╗  ██████╗  ██████╗ ███████╗██████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗
   ██╔════╝██║    ██║██╔══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝
   ███████╗██║ █╗ ██║███████║██║  ███╗██║  ███╗█████╗  ██████╔╝██║ █╗ ██║███████║██████╔╝█████╗  
   ╚════██║██║███╗██║██╔══██║██║   ██║██║   ██║██╔══╝  ██╔══██╗██║███╗██║██╔══██║██╔══██╗██╔══╝  
   ███████║╚███╔███╔╝██║  ██║╚██████╔╝╚██████╔╝███████╗██║  ██║╚███╔███╔╝██║  ██║██║  ██║███████╗
   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
     1 - soundcloud 
     2 - twitch
     3 - steam
     4 - twitter
     5 - bsky
     6 - tiktok
     7 - instagram
    """
    print(banner)

def generate_username():
    choice = random.choice(["letters", "numbers", "both"])
    if choice == "letters":
        return ''.join(random.choices(string.ascii_lowercase, k=4))
    elif choice == "numbers":
        return ''.join(random.choices(string.digits, k=4))
    else:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

def load_headers_from_file():
    try:
        with open('headers.txt', 'r') as file:
            headers_list = file.readlines()
        headers_list = [header.strip() for header in headers_list if header.strip()]
        return headers_list
    except FileNotFoundError:
        print(f"{Fore.YELLOW}[ERROR] headers.txt file not found. Please ensure the file exists.{Style.RESET_ALL}")
        return []

def generate_random_headers():
    headers_list = load_headers_from_file()
    if not headers_list:
        return {
            "User-Agent": "Default-User-Agent",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "close"
            
        
        }

    random_header = random.choice(headers_list)
    return {
        "User-Agent": random_header,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "close"
    }

def check_username_with_no_proxy(url, headers):
    try:
        response = requests.head(url, headers=headers, allow_redirects=True, timeout=3)
        return response.status_code
    except requests.RequestException as e:
        print(f"{Fore.YELLOW}[ERROR] Request failed: {e}{Style.RESET_ALL}")
        return None

def check_soundcloud_username(username):
    url = f"https://soundcloud.com/{username}"
    headers = generate_random_headers()
    status = check_username_with_no_proxy(url, headers)
    if status == 200:
        print(f"{Fore.RED}[TAKEN] SoundCloud: {username}{Style.RESET_ALL}")
        return False
    elif status is None:
        return False
    else:
        print(f"{Fore.GREEN}[AVAILABLE] SoundCloud: {username}{Style.RESET_ALL}")
        return True

def check_twitch_username(username):
    url = f"https://www.twitch.tv/{username}"
    headers = generate_random_headers()
    status = check_username_with_no_proxy(url, headers)
    if status == 200:
        print(f"{Fore.RED}[TAKEN] Twitch: {username}{Style.RESET_ALL}")
        return False
    elif status is None:
        return False
    else:
        print(f"{Fore.GREEN}[AVAILABLE] Twitch: {username}{Style.RESET_ALL}")
        return True

def check_steam_username(username):
    url = f"https://steamcommunity.com/id/{username}"
    headers = generate_random_headers()
    status = check_username_with_no_proxy(url, headers)
    if status == 200:
        print(f"{Fore.RED}[TAKEN] Steam: {username}{Style.RESET_ALL}")
        return False
    elif status is None:
        return False
    else:
        print(f"{Fore.GREEN}[AVAILABLE] Steam: {username}{Style.RESET_ALL}")
        return True

def check_twitter_username(username):
    url = f"https://twitter.com/{username}"
    headers = generate_random_headers()
    status = check_username_with_no_proxy(url, headers)
    if status == 200:
        print(f"{Fore.RED}[TAKEN] Twitter: {username}{Style.RESET_ALL}")
        return False
    elif status is None:
        return False
    else:
        print(f"{Fore.GREEN}[AVAILABLE] Twitter: {username}{Style.RESET_ALL}")
        return True

def check_bsky_username(username):
    url = f"https://bsky.app/profile/{username}.bsky.social"
    headers = generate_random_headers()
    status = check_username_with_no_proxy(url, headers)
    if status == 200:
        print(f"{Fore.RED}[TAKEN] Bluesky: {username}{Style.RESET_ALL}")
        return False
    elif status is None:
        return False
    else:
        print(f"{Fore.GREEN}[AVAILABLE] Bluesky: {username}{Style.RESET_ALL}")
        return True

def check_tiktok_username(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = generate_random_headers()
    status = check_username_with_no_proxy(url, headers)
    if status == 200:
        print(f"{Fore.RED}[TAKEN] TikTok: {username}{Style.RESET_ALL}")
        return False
    elif status is None:
        return False
    else:
        print(f"{Fore.GREEN}[AVAILABLE] TikTok: {username}{Style.RESET_ALL}")
        return True

def check_instagram_username(username):
    url = f"https://www.instagram.com/{username}/"
    headers = generate_random_headers()
    status = check_username_with_no_proxy(url, headers)
    if status == 200:
        print(f"{Fore.RED}[TAKEN] Instagram: {username}{Style.RESET_ALL}")
        return False
    elif status is None:
        return False
    else:
        print(f"{Fore.GREEN}[AVAILABLE] Instagram: {username}{Style.RESET_ALL}")
        return True

def send_to_discord(message):
    if not ENABLE_DISCORD_WEBHOOK or not DISCORD_WEBHOOK_URL:
        return

    payload = {"content": message}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print(f"{Fore.CYAN}[INFO] Message sent to Discord{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[WARNING] Failed to send to Discord: {response.status_code}{Style.RESET_ALL}")
    except requests.RequestException as e:
        print(f"{Fore.YELLOW}[ERROR] Discord webhook failed: {e}{Style.RESET_ALL}")

def worker(usernames, platform, available_usernames):
    for username in usernames:
        if platform == "1":
            if check_soundcloud_username(username):
                available_usernames.append(username)
        elif platform == "2":
            if check_twitch_username(username):
                available_usernames.append(username)
        elif platform == "3":
            if check_steam_username(username):
                available_usernames.append(username)
        elif platform == "4":
            if check_twitter_username(username):
                available_usernames.append(username)
        elif platform == "5":
            if check_bsky_username(username):
                available_usernames.append(username)
        elif platform == "6":
            if check_tiktok_username(username):
                available_usernames.append(username)
        elif platform == "7":
            if check_instagram_username(username):
                available_usernames.append(username)

def main():
    display_banner()

    platform = input("--> : ")
    if platform not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice. Please restart the program and choose a valid option.")
        return

    num_usernames = int(input("Enter the number of usernames to generate (max 1000): "))
    if num_usernames > 1000:
        num_usernames = 1000  # Enforce the maximum number of usernames

    usernames = [generate_username() for _ in range(num_usernames)]

    print("\nStarting username checks...\n")

    available_usernames = []

    # Split usernames into chunks for threading
    chunk_size = max(1, len(usernames) // 10)  # Reduced chunk size for illustration
    chunks = [usernames[i:i + chunk_size] for i in range(0, len(usernames), chunk_size)]

    threads = []

    for chunk in chunks:
        thread = threading.Thread(target=worker, args=(chunk, platform, available_usernames))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

   
    with open('untaken.txt', 'w') as f:
        for username in available_usernames:
            f.write(f"{username}\n")

    print(f"\nAvailable usernames have been saved to 'untaken.txt'.")

  
    

if __name__ == "__main__":
    main()
