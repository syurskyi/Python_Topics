const convertForeignGridToLocalGrid = require('../src/convertForeignGridToLocalGrid');

const createSeat = (x, y) => {
  return {
    x,
    y
  };
};

test('creates grid starting (0, 0)', () => {
  const input = [
    createSeat(1, 1),
    createSeat(2, 1),
    createSeat(1, 2),
    createSeat(2, 2)
  ];

  const output = [
    createSeat(0, 0),
    createSeat(1, 0),
    createSeat(0, 1),
    createSeat(1, 1)
  ];

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('throws an error if there are not enough seats do determine the most common horizontal space between seats', () => {
  const input = [
    createSeat(10, 10),
    createSeat(10, 20)
  ];

  const output = 'error';

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('throws an error if there are not enough seats do determine the most common vertical space between seats', () => {
  const input = [
    createSeat(10, 10),
    createSeat(20, 10)
  ];

  const output = 'error';

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('throws an error if seat locations overlap', () => {
  const input = [
    createSeat(10, 10),

    createSeat(10, 10),
    createSeat(20, 10),

    createSeat(10, 20),
    createSeat(20, 20)
  ];

  const output = 'error';

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('throws an error if seat locations overlap', () => {
  const input = [
    createSeat(11, 10),

    createSeat(10, 10),
    createSeat(20, 10),

    createSeat(10, 20),
    createSeat(20, 20)
  ];

  const output = 'error';

  expect(convertForeignGridToLocalGrid(input, 20)).toEqual(output);
});

test('reduces to spaceless grid', () => {
  const input = [
    createSeat(10, 10),
    createSeat(20, 10),

    createSeat(10, 20),
    createSeat(20, 20)
  ];

  const output = [
    createSeat(0, 0),
    createSeat(1, 0),

    createSeat(0, 1),
    createSeat(1, 1)
  ];

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('reduces to spaceless grid', () => {
  const input = [
    createSeat(10, 10),
    createSeat(20, 10),
    createSeat(30, 10),

    createSeat(10, 20),
    createSeat(30, 20)
  ];

  const output = [
    createSeat(0, 0),
    createSeat(1, 0),
    createSeat(2, 0),

    createSeat(0, 1),
    createSeat(2, 1)
  ];

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('ignores missing seats (vertical)', () => {
  const input = [
    createSeat(10, 10),
    createSeat(20, 10),

    createSeat(20, 20),

    createSeat(10, 30),
    createSeat(20, 30)
  ];

  const output = [
    createSeat(0, 0),
    createSeat(1, 0),

    createSeat(1, 1),

    createSeat(0, 2),
    createSeat(1, 2)
  ];

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('vertical size of space between seats is separate from horizontal', () => {
  const input = [
    createSeat(10, 50),
    createSeat(20, 50),
    createSeat(30, 50),

    createSeat(10, 100),
    createSeat(20, 100),
    createSeat(30, 100),

    createSeat(10, 150),
    createSeat(20, 150),
    createSeat(30, 150)
  ];

  const output = [
    createSeat(0, 0),
    createSeat(1, 0),
    createSeat(2, 0),

    createSeat(0, 1),
    createSeat(1, 1),
    createSeat(2, 1),

    createSeat(0, 2),
    createSeat(1, 2),
    createSeat(2, 2)
  ];

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('horizontal size of space between seats is separate from vertical', () => {
  const input = [
    createSeat(50, 10),
    createSeat(100, 10),
    createSeat(150, 10),

    createSeat(50, 20),
    createSeat(100, 20),
    createSeat(150, 20),

    createSeat(50, 30),
    createSeat(100, 30),
    createSeat(150, 30)
  ];

  const output = [
    createSeat(0, 0),
    createSeat(1, 0),
    createSeat(2, 0),

    createSeat(0, 1),
    createSeat(1, 1),
    createSeat(2, 1),

    createSeat(0, 2),
    createSeat(1, 2),
    createSeat(2, 2)
  ];

  expect(convertForeignGridToLocalGrid(input)).toEqual(output);
});

test('normalizes alignment of nearby seats (horizontal; 20% error', () => {
  const input = [
    createSeat(1 * 10 + 9, 10),
    createSeat(2 * 10 + 10, 10),
    createSeat(3 * 10 + 11, 10),
    createSeat(4 * 10 + 10, 10),
    createSeat(5 * 10 + 9, 10),
    createSeat(6 * 10 + 10, 10)
  ];

  const output = [
    createSeat(1, 0),
    createSeat(2, 0),
    createSeat(3, 0),
    createSeat(4, 0),
    createSeat(5, 0),
    createSeat(6, 0)
  ];

  expect(convertForeignGridToLocalGrid(input, 20)).toEqual(output);
});

test('normalizes alignment of nearby seats (horizontal; 20% error) (relative to nearest neighbour; left-to-right', () => {
  const input = [
    createSeat(1 * 10 + 10, 10),
    createSeat(2 * 10 + 11, 10),
    createSeat(3 * 10 + 12, 10),
    createSeat(4 * 10 + 13, 10),
    createSeat(5 * 10 + 14, 10),
    createSeat(6 * 10 + 15, 10)
  ];

  const output = [
    createSeat(1, 0),
    createSeat(2, 0),
    createSeat(3, 0),
    createSeat(4, 0),
    createSeat(5, 0),
    createSeat(6, 0)
  ];

  expect(convertForeignGridToLocalGrid(input, 20)).toEqual(output);
});

test('normalizes alignment of nearby seats (vertical; 20% error', () => {
  const input = [
    createSeat(10, 1 * 10 + 9),
    createSeat(10, 2 * 10 + 10),
    createSeat(10, 3 * 10 + 11),
    createSeat(10, 4 * 10 + 10),
    createSeat(10, 5 * 10 + 9),
    createSeat(10, 6 * 10 + 10)
  ];

  const output = [
    createSeat(0, 1),
    createSeat(0, 2),
    createSeat(0, 3),
    createSeat(0, 4),
    createSeat(0, 5),
    createSeat(0, 6)
  ];

  expect(convertForeignGridToLocalGrid(input, 20)).toEqual(output);
});

test('normalizes alignment of nearby seats (vertical; 20% error', () => {
  const input = [
    createSeat(10, 1 * 10 + 10),
    createSeat(10, 2 * 10 + 11),
    createSeat(10, 3 * 10 + 12),
    createSeat(10, 4 * 10 + 13),
    createSeat(10, 5 * 10 + 14),
    createSeat(10, 6 * 10 + 15)
  ];

  const output = [
    createSeat(0, 1),
    createSeat(0, 2),
    createSeat(0, 3),
    createSeat(0, 4),
    createSeat(0, 5),
    createSeat(0, 6)
  ];

  expect(convertForeignGridToLocalGrid(input, 20)).toEqual(output);
});