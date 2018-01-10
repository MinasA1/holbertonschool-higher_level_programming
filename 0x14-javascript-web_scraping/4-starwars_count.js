#!/usr/bin/node
if (!(process.argv.length === 3)) {
  console.log('Usage: ./starwars_count.js <API>');
  process.exit();
}
if (!(process.argv[2] === 'http://swapi.co/api/films/' ||
      process.argv[2] === 'https://swapi.co/api/films/' ||
      process.argv[2] === 'https://swapi.co/api/films' ||
      process.argv[2] === 'http://swapi.co/api/films')) {
  process.exit();
}
const request = require('request');
let name = 'https://swapi.co/api/people/18/';
request(process.argv[2], function (error, response, body) {
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
