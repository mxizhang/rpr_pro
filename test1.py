from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def init_phantomjs_driver(*args, **kwargs):

    headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Connection': 'keep-alive'
    }

    for key, value in headers.iteritems():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

    driver =  webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1600, 1200)

    return driver


def main():

	driver = init_phantomjs_driver(service_args=['--load-images=no'])
	driver.get("https://www.narrpr.com/")

	driver.get_screenshot_as_file('rpr1.png')
	print "#################Logging In################"
	user = driver.find_element_by_name("SignInEmail")
	user.send_keys("1992crodriguez@gmail.com")
	pasw = driver.find_element_by_name("SignInPassword")
	pasw.send_keys("471amwell")
	driver.find_element_by_xpath("//*[@id='SignInBtn']").click()
	time.sleep(5)

	#driver.get_screenshot_as_file('rpr2.png')

	try:
		driver.find_element_by_xpath('//*[@id="ui-id-1"]/div/a').click()
	except:
		pass

	address = driver.find_element_by_xpath('//*[@id="SiteSearchForm_SearchTxt"]')
	address.send_keys('101 13th Street, Somerset')
	driver.find_element_by_xpath('//*[@id="SiteSearchForm_SearchBtn"]').click()
	time.sleep(5)
	driver.get_screenshot_as_file('rpr3.png')
	print driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div[3]/div[2]/div/div[1]/span').text
	print driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div[3]/div[2]/div/div[2]/div[2]').get_attribute("origscore")

	driver.back()
	driver.get_screenshot_as_file('rpr4.png')

if __name__ == "__main__":
	main()