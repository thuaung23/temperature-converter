# This program convert temperature from Celsius to Fahrenheit, Kevin and vice versa.
# Written by: Thu Aung
# Written on: Sept 9, 2020

# Create a function to convert Celsius temperature to Fahrenheit.
def cel_to_fah():
    return ((temp * 9) / 5 ) + 32

# Create a function to convert Fahrenheit temperature to Celsius.
def fah_to_cel():
    return ((temp - 32) * 5) / 9

# Create a function to convert Celsius temperature to Kevin.
def cel_to_kev():
    return temp + 273.15

# Create a function to convert Kevin temperature to Celsius.
def kev_to_cel():
    return temp - 273.15

while True:
    # Take user's input as a string to decide which function to call.
    choice = input("Please enter 1, 2, 3 , 4 or 5 for (C-->F), (F-->C), (C-->K), (K-->C), (QUIT?) respectively: ")

    if choice == '1':
        temp = float(input("Enter temperature in Celsius: "))
        # Take user input of temperature and call the respective function created above.
        print(f'The temperature is {cel_to_fah(): 1.2f} Fahrenheit.')

    elif choice == '2':
        temp = float(input("Enter temperature in Fahrenheit: "))
        # Take user input of temperature and call the respective function created above.
        print(f'The temperature is {fah_to_cel(): 1.2f} Celsius.')

    elif choice == '3':
        temp = float(input("Enter temperature in Celsius: "))
        # Take user input of temperature and call the respective function created above.
        print(f'The temperature is {cel_to_kev(): 1.2f} Kevin.')

    elif choice == '4':
        temp = float(input("Enter temperature in Kevin: "))
        # Take user input of temperature and call the respective function created above.
        print(f'The temperature is {kev_to_cel(): 1.2f} Kevin.')

    elif choice == '5':
        print("Thank you for using this temperature converter.")
        print('Have a great day!!!')
        break

    else:
        # This is to make sure user input only valid numbers.
        print("Please enter 1, 2, 3 or 4")