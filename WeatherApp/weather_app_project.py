# Weather App - Final Project
# Author Soma Shekar Vayuvegula
# 06/03/2022

# Change#:1
# Change(s) Made: Final project - Using weather app
# Date of Change: 06/03/2022
# Author: Soma Shekar Vayuvegula
# Change Approved by: Michael Eller
# Date Moved to Production: 06/03/2022

import requests


# Function to call Weather App API and display required details
# input params: city_name, lat, lon, units
# return params: None
def weather_details(city_name, lat, lon, units):
    api_key = "c2fa89cf96d6e6aac35fa58ca717cf5d"
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}"

    try:
        response = requests.get(url)
        if response is not None and response.status_code is not None and response.status_code == 200:
            json_response = response.json()
            response_main = json_response['list'][0]['main']
            response_weather = json_response['list'][0]['weather']
            current_temp = response_main['temp']
            high_temp = response_main['temp_max']
            low_temp = response_main['temp_min']
            pressure = response_main['pressure']
            humidity = response_main['humidity']

            print("\n\nCurrent Weather Conditions For", city_name)
            print("==============================================\n")
            print("Current Temp: ", current_temp, "degrees")
            print("High Temp: ", high_temp, "degrees")
            print("Low Temp: ", low_temp, "degrees")
            print("Pressure: ", pressure, "hPa")
            print("Humidity: ", humidity, "%")
            for weather in response_weather:
                weather_main = weather['main']
                cloud_cover = weather['description']
                if weather_main == 'Clouds':
                    print("Cloud Cover: " + cloud_cover)
                else:
                    print("Description: " + cloud_cover)
        else:
            print("Received error response from Weather App API:", response.status_code, response.reason)

    except Exception as ex:
        print("Exception occurred while calling Weather App API:", ex)


# Function to geo details API by city name
# input params: city_name, state_cd, units
# return params: None
def geo_details_city(city_name, state_cd, units):
    limit = 5
    api_key = "c2fa89cf96d6e6aac35fa58ca717cf5d"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_cd},USA&limit={limit}&appid={api_key}"

    try:
        response = requests.get(url)
        if response is not None and response.status_code is not None and response.status_code == 200:
            json_response = response.json()

            lat = json_response[0]['lat']
            lon = json_response[0]['lon']

            weather_details(city_name, lat, lon, units)
        else:
            print("Received error response from Geo Details API:", response.status_code, response.reason)
    except Exception as e:
        print("Exception occurred while calling Geo Details API:", e)


# Function to geo details API by ZIP code
# input params: zip_cd, units
# return params: None
def geo_details_zip(zip_cd, units):
    api_key = "c2fa89cf96d6e6aac35fa58ca717cf5d"
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_cd}&appid={api_key}"

    try:
        response = requests.get(url)
        if response is not None and response.status_code is not None and response.status_code == 200:
            json_response = response.json()

            lat = json_response['lat']
            lon = json_response['lon']
            city_name = json_response['name']

            weather_details(city_name, lat, lon, units)
        else:
            print("Received error response from Geo Details API: ", response.status_code, response.reason)
    except Exception as e:
        print("Exception occurred while calling Geo details API: ", e)


# Mapping function to map temperature units provided by user to units accepted by weather app API.
# input params: units
# return params: app_units
def weather_units(units):
    if units is not None:
        if units == 'C':
            return 'metric'
        elif units == 'F':
            return 'imperial'
        elif units == 'K':
            return 'standard'
        else:
            print("Defaulting to Kelvin temperature units as the entered temperature units is invalid.")


# Main function to request input from user and call a function for geo details API call.
def main():
    print("Welcome to Texas Meteorological Department!")
    lookup = True
    while lookup:
        input_type = input(
            "\n\nWould you like to lookup weather data by US City or ZIP code? Enter 1 for US City 2 for ZIP:")
        if input_type is not None and input_type != '' and input_type == "1":
            city_name = input("\nEnter city name:")
            state_cd = input("Enter state code:")
            units = input(
                " Would you like to view temps in Fahrenheit, Celsius, or Kelvin? Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin :")
            if city_name is not None and city_name != '' and state_cd is not None and state_cd != '':
                geo_details_city(city_name, state_cd, weather_units(units))
        elif input_type is not None and input_type != '' and input_type == "2":
            zip_cd = input("\nEnter Zip Code:")
            units = input(
                "Would you like to view temps in Fahrenheit, Celsius, or Kelvin? Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin :")
            if zip_cd is not None and zip_cd != '':
                geo_details_zip(zip_cd, weather_units(units))
            else:
                print("City name or State code or Country code cannot be null or blank. Please enter a valid value")
        else:
            print("Please enter a valid option - 1 for US City 2 for zip")

        lookup = input("\n\nWould you like to perform another weather lookup? (Y/N): ")
        if lookup.lower() == 'n':
            break


# Call to main method to start program execution
if __name__ == "__main__":
    main()
