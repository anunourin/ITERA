import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chrome\\chromedriver.exe")
driver.get("https://itera-qa.azurewebsites.net/home/automation")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name=driver.find_element(by=By.ID,value="name")
name.send_keys("anu_nourin")
time.sleep(2)
mobilenumber=driver.find_element(by=By.ID,value="phone")
mobilenumber.send_keys("8129873064")
time.sleep(2)
email=driver.find_element(by=By.ID,value="email")
email.send_keys("anunourin1234@gmail.com")
time.sleep(2)
password=driver.find_element(by=By.ID,value="password")
password.send_keys("Shahanas@1122")
time.sleep(2)
address=driver.find_element(by=By.ID,value="address")
address.send_keys("calicut,kozhikode,673001")
submit=driver.find_element(by=By.NAME,value="submit")
submit.click()
time.sleep(5)
radio=driver.find_element(by=By.NAME,value="optionsRadios")
radio.click()
time.sleep(2)
monday=driver.find_element(by=By.ID,value="monday").click()
sunday=driver.find_element(by=By.ID,value="sunday").click()
friday=driver.find_element(by=By.ID,value="friday").click()
time.sleep(4)
dropdown=driver.find_element(by=By.XPATH,value="/html/body/div/div[4]/div[2]/div/select")
sel=Select(dropdown)
sel.select_by_index(8)
time.sleep(2)
YOE=driver.find_element(by=By.XPATH,value="/html/body/div/div[5]/div[2]/div[1]/div[2]/label")
YOE.click()
time.sleep(2)
automationtool=driver.find_element(by=By.XPATH,value="/html/body/div/div[5]/div[2]/div[2]/div[1]/label").click()
cucumber=driver.find_element(by=By.XPATH,value="/html/body/div/div[5]/div[2]/div[2]/div[2]/label").click()
mabl=driver.find_element(by=By.XPATH,value="/html/body/div/div[5]/div[2]/div[2]/div[5]/label").click()
testim=driver.find_element(by=By.XPATH,value="/html/body/div/div[5]/div[2]/div[2]/div[6]/label").click()
time.sleep(4)
uploadfile=driver.find_element(by=By.ID,value="inputGroupFile02")
uploadfile.send_keys("C:/Users/User/Desktop/new.txt")
uploadbutton=driver.find_element(by=By.XPATH,value="/html/body/div/div[6]/div[2]/div/div/div[2]/span")
uploadbutton.click()
time.sleep(3)

# login
login=driver.find_element(by=By.LINK_TEXT,value="Login")
login.click()
time.sleep(2)
username=driver.find_element(by=By.NAME,value="Username")
username.send_keys("anu_nourin")
password=driver.find_element(by=By.ID,value="Password")
password.send_keys("Shahanas@1122")
time.sleep(4)
login=driver.find_element(by=By.NAME,value="login")
login.click()
time.sleep(6)

# create new user
createnew=driver.find_element(by=By.XPATH,value="/html/body/div/div/p[1]/a")
createnew.click()
time.sleep(2)
name=driver.find_element(by=By.CSS_SELECTOR,value="input#Name")
name.send_keys("ANUNOURIN")
time.sleep(2)
company=driver.find_element(by=By.CSS_SELECTOR,value="input#Company")
company.send_keys("infosys")
time.sleep(2)
address=driver.find_element(by=By.NAME,value="Address")
address.send_keys("calicut")
time.sleep(2)
city=driver.find_element(by=By.ID,value="City")
city.send_keys("kozhikode")
time.sleep(2)
phone=driver.find_element(by=By.NAME,value="Phone")
phone.send_keys("8129873064")
time.sleep(2)
email=driver.find_element(by=By.NAME,value="Email")
email.send_keys("anunourin1234@gmail.com")
time.sleep(2)
createbutton=driver.find_element(by=By.XPATH,value="/html/body/div/form/div/div[7]/div/input")
createbutton.click()
time.sleep(3)

# searching the created user
searchname=driver.find_element(by=By.NAME,value="searching")
searchname.send_keys("anunourin")
time.sleep(2)
searchbutton=driver.find_element(by=By.XPATH,value="/html/body/div/div/form/input[2]")
searchbutton.click()
time.sleep(3)

# editing the existing user
edit=driver.find_element(by=By.XPATH,value="/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]")
edit.click()
time.sleep(2)
name=driver.find_element(by=By.ID,value="Name")
name.send_keys("ep")
time.sleep(2)
company=driver.find_element(by=By.NAME,value="Company")
company.send_keys("trivandrum")
time.sleep(2)
save=driver.find_element(by=By.XPATH,value="/html/body/div/form/div/div[7]/div/input")
save.click()
time.sleep(2)

# searching the edited name
searchname=driver.find_element(by=By.NAME,value="searching")
searchname.send_keys("anunourinep")
time.sleep(2)
searchbutton=driver.find_element(by=By.XPATH,value="/html/body/div/div/form/input[2]")
searchbutton.click()
time.sleep(2)

# getting the details of edited user
details=driver.find_element(by=By.XPATH,value="/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]")
time.sleep(2)
details.click()
time.sleep(2)
backtolist=driver.find_element(by=By.XPATH,value="/html/body/div/p/a[2]")
backtolist.click()
time.sleep(2)
logout=driver.find_element(by=By.XPATH,value="//*[@id='navbarColor01']/form/ul/li[2]/a")
logout.click()