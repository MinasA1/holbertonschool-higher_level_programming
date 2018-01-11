#!/usr/bin/node
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
