import unittest
from unittest.mock import patch
import pyautogui
import time
from bot import main
from utils import login, logout, collect_resources, upgrade_buildings, train_troops
from config import DELAY, MAX_ATTEMPTS

class TestLogin(unittest.TestCase):
    @patch('pyautogui')
    def test_login(self, mock_pyautogui):
        login("username", "password")
        
        mock_pyautogui.write.assert_called_with("username")
        
        mock_pyautogui.press.assert_called_with('enter')

@patch('pyautogui')
def test_logout(self, mock_pyautogui):
    logout()
    mock_pyautogui.click.assert_called_with(100, 100)

@patch('pyautogui')
def test_collect_resources(self, mock_pyautogui):
    collect_resources()
    mock_pyautogui.click.assert_called_with(200, 200)

@patch('pyautogui')
def test_upgrade_buildings(self, mock_pyautogui):
    upgrade_buildings()
    mock_pyautogui.click.assert_called_with(400, 400)

@patch('pyautogui')
def test_train_troops(self, mock_pyautogui):
    train_troops()
    mock_pyautogui.click.assert_called_with(600, 600)

def test_delay(self):
    self.assertEqual(DELAY, 10)

def test_max_attempts(self):
    self.assertEqual(MAX_ATTEMPTS, 5)
```

if *name* == '*main*':
unittest.main()
