from abc import ABC, abstractmethod
import time
from typing import Dict

possible_lights = ['red', 'orange', 'green']


class BaseTrafficLight(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError("run() method must be implemented")


class TrafficLight(BaseTrafficLight):
    def __init__(self, duration: Dict[str, float], ui, killer):
        for k in duration.keys():
            if k not in possible_lights:
                raise ValueError(f"{k} is not valid signal. Possible signals: {possible_lights}")

        self.killer = killer
        self.duration = duration
        self.ui = ui
        self._len = len(duration.keys())

    def run(self):
        while not self.killer.shutdown_now:
            if self._len == 0:
                self.ui.plot_blank()
                time.sleep(60)

            for signal, dur in self.duration.items():
                if signal == 'red':
                    self.ui.plot_red_signal()
                    time.sleep(dur)
                    print("\n" * 1000)
                if signal == 'orange':
                    self.ui.plot_orange_signal()
                    time.sleep(dur)
                    print("\n" * 1000)
                if signal == 'green':
                    self.ui.plot_green_signal()
                    time.sleep(dur)
                    print("\n" * 1000)
