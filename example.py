import sys

from SOC import soc

battery_remaining = soc(float(sys.argv[1]))

if battery_remaining is not None:
    battery_remaining = round(battery_remaining, 2)
    print(f"{battery_remaining}%")
