#!/usr/bin/node
if (!(process.argv.length === 3)) {
  console.log('Usage: ./3-starwars_title.js <episode_id>');
  process.exit();
}
const request = require('request');
let url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit();
  }
  let js = JSON.parse(body);
  console.log(js['title']);
});
