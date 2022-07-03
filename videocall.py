# import required modules
from attr import s
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time




def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://apps.google.com/meet/?hs=197')

    #click sign in button
    s=driver.find_element("xpath",'//*[@id="drawer"]/div/div[3]/div[1]/div/span[1]/a')
    s.click()

    #adding a wait so that next page load
    driver.implicitly_wait(2)

    # input Gmail
    #input username
    username=driver.find_element("xpath",'//*[@id="identifierId"]')
    username.click()
    username.send_keys(mail_address)

    #click next
    next1=driver.find_element("xpath",'//*[@id="identifierNext"]')
    next1.click()

    #adding a wait so that next page load
    driver.implicitly_wait(2)
    # input Password
    pswd=driver.find_element("xpath",'//*[@id="password"]/div[1]/div/div[1]/input')
    pswd.click()
    pswd.send_keys(password)

    #click next
    next2=driver.find_element("xpath",'//*[@id="passwordNext"]')
    next2.click()

    #adding a wait so that next page load
    driver.implicitly_wait(7)


    start_button=driver.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button/span')
    start_button.click()


    call_button=driver.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/ul/li[2]/span[3]')
    call_button.click()

    link_button=driver.find_element("xpath",'//*[@id="ow3"]/div[3]/div[2]/div[3]/div[1]/div[1]')
    print(link_button.text)
    LINK=link_button.text





# assign email id and password
mail_address = 'u1903092@rajagiri.edu.in'
password = 'iamaHEROMAN@27!'

# create chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized') #chrome browser will always open in full screen
opt.add_argument('--disable-extensions') #disable all chrome extension

#pass the arguments 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 2,
	"profile.default_content_setting_values.notifications": 1
})

#Gives path to chrome webdriver and loads classroom webpage
driver=webdriver.Chrome(
	options=opt, 
	executable_path='C:\\Users\\hemal\\Downloads\\chromedriver_win32\\chromedriver.exe')

# login to Google account
Glogin(mail_address, password)



