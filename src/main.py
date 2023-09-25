import json
import sys

from gui import UI
from shutdown import GracefulShutdown
from traffic_light import TrafficLight


if __name__ == '__main__':
    duration = json.loads(sys.argv[1])
    killer = GracefulShutdown()
    traffic_light = TrafficLight(duration, UI(), killer)
    traffic_light.run()
    print('Exiting Traffic Light Simulator')
