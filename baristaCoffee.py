# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Tyler Baxter
# Section: 03
# Date: 01/24/22
#
from baristaCoffeeFuncs import *


def main():
    repeat = "y"
    while repeat == "y":
        drink = coffee_type()
        milk = milk_on_the_side(drink)
        take = order_for_takeout()
        size = coffee_size()
        price = order_price(drink, milk, size)
        print_info(drink, size, milk, take, price)
        repeat = input("Would you like to order again (y/n)? ")
        while not (repeat == "n" or repeat == "y"):
            repeat = input("Would you like to order again (y/n)? ")
        print()


if __name__ == '__main__':
    main()
