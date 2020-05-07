import Calc from '../src/Calc';

const assert = require('assert');

describe('Calc', () => {
	const calc = new Calc();

	describe('add()', () => {
		assert.equal(15, calc.add(10, 5));
		assert.equal(5, calc.add(8, -3));
	});

	describe('pow', () => {
		assert.equal(125, calc.pow(5, 3));
		assert.equal(0x7FFFFFFF, calc.pow(2, 31) - 1);
	});
});