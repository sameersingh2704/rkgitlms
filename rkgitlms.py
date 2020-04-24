from selenium import webdriver


user_name=input("Enter your username")
user_pass=input("Enter your password")
class_section=input("Enter your class and section like:3D or 3C")
req_url="http://rkgitlms.in/login/index.php"

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
    driver.find_element_by_id("join_button_input").click()
def cse_3c():
    driver.get("http://rkgitlms.in/mod/bigbluebuttonbn/view.php?id=230")
    driver.find_element_by_id("join_button_input").click()

login_page(req_url)
authorization(user_name,user_pass)
if(class_section=="3D"):
    cse_3d()
elif(class_section=="3C"):
    cse_3c()
else:
    print("invalid class")