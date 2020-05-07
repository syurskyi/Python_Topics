package sample_test

import (
"testing"
c "."
)

var calc = c.Calc{}

func TestCalc_Add(t *testing.T) {
	if calc.Add(10, 5) != 15 {
		t.Error("Add Failed");
	}
	if calc.Add(8, -3) != 5 {
		t.Error("Add Failed");
	}
}

func TestCalc_Pow(t *testing.T) {
	if calc.Pow(5, 3) != 125 {
		t.Error("Pow Failed");
	}
	if calc.Pow(2, 31) - 1 != 0x7FFFFFFF {
		t.Error("Pow Failed");
	}
}
