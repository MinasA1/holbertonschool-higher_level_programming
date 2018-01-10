#!/usr/bin/node
if (!(process.argv.length === 3)) {
  console.log('Usage: ./starwars_count.js <API>');
  process.exit();
}
const request = require('request');
let url = 'https://swapi.co/api/people/18'
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit();
  }
  let js = JSON.parse(body);
  console.log(js['films'].length);
});
