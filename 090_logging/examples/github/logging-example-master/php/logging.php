<?php

# do `composer require monolog/monolog` to install

use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Formatter\JsonFormatter;

# reset error handling for this script
error_reporting(-1);
ini_set('display_errors', 1);

require_once('vendor/autoload.php');


function el_format_record(array $record) {
    return array(
        "timestamp" => date_timestamp_get($record['datetime']),
        "log_level" => $record['level_name'],
        "process" => $record['channel'],
        "section" => __FILE__, # pretty sure this won't work as I expect it to
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

$log = new Logger('example-app');
$formatter = new eLifeJsonFormatter();
$stream = new StreamHandler('/tmp/monolog-test.log', Logger::DEBUG);
$stream->setFormatter($formatter);
$log->pushHandler($stream);

//
//
//

$log->addWarning('this is a warning');
$log->addError('this is an error');
