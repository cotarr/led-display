#!/usr/bin/python3
#
"""Raspberry Pi Sense Hat remote temperature display

This is a simple program used to display the current 
temperature on a Raspberry Pi Sense Hat.
A http client is used to obtain temperature data
from a different Raspberry Pi on the local network.

The main-dual-sensor.py version will support either single 
sensor, where data is a python dictionary or dual sensor, 
where data is a python list containing two dictionaries.

In the case of outdoor sensors where one sensor is in
morning sun and the other sensor is in afternoon sun
the lower value (in the shade) will be selected.


Single sensor data format
{
    "timestamp": 1674937453,
    "data": -4.437,
    "error": 0,
    "errorMessage": ""
}


Dual sensor data format

[
    {
        "timestamp": 1674937453,
        "data": 21.437,
        "error": 0,
        "errorMessage": ""
    },
    {
        "timestamp": 1674937453,
        "data": 19.233,
        "error": 0,
        "errorMessage": ""
    }
]

timestamp - Integer (Unix time in seconds)
data - Float (Temperature in degrees C)
error - Integer (error code, 0 = no error)
errorMessage - String, empty string if no error.
"""

import json
import time

import api_get_data
import local_get_data
import led_2_digit
import copy

#
# Configuration file: ./config.json (See README.md)
#
config = {}
try:
    f = open("./config.json","r")
    config = json.load(f)
    f.close()
except Exception as x:
    print("Configuration error {}".format(x))
    exit(1)

#
# Validate expected keys in config.json file.
#
if "brightness"           in config and \
    "units"               in config and \
    "address"             in config and \
    "path"                in config and \
    "use_ssl"             in config and \
    "ssl_check_hostname"  in config and \
    "ssl_custom_certs"    in config and \
    "ssl_CA_cert"         in config and \
    "ssl_client_cert"     in config and \
    "ssl_client_key"      in config and \
    "local_sensor_enable" in config and \
    "local_calib_zero"    in config and \
    "local_calib_span"    in config:
    pass
else:
    print("Configuration error, missing key in config.json")
    exit(1)
#
# Validate Units are C, F, or B (B =  Both, alternating C and F)
#
if config["units"] != "C" and config["units"] != "F" and config["units"] != "B":
    print("Configuration error: units must be: C, F, or B (B=both)")
    exit(1)

#
# Validate brightness 0-255
#
brightness = config["brightness"]
if brightness < 0 or brightness > 255:
    print("Configuration error: Brightness must be 0-255")
    exit(1)

error_brightness = config["brightness"]
if error_brightness < 150:
    error_brightness = 150

#
# Validate calibration span value not zero
#
if config["local_calib_span"] < 0.1:
    print("Configuration error: local_calib_span out of range")
    exit(1)

def get_timestamp():
    """Get current linux timestamp in seconds"""
    return int(time.time())

# In seconds
data_expiration = 180
# Temperature in C
data_minimum_valid = -50
data_maximum_valid = 150

# Display will show expired data ("EE") until a valid read.
cached_data = {
    "timestamp": 0,
    "data": -100,
    "error": 20,
    "errorMessage": "No Cached data"
}
cached_data2 = {
    "timestamp": 0,
    "data": -100,
    "error": 20,
    "errorMessage": "No Cached data (sensor 2)"
}
sensor_count = 1
cached_sensor_count = 1

