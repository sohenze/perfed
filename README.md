# Perfed

**Perfed** is a lightweight and easy-to-use package for measuring and analyzing execution times in Python code. It is a wrapper around `time.perf_counter_ns()` to provide precise performance timing with an intuitive interface and convenient tools for displaying and analyzing results.




## Features

✅ Measure execution time of code blocks and functions  
✅ Display results as tables in the console  
✅ Output timings as a pandas DataFrame for further analysis  
✅ Compute aggregated statistics (average, min, max) for decorated functions

## Requirements

- Python 3.12 or higher

## Installation

```
pip install perfed
```

## Usage

### Using **TimerManager**
Measure and manage multiple timers concurrently.

```Python
import logging
import time

from IPython.display import display as ipy_display

from perfed.timer_manager import TimerManager


logger = logging.getLogger("tm_logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler("tmp/timers.log"))

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

print("~~~~~~~~~~TUPLES~~~~~~~~~~")
print(tm.to_tuples("min"))

print("~~~~~~~~~~DICTIONARY~~~~~~~~~~")
print(tm.to_dict("ms"))

print("~~~~~~~~~~DATAFRAME~~~~~~~~~~")
ipy_display(tm.to_dataframe("ns"))

tm.save("tmp/timers.csv", "csv")
tm.show(print_fn=logger.debug)
```

Output:
```
~~~~~~~~~~TIMERS~~~~~~~~~~
Timer      Duration
-------  ----------
first      0.200236
second     0.300272
third      0.400313
~~~~~~~~~~TUPLES~~~~~~~~~~
[('first', 0.0033372583333333337), ('second', 0.005004535), ('third', 0.0066718866666666665)]
~~~~~~~~~~DICTIONARY~~~~~~~~~~
{'first': 200235.5, 'second': 300272.1, 'third': 400313.2}
~~~~~~~~~~DATAFRAME~~~~~~~~~~
	Timer	 Duration
0	first	 200235500.0
1	second 300272100.0
2	third	 400313200.0
~~~~~~~~~~tmp/timers.csv~~~~~~~~~~
first,0.2002355
second,0.3002721
third,0.4003132
~~~~~~~~~~tmp/timers.log~~~~~~~~~~
Timer      Duration
-------  ----------
first      0.200236
second     0.300272
third      0.400313
```

### Using **TimerDecorator**
Automatically measure execution time of decorated functions and view aggregate statistics.

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
```

Output:
```
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
```

## How It Works
This package consists of 3 main components:
- **Timer**

  Represents a single timer that can be started and stopped. It also supports context manager usage (`with Timer() as t:`) and can report the elapsed duration in various time units (nanoseconds, milliseconds, seconds, or minutes).

- **TimerManager**

  Manages a collection of named `Timer` instances. It lets you:
    - Start and stop timers by name.
    - Use timers as context managers.
    - View all timers and their durations in different formats (tuples, dictionary, pandas DataFrame).
    - Save the results to a CSV or JSON file.
    - Display the timers in a tabular format in the console.
    - Show basic statistics (average, max, min) across all timers.

- **TimerDecorator**

  Enables easy timing of function executions through a decorator. Decorated functions are each assigned a dedicated `TimerManager`, which starts and stops a `Timer` instance for each function call. Assigned `TimerManager` instances are tracked within a class variable in `TimerDecorater` and can be individually accessed for further analysis.

## Why Perfed?
Perfed is inspired by [perfcounters](https://github.com/ebursztein/perfcounters). I created this project to add some original ideas and to share a simple, flexible performance timing tool with the community.
