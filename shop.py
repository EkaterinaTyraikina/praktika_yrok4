# # отображение страницы товара
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension =r'C:\Users\Екатерина\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(15)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# #1
# driver.get("http://practice.automationtesting.in/" )
# #2
# account=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# account.click()
# login_email=driver.find_element_by_id("username")
# login_email.send_keys("agafonova_e_v@mail.ru")
# login_parol=driver.find_element_by_id("password")
# login_parol.send_keys("25031990:Katerina")
# login_btn=driver.find_element_by_name("login")
# login_btn.click()
# #3
# shop=driver.find_element_by_css_selector ("[href='http://practice.automationtesting.in/shop/']")
# shop.click()
# #4
# kniga_html=driver.find_element_by_css_selector("[alt='Mastering HTML5 Forms']")
# time.sleep(5)
# kniga_html.click()
# #5
# kniga_title=driver.find_element_by_css_selector("[itemprop='name']")
# kniga_title_text=kniga_title.text
# assert kniga_title_text == "HTML5 Forms"
# if kniga_title_text == "HTML5 Forms":
#     print("Заголовок книги:", kniga_title_text)
# else:
#     print("Проверка не пройдена. Заголовок книги отличается от заданного:", kniga_title_text)
#
# driver.quit()
#
#
# #количество товаров в категории
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension =r'C:\Users\Екатерина\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(15)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# #1
# driver.get("http://practice.automationtesting.in/" )
# #2
# account=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# account.click()
# login_email=driver.find_element_by_id("username")
# login_email.send_keys("agafonova_e_v@mail.ru")
# login_parol=driver.find_element_by_id("password")
# login_parol.send_keys("25031990:Katerina")
# login_btn=driver.find_element_by_name("login")
# login_btn.click()
# #3
# shop=driver.find_element_by_css_selector ("[href='http://practice.automationtesting.in/shop/']")
# shop.click()
# #4
# kat_html=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']")
# time.sleep(7)
# kat_html.click()
# #5
# items_count =driver.find_element_by_css_selector("[class='products masonry-done']")
# if len(items_count) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Не верно. Количество товаров отображается: ", str(len(items_count)))
#
# driver.quit()
#
#
# #сортировка товаров
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# #1
# driver.get("http://practice.automationtesting.in/" )
# #2
# account=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# account.click()
# login_email=driver.find_element_by_id("username")
# login_email.send_keys("agafonova_e_v@mail.ru")
# login_parol=driver.find_element_by_id("password")
# login_parol.send_keys("25031990:Katerina")
# login_btn=driver.find_element_by_name("login")
# login_btn.click()
# #3
# shop=driver.find_element_by_css_selector ("[href='http://practice.automationtesting.in/shop/']")
# shop.click()
# #4
# sort=driver.find_element_by_name("orderby")
# select=Select(sort)
# select.select_by_value("menu_order")
# #5
# sort=driver.find_element_by_name("orderby")
# select=Select(sort)
# select.select_by_value("price-desc")
# #6,7
# sort=driver.find_element_by_name("orderby")
# select=Select(sort)
# select.select_by_value("price-desc")
# sort_ybivanie=sort.get_attribute("value")
# if sort_ybivanie=="price-desc":
#     print("Выбрана сортировка от большего к меньшему")
# else:
#     print("Не выбрана сортировка от большего к меньшему")
# driver.quit()
#
# # отображение, скидка товаров
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension =r'C:\Users\Екатерина\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_1'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(15)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# #1
# driver.get("http://practice.automationtesting.in/" )
# #2
# account=driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# account.click()
# login_email=driver.find_element_by_id("username")
# login_email.send_keys("agafonova_e_v@mail.ru")
# login_parol=driver.find_element_by_id("password")
# login_parol.send_keys("25031990:Katerina")
# login_btn=driver.find_element_by_name("login")
# login_btn.click()
# #3
# shop=driver.find_element_by_css_selector ("[href='http://practice.automationtesting.in/shop/']")
# shop.click()
# #4
# kniga=driver.find_element_by_css_selector("[src='http://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-300x300.png']")
# kniga.click()
# #5
# star_cena=driver.find_element_by_css_selector("[class='woocommerce-Price-amount amount']")
# star_cena_txt=star_cena.text
# assert star_cena_txt=="₹600.00"
# if star_cena_txt==₹600.00:
#     print("Старая цена:" , star_cena_txt)
# else:
#     print("Неверно. ")
# #6
# nov_cena=driver.find_element_by_css_selector("[class='woocommerce-Price-amount amount']")
# nov_cena_txt=nov_cena.text
# assert nov_cena_txt=="₹450.00"
# if nov_cena_txt==₹450.00:
#     print("Новая цена:" , nov_cena_txt)
# else:
#     print("Неверно. ")
# #7
# open_kniga= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='Android Quick Start Guide']")))
# open_kniga.click()
# #8
# close_kniga= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='pp_close']")))
# close_kniga.click()
# driver.quit()
#
#
# # проверка цены в корзине
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension =r'C:\Users\Екатерина\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(15)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# #1
# driver.get("http://practice.automationtesting.in/" )
# #2
# shop=driver.find_element_by_css_selector ("[href='http://practice.automationtesting.in/shop/']")
# shop.click()
# #3
# add_bascet=driver.find_element_by_css_selector("[data-product_id='182']")
# add_bascet.click()
# #4
# kolvo=driver.find_element_by_css_selector("[class='cartcontents']")
# kolvo_txt=kolvo.text
# assert kolvo_txt == "1 Item"
# stoimost=driver.find_element_by_css_selector("[class='amount']")
# stoimost_txt=stoimost.text
# assert kolvo_txt == "₹180.00"
# #5
# bascet=driver.find_element_by_css_selector("[class='wpmenucart-contents']")
# bascet.click()
# #6
# subtotal= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-Price-amount amount']"), "₹180.00"))
# #7
# total= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "strong"), "₹189.00"))
# driver.quit()
#
# # работа в корзине
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension =r'C:\Users\Екатерина\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(15)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# #1
# driver.get("http://practice.automationtesting.in/" )
# #2
# shop=driver.find_element_by_css_selector ("[href='http://practice.automationtesting.in/shop/']")
# shop.click()
# #3
# driver.execute_script("window.scrollBy(0,300)")
# add_bascet=driver.find_element_by_css_selector("[data-product_id='182']")
# add_bascet.click()
# time.sleep(5)
# add_bascet1=driver.find_element_by_css_selector("[data-product_id='180']")
# add_bascet1.click()
# #4
# time.sleep(5)
# bascet=driver.find_element_by_css_selector("[class='wpmenucart-contents']")
# bascet.click()
# #5
# time.sleep(5)
# delete=driver.find_element_by_css_selector("[data-product_id='182']")
# delete.click()
# #6
# time.sleep(5)
# undo=driver.find_element_by_link_text("Undo?")
# undo.click()
# #7
# time.sleep(5)
# quantity=driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quantity.clear()
# quantity.send_keys("3")
# #8
# update=driver.find_element_by_name("update_cart")
# update.click()
# #9
# quantity_valye=driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quantity_valye_znachenie=quantity_valye.text
# assert quantity_valye_znachenie == 3, "Верно"
# #10
# time.sleep(10)
# apply=driver.find_element_by_name("apply_coupon")
# apply.click()
# #11
# #Сообщения не возникает
# driver.quit()