#
# Program enters infinite loop for data collection
#
while 0==0:
    gauge_temp = -100
    data_age = 0
    error_exist = False

    # Illuminate activity indicator for network activity
    led_2_digit.set_activity(0, brightness)

    #
    # Part 1 of 3, data request
    #
    try:
        # Build SSL/TLS options from config file.
        options = {}
        options["use_ssl"]        = config["use_ssl"]
        options["check_hostname"] = config["ssl_check_hostname"]
        options["custom_certs"]   = config["ssl_custom_certs"]
        options["cafile"]         = config["ssl_CA_cert"]
        options["certfile"]       = config["ssl_client_cert"]
        options["keyfile"]        = config["ssl_client_key"]


        if config["local_sensor_enable"]:
            # Use the local Sense Hat board to obtain temperature
            data_json = local_get_data.read_sense_hat(config["local_calib_zero"], config["local_calib_span"])
        else:
            # Perform the HTTP GET request to read temperature from network
            data_json = api_get_data.call_API(config["address"], config["path"], options);

        if (type(data_json) == list) or (type(data_json) == dict):
            # Option 1, data is dictionary (single sensor)
            # Option 2, data is list of dictionaries (dual sensor)
            sensor_count = 1
            if type(data_json) == list:
                sensor_count = 2
                data_json2 = data_json[1]
                data_json = data_json[0]
        else:
            print("Error expect dictionary or list")
            error_exist = true

        if not error_exist:
            # Check API call for error code (from upstream)
            if "error" in data_json and data_json["error"] != 0:
                print(data_json["errorMessage"])
                error_exist = True
            if (not error_exist) and sensor_count == 2 and "error" in data_json2 and data_json2["error"] != 0:
                print(data_json2["errorMessage"])
                error_exist = True

        if not error_exist:
            # Check for required keys in response
            if  "data" in data_json and "timestamp" in data_json and \
                "error" in data_json and "errorMessage" in data_json:
                # Expire old data (seconds)
                if get_timestamp() - data_json["timestamp"] > data_expiration:
                    error_exist = True
                    print("Error: timestamp expired")
                # Check Data in Range, check for gauge error
                if (data_json["data"] < data_minimum_valid) or (data_json["data"] > data_maximum_valid):
                    error_exist = True
                    print("Error: data out of range")
            else:
                print('Error, json schema mis-match')
                error_exist = True

        if (not error_exist) and sensor_count == 2:
            # Check for required keys in response
            if  "data" in data_json2 and "timestamp" in data_json2 and \
                "error" in data_json2 and "errorMessage" in data_json2:
                # Expire old data (seconds)
                if get_timestamp() - data_json2["timestamp"] > data_expiration:
                    error_exist = True
                    print("Error: timestamp expired (sensor 2")
                # Check Data in Range, check for gauge error
                if (data_json2["data"] < data_minimum_valid) or (data_json2["data"] > data_maximum_valid):
                    error_exist = True
                    print("Error: data out of range (sensor 2")
            else:
                print('Error, json schema mis-match (sensor 2')
                error_exist = True

    except Exception as x:
        print("Error {}".format(x))
        error_exist = True

    #
    # Part 2 of 3 - Check for errors
    #
    if not error_exist:
        # Clear activity indicator for network activity
        led_2_digit.clear_activity(0)
        # Case of single sensor. Copy valid data to the cache
        cached_data = copy.deepcopy(data_json)
        cached_sensor_count = 1;
        if sensor_count == 2:
            # Case of dual ssensor, second dictionary for sensor 2
            cached_data2 = copy.deepcopy(data_json2)
            cached_sensor_count = 2;
    else:
        led_2_digit.set_error(0, error_brightness)
        pass

    #
    # Part 3 of # - Update Display
    #
    # Check if cache data is expired
    if get_timestamp() - cached_data["timestamp"] < data_expiration:
        # 
        # Case of Cache not expired, update display from cache
        #
        toggleUnits = False;
        for i in range(12):
            if toggleUnits == True:
                toggleUnits = False
            else: 
                toggleUnits = True

            # Case of single sensor, use value
            temp_C = cached_data["data"]
            # Case of dual sensor, take the lower of 2 values
            if (cached_sensor_count == 2) and (temp_C > cached_data2["data"]):
                temp_C = cached_data2["data"]

            if (config["units"] == "F") or ((config["units"] == "B") and (toggleUnits == True)):
                # Display Temperature in Degrees F
                temp_F = int((temp_C * 9.0 / 5.0 ) + 32.0)
                led_2_digit.show_2_digits(temp_F,0,1,brightness,brightness,0)
            else:
                # Display Temperature in Degrees C
                temp_C = int(temp_C)
                led_2_digit.show_2_digits(temp_C,0,1,0,brightness,brightness)
            time.sleep(2.25)
            # If alternating C and F, short activity indicator not required.
            if config["units"] != "B":
                # Illuminate activity indicator
                led_2_digit.set_activity(7, brightness)
            time.sleep(0.25)
            led_2_digit.clear_activity(7)
            time.sleep(2.5)

    else:
        #
        # Case of cache is expired, display error ("EE")
        #
        # Error display does not require additional error LED
        led_2_digit.clear_activity(0)
        # Else, Case of Cache expired. Display "EE" to show error
        for i in range(12):
            led_2_digit.show_2_digits(1000,0,1,error_brightness,0,0)
            time.sleep(2.25)
            # Illuminate activity indicator
            led_2_digit.set_activity(7, brightness)
            time.sleep(0.25)
            led_2_digit.clear_activity(7)
            time.sleep(2.5)

