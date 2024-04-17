from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
import time


def book(url, dots, user_name, user_phone_number, user_email):
    print("Выберите количество билетов которое хотите купить: ")
    ticket_quantity = int(input())
    # Указать путь к WebDriver
    webdriver_path = 'D:\\Python_Problems\\chromedriver.exe'  # Убедитесь, что путь указан правильно

    # Создание объекта Service с указанием пути к ChromeDriver
    service = Service(executable_path=webdriver_path)

    # Настройка опций браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    # Инициализация драйвера с использованием Service и опций
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)  # Перейти на нужную веб-страницу
    time.sleep(10)

    driver.find_element(By.CLASS_NAME, 'outline-x24-icon-plus').click()

    for i in range(ticket_quantity):
        # Предположим, что у вас есть координаты относительно всего экрана
        absolute_x = dots[i][0]
        absolute_y = dots[i][1] + 55  # Подгоняем координату y потому что на скриншоте не учиывается интерфейс
        # Переместить мышь к абсолютным координатам и выполнить клик
        pyautogui.moveTo(absolute_x, absolute_y)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
    pyautogui.moveTo(1770, 960)
    pyautogui.click()
    time.sleep(4)

    driver.find_element(By.NAME, 'name').send_keys(user_name)
    driver.find_element(By.NAME, 'phone').send_keys(user_phone_number)
    driver.find_element(By.NAME, 'email').send_keys(user_email)
    pyautogui.moveTo(950, 800)
    pyautogui.click()
    time.sleep(7)
    screenshot = driver.get_screenshot_as_png()
    driver.save_screenshot("result.png")
    driver.quit()  # Закрытие браузера после создания скриншота

