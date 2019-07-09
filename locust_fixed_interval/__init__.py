import time

from locust import TaskSet


class FixedIntervalTaskSet(TaskSet):
    """
    A Locust TaskSet that sends requests at a constant rate.

    The instance 'interval' attribute defines the time interval between successive
    requests per user in seconds (default 1.0). This value must be greater than
    the average HTTP request roundtrip time.  For example, if your request takes
    1.9 seconds to get to the server and back, and the execution of your code and
    the Locust framework code additionally requires 0.1 second between requests,
    you should set 'interval' to a value over 2.0 seconds. If you need a higher
    request rate, increase the number of simulated users.

    Example:

      >>> class MyTaskSet(FixedIntervalTaskSet):
      >>> 
      >>>   def setup(self):
      >>>       self.interval = 2.5 
      >>> 
      >>>   @task
      >>>   def task1(self):
      >>>     ...

      >>> class MyLocust(HttpLocust):
      >>>     task_set = MyTaskSet

    """

    interval = 1.0

    _previous_request_wallclock = -1
    _current_wait_time = 0

    def wait_function(self):
        """
        Override TaskSet.wait_function(). Called after each request is sent, returns
        time to wait in milliseconds.
        """
        current_wallclock = time.monotonic()
        if self._previous_request_wallclock != -1:
            actual_interval = current_wallclock - self._previous_request_wallclock
            self._current_wait_time += self.interval - actual_interval
        self._previous_request_wallclock = current_wallclock
        if self._current_wait_time < 0:
            return 0
        return self._current_wait_time * 1000
