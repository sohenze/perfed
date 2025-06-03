# Perfed

Perfed is a simplified approach to performance timing in Python.

## Usage
```Python
import time
from perfed.timers import Timers

timers = Timers()

timers.start("first")
time.sleep(0.2)
timers.stop("first")

timers.start("second")
time.sleep(0.3)
timers.stop("second")

with timers.start("third"):
    time.sleep(0.4)

timers.show()
```
