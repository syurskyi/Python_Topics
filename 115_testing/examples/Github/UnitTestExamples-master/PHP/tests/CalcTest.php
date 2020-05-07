<?php
namespace Sample;

use PHPUnit\Framework\TestCase;

class CalcTest extends TestCase
{
    public $calc;

    function __construct($name = null, array $data = [], $dataName = '')
    {
        parent::__construct($name, $data, $dataName);
        $this->calc = new Calc();
    }

    public function testAdd()
    {
        $this->assertEquals(15, $this->calc->add(10, 5));
        $this->assertEquals(5, $this->calc->add(8, -3));
    }

    public function testPow()
    {
        $this->assertEquals(125, $this->calc->pow(5, 3));
        $this->assertEquals(0x7FFFFFFF, $this->calc->pow(2, 31) - 1);
    }
}