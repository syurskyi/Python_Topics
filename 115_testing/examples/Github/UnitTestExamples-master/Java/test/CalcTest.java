import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalcTest {
	private Calc calc = new Calc();

	@Test
	void add() {
		assertEquals(15, calc.add(10, 5));
		assertEquals(5, calc.add(8, -3));
	}

	@Test
	void pow() {
		assertEquals(125, calc.pow(5, 3));
		assertEquals(Integer.MAX_VALUE, calc.pow(2, 31) - 1);
	}

}