#code for a temperature convertor that converts temperatures in Celicius, Fahrenheight and Kelvin

FAHRENHEGHT = 1
CELICIUS = 2
KELVIN = 3

user_choice = input("Enter the conversion you want to proceed with, \n 1. Fahrenheight to Celicius. \n 2. Celicius to Fahrenheight. \n 3. Fahrenheight to Kelvin. \n 4. Kelvin to Fahrenheight. \n 5. Celicius to Kelvin. \n 6. Kelvin to Celicius.: ")

if user_choice == "1":
    fah = float(input("Enter the temperature in fahrenheight: "))
    cel = (fah - 32) * 5/9
    print(str(fah) + " degrees Fahrenheight is " + str(cel) + " degrees Celicius.")
elif user_choice == "2":
    cel = float(input("Enter the temperature in Celicius: "))
    fah = (cel * 9/5) + 32
    print(str(cel) + " degress Celicius is " + str(fah) + " degrees Fahrenheight.")
elif user_choice == "3":
    fah = float(input("Enter the tempearture in Fahrenheit: "))
    kel = (fah * 5/9) + 459.67
    print(str(fah) + " degrees in Fahrenheight is " + str(kel) + " degress Kelvin." )
elif user_choice == "4":
    kel = float(input("Enter the temperature in Kelvin: "))
    fah = ((kel - 273.15) * 9/5) + 32
    print(str(kel) + " degress Kelvin is " + str(fah) + " degress Fahrenheight.")
elif user_choice == "5":
    cel = float(input("Enter the temperature in Celsius: "))
    kel = (cel + 273.15)
    print(str(cel) + " degress Celicius is " + str(kel) + " degress Kelvin.")
elif user_choice == "6":
    kel = float(input("Enter the temperature in Kelvin: "))
    cel = (kel - 273.15)
    print(str(kel) + " degress Kelvin is " + str(cel) + " degress Celicius.")
else:
    print("Please select either option 1 0r 2.")
