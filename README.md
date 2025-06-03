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

## Credit
This is heavily inspired by [perfcounters](https://github.com/ebursztein/perfcounters). I decided to create this repository as I have some original ideas and would like to try my hand at making my own Python package. 
