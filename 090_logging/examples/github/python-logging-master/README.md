# Python Logging Example

## Background

The logging module is a core module within Python, and is a great alternative to
print statements within your programs. This allows you to preserve your
debugging statements within your code, and enable it on demand. By default there
are four logging levels, DEBUG, INFO, WARNING and CRITICAL. Each of your logging
statements can log at any of these levels, and then you can decide globally what
level you want to log at.

Logging also applies to any modules or libraries you develop, and other developers can use this logging within their program how they see fit.

## Basic Example

The basic-example.py sets up logging using the basicConfig method, configures a
logging format, and logs everything from the root logger at level DEBUG to the
console.

This example also imports sample_module, which demonstrates how to setup logging
within your modules. We call the log_message method twice, once with DEBUG
enabled, and once with the log level for sample_module set to INFO. This
demonstrates how to silence or change the logging level on individual modules.

Other core and third-party modules that support logging, such as requests or
database drivers, will also log at the logging level specified automatically.

### Output
```
$ ./basic-example.py
2017-07-18 13:26:55,987 - root - DEBUG - Debug Message
2017-07-18 13:26:55,987 - root - INFO - Info Message
2017-07-18 13:26:55,987 - root - WARNING - Warning Message
2017-07-18 13:26:55,987 - sample_module - DEBUG - Asked to log message: Module Logging Test
2017-07-18 13:26:55,987 - sample_module - INFO - Logging Message in Module: Module Logging Test
2017-07-18 13:26:55,987 - sample_module - INFO - Logging Message in Module: Module Logging Test without debug
2017-07-18 13:26:55,987 - root - INFO - Testing divide by 0 exception
2017-07-18 13:26:55,987 - root - ERROR - division by zero
```

## Full Example

full-example.py demonstrates how to setup more sophisticated logging for programs. Here we initialize logging by attaching log handlers to the root logger instead of using the basicConfig method. This is useful if you want to log to more than one location, such as to the console and to a file. You could also add a third log handler for a syslog server or other log destination.

For each log handler, we can individually set the log level we want to log at, as well as the log format. You may only want to log at level WARNING on your console, but capture all INFO messages within your log file. Setting up individual log handlers will give you this flexibility. If you are sending to syslog, you may want to strip the datestamps from the log messages since they may be duplicated.

With this example, you should be able to see how you can combine different handlers and achieve the flexibility you need in production.

### Notes

* The requests module is required for this example to demonstrate third-party module logging

### Usage Options
```
$ ./full-example.py -h
usage: full-example.py [-h] [-level {debug,info,warning,critical}]
                       [-tracebacks] [-warn_urllib3] [-v]

Logging Example Program

optional arguments:
  -h, --help            show this help message and exit
  -level {debug,info,warning,critical}
                        Set logging level
  -tracebacks           Enable Tracebacks on Errors in Logs
  -warn_urllib3         Set urllib3 to log at WARNING
  -v                    Verbose Output
```

### Test with default level of WARNING
```
$ ./full-example.py
2017-07-18 14:20:14,741 full-example:WARNING: Warning Message
2017-07-18 14:20:14,741 full-example:CRITICAL: Critical Message
2017-07-18 14:20:14,937 full-example:ERROR: division by zero
```

#### Logfile contents (always logs at INFO or below)
```
$ tail example.log
2017-07-18 14:20:27,807 full-example:INFO: Info Message
2017-07-18 14:20:27,807 full-example:WARNING: Warning Message
2017-07-18 14:20:27,807 full-example:CRITICAL: Critical Message
2017-07-18 14:20:27,807 sample_module:INFO: Logging Message in Module: Testing
2017-07-18 14:20:27,998 full-example:INFO: Successfully retrieved URL: https://www.google.com
2017-07-18 14:20:27,998 full-example:ERROR: division by zero
```

### Test with verbose enabled (level INFO)
```
$ ./full-example.py -v
2017-07-18 14:20:50,589 full-example:INFO: Info Message
2017-07-18 14:20:50,589 full-example:WARNING: Warning Message
2017-07-18 14:20:50,589 full-example:CRITICAL: Critical Message
2017-07-18 14:20:50,589 sample_module:INFO: Logging Message in Module: Testing
2017-07-18 14:20:50,780 full-example:INFO: Successfully retrieved URL: https://www.google.com
2017-07-18 14:20:50,781 full-example:ERROR: division by zero
```

### Test with DEBUG level enabled
```
$ ./full-example.py -level debug
2017-07-18 14:21:43,599 full-example:DEBUG: Debug Message
2017-07-18 14:21:43,599 full-example:INFO: Info Message
2017-07-18 14:21:43,599 full-example:WARNING: Warning Message
2017-07-18 14:21:43,599 full-example:CRITICAL: Critical Message
2017-07-18 14:21:43,599 sample_module:DEBUG: Asked to log message: Testing
2017-07-18 14:21:43,600 sample_module:INFO: Logging Message in Module: Testing
2017-07-18 14:21:43,600 full-example:DEBUG: Requesting URL: https://www.google.com
2017-07-18 14:21:43,608 urllib3.connectionpool:DEBUG: Starting new HTTPS connection (1): www.google.com
2017-07-18 14:21:43,800 urllib3.connectionpool:DEBUG: https://www.google.com:443 "GET / HTTP/1.1" 200 None
2017-07-18 14:21:43,803 full-example:INFO: Successfully retrieved URL: https://www.google.com
2017-07-18 14:21:43,803 full-example:DEBUG: First 50 chars returned from URL: <!doctype html><html itemscope="" itemtype="http:/
2017-07-18 14:21:43,803 full-example:DEBUG: Testing Divide by 0 exception
2017-07-18 14:21:43,803 full-example:ERROR: division by zero
```

### Test with DEBUG level enabled, but urllib3 set to WARNING

* Note: This will disable all debug messages from urllib3
```
$ ./full-example.py -level debug -warn
2017-07-18 14:22:14,476 full-example:DEBUG: Debug Message
2017-07-18 14:22:14,477 full-example:INFO: Info Message
2017-07-18 14:22:14,477 full-example:WARNING: Warning Message
2017-07-18 14:22:14,477 full-example:CRITICAL: Critical Message
2017-07-18 14:22:14,477 sample_module:DEBUG: Asked to log message: Testing
2017-07-18 14:22:14,477 sample_module:INFO: Logging Message in Module: Testing
2017-07-18 14:22:14,477 full-example:DEBUG: Requesting URL: https://www.google.com
2017-07-18 14:22:14,675 full-example:INFO: Successfully retrieved URL: https://www.google.com
2017-07-18 14:22:14,675 full-example:DEBUG: First 50 chars returned from URL: <!doctype html><html itemscope="" itemtype="http:/
2017-07-18 14:22:14,675 full-example:DEBUG: Testing Divide by 0 exception
2017-07-18 14:22:14,675 full-example:ERROR: division by zero
```
