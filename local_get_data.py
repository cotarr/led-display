"""Module to read the Raspberry Pi Sense Hat Sensors

This module includes the function read_sense_hat() that will 
perform a temperature query of the Sense Hat on board 
temperature sensor. Successful request will return 
a Python dictionary.
"""

import json
import time

from sense_hat import SenseHat
sense = SenseHat()

def read_sense_hat(calibration_zero: float, calibration_span: float):
    """Read the Sense Hat on-board temperature sensor.
    calibration_zero - Float, Temperature calibration offset
    calibration_span - Float, Temperature calibration span
    Adjusted Value = (Actual * calibration_span) + calibration_zero.
    Returns - Python dictionary containing decoded JSON data."""

    try:
        temperature = sense.get_temperature()

        temperature = (temperature * calibration_span) + calibration_zero

        jsondata = {}
        jsondata['timestamp'] = int(time.time())
        jsondata['data'] = temperature
        jsondata['error'] = 0
        jsondata['errorMessage'] = ""

    except Exception as x:
        jsondata = {}
        jsondata['timestamp'] = int(time.time())
        jsondata['data'] = -100
        jsondata["error"] = 8
        jsondata["errorMessage"] = "Sense Hat Error: {}".format(x)

    return jsondata

if __name__ == "__main__":
    # For debug read the sensor and display result
    #
    f = open("./config.json","r")
    config = json.load(f)
    f.close()

    sh_data = read_sense_hat(config["local_calib_zero"], config["local_calib_span"])
    
    print(json.dumps(sh_data, indent=4))
