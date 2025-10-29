from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By 
import pytest 
import time 

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.mark.parametrize("username,password,expected_success", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user" , "secret_sauce", True),
    ("error_user" , "secret_sauce", True),
    ("visual_user" , "secret_sauce", True)
     
])    
    
    
def test_login(driver , username , password , expected_success):
    driver.get("https://www.saucedemo.com/")
    
    user_input = WebDriverWait(driver , 5 ).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    
    pw_input = driver.find_element(By.ID, "password" )
    login_btn = driver.find_element(By.ID, "login-button")

    user_input.clear()
    user_input.send_keys(username)
    pw_input.clear()
    pw_input.send_keys(password)
    login_btn.click()
    
    
    try:
        WebDriverWait(driver ,10).until(
               EC.url_contains("/inventory.html")
        )
        success = True
    except:
        success = False   
    assert success == expected_success, f"Login for {username} expacted {expected_success} but get {success} "


