const fs = require('fs');
const sampleData = require('./sample-input.json');
const convertForeignGridToLocalGrid = require('./convertForeignGridToLocalGrid');
const {
  createCoordinateGridMember,
  drawCoordinateGrid
} = require('coordinate-grid');

const localGrid = convertForeignGridToLocalGrid(sampleData, 10);

console.log(
  drawCoordinateGrid(
    localGrid.map((seat) => {
      return createCoordinateGridMember(seat.x, seat.y, 'x')
    }), ' '
  )
);