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

"""
Output:

Timer      Elasped Time
-------  --------------
first          0.200766
second         0.301181
third          0.400664
------CSV-----
Timer,Elasped Time
first,0.200766
second,0.301181
third,0.4006642
"""
```

```Python
import time
from perfed.timer_decorator import TimerDecorator

@TimerDecorator.decorate("foo_timer")
def foo(x: int):
    print(x)
    time.sleep(0.2)

@TimerDecorator.decorate("bar_timer")
def bar(x: str):
    print(x)
    time.sleep(0.3)

foo(49)
foo(200)
foo(455)

bar("cat")
bar("dog")

TimerDecorator.get_manager("foo_timer").show()
print(TimerDecorator.get_manager("foo_timer").average())
TimerDecorator.get_manager("bar_timer").show()
print(TimerDecorator.get_manager("bar_timer").average())

"""
Output:

49
200
455
cat
dog
Timer           Elasped Time
------------  --------------
foo_timer(1)        0.200183
foo_timer(2)        0.200126
foo_timer(3)        0.200508
0.20027236666666665
Timer           Elasped Time
------------  --------------
bar_timer(1)        0.300116
bar_timer(2)        0.300573
0.3003445
"""
```

## Credit
This is heavily inspired by [perfcounters](https://github.com/ebursztein/perfcounters). I decided to create this repository as I have some original ideas and would like to try my hand at making my own Python package. 
