# Changelog

All notable changes to this project will be documented in this file.

2023-06-19 Added alternate version main-dual-sensor.py.

The startup file `main-dual-sensor.py` is capable to read either single sensor data 
where the HTTP fetch of a JSON object is parsed as a python dictionary or alternately 
dual sensor data where the HTTP fetch of a JSON encoded array of objects is parsed 
as a python list of python dictionaries. The selection is automatic based 
python type checking for `type() == list` or `type() == dict`.

The original main.py file remains unchanged.

2023-01-31 Clean up code, add comments, move to GitHub

2015-11-08 Initial version complete

