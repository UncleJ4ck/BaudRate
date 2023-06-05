# BaudRate

## Overview

a compact python script to determine the baud rate of serial connections. I've been interested in IOT pentesting lately and i found out there's this script that can identify baud rate ![Baudrate.py](https://github.com/biw/Baudrate.py), but it's old and it's not working i decided to create my own version.

## What's a baud rate ? 

Baud rate is a measure of the speed of data transmission in a communication system. It refers to the number of signal units per second that are required to represent the data being transmitted.

In serial communication, baud rate is very crucial. It's like the language of communication for devices. Both the sender and the receiver must agree on a specific baud rate for successful data exchange.

## Serial Connections?

Serial connections are a method of data transfer where data is sent over a communication channel sequentially, one bit at a time. This contrasts with parallel connections where multiple bits are sent simultaneously over multiple channels. Serial communication is used extensively in computing and telecommunication systems due to its simplicity and reliability, especially over long distances. Examples of serial connections include USB, RS-232, and RS-485 among others.

## Installation & Usage

```
git clone https://github.com/UncleJ4ck/BaudRate
cd BaudRate
sudo python3 baudrate.py
```
- Ensure that your device is connected to your laptop and switched on before running the script.