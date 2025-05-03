import os
import sys
from pathlib import Path
from sensor.logger import logging

# Add the project root directory to Python path
sys.path.append(str(Path(__file__).parent))

from sensor.exception import SensorException

def test_sensor_exception():
    try:
        logging.info("Starting the test_sensor_exception function")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__ == "__main__":
    try:
        test_sensor_exception()
    except Exception as e:
        print(e)
