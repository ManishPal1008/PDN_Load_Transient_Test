import pyvisa
import csv
import time
from datetime import datetime

# Initialize VISA resource manager
rm = pyvisa.ResourceManager()

# Connect to instruments (example VISA addresses)
psu = rm.open_resource("USB::0x05E6::2230::INSTR")
eload = rm.open_resource("USB::0x05E6::2380::INSTR")
dmm = rm.open_resource("USB::0x05E6::6500::INSTR")

def initialize_instruments():

    print("Initializing instruments")

    # Configure PSU
    psu.write("VOLT 5")
    psu.write("CURR 5")
    psu.write("OUTP ON")

    # Configure Electronic Load
    eload.write("MODE CC")

def run_transient_test(rail_name, max_current):

    results = []

    print("Starting transient test")

    for i in range(10):

        print(f"Test Cycle {i+1}")

        # Low load
        eload.write(f"CURR {0.1 * max_current}")
        time.sleep(0.5)

        # High load
        eload.write(f"CURR {0.9 * max_current}")
        time.sleep(0.5)

        voltage = dmm.query("MEAS:VOLT?")

        timestamp = datetime.now()

        results.append([rail_name, voltage.strip(), timestamp])

    return results


def save_results(data):

    filename = "results.csv"

    with open(filename, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["Rail", "Voltage", "Timestamp"])

        for row in data:
            writer.writerow(row)

    print("Results saved to results.csv")


def main():

    initialize_instruments()

    data = run_transient_test("3V3", 3)

    save_results(data)


if __name__ == "__main__":
    main()
