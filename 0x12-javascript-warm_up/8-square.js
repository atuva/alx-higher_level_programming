#!/usr/bin/node
const argv = require('process').argv;
const num = Number(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      square = square + 'X';
    }
    square = square + '\n';
  }
  console.log(square);
}
