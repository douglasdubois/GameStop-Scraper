import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from send_email import send_email

file = open('products.json')
data = json.load(file)
file.close()

options = Options()
options.add_argument("--headless")

while True:
    for index, product in enumerate(data['products']):
        try:
            browser = webdriver.Chrome(options=options)
            browser.get(product['url'])
            for condition in browser.find_elements_by_class_name('condition-label'):
                if condition.text != 'Digital':
                    condition.click()
                    time.sleep(1)
                    if browser.find_element_by_class_name('add-to-cart').text == 'Add to Cart':
                        send_email(
                            product['name'], product['url'], condition=condition.text)
        except Exception as error:
            send_email(product['name'], product['url'],
                       subject='Error', error=error)
            pass
        finally:
            browser.close()
            time.sleep(5)
