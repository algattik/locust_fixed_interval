# locust_fixed_interval

## About

A Locust TaskSet that sends requests at a constant rate (with a fixed time
interval). Based on [Locust issue
#646](https://github.com/locustio/locust/issues/646).
 
The instance 'interval' attribute defines the time interval between successive
requests per user in seconds (default 1.0). This value must be greater than
the average HTTP request roundtrip time.  For example, if your request takes
1.9 seconds to get to the server and back, and the execution of your code and
the Locust framework code additionally requires 0.1 second between requests,
you should set 'interval' to a value over 2.0 seconds. If you need a higher
request rate, increase the number of simulated users.

## Installing

```
pip install locust-fixed-interval
```

## Example usage

```python
class MyTaskSet(FixedIntervalTaskSet):

  def setup(self):
      self.interval = 2.5 

  @task
  def task1(self):
    #...

class MyLocust(HttpLocust):
    task_set = MyTaskSet
```
