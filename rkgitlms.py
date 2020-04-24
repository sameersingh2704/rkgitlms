from selenium import webdriver


user_name=input("Enter your username: ")
user_pass=input("Enter your password: ")
class_section=input("Enter your class and section (like 3D or 3C): ")
req_url="http://rkgitlms.in/login/index.php"

driver=webdriver.Chrome()

def login_page(req_url):
    
    driver.set_page_load_timeout(30)
    login_page=driver.get(req_url)
    

def authorization(user_name,user_pass):
    driver.find_element_by_id("username").send_keys(user_name)
    driver.find_element_by_id("password").send_keys(user_pass)
    driver.find_element_by_id("loginbtn").click()


def joinclass(class_section):
    if(class_section=="3D"):
        driver.get("http://rkgitlms.in/mod/bigbluebuttonbn/view.php?id=231")
    elif(class_section=="3C"):
        driver.get("http://rkgitlms.in/mod/bigbluebuttonbn/view.php?id=230")
    elif(class_section=="3A"):
        driver.get("http://rkgitlms.in/mod/bigbluebuttonbn/view.php?id=228")
    elif(class_section=="3B"):
        driver.get("http://rkgitlms.in/mod/bigbluebuttonbn/view.php?id=229")
    else:
        print("invalid class")
        exit()
    
    driver.find_element_by_id("join_button_input").click()


login_page(req_url)
authorization(user_name,user_pass)
joinclass(class_section)