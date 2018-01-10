#!/usr/bin/node
if (!(process.argv.length === 4)) {
  console.log('Usage:./5-request_store.js <URL> <filepath>');
  process.exit();
}
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
        process.exit();
      }
    });
  }
});
