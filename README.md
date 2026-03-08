# PDN Load Transient Test Automation

This repository contains a Python-based automation framework used for testing the load transient response of a Power Distribution Network (PDN).

The test system uses SCPI commands through PyVISA to control laboratory instruments.

## Instruments Used

Keithley 2230-30-1 Programmable Power Supply  
Keithley 2380 Series Electronic Load  
Keysight DSOX6004A Oscilloscope  
Keithley DMM6500 Multimeter  

## Test Workflow

1. Initialize all instruments
2. Set power supply to 5V
3. Apply step load using electronic load
4. Capture voltage measurement using DMM
5. Log results to CSV file

## Example Load Step

0.3A → 2.7A

## Running the Script

Install dependencies:

pip install -r requirements.txt

Run the script:

python load_transient_test.py

## Output

Results are saved in results.csv.
