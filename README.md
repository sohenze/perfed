# Perfed

Perfed is a simplified approach to performance timing in Python.

## Usage
```Python
import time
from perfed.timer_manager import TimerManager

tm = TimerManager()

tm.start("first")
time.sleep(0.2)
tm.stop("first")

tm.start("second")
time.sleep(0.3)
tm.stop("second")

with tm.start("third"):
    time.sleep(0.4)

tm.show(unit="sec")
print("------CSV-----")
tm.to_csv(unit="sec")

"""
Output:

Timer      Elasped Time
-------  --------------
first          0.200358
second         0.300527
third          0.4004
------CSV-----
Timer,Elasped Time
first,0.2003583
second,0.300527
third,0.4004005
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
foo_timer(1)        0.200797
foo_timer(2)        0.200652
foo_timer(3)        0.201026
0.2008254
Timer           Elasped Time
------------  --------------
bar_timer(1)        0.300231
bar_timer(2)        0.300369
0.3003001
"""
```

## Credit
Perfed is inspired by [perfcounters](https://github.com/ebursztein/perfcounters). I decided to create this project as I have some original ideas and would like to try my hand at publishing my own Python package. 
