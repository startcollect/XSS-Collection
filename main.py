import os
import subprocess

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"
NC = "\033[0m"

TOOLS_DIR = "Tools"

os.makedirs(TOOLS_DIR, exist_ok=True)

def check_install_dependencies():
    if subprocess.call("command -v wget", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0 or \
       subprocess.call("command -v unzip", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print(f"{YELLOW}Menginstal dependensi...{NC}")
        if 'TERMUX_VERSION' in os.environ:
            subprocess.call("pkg install -y wget unzip", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os.geteuid() == 0 or subprocess.call("command -v sudo", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            subprocess.call("apt install -y wget unzip", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

commands = {
    "1": ("https://raw.githubusercontent.com/dorara-tech/Ddos-Collect/refs/heads/main/.main/DSXS.zip", "DSXS"),
    "2": ("https://raw.githubusercontent.com/dorara-tech/Ddos-Collect/refs/heads/main/.main/PwnXSS.zip", "PwnXSS"),
    "3": ("https://raw.githubusercontent.com/dorara-tech/Ddos-Collect/refs/heads/main/.main/XSS-LOADER.zip", "XSS-LOADER"),
    "4": ("https://raw.githubusercontent.com/dorara-tech/Ddos-Collect/refs/heads/main/.main/XSSCon.zip", "XSSCon"),
    "5": ("https://raw.githubusercontent.com/dorara-tech/Ddos-Collect/refs/heads/main/.main/xsscrapy.zip", "xsscrapy"),
    "6": ("https://raw.githubusercontent.com/dorara-tech/Ddos-Collect/refs/heads/main/.main/xsser.zip", "xsser"),
    "7": ("https://raw.githubusercontent.com/dorara-tech/Ddos-Collect/refs/heads/main/.main/XSStrike.zip", "XSStrike"),
}

print(f"{GREEN}====================================")
print("      TOOLS XSS INSTALLER        ")
print("====================================" + NC)
print()
print(f"{YELLOW}List Tools")
for key, (_, name) in commands.items():
    print(f"{WHITE}{key}.{GREEN}{name}")

print()
pilihan = input(f"{BLUE}Choose a number:{WHITE} ")

if pilihan in commands:
    zip_url, folder_name = commands[pilihan]
    zip_path = os.path.join(TOOLS_DIR, f"{folder_name}.zip")
    extract_path = os.path.join(TOOLS_DIR, folder_name)

    print(f"{YELLOW}Downloading {folder_name}...{NC}")
    
    subprocess.call(f"wget -q {zip_url} -O {zip_path}", shell=True)
    
    if os.path.exists(extract_path):
        subprocess.call(f"rm -rf {extract_path}", shell=True)

    os.makedirs(extract_path, exist_ok=True)
    subprocess.call(f"unzip -o {zip_path} -d {extract_path} > /dev/null 2>&1", shell=True)

    os.remove(zip_path)

    print(f"{GREEN}Installation completed! Check directory Tools.{NC}")
else:
    print(f"{RED}[ERROR] Invalid option!{NC}")
