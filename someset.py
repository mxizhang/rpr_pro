import time
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
'''
check: sale_no date address rpr_price print
'''
DOMAIN = 'http://www.co.somerset.nj.us/'
def save_items():
	list_all = []
	list_all.append(['sale_no', 'sale_date', 'address', 'pdf_link','rpr_price', 'screenshot'])

	driver = webdriver.PhantomJS()
	driver.get(DOMAIN+"government/elected-officials/sheriff-s-office/divisions/sheriff-sales")
	index = 3
	try:
		while(True):
			item = [0 for x in range(6)]
			text = driver.find_element_by_xpath('//*[@id="widget_4_3404_3181"]/p[%s]' % index).text.split('   ')
			#print text
			item[0] = text[0]
			item[1] = text[1]
			item[2] = text[2]
			list_all.append(item)
			index = index+1
	except Exception as e:
		driver.quit()
	with open("someset_items.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(list_all)
		
def check_rpr():
	#Sign In
	driver = webdriver.PhantomJS()
	driver.get("https://www.narrpr.com/")
	#driver.get_screenshot_as_file('rpr1.png')
	print "#################Logging In################"
	user = driver.find_element_by_name("SignInEmail")
	user.send_keys("1992crodriguez@gmail.com")
	pasw = driver.find_element_by_name("SignInPassword")
	pasw.send_keys("471amwell")
	driver.find_element_by_xpath("//*[@id='SignInBtn']").click()
	time.sleep(3)
	
def main():

	save_items()

if __name__ == "__main__":
    main()