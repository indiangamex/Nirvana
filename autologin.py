import time
import keyboard
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/login/")
browser.maximize_window()
time.sleep(3)
browser.find_element_by_name("username").send_keys("optra_releven_2077")
browser.find_element_by_name("password").send_keys("Dystopian_Cyberpunk//_")
keyboard.press_and_release("enter")



