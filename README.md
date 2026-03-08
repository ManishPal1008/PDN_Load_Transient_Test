# PDN Load Transient Test Automation

This repository contains a Python-based automation framework for testing the load transient response of a Power Distribution Network (PDN).

The script uses PyVISA to control laboratory instruments using SCPI commands.

## Instruments Used

Keithley 2230-30-1 Programmable Power Supply  
Keithley 2380 Series Electronic Load  
Keysight DSOX6004A Oscilloscope  
Keithley DMM6500 Multimeter  

## Test Procedure

1. Initialize instruments using PyVISA
2. Set PSU to 5V
3. Apply step load using electronic load
4. Measure output voltage using DMM
5. Log results with timestamps

## Load Step Example

0.3A → 2.7A

## Running the Script

Install dependencies:

pip install -r requirements.txt

Run:

python load_transient_test.py

## Output

Results are stored in results.csv
