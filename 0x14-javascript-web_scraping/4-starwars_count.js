#!/usr/bin/node
if (!(process.argv.length === 3)) {
  console.log('Usage: ./starwars_count.js <API>');
  process.exit();
}

const request = require('request');
let name = 'https://swapi.co/api/people/18/';
let url = 'http://swapi.co/api/films/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit();
  }
  let count = 0;
  let js = JSON.parse(body);
  for (let el in js.results) {
    if (js.results[el].characters.indexOf(name) >= 0) {
      count = count + 1;
    }
  }
  console.log(count);
});
