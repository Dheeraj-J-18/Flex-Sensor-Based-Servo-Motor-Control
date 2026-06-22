# Flex Sensor Based Servo Motor Control System

## Overview

This project uses a Flex Sensor to control the position of a Servo Motor in real time. The bending angle of the flex sensor is measured using an Arduino Uno and displayed on a 16x2 LCD. The servo motor rotates according to the amount of bending detected by the sensor.

## Features

- Real-time flex sensor monitoring
- Servo motor angle control (0°–180°)
- LCD display for sensor readings and angle values
- Simple and low-cost implementation
- Suitable for robotics and gesture-controlled applications

## Components Used

- Arduino Uno
- Flex Sensor
- Servo Motor (SG90)
- 16x2 LCD with I2C Module
- 10kΩ Resistor
- Breadboard
- Jumper Wires

## Working Principle

1. The flex sensor changes resistance when bent.
2. Arduino reads the analog voltage through a voltage divider circuit.
3. The sensor value is mapped to a servo angle.
4. The servo rotates according to the bend.
5. Sensor value and servo angle are displayed on the LCD.

## Circuit Connections

### Flex Sensor
- One end → 5V
- Other end → A0
- 10kΩ resistor between A0 and GND

### Servo Motor
- Signal → D9
- VCC → 5V
- GND → GND

### I2C LCD
- SDA → A4
- SCL → A5
- VCC → 5V
- GND → GND

## Applications

- Gesture-controlled systems
- Robotic hand control
- Prosthetic devices
- Human-machine interaction
- Rehabilitation systems

## Future Improvements

- Wireless monitoring using ESP32
- Multiple flex sensor integration
- Robotic arm control
- IoT-based data logging

## Author

Dheeraj J

Electronics and Communication Engineering

M. S. Ramaiah Institute of Technology
