import time
import random
import subprocess
import pyautogui
import pyttsx3
import tkinter as tk
import pygame
import os
import hashlib
from tqdm import tqdm
from colorama import init, Fore, Style
from datetime import datetime, timedelta
from rich.console import Console
import pyfiglet
from cryptography.fernet import Fernet
from scapy.all import IP, ICMP, sr1, sniff, sendp, Ether, IP, UDP
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
from uuid import uuid4
from IPython import embed
from alive_progress import alive_bar, showtime

# Initialize libraries
init(autoreset=True)
console = Console()
pygame.init()
pygame.mixer.init()

# Constants
POSSIBLE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
STARTUP_SOUND_PATH = "/Users/al3inaw/sounds/startup.wav"  # Updated path to a sound file

def generate_key():
    key = urlsafe_b64encode(hashlib.sha256(str(uuid4()).encode()).digest())
    console.print(f"Generated secure key: {key}", style="bold cyan")
    return key

def rsa_encryption():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    message = b"Secret RSA encrypted message"
    encrypted = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    console.print("Message encrypted using RSA.", style="bold magenta")
    return private_key, encrypted

def decrypt_rsa(private_key, encrypted):
    original_message = private_key.decrypt(encrypted, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    console.print(f"Decrypted RSA message: {original_message.decode()}", style="bold green")

def simulate_network_sniffing():
    try:
        console.print("Starting network packet sniffing...", style="bold red")
        packets = sniff(count=10)
        for packet in packets:
            console.print(f"Sniffed packet: {packet.summary()}", style="bold yellow")
    except PermissionError:
        console.print("Permission denied for network sniffing. Please run the script as root/administrator.", style="bold red")

def simulate_data_leak():
    fake_data = "user:pass;admin:123456;root:toor"
    console.print("Simulating data leak...", style="bold magenta")
    hashes = [hashlib.md5(user.encode()).hexdigest() for user in fake_data.split(';')]
    for h in hashes:
        console.print(f"Leaked data hash: {h}", style="bold red")

def track_watcher():
    console.print("Checking for watchers...", style="bold red")
    if random.choice([True, False]):
        console.print("Watcher detected! Initiating countermeasures...", style="bold green")
    else:
        console.print("No watchers detected. Proceeding safely.", style="bold green")

def manipulate_time():
    fake_time = datetime.now() + timedelta(days=365)
    console.print(f"Manipulated system time to: {fake_time}", style="bold yellow")

def create_gui():
    root = tk.Tk()
    root.title("Decoy Application")
    tk.Label(root, text="This is not a hacking tool.").pack()
    root.mainloop()

def simulate_key_strokes():
    with alive_bar(100, title='Simulating Keystrokes') as bar:
        for _ in range(100):
            pyautogui.typewrite(random.choice(POSSIBLE_CHARS), interval=0.1)
            bar()
    console.print("Simulated random keystrokes.", style="bold cyan")

def loading_shapes():
    shapes = ["░░░░░░░░░░░░░░░░", "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒", "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", "████████████████"]
    for shape in tqdm(shapes, desc=Fore.BLUE + "Loading", ascii=True):
        console.print(pyfiglet.figlet_format(shape))
        time.sleep(0.5)

def execute_script(filepath):
    try:
        console.print(f"Executing script: {filepath}", style="bold blue")
        subprocess.run(['python', filepath], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"Failed to execute {filepath}: {str(e)}", style="bold red")

def play_sound(sound_path):
    try:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    except Exception as e:
        console.print(f"Error playing sound {sound_path}: {str(e)}", style="bold red")

def simulate_hacking_activities():
    activities = [generate_key, rsa_encryption, simulate_network_sniffing, simulate_data_leak, track_watcher, manipulate_time, simulate_key_strokes]
    for activity in activities:
        activity()
        time.sleep(random.randint(1, 3))  # Random delay to simulate real-time activities

def run_bash_script():
    bash_script_path = "/Users/al3inaw/simulate_hacking.sh"
    try:
        console.print(f"Executing Bash script: {bash_script_path}", style="bold blue")
        subprocess.run(["bash", bash_script_path], check=True)
        console.print("Hacking simulation script completed successfully.", style="bold green")
    except subprocess.CalledProcessError as e:
        console.print(f"An error occurred while executing the Bash script: {e}", style="bold red")

def main():
    console.print(Fore.CYAN + Style.BRIGHT + "Initializing hack simulation...", style="bold cyan")
    time.sleep(2)
    scripts = ["/Users/al3inaw/scorp.py", "/Users/al3inaw/earth.py", "/Users/al3inaw/brazil.py", "/Users/al3inaw/city.py"]
    random.shuffle(scripts)  # Randomize the order of script execution
    for script in scripts:
        execute_script(script)
        simulate_hacking_activities()  # Simulate hacking activities between script executions
    run_bash_script()  # Execute the Bash script
    play_sound(STARTUP_SOUND_PATH)
    loading_shapes()
    create_gui()
    embed()  # Start IPython REPL here

if __name__ == "__main__":
    main()
