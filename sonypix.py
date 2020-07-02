import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#chrome  
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


fav=['hangover']

driver =''
def login():
	global driver
	chrome_options = Options()
	chrome_options.add_argument("--headless") 
	driver=webdriver.Chrome(options=chrome_options)



def logic():
	global driver 
	found=[]
	driver.get('https://tvscheduleindia.com/channel/sony-pix')
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, "//select/option[@value='100']"))
	    )
	except:
		pass
	driver.find_element_by_xpath("//select/option[@value='100']").click();
	movies=driver.find_elements_by_xpath('//a[@class="showDetails"]')
	movies=[i.text for i in movies]
	for i in movies:
		for j in fav:
			if j.lower() in i.lower():
				found.append(i)
	startTime=[]
	stap=[]
	endTime=[]
	etap=[]
	for i in range(len(movies)):
		temp=driver.find_element_by_id("starttime_{}".format(i+1)).text
		temp1,temp2=temp.split(' ')
		startTime.append(temp1)
		stap.append(temp2)
		# print(temp1,temp2)
		temp=driver.find_element_by_id("endtime_{}".format(i+1)).text
		temp1,temp2=temp.split(' ')
		endTime.append(temp1)
		etap.append(temp2)
		# print(temp1,temp2)
	return startTime,stap,endTime,etap,movies,found

			

def hey():
	print('hey you can watch this movie')

login()
startTime,stap,endTime,etap,movies,found=logic()

msg=''
for i in found:
	indx=movies.index(i)
	msg+=i+'\n'+'StartTime:'+startTime[indx]+' '+stap[indx]+'\n'+'EndTime:'+endTime[indx]+' '+etap[indx]+'\n'


print(msg)