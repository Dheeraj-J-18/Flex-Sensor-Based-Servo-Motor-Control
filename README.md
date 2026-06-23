# Flex Sensor Based Servo Motor Control System using Raspberry Pi Pico

## Overview

This project demonstrates real-time servo motor control using a flex sensor and Raspberry Pi Pico. The resistance of the flex sensor changes when bent, and the Pico reads the corresponding analog value through its ADC pin. The sensor value is then mapped to a servo angle, allowing the servo motor to move according to the amount of bending.

An I2C LCD is used to display the flex sensor readings and servo angle in real time.

## Features

- Real-time flex sensor monitoring
- Servo motor control from 0° to 180°
- Live display of sensor values on I2C LCD
- Implemented using MicroPython
- Low-cost embedded system design

## Hardware Components

- Raspberry Pi Pico
- Flex Sensor
- SG90 Servo Motor
- 16x2 LCD with I2C Module
- 10kΩ Resistor
- Breadboard
- Jumper Wires

## Software Used

- Thonny IDE
- MicroPython
- Raspberry Pi Pico SDK Libraries

## Working Principle

1. The flex sensor acts as a variable resistor.
2. Raspberry Pi Pico reads the sensor voltage using its ADC.
3. Sensor readings are mapped to a corresponding servo angle.
4. The servo motor rotates according to the bend of the sensor.
5. LCD displays sensor values and motor position.

## Circuit Diagram

![Circuit Diagram](Circuit_Diagram/circuit.png)

## Project Images

### Hardware Setup

![Setup](Images/setup.jpg)

### Working Demonstration

![Working](Images/working1.jpg)

## Applications

- Gesture-controlled systems
- Robotic hand control
- Prosthetic devices
- Human-machine interaction
- Rehabilitation systems
- Embedded Systems Education

## Future Improvements

- Wireless monitoring using Wi-Fi
- Multi-flex sensor glove
- Robotic arm implementation
- IoT integration for remote monitoring

## Repository Structure

Flex-Sensor-Servo-Control-System/
├── main.py
├── Images/
├── Circuit_Diagram/
├── Documentation/
└── README.md

## Author

Dheeraj J

B.E. Electronics and Communication Engineering

M. S. Ramaiah Institute of Technology
