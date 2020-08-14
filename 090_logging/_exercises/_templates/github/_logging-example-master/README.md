# Logging

The preferred log format for eLife applications.

`<timestamp> - <log level> - <process name> - <program section> - <message>`

__Why be so formal about this?__ These log files are eventually parsed by other 
programs and the extracted bits are used in calculations, stored, displayed, etc.

Many applications with many different logging formats means more work for me. 
[__KISS__](http://en.wikipedia.org/wiki/KISS_principle)

Examples:

* `1420811950.9472651 - DEBUG - elife-api - somemodule.py - a message goes here`
* `1420811950.9472651 - INFO - elife-bot - somemodule.py - a message goes here`
* `1420811950.9472651 - WARN - SimpleScraper.js - func_name - a message goes here`
* `1420811950.9472651 - ERROR - foo - somemodule.py - a message goes here`
* `1420811950.9472651 - CRITICAL - bar - somemodule.py - a message goes here`
* `1420811950 - INFO - baz - somemodule.py - a message goes here`

__timestamp__: the time in seconds since the epoch as a floating point or integer 
number.

__log level__: one of DEBUG, INFO, WARN, ERROR or CRITICAL.

__process name__: name of the running program/process.

__program section__: where within the application this log entry originated.

__message__: a free form message; may include hyphens; avoid line breaks.

## Structure

If your application and preferred logging library can handle it easily, please 
use JSON with the following keys:

```
{"timestamp": ..., "log_level": ..., "process": ..., "section": ..., "message": ..., "context": {...}}
```

With `__context__` being a simple map of additional key+values. An empty context can be either an empty list or an empty map (because of the nature of PHP's keyed arrays).

Examples:

```json
{"timestamp":1439482969,"log_level":"ERROR","process":"example-app","section":"\/srv\/ingestor\/web\/logging.php","message":"this is an error"}

{"timestamp":1439482969,"log_level":"ERROR","process":"example-app","section":"\/srv\/ingestor\/web\/logging.php","message":"this is an error", "context": []}

{"timestamp":1439482969,"log_level":"ERROR","process":"example-app","section":"\/srv\/ingestor\/web\/logging.php","message":"this is an error", "context": {}}

{"timestamp":1439482969,"log_level":"ERROR","process":"example-app","section":"\/srv\/ingestor\/web\/logging.php","message":"this is an error", "context": {"key": "val"}}
```

## Python

Use this formatter:

`%(created)f - %(levelname)s - %(processName)s - %(name)s - %(message)s`

The included example can be run with: 

`cd python && ./main.py`

Python docs for the `logging` module are here: 
https://docs.python.org/2/library/logging.html#logrecord-attributes

## PHP+Monolog

The below custom formatter coerces some of the naming of the original record to
familiar values and converts the date to a Unix timestamp (sans microseconds):

```php
function el_format_record(array $record) {
    return array(
        "timestamp" => date_timestamp_get($record['datetime']),
        "log_level" => $record['level_name'],
        "process" => $record['channel'],
        "section" => __FILE__,
        "message" => $record['message'],
        "context" => $record['context'],
    );
}

class eLifeJsonFormatter extends Monolog\Formatter\JsonFormatter {
    public function format(array $record) {
        return parent::format(el_format_record($record));
    }

    public function formatBatch(array $records) {
        $records = array_map('el_format_record', $records);
        return parent::formatBatch($records);
    }
}
```

See the [php example](php/logging.php) for usage.

## Javascript

...

## notes

I use Unix time `%(created)f` rather than the `YMD` format because Unix time 
is used natively by [Riemann](http://riemann.io) (our realtime monitor).

# Logging in production

Storage is cheap, logging is easy, so why wouldn't we log everything we possibly 
can and keep it around forever?

* data must be transformed into information, otherwise it's worthless

All other reasons derive from this one. If logging data is not used then it's 
just noise.

## retention

__INFO__ is the default level for all applications in production. 

__DEBUG__ log statements are discarded by monitoring applications and will not 
be stored.

All __application__ log messages sent to the monitoring server will be kept for 
__6 months__. This is _entirely arbitrary_ and handled by the `logrotate` 
application.

All __audit__ log messages sent to the monitoring server will be kept 
__indefinitely__, or, as long as some business rule tells us. This rule will be 
encapsulated entirely within code.

## audit logs

Auditing is a _type_ of logging. 

Auditing within an application exists because there is a business requirement 
to do so. A regular log message might be _'user "joe" logged in'_, but becomes 
part of the audit trail when there is a business requirement to track a user's
activities through a system.

If a formal audit log is required, it _must_ go to it's own log file.

## S3 bucket access

Logging for an S3 bucket should only be enabled if:

1. a person explicitly wants it monitored
2. the bucket is acting as a server and is the only point of access to that data  

All S3 access logs should go to the logging bucket `elife-log-data` with the 
name of the originating bucket as the prefix.

For example, if the S3 bucket "elife-annual-2012" require access logging, the
'target bucket' will be `elife-log-data` and the 'target prefix' will be 
`elife-annual-2012/`.

![S3 logging example](s3-logging-example.png)



