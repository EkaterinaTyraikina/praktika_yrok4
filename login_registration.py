'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
#1
driver.get("http://practice.automationtesting.in/" )
#2
account=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
account.click()
#3
registr_email=driver.find_element_by_id("reg_email")
registr_email.send_keys("agafonova_e_v@mail.ru")
#4
registr_parol=driver.find_element_by_id("reg_password")
registr_parol.send_keys("25031990:Katerina")
#5
registr_btn=driver.find_element_by_name("register")
registr_btn.click()

driver.quit()'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
#1
driver.get("http://practice.automationtesting.in/" )
#2
account=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
account.click()
#3
login_email=driver.find_element_by_id("username")
login_email.send_keys("agafonova_e_v@mail.ru")
#4
login_parol=driver.find_element_by_id("password")
login_parol.send_keys("25031990:Katerina")
#5
login_btn=driver.find_element_by_name("login")
login_btn.click()
#6
element=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/customer-logout/']")
element_get_text=element.text
assert element_get_text=="Logout"
if element_get_text=="Logout":
    print("Элемент Logout найден на странице")
else:
    print("Элемент Logout не найден на странице")

driver.quit()