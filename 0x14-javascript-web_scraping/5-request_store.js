#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.
const argv = require('process').argv;
const request = require('request');
const fs = require('fs');

request
  .get(argv[2])
  .on('error', err => {
    console.log(err);
  })
  .pipe(fs.createWriteStream(argv[3], 'utf-8'));
