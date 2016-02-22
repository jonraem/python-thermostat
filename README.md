# python-thermostat
Thermostat application for Raspberry Pi. Written in Python.

About
-
This was a school project for a university embedded electronics course. The purpose was to build a system to simulate a thermostat with Raspberry Pi and a temperature sensor (TCN75A). Communication between Raspberry Pi and the sensor happens via I2C bus. The code that controls the sensor is written in Python.

The system keeps the room temperature between 24-25 degrees Celsius. Two LED lights are connected to Raspberry Pi: a green LED for when the temperature is in the "green zone" (i.e. between 24 and 25 degrees) and a red LED for when it isn't. The current temperature is also printed to the console every second. The temperature accuracy is set on hardware level.

Unfortunately no pictures exist of this project. However, attached you will find the original assignment in Finnish.
