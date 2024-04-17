from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def make_screenshot(url):
    webdriver_path = 'D:\\Python_Problems\\chromedriver.exe'  # Убедитесь, что путь указан правильно

    # Создание объекта Service с указанием пути к ChromeDriver
    service = Service(executable_path=webdriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    # Инициализация драйвера с использованием Service и опций
    driver = webdriver.Chrome(service=service, options=options)
    # Устанавливаем размер окна браузера

    driver.get(url)  # Перейти на нужную веб-страницу
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, 'outline-x24-icon-plus').click()
    time.sleep(3)
    # Создание скриншота страницы
    driver.save_screenshot("screenshot.png")
    driver.quit()  # Закрытие браузера после создания скриншота


