import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_found_button_on_the_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	time.sleep(30)
	button = browser.find_elements(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
	assert len(button) > 0, "The button not found"


