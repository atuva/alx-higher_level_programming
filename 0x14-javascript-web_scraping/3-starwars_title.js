#!/usr/bin/node
// Displays the status of a GET request
const argv = require('process').argv;
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
