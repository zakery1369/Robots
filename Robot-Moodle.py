from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


loginpassword = ['123456'];
# Number of robots
robot = 1

counter = 0
while counter < 410:
    driver = webdriver.Firefox(executable_path="./geckodriver")
    # Moodle login address
    driver.get("https://Example.com/login/index.php")

    time.sleep(5)
    username =  driver.find_element_by_name("username")
    username.send_keys('robot' + str(robot))
    password =  driver.find_element_by_name("password")
    password.send_keys(loginpassword)
    login = driver.find_element_by_id("loginbtn").click()
    # Word search to ensure correct login
    sourcetext=driver.page_source
    searchword="any word in this page"
    # True or False
    print(searchword in sourcetext)
    # Show robot number 
    print(str(robot))

    robot = robot +1
    counter = counter + 1
    time.sleep(5)
    driver.close()