# покупка товара
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
path_to_extension =r'C:\Users\Екатерина\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(15)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
#1
driver.get("http://practice.automationtesting.in/" )
#2
shop=driver.find_element_by_css_selector ("[href='http://practice.automationtesting.in/shop/']")
shop.click()
driver.execute_script("window.scrollBy(0,300)")
#3
add_bascet=driver.find_element_by_css_selector("[data-product_id='182']")
add_bascet.click()
time.sleep(5)
#4
time.sleep(5)
bascet=driver.find_element_by_css_selector("[class='wpmenucart-contents']")
bascet.click()
#5
proceed_btn= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='checkout-button button alt wc-forward']")))
proceed_btn.click()
#6
first_name=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='billing_first_name']")))
first_name.send_keys("Ekaterina")
last_name=driver.find_element_by_id("billing_last_name")
last_name.send_keys("Tyraikina")
email=driver.find_element_by_id("billing_email")
email.send_keys("agafonova_e_v@mail.ru")
phone=driver.find_element_by_id("billing_phone")
phone.send_keys("9988776")
country=driver.find_element_by_id("select2-chosen-1")
country.click()
country_input=driver.find_element_by_class_name("select2-input")
country_input.send_keys("Russia")
time.sleep(5)
country_input_v=driver.find_element_by_class_name("select2-match")
country_input_v.click()
time.sleep(5)
adress=driver.find_element_by_id("billing_address_1")
adress.send_keys("Ylica d.1")
city=driver.find_element_by_id("billing_city")
city.send_keys("Sankt-Prterburg")
state=driver.find_element_by_id("billing_state")
state.send_keys("Sankt-Prterburg")
post=driver.find_element_by_id("billing_postcode")
post.send_keys("1900000")
#7
driver.execute_script("window.scrollBy(0,600)")
time.sleep(5)
oplata=driver.find_element_by_id("payment_method_cheque")
oplata.click()
#8
pl_older=driver.find_element_by_id("place_order")
pl_older.click()
#9
proverka=WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received."))
#10
proverka2=WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='method']"), "Check Payments"))
driver.quit()
