from selenium import webdriver
d = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
d.get("https://naukri.com")
#d.find_element_by_id("eLoginNew").send_keys("akshaykalyanashetti@gmail.com")
d.find_element_by_xpath("/html/body/div[2]/div/ul/li[7]/a/div").click()
d.find_element_by_id("eLoginNew").send_keys("mahic4148@gmail.com")
d.find_element_by_id("pLogin").send_keys("jaihanuman147")
d.find_element_by_xpath('//*[@id="lgnFrmNew"]/div[9]/button').click()
d.find_element_by_xpath('//*[@id="root"]/div/div[1]/span/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div').click()
fileinput = d.find_element_by_id("attachCV")
fileinput.send_keys('C:\\Users\\Akshay\\Desktop\\mahesh\\PDF\\Resume\\')