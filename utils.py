def login(username, password):
# Kode untuk login ke game
pyautogui.write(username)
pyautogui.press('enter')
pyautogui.write(password)
pyautogui.press('enter')

def logout():
# Kode untuk logout dari game
pyautogui.click(1, 1)  # Koordinat tombol logout

def collect_resources():
# Kode untuk mengumpulkan sumber daya
pyautogui.click(2, )  # Koordinat tombol kumpulkan

def collect_gold():
# Kode untuk mengumpulkan emas
pyautogui.click(3, 3)  # Koordinat tombol kumpulkan emas

def upgrade_buildings():
# Kode untuk meningkatkan bangunan
pyautogui.click(4, 4)  # Koordinat tombol upgrade

def build_new_building():
# Kode untuk membangun bangunan baru
pyautogui.click(5, 5)  # Koordinat tombol bangun

def train_troops():
# Kode untuk melatih pasukan
pyautogui.click(6, 6)  # Koordinat tombol latih

def upgrade_troops():
# Kode untuk meningkatkan pasukan
pyautogui.click(7, 7)  # Koordinat tombol upgrade pasukan

def wait(delay):
# Fungsi untuk menunggu
time.sleep(delay)

def log_message(message):
# Fungsi untuk mencatat log
with open("log.txt", "a") as f:
f.write(message + "\n")

DELAY = config.DELAY
MAX_ATTEMPTS = config.MAX_ATTEMPTS
