from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options


loginpassword = ['123456'];
# Number of robots
robot = 1

while robot < 411:
    # Witout opening browser
    Options = webdriver.FirefoxOptions()
    Options.add_argument('--headless')
    driver = webdriver.Firefox(executable_path="./geckodriver" ,options=Options)
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
    print('Robot ' + str(robot) + ' logged in')

    robot = robot +1
    time.sleep(5)
    # Close browser
    driver.close()
