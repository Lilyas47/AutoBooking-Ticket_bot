import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import re


def change_url_to_clean(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Парсим html с помощью bs4
        soup = BeautifulSoup(response.text, "lxml")
        # Ищем div с 'intickets-frame-container' class
        container = soup.find('div', class_='intickets-frame-container')
        # Извлекаем URL из 'data-url'
        if container:
            url = container.get('data-url')
            return url
        else:
            print("URL не найден")
    else:
        print("Не получилось загрузить страницу")


def parse_prices(url):
    prices = []
    list_rgb_values = []
    webdriver_path = 'D:\\Python_Problems\\chromedriver.exe'
    service = Service(executable_path=webdriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Uncomment if you do not want a browser GUI to pop up
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url)

        # Ждем пока картинка отрисуется
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'price-view'))
        )

        # Extract the element after the page has fully loaded
        price_view_elements = driver.find_elements(By.CLASS_NAME, 'price-view')

        for element in price_view_elements:
            cleaned_price = element.text.strip()
            prices.append(cleaned_price)

        color_view_elements = driver.find_elements(By.CLASS_NAME, 'legend-color')

        for element in color_view_elements:
            style_attribute = element.get_attribute('style')
            match = re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', style_attribute)
            if match:
                rgb_values = list(map(int, match.groups()))
                list_rgb_values.append(rgb_values)
                print(rgb_values)
            else:
                print("No RGB values found.")
            print(style_attribute)

    finally:
        driver.quit()

    return prices, list_rgb_values





