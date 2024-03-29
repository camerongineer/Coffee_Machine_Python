import drink

required_water = 200
required_milk = 50
required_beans = 15
water_ml = 400
milk_ml = 540
bean_grams = 120
cups = 9
money = 550


def menu():
    while True:
        option = input("Write action (buy, fill, take, remaining, exit): \n")
        if option == "fill":
            add_supplies()
        elif option == "buy":
            buy_drink()
        elif option == "take":
            withdrawal_money()
        elif option == "remaining":
            display_machine_supplies()
        elif option == "exit":
            return
        else:
            print("Invalid input")
        print()


def display_machine_supplies():
    print("The coffee machine has:\n"
          + f"{water_ml} ml of water\n"
          + f"{milk_ml} ml of milk\n"
          + f"{bean_grams} g of coffee beans\n"
          + f"{cups} disposable cups\n"
          + f"${money} of money")


def add_supplies():
    global water_ml
    global milk_ml
    global bean_grams
    global cups
    print("Write how many ml of water you want to add:")
    water_ml += int(input())
    print("Write how many ml of milk you want to add:")
    milk_ml += int(input())
    print("Write how many grams of coffee beans you want to add:")
    bean_grams += int(input())
    print("Write how many disposable cups you want to add:")
    cups += int(input())


def has_enough_resources(coffee_type):
    global water_ml
    global milk_ml
    global bean_grams
    global cups
    short_supplies = list()
    if coffee_type.water.value > water_ml:
        short_supplies.append("water")
    if coffee_type.milk.value > milk_ml:
        short_supplies.append("milk")
    if coffee_type.beans.value > milk_ml:
        short_supplies.append("beans")
    if cups == 0:
        short_supplies.append("cups")
    if len(short_supplies) == 0:
        return True
    else:
        print(f"Sorry, not enough {', '.join(short_supplies)}!")
        return False


def buy_drink():
    global water_ml
    global milk_ml
    global bean_grams
    global cups
    global money
    option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
    if option == "1":
        coffee_type = drink.Espresso
    elif option == "2":
        coffee_type = drink.Latte
    elif option == "3":
        coffee_type = drink.Cappuccino
    elif option == "back":
        return
    else:
        print("Invalid input")
        return
    if has_enough_resources(coffee_type):
        print("I have enough resources, making you a coffee!")
        water_ml -= coffee_type.water.value
        milk_ml -= coffee_type.milk.value
        bean_grams -= coffee_type.beans.value
        cups -= 1
        money += coffee_type.cost.value


def withdrawal_money():
    global money
    print(f"I gave you ${money}")
    money = 0


menu()
