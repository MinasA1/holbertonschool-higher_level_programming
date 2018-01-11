#!/usr/bin/node
if (!(process.argv.length === 3)) {
  console.log('Usage: ./100-starwars_characters.js <episode_id>');
  process.exit();
}
const request = require('request');
let url = 'https://swapi.co/api/films/' + process.argv[2];
function syncReq (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, response, body) {
      if (error) reject(error);
      resolve(JSON.parse(body).name);
    });
  });
}
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit();
  }
  let js = JSON.parse(body);
  let resolves = [];
  for (let el in js['characters']) {
    resolves.push(syncReq(js['characters'][el]));
  }
  Promise.all(resolves).then(function (names) {
    for (let name of names) {
      console.log(name);
    }
  });
});
