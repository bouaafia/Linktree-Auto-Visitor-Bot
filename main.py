import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    os.system("cls || clear")
import requests
try:
    from colorama import Fore, Style, init
except ImportError:
    os.system("pip install colorama")
    os.system("cls || clear")
    from colorama import Fore, Style, init
    
try:
    from selenium import webdriver
except ImportError:
    os.system("pip intsall selenium")
    os.system("cls || clear")
    from selenium import webdriver
    
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    os.system("pip install webdriver_manager")
    os.system("cls || clear")
    from webdriver_manager.chrome import ChromeDriverManager
try:
    from fake_useragent import UserAgent
except ImportError:
    os.system("pip install fake_useragent")
    os.system("cls || clear")
    from fake_useragent import UserAgent
    
try:
    import webbrowser
except ImportError:
    os.system("pip install webbrowser")
    os.system("cls || clear")
    import webbrowser
    
webbrowser.open("https://t.me/x0jbb")
# --------------------------- 0XASTA -------------------------------
init(autoreset=True)
DISCLAIMER = f"""{Fore.YELLOW}
======================================================
      ⚠️  EDUCATIONAL PURPOSES ONLY ⚠️
======================================================
This script is for learning and research only.
Do not use it for illegal activities.
I take no responsibility for any misuse.
======================================================{Style.RESET_ALL}
"""

CREDITS = f"""
{Fore.MAGENTA}=================================
{Fore.CYAN}  LINKTREE AUTO VISITOR BOT 🚀
{Fore.MAGENTA}=================================

{Fore.CYAN}======================================================
💻 Developed by: @x0jb & @amiinee.bou
📢 Telegram: t.me/x0jbb
======================================================{Style.RESET_ALL}
"""

def get_proxies():
    try:
        print(Fore.YELLOW + "[INFO] Fetching fresh proxies..." + Style.RESET_ALL)
        response = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
        if response.status_code == 200:
            proxy_list = response.text.split("\n")
            return [p.strip() for p in proxy_list if p.strip()]
    except requests.RequestException:
        print(Fore.RED + "[ERROR] Failed to retrieve proxies." + Style.RESET_ALL)
    return []

def setup_selenium(proxy=None):
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-agent={UserAgent().random}")
    options.add_argument("--window-size=1400x1080")
    options.add_argument("--mute-audio")
    options.add_argument("--disable-extensions")

    if proxy:
        options.add_argument(f"--proxy-server=http://{proxy}")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        print(Fore.RED + f"[ERROR] WebDriver Issue: {type(e).__name__}" + Style.RESET_ALL)
        return None

def visit_linktree(link, visit_count, use_proxies):
    proxies = get_proxies() if use_proxies else []
    proxy_index = 0
    success_count = 0

    while success_count < visit_count:
        os.system("cls" if os.name == "nt" else "clear")

        print(CREDITS)
        print(Fore.YELLOW + f"Link: {link}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Visits: {success_count}/{visit_count}" + Style.RESET_ALL)

        proxy = proxies[proxy_index] if use_proxies and proxy_index < len(proxies) else None
        driver = setup_selenium(proxy)

        if driver is None:
            print(Fore.RED + "[ERROR] Failed to initialize Selenium." + Style.RESET_ALL)
            break

        try:
            driver.get(link)
            success_count += 1
            print(Fore.GREEN + f"[SUCCESS] Visit {success_count}/{visit_count} completed!" + Style.RESET_ALL)

            # Random delay to mimic human behavior

        except Exception as e:
            print(Fore.RED + f"[ERROR] Visit failed: {type(e).__name__}" + Style.RESET_ALL)

        finally:
            driver.quit()
            if use_proxies:
                proxy_index += 1

def main():
    os.system("title LINKTREE AUTO VISITOR BOT 🚀")
    os.system("cls" if os.name == "nt" else "clear")
    print(CREDITS)
    print(DISCLAIMER)
    link = input(Fore.CYAN + "Enter the Linktree profile URL: " + Style.RESET_ALL)

    try:
        visit_count = int(input(Fore.CYAN + "Enter the number of visits: " + Style.RESET_ALL))
        
        proxy_choice = input(Fore.CYAN + "Do you want to use proxies? (yes/no): " + Style.RESET_ALL).strip().lower()
        use_proxies = proxy_choice == "yes"

        visit_linktree(link, visit_count, use_proxies)

    except ValueError:
        print(Fore.RED + "[ERROR] Invalid number format!" + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[INFO] Process interrupted by user." + Style.RESET_ALL)

if __name__ == "__main__":
    main()


# ----------------------- END --------------------------------------
