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

print("~~~~~~~~~~TIMERS~~~~~~~~~~")
tm.show(unit="sec")

print("~~~~~~~~~~DATAFRAME~~~~~~~~~~")
display(tm.to_dataframe("ns"))

"""
Output:

~~~~~~~~~~TIMERS~~~~~~~~~~
Timer      Elasped Time
-------  --------------
first          0.2008
second         0.300584
third          0.400186
~~~~~~~~~~DATAFRAME~~~~~~~~~~
    Timer	Elasped Time
0	first	200800500.0
1	second	300583900.0
2	third	400186100.0

"""
```

```Python
import time
from perfed.timer_decorator import TimerDecorator

@TimerDecorator.decorate("foo_tm")
def foo(x: int):
    print(x)
    time.sleep(0.2)

@TimerDecorator.decorate("bar_tm")
def bar(x: str):
    print(x)
    time.sleep(0.3)

foo(49)
foo(200)
foo(455)

bar("cat")
bar("dog")

print("~~~~~~~~~~FOO TIMERS~~~~~~~~~~")
TimerDecorator.get_manager("foo_tm").show()
print("~~~~~~~~~~FOO STATS~~~~~~~~~~")
TimerDecorator.get_manager("foo_tm").show_stats()

print("~~~~~~~~~~BAR TIMERS~~~~~~~~~~")
TimerDecorator.get_manager("bar_tm").show()
print("~~~~~~~~~~BAR STATS~~~~~~~~~~")
TimerDecorator.get_manager("bar_tm").show_stats()

"""
Output:

49
200
455
cat
dog
~~~~~~~~~~FOO TIMERS~~~~~~~~~~
Timer        Elasped Time
---------  --------------
foo_tm(1)        0.200905
foo_tm(2)        0.200426
foo_tm(3)        0.200805
~~~~~~~~~~FOO STATS~~~~~~~~~~
Stat        Value
-------  --------
Average  0.200712
Max      0.200905
Min      0.200426
~~~~~~~~~~BAR TIMERS~~~~~~~~~~
Timer        Elasped Time
---------  --------------
bar_tm(1)         0.30011
bar_tm(2)         0.30071
~~~~~~~~~~BAR STATS~~~~~~~~~~
Stat       Value
-------  -------
Average  0.30041
Max      0.30071
Min      0.30011
"""
```

## Credit
Perfed is inspired by [perfcounters](https://github.com/ebursztein/perfcounters). I decided to create this project as I have some original ideas and would like to try my hand at publishing my own Python package. 
