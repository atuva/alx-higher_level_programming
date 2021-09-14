#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

fs.readFile(argv[2], (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data.toString());
});
