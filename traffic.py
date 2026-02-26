
import time
from itertools import cycle

def traffic_light_simulator():
    """Simulates a standard traffic light cycle: Red -> Green -> Yellow."""

    states = cycle([
        ("RED", 5),
        ("GREEN", 5),
        ("YELLOW", 2)
    ])
    
    try:
        for color, duration in states:
            print(f"Traffic Light is: {color}")
            time.sleep(duration)
    except KeyboardInterrupt:
        print("\nSimulator stopped.")

if __name__ == "__main__":
    traffic_light_simulator()

