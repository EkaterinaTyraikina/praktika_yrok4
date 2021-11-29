from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
#1
driver.get("http://practice.automationtesting.in/" )
#2
driver.execute_script("window.scrollBy(0,600)")
#3
ruby_btn=driver.find_element_by_partial_link_text("Selenium Ruby")
ruby_btn.click()
#4
reviews=driver.find_element_by_css_selector("[href='#tab-reviews']")
reviews.click()
#5
zvezda=driver.find_element_by_css_selector(".stars .star-5")
zvezda.click()
#6
review_okno=driver.find_element_by_id("comment")
review_okno.send_keys("Nice book!")
#7
name=driver.find_element_by_id("author")
name.send_keys("Ekaterina")
#8
email=driver.find_element_by_id("email")
email.send_keys("agafonova_e_v@mail.ru")
#9
submit=driver.find_element_by_id("submit")
submit.click()
driver.quit()