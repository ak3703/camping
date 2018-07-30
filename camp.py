from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys, os

SOL_DUC = "https://www.recreation.gov/camping/sol-duc-hot-springs-resort-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=139890"

KALALOCH = "https://www.recreation.gov/camping/kalaloch/r/campgroundDetails.do?contractCode=NRSO&parkId=70944"

def get_tickets():
    ''' opens a new chrome application and clicks on the register then checkout button'''
    # MANDATORY: include direct path to chromedriver here
    driver = webdriver.Chrome(os.path.dirname(os.path.realpath(__file__)) + '/chromedriver')
    # wait until time is equal or after ticket_time to open the site and click the buttons
    # opens bacchanal eventbrite ticketing page
    driver.get(SOL_DUC)

    arrivalDate = driver.find_element_by_id("arrivalDate") 
    arrivalDate.clear()
    arrivalDate.send_keys("08/11/2018")
    
    departureDate = driver.find_element_by_id("departureDate") 
    departureDate.clear()
    departureDate.send_keys("Tue Jul 31 2018")

    driver.find_element_by_id("filter").click()

    result = driver.find_element_by_class_name("matchSummary").get_attribute('innerHTML')

    if int(result.split(" ")[0]) >= 0 :
        print(result.split(" ")[0])

    while 1:
        continue
           


if __name__ == "__main__":
    get_tickets()    

