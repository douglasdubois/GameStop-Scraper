import json
import os
import random
import time

from selenium import webdriver

from send_email import send_email

file = open('products.json')
data = json.load(file)
file.close()

browser = webdriver.Chrome('./chromedriver*')

while True:
    for index, product in enumerate(data['products']):
        try:
            browser.get(product['url'])
            # conditions = browser.find_elements_by_class_name('condition-label')
            for condition in browser.find_elements_by_class_name('condition-label'):
                condition.click()
                if browser.find_element_by_class_name('add-to-cart').text == 'ADD TO CART':
                    send_email(product['name'], condition=condition.text, url=product['url'])
                time.sleep(1)
        except Exception as error:
            send_email(product['name'], subject="Error", error=error)
        finally:
            time.sleep(random.randint(5, 10))
