# Functions (have at least 4 functions)
# Project 2: Barista Coffee Assistant
#
# Name: Tyler Baxter
# Section: 03
# Date: 01/24/22
#

from sys import exit


# This function prompts the user for a coffee type and returns it
# none -> string
def coffee_type():
    c_type = input("What coffee type would you like? ")
    c_type = c_type.lower()
    counter = 1
    while not((c_type == "americano") or (c_type == "flat white") or (c_type == "latte") or (c_type == "espresso")):
        counter += 1
        if counter > 3:
            print("Sorry, we cannot help you here.")
            exit()
        c_type = input("Can you please try again? ")
    return c_type


# This function prompts the user if they want milk of not, and returns the value
# none -> string
def milk_on_the_side(c_type):
    milk = "n"
    if (c_type == "americano") or (c_type == "espresso"):
        milk = input("Would you like milk on the side (y,n)? ")
        milk = milk.lower()
        counter = 1
        while not((milk == "y") or (milk == "n")):
            counter += 1
            if counter > 3:
                print("Sorry, we cannot help you here.")
                exit()
            milk = input("Can you please try again? ")
    return milk


# This function prompts the user if they want to have their coffee takeout
# none -> string
def order_for_takeout():
    takeout = input("Is your coffee takeout (y,n)? ")
    takeout = takeout.lower()
    counter = 1
    while not((takeout == "y") or (takeout == "n")):
        counter += 1
        if counter > 3:
            print("Sorry, we cannot help you here.")
            exit()
        takeout = input("Can you please try again? ")
    return takeout


# This function prompts the user for what size drink they want
# none -> string
def coffee_size():
    size = input("What size would you like (Large, Medium, Small)? ")
    size = size.lower()
    counter = 1
    while not((size == "large") or (size == "medium") or (size == "small")):
        counter += 1
        if counter > 3:
            print("Sorry, we cannot help you here.")
            exit()
        size = input("Can you please try again? ")
    return size


# This function calculates the price based on the type, milk or not, and size
# string, string, string -> float
def order_price(cof_type, milk, size):
    price = 0.0
    if cof_type == "flat white":
        if size == "small":
            price = 2.95
        if size == "medium":
            price = 3.00
        if size == "large":
            price = 3.75
    if cof_type == "americano":
        if size == "small":
            price = 2.75
        if size == "medium":
            price = 2.95
        if size == "large":
            price = 3.25
    if cof_type == "espresso":
        if size == "small":
            price = 2.75
        if size == "medium":
            price = 2.95
        if size == "large":
            price = 3.25
    if cof_type == "latte":
        if size == "small":
            price = 2.85
        if size == "medium":
            price = 3.75
        if size == "large":
            price = 4.15
    if milk == "y":
        price += 0.25
    return price


# This function prints out the coffee type, size, price, milk(y/n) and takeout(y/n)
# string, string, string, string, int -> none
def print_info(c_type, size, milk, takeout, price):
    print()
    if c_type == "americano":
        print("Americano")
    elif c_type == "flat white":
        print("Flat White")
    elif c_type == "latte":
        print("Latte")
    elif c_type == "espresso":
        print("Espresso")
    if size == "large":
        print("Large")
    if size == "medium":
        print("Medium")
    if size == "small":
        print("Small")
    if milk == "y":
        print("Milk on the side")
    else:
        print("No extras")
    if takeout == "y":
        print("Takeout")
    else:
        print("In cafe")
    print("Please pay $", price, "to the cashier")
