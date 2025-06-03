import csv
import sys
from typing import Dict, Literal

from tabulate import tabulate

from perfed.timer import Timer


class TimerManager:
    """Manages a collection of timers.
    """
    def __init__(self) -> None:
        self._timers: Dict[str, Timer] = {}
    
    def _create_timer(self, name: str) -> Timer:
        """Create a timer.

        Args:
            name (str): Name of timer

        Raises:
            ValueError: Timer with name already exists.

        Returns:
            Timer: Created timer.
        """
        if name in self._timers:
            raise ValueError(f"Timer with the name: {name} already exists.")

        timer = Timer(name=name)
        self._timers[name] = timer
        return timer
    
    def start(self, name: str) -> Timer:
        """Create and start a timer.

        Args:
            name (str): Name of timer.

        Returns:
            Timer: Started timer.
        """
        timer = self._create_timer(name)
        timer.start()
        return timer

    def stop(self, name: str) -> None:
        """Stop a timer.

        Args:
            name (str): Name of timer.
        
        Raises:
            ValueError: Timer with name does not exist.
        """
        if (timer := self._timers.get(name)) is None:
            raise ValueError(f"Timer with the name {name} does not exist.")

        timer.stop()


    def show(self, unit: Literal["ns", "ms", "sec", "min"] = "sec") -> None:
        """Print timers to stdout.

        Args:
            unit (Literal[&quot;ns&quot;, &quot;ms&quot;, &quot;sec&quot;, &quot;min&quot;], optional):
            Unit of time to be used. Defaults to "sec".
        """
        headers = ["Timer", "Elasped Time"]
        data = [[name, timer.get(unit=unit)] for name, timer in self._timers.items()]
        tabulated = tabulate(data, headers=headers)
        print(tabulated)

    def to_csv(self, unit: Literal["ns", "ms", "sec", "min"] = "sec") -> None:
        """Print timers to stdout in csv format.

        Args:
            unit (Literal[&quot;ns&quot;, &quot;ms&quot;, &quot;sec&quot;, &quot;min&quot;], optional):
            Unit of time to be used. Defaults to "sec".
        """
        headers = ["Timer", "Elasped Time"]
        data = [[name, timer.get(unit=unit)] for name, timer in self._timers.items()]
        data.insert(0, headers)
        
        writer = csv.writer(sys.stdout)
        for row in data:
            writer.writerow(row)
