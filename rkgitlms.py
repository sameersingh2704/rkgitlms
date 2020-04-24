from selenium import webdriver


req_url="http://rkgitlms.in/login/index.php"
user_name="1703310170"
user_pass="Sameer@123"
driver=webdriver.Chrome()

def login_page(req_url):
    
    driver.set_page_load_timeout(30)
    login_page=driver.get(req_url)
    

def authorization(user_name,user_pass):
    driver.find_element_by_id("username").send_keys(user_name)
    driver.find_element_by_id("password").send_keys(user_pass)
    driver.find_element_by_id("loginbtn").click()


def cse_3d():
    driver.get("http://rkgitlms.in/mod/bigbluebuttonbn/view.php?id=231")
    driver.find_element_by_id("join_button_input")

login_page(req_url)
authorization(user_name,user_pass)
cse_3d()