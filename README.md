# led-display

## Description

This is a simple python3 program that uses a HTTP fetch request to 
retrieve the current temperature from a remote Raspberry Pi and 
display the remote temperature value on a Raspberry Pi Sense Hat 
8 x 8 LED display.

This is written in native python3. No external PIP dependencies are 
required, and running the program does not require a virtual environment.

### File: api_get_data.py

The file 'api_get_data.py' uses the internal python3 http.client 
module to perform an HTTP GET request. The expected response is a 
JSON object containing a Unix timestamp in seconds and a 
data property for temperature in degrees celsius.  

Expected response from remote IOT device:

```json
{
  "timestamp": 1675171358,
  "data": 21.875,
  "error": 0,
  "errorMessage": ""
}
```
where

```
timestamp - Integer (Unix time in seconds)
data - Float (Temperature in degrees C)
error - Integer (error code, 0 = no error)
errorMessage - String, empty string if no error.
```

### File: led_2_digit.py

The file 'led_2_digit.py' will convert the current temperature value 
into a 2 digit temperature value, configurable in either fahrenheit or celsius.
Drivers included with the Raspberry Pi Os are used to select 
and illuminate the 8 x 8 LED matrix in order to display 
numeric digits formed using 3 x 5 pixel characters.

Example, temperature of 34 degrees:

```
---------------------
|                   |
|   O O O   O   O   |
|       O   O   O   |
|   O O O   O O O   |
|       O       O   |
|   O O O       O   |
|                   |
---------------------
```

### File: local_get_data.py

The file 'local_get_data.py' contains code to read the local 
ambient temperature sensor on the Sense Hat board. The program 
can optionally be configured to use the local temperature sensor.
This will disable the network request for remote data.

### File: main.py

The file 'main.py' is the main program start file.
It will read and parse the configuration from the file 'config.json'.
On startup, it will initiate an infinite loop.
New data will be fetched once per minute. 
The Sense Hat display will be updated with the current temperature.

## References

Published documentation for the 
[Raspberry Pi Sense Hat](https://www.raspberrypi.com/documentation/accessories/sense-hat.html)

## Installation

### Background

The program originally written in 2015 using an older version of python3.
The code was cleaned up in 2023 using a fresh install of Raspberry Pi OS.

Hardware used:

- Raspberry Pi 2 Model B
- Raspberry Pi Sense Hat V 1.0 (2015)

Software used:

- Raspberry Pi OS armhf-lite (32 bit Debian 11 Bullseye 2022-09-22)
- Python 3.9.2 (Default with Raspberry Pi OS)

### Prerequisites

These instructions assume that a dedicated Raspberry Pi will 
be equipped with a Raspberry Pi Sense hat for the purpose 
of displaying a remote temperature. Therefore, it is 
recommended to perform a clean install of the current 
version of Raspberry Pi OS Lite 
from [here](https://www.raspberrypi.com/software/operating-systems/).
Any system updates should be installed at this time.

If you create a dedicated user to run this program, the user 
will need to belong to groups: gpio i2c input video

Install sense-hat software from Raspberry Pi OS package manager

```
sudo apt-get update
sudo apt-get install sense-hat
```

### Clone Repository

The led-display repository is located on GitHub. The easiest way 
to install the program is to clone the git repository using the 
terminal git command. If necessary, git may be installed on 
the Raspberry Pi using `sudo apt-get install git`.

Navigate to a directory where you wish to put the led-display program. 
The git repository can be cloned using the git clone command 
shown here. After cloning, change to the repository directory.

```
git clone https://github.com/cotarr/led-display.git
cd led-display
```

### Configuration

Copy the example configuration file using the following bash command.

```
cp -v example-config.json config.json
```

The configuration file is stored in JSON format.
To avoid a JSON parsing error, be careful to use the 
proper double quotes, commas, and lower case boolean true/false.

The "units" property can be set to "C" for Celsius, "F" for 
fahrenheit, or "B" for both. Fahrenheit will display in 
a yellow color, celsius will display in light blue. 
When set to both, the display will alternate each 5 seconds.

There are 2 choices for the source of the temperature data. 
If "local_sensor_enable" is set to true, the network 
data request will be disabled, and the source of the temperature 
will be set to use the on-board temperature sensor on 
the Raspberry Pi Sense Hat.
In practice, the on-board sensor tends to read an artificially 
high temperature due to heat generated on the Sense Hat board 
and the Raspberry Pi board.
In this case, the on-board temperature value can be 
corrected using the calibration zero and span parameters.
The zero and span parameters will not impact remote 
temperatures retrieved from the network.

When the "local_sensor_enable" is set to false, temperature will 
be retrieved from another Raspberry Pi on the local network. 
The "address" can be a valid domain name and port number 
"myhost.example.com:8000" of numeric IPV4 address and port 
number "192.168.0.120:8000" or IPV6 address and port "[fc00:1::1234]:8000".
The path specifies the data location on the remote API web server. 

Configuration Parameters:

| Parameter           | Example                       | Description                                        |
| ------------------- | :---------------------------- | :------------------------------------------------- |
| brightness          | 60                            | LED brightness value 0 to 255                      |
| units               | "F"                           | "F"=fahrenheit "C"=celsius "B"=Both (Alternate)    |
| address             | "127.0.0.1:8000"              | Domain-name:port or IP-address:port                |
| path                | "/v1/data/0"                  | API path on remote API web server                  |
| use_ssl             | false                         | Boolean value set to true to enable SSL/TLS        |
| ssl_check_hostname  | false                         | Verify remote hostname matches TLS certificate     |
| ssl_custom_certs    | false                         | Enable custom SSL/TLS certificates                 |
| ssl_CA_cert         | "/home/user1/.tls/CAcert.pem" | Filename of TLS CA certificate                     |
| ssl_client_cert     | "/home/user1/.tls/cert.pem"   | Filename of web server TLS server certificate      |
| ssl_client_key      | "/home/user1/.tls/key.pem"    | Filename of web server TLS private key certificate |
| local_sensor_enable | false                         | Boolean value set to true to use on-board sensor   |
| local_calib_zero    | 0.0                           | Calibration Sense Hat on-board sensor, default 0.0 |
| local_calib_span    | 1.0                           | Calibration Sense Hat on-board sensor, default 1.0 |

If SSL/TLS is disabled by setting "use_ssl" to false, 
custom certificate files are not required 
and the filename parameters will be ignored. 

If SSL/TLS is enabled, but the "ssl_custom_certs" is set to false, 
the python3 http.client will use the default 
operating system SSL/TLS client certificates for the SSL/TLS connection. 
If ssl_check_hostname is set to true, the 
operating system default root CA certificates will be used.
In this case custom certificate files are not required and the 
configuration filename parameters will be ignored. 

Custom TLS certificates should only be needed for two use cases.
One case is where the remote API requires a TLS client 
certificate that is signed by a custom CA (Certificate Authority). 
The second case is where this program will perform hostname 
verification for a remote API where the TLS server certificate 
is signed by a custom CA. 

The original implementation of this program used a custom CA 
to sign TLS server and TLS client certificates. 
TLS client certificates were used to authenticate the identity of different Raspberry Pi
devices as they connect to each other on the local network. 
This GitHub repository [cert-numeric-ip](https://github.com/cotarr/cert-numeric-ip)
can be used to generate custom CA, server, and client 
certificates for use with numeric IP addresses.

TLS Parameters:

|  ssl  | check | custom | Description                                                                |
| ----- | ----- | ------ | :------------------------------------------------------------------------- |
| False |       |        | Use un-encrypted (http) request                                            |
| True  | False | False  | Use TLS (https) system default certificates, without hostname verification |
| True  | True  | False  | Use TLS (https) system default certificates, verify hostname               |
| True  | False | True   | Use Custom TLS (https) certificates, without hostname verification         |
| True  | True  | True   | Use Custom TLS (https) certificates, verify hostname

### Testing

The LED display, network request and internal temperature sensor
may be tested separately. This is optional and you may skip to
starting the program below.

#### 1 - Test LED Display

To debug the LED display, run the "led_2_digit.py" module by itself.
The LED display will cycle through all possible numbers.

```
python3 led_2_digit.py
```

#### 2 - Test On Board Temperature Sensor

To debug the local sensor on the Sense Hat board,
run the "local_get_data.py" module by itself. 
This will read the Sense Hat temperature sensor and print
the response as a python dictionary.

```
python3 local_get_data.py
```

Expected response:

```json
{
    "timestamp": 1675117930,
    "data": 24.946403884887694,
    "error": 0,
    "errorMessage": ""
}
```

#### 3 - Test Network API Fetch Request

To debug the HTTP client to perform a GET request to the 
configuration address and path, run the "api_get_data.py" module by itself.
The module will perform the network fetch request, it will decode the 
returned JSON object. This will print the data as a python dictionary.

```
python3 api_get_data.py
```

Expected Response:

```json
{
    "timestamp": 1675118078,
    "data": 24.172,
    "error": 0,
    "errorMessage": ""
}
```

## Run the program

To run the program, change directory to the base directory of the repository.
Start the program by typing:

```
python3 main.py
```

While running, error messages will be printed to the console terminal.

Note: If this program is running with the original Sense Hat Version 1, 
the older board will not have the light/color sensor that was introduced 
in Sense Hat Version 2. Therefore, you can ignore any error message that states 
"... colour sensor. (sensor not present) ..."

The program contains an activity indicator LED. If the display is 
configured to display units of "F" or "C", the lower right LED 
will flash green once each 5 seconds to show the program is still running.
If the units are set to "B" the activity icon is not used because 
activity can be inferred from the alternating C and F displays.

The lower left LED will illuminate green during the network fetch request.
If the network fetch request generates an error, the lower left LED will 
illuminate red. If a time period of more than 3 minutes passes without 
retrieving valid temperature data from the network, the numeric display 
will show "EE" in color red. If the data JSON retrieved from upstream 
devices has an "error" property with value > 0, the display will also 
display the red error LED and "EE" in red. 

## Example Data Source

This GitHub repository [ds18b20-api](https://github.com/cotarr/ds18b20-api) 
can be viewed as an example program to read a DS18B20 temperature 
and make the data available in the proper format.

---

# Dual Sensor Version

The git repository contains a second alternate version of the program 
in file `main-dual-sensor.py`.

This is intended for the case of outdoor weather monitoring where 
one sensor is in morning sun and the other sensor is in afternoon sun.
The sensor with the lower value (in the shade) will be selected and displayed
on the LED display.

The GitHub repository [ds18b20-api](https://github.com/cotarr/ds18b20-api) 
is capable to read two sensor inputs and return both results in a single API response.
If more than 2 are configured, the first two at index [0] and [1] are used.

To run the alternate version:

```
python3 main-dual-sensor.py
```

The startup file `main-dual-sensor.py` is capable to read either single sensor data 
where the HTTP fetch of a JSON object is parsed as a python dictionary or alternately 
dual sensor data where the HTTP fetch of a JSON encoded array of objects is parsed 
as a python list of python dictionaries. The selection is automatic based 
python type checking for `type() == list` or `type() == dict`.

Single sensor data format
```json
{
    "timestamp": 1674937453,
    "data": -4.437,
    "error": 0,
    "errorMessage": ""
}
```


Dual sensor data format

```json
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
```
where

```
timestamp - Integer (Unix time in seconds)
data - Float (Temperature in degrees C)
error - Integer (error code, 0 = no error)
errorMessage - String, empty string if no error.
```

The original `main.py` version is also available
for use with single sensors.
