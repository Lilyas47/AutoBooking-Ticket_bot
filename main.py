from Parse_url import *
from search_coordinates import *
from Screenshoting_tickets import *
from Booking_tickets import *

def menu(prices, colors):
    print("Выберите цену: ")
    for price in range(len(prices)):
        print(price + 1, prices[price])
    selected_price = input()
    print("Сейчас вам потребуется ввести ваши данные, сделайте это внимательно!")
    print("Введите ваше ФИО: ")
    user_name = input()
    print("Введите ваше номер телефона: ")
    user_phone_number = input()
    print("Введите вашу почту: ")
    user_email = input()
    return user_name, user_phone_number, user_email


print("Скопируйте ссылку на ваше мероприятие: ")
url = input()

url = change_url_to_clean(url)
prices, colors = parse_prices(url)

user_name, user_phone_number, user_email = menu(prices, colors)
make_screenshot(url)
dots = search_coord()
book(url, dots, user_name, user_phone_number, user_email)

