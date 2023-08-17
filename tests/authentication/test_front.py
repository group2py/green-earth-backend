from selenium.webdriver.common.by import By
from time import sleep
import pytest

import os
import sys

parent_path = os.path.join(os.path.abspath('__path__'), '..', '..')
sys.path.append(parent_path)
from authentication.models import Users


@pytest.mark.selenium
@pytest.mark.django_db
def test_registers_user_with_selenium_then_must_go_to_login(browser, user_data):
    browser.find_element(by=By.XPATH, value='//*[@id="navbarNavDropdown"]/ul/li[2]/a').click()
    sleep(3)
    # Defining the data
    # username = user_data['username'].replace(' ','_')
    username = 'Vinicius'  # tem que arrumar a verificaçção de nome
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
# '//*[@id="root"]/div[1]/div/form/div/div/div[4]/input'
# '//*[@id="1"]/div[1]/div[2]'
# @pytest.mark.teste

# AVISO -> É necessário criar um usuário com o email "admin@admin.com" e senha "Admin123!" para o teste abaixo funcionar, crie um novo usuário ou altere esses dados
@pytest.mark.selenium
@pytest.mark.django_db
def test_login_the_user_then_must_go_to_the_dashboard(browser):
    browser.find_element(by=By.XPATH, value='//*[@id="navbarNavDropdown"]/ul/li[3]/a').click()
    sleep(2)
    browser.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/form/div/div/input').send_keys(
        "admin@admin.com")
    browser.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/form/div/div/div[2]/input').send_keys(
        "Admin123!")
    browser.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/form/div/div/div[3]/input').click()
    sleep(2)
    assert browser.current_url == "https://courageous-jalebi-621420.netlify.app/dashboard"

    # //*[@id="navbarNavDropdown"]/ul/li[3]/a
    # //*[@id="root"]/div[1]/div/form/div/div/input
    # //*[@id="root"]/div[1]/div/form/div/div/div[2]/input
    # //*[@id="root"]/div[1]/div/form/div/div/div[3]/input
