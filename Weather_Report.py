# DSC 510 Intro to Programming
# Programming Assignment Final Project ( Week 12)
# Writing program to display the weather report either by zip code or name of city + state
# Sameer Nepal
# Date : November 20, 2021

import requests    # importing the request library


def main():
    """main function where user can choose the option to display weather by city/state or zipcode"""
    method = input("\nWould you like to lookup weather data by US City or zip code?"
                   "Enter 1 for US City 2 for Zip ")
    while not (method == "1" or method == "2"):
        method = input("Wrong entry!!! Enter 1 for US City 2 for Zip ")
    if method == "1":
        city()
    if method == "2":
        zip_code()


def city():
    """Function where name of city and state is used to gather the weather report"""
    city = input("\nPlease enter the name of city ").strip().upper()
    state = input('Please enter the state abbreviation ').strip().upper()
    url_city = base_url + "q=" + city + "," + state + ",US&appid=cd295d1ee8a9d0884cf6a0eecc61695a"  # creating url using the api key to get connetcted to the data
    try:  # checking whether the entered city exists in the database
        response = requests.get(url_city)  # getting the data from the api
        data = response.json()      # getting the jason of the response
        main_data = data['main']
    except LookupError:
        city = input('An Error has occurred with making the connection. Please enter another city ').strip().upper()
    unit = input("Would you like to view temps in Fahrenheit, Celsius, or Kelvin."
                 " Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin ").upper().strip()
    while not (unit == 'F' or unit == 'C' or unit == 'K'):
        unit = input("Invalid!!! Would you like to view temps in Fahrenheit, Celsius, or Kelvin."
                     "Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:").upper().strip()
    if unit == 'K':
        url_city = base_url + "q=" + city + "," + state + ",US&appid=cd295d1ee8a9d0884cf6a0eecc61695a"
    if unit == 'C':
        url_city = base_url + "q=" + city + "," + state + ",us&units=metric&appid=cd295d1ee8a9d0884cf6a0eecc61695a"
    if unit == 'F':
        url_city = base_url + "q=" + city + "," + state + ",us&units=imperial&appid=cd295d1ee8a9d0884cf6a0eecc61695a"
    response = requests.get(url_city)
    data = response.json()
    main_data = data['main']     # getting the values present in main key  which contains the min, max temp we are interested in
    cloud = data['weather']      # getting the values in weather key which has cloud cover information
    print('\n Current weather condition for', city, '\n',
          'Current Temp:', main_data['temp'], 'degrees', unit, '\n',  # getting the temp value from the key main
          'High Temp:', main_data['temp_max'], 'degrees', unit, '\n',
          'Low Temp:', main_data['temp_min'], 'degrees', unit, '\n',
          'Pressure:', main_data['pressure'], 'hPa', '\n',
          'Humidity:', main_data['humidity'], '%', '\n',
          'Cloud Cover:', cloud[0]['description'], '\n',  # getting the description value from the key weather
          )
    again = input('Do you want to perform another lookup Y or N ').upper().strip()  # asking if customers want to search again
    while not (again == 'Y' or again == 'N'):   # condition that keeps running until customer enter Y or N
        again = input('You did not enter correct.\n\nDo you want to perform another lookup Y or N ').upper().strip()
    if again == 'Y':
        main()
    if again == 'N':
        print('Please, Comeback when you need weather information')


def zip_code():
    """function used to display the weather condition  using zip code"""
    zip_code = input('\nWhat is the zip code you want to search for? ').strip()
    url_zip = base_url + "zip=" + zip_code + ",us&appid=cd295d1ee8a9d0884cf6a0eecc61695a"  # url for zip in the api
    try:
        response = requests.get(url_zip)
        data = response.json()
        main_data = data['main']
    except LookupError:
        zip_code = input('An Error has occurred with making the connection. Please enter another zip ').strip()
    unit = input("Would you like to view temperature in Fahrenheit, Celsius, or Kelvin."
                 " Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin ").upper().strip()
    while not (unit == 'F' or unit == 'C' or unit == 'K'):  # using while loop to use customer input to selects the units
        unit = input("Invalid!!! Would you like to view temperature in Fahrenheit, Celsius, or Kelvin."
                     " Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:").upper().strip()
    if unit == 'K':
        url_zip = base_url + "zip=" + zip_code + ",us&appid=cd295d1ee8a9d0884cf6a0eecc61695a"  # url to display Kelvin unit
    if unit == 'C':
        url_zip = base_url + "zip=" + zip_code + ",us&units=metric&appid=cd295d1ee8a9d0884cf6a0eecc61695a"  # url to display Celsius
    if unit == 'F':
        url_zip = base_url + "zip=" + zip_code + ",us&units=imperial&appid=cd295d1ee8a9d0884cf6a0eecc61695a"  # url to display Fahrenheit
    response = requests.get(url_zip)
    data = response.json()
    main_data = data['main']
    cloud = data['weather']
    print('\n Current weather condition for Zip ', zip_code, '\n',
          'Current Temp:', main_data['temp'], 'degrees', unit, '\n',
          'High Temp:', main_data['temp_max'], 'degrees', unit, '\n',
          'Low Temp:', main_data['temp_min'], 'degrees', unit, '\n',
          'Pressure:', main_data['pressure'], 'hPa', '\n',
          'Humidity:', main_data['humidity'], '%', '\n',
          'Cloud Cover:', cloud[0]['description'], '\n',
          )
    again = input('Do you want to perform another lookup Y or N ').upper().strip()
    while not (again == 'Y' or again == 'N'):
        again = input('You did not enter correct.\n\nDo you want to perform another lookup Y or N').upper().strip()
    if again == 'Y':
        main()
    if again == 'N':
        print('Please, Comeback when you need weather information')


print('Welcome to the program which displays the weather report by city or zip code')  # welcoming the user to the weather report program
base_url = "http://api.openweathermap.org/data/2.5/weather?"  # base url where api key is added to get the contents of the website

if __name__ == '__main__':     # calling the main function
    main()
