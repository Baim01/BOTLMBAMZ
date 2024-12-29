import pyautogui
import time
import config
import utils

def main():
    print("Bot Lords Mobile aktif!")
    utils.login()
    while True:
        utils.collect_resources()
        utils.upgrade_buildings()
        utils.train_troops()
        time.sleep(config.delay)

if __name__ == "__main__":
    main()
