import pyvisa
import csv
import time
from datetime import datetime

rm = pyvisa.ResourceManager()

# Connect instruments
psu = rm.open_resource("USB::0x05E6::2230::INSTR")
eload = rm.open_resource("USB::0x05E6::2380::INSTR")
scope = rm.open_resource("USB::0x0957::DSOX6004A::INSTR")
dmm = rm.open_resource("USB::0x05E6::6500::INSTR")

def initialize_instruments():

    print("Initializing instruments...")

    psu.write("VOLT 5")
    psu.write("CURR 5")
    psu.write("OUTP ON")

    eload.write("MODE CC")

    scope.write(":TIM:SCAL 1e-3")

def load_transient_test(rail_name, max_current):

    results = []

    for i in range(10):

        print(f"Running test {i+1}")

        eload.write(f"CURR {0.1 * max_current}")
        time.sleep(0.5)

        eload.write(f"CURR {0.9 * max_current}")
        time.sleep(0.5)

        voltage = dmm.query("MEAS:VOLT?")

        timestamp = datetime.now()

        results.append([rail_name, voltage, timestamp])

    return results


def save_results(data):

    with open("results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Rail", "Voltage", "Timestamp"])

        for row in data:
            writer.writerow(row)


initialize_instruments()

data = load_transient_test("3V3", 3)

save_results(data)

print("Test completed. Results saved.")
