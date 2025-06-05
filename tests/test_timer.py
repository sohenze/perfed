import random
import time

import pytest

from perfed.timer import Timer
from tests.util import tolerant_approx


class TestTimer:
    def test_init(self):
        timer = Timer("test_timer")

        assert timer._name == "test_timer"
        assert timer._start == -1
        assert timer._stop == -1

    def test_start(self):
        timer = Timer("test_timer")

        timer.start()
        assert timer._start > 0

        curr_start = timer._start
        timer.start()
        assert curr_start == timer._start

    def test_stop(self):
        timer = Timer("test_timer")
        timer.start()

        timer.stop()
        assert timer._stop > 0

        curr_stop = timer._stop
        timer.stop()
        assert curr_stop == timer._stop

    def test_stop_not_started(self):
        timer = Timer("test_timer")
        with pytest.raises(RuntimeError):
            timer.stop()

    def test_get(self):
        timer_a = Timer("test_timer_a")
        timer_b = Timer("test_timer_b")
        timer_c = Timer("test_timer_c")
        sleep_dur_a = random.uniform(0.1, 0.3)
        sleep_dur_b = random.uniform(0.1, 0.3)
        sleep_dur_c = random.uniform(0.1, 0.3)

        # Test get with start/stop
        timer_a.start()
        time.sleep(sleep_dur_a)
        timer_a.stop()
        assert timer_a.get() == tolerant_approx(sleep_dur_a)

        # Test get without stops
        timer_b.start()
        time.sleep(sleep_dur_b)
        assert timer_b.get() == tolerant_approx(sleep_dur_b)
        time.sleep(0.1)
        assert timer_b.get() == tolerant_approx(sleep_dur_b + 0.1)

        # Test get with context manager
        with timer_c:
            time.sleep(sleep_dur_c)
        assert timer_c.get() == tolerant_approx(sleep_dur_c)

    def test_get_without_start(self):
        timer = Timer("test_timer")
        with pytest.raises(RuntimeError):
            timer.get()
