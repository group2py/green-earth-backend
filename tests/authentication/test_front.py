from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.mark.selenium
def test_registers_user_with_selenium_then_must_go_to_login(browser, user_data):
    browser.find_element(by=By.XPATH, value='//*[@id="navbarNavDropdown"]/ul/li[2]/a').click()
    sleep(3)
    # Defining the data
    # username = user_data['username'].replace(' ','_')
    username = 'Vinicius' #tem que arrumar a verificaçção de nome
    email = user_data['email']
    password = user_data['password']
    # Entering info into forms
    browser.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/form/div/div/input[1]").send_keys(username)
    browser.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/form/div/div/input[2]").send_keys(email)
    browser.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/form/div/div/div[2]/input").send_keys(password)
    browser.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/form/div/div/div[3]/input").send_keys(password)
    # Clicking the send button
    browser.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/form/div/div/div[4]/input').click()
    sleep(3)
    assert browser.current_url == "https://courageous-jalebi-621420.netlify.app/signin"   






# "/html/body/div/div[1]/div/form/div/div/input[1]"
# "/html/body/div/div[1]/div/form/div/div/input[2]"
# "/html/body/div/div[1]/div/form/div/div/div[2]/input"
# "/html/body/div/div[1]/div/form/div/div/div[3]/input"
#'//*[@id="root"]/div[1]/div/form/div/div/div[4]/input'
#'//*[@id="1"]/div[1]/div[2]'
