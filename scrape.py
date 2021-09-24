import json
import os
import random
import time

from selenium import webdriver

from send_email import send_email

file = open('products.json')
data = json.load(file)
file.close()

browser = webdriver.Chrome()

while True:
    for index, product in enumerate(data['products']):
        try:
            browser.get(product['url'])
            for condition in browser.find_elements_by_class_name('condition-label'):
                condition.click()
                time.sleep(1)
                if condition.text != 'Digital' and browser.find_element_by_class_name('add-to-cart').text == 'ADD TO CART':
                    send_email(product['name'], product['url'],
                               condition=condition.text)
        except Exception as error:
            send_email(product['name'], product['url'],
                       subject='Error', error=error)
            continue
        finally:
            time.sleep(random.randint(5, 10))
