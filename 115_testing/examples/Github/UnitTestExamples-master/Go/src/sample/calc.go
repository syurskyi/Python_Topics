package sample

import (
	"math"
)

type Calc struct {}

func (calc *Calc) Add(x, y int) int {
	return x + y
}

func (calc *Calc) Pow(x, y float64) float64 {
	return math.Pow(x, y)
}