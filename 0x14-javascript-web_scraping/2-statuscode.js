#!/usr/bin/node
if (!(process.argv.length === 3)) {
  console.log('Usage: ./2statuscode.js <URL>');
  process.exit();
}
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
