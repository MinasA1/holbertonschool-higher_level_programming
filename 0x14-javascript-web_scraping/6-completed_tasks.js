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
  dict = JSON.parse(body)
  let newD = {};

  for (let k in dict) {
    if (dict[k].userId in newD) {
      newD[dict[k].userId] = newD[dict[k].userId] + 1;
    } else {
      newD[dict[k].userId] = 1;
    }
  }
  console.log(newD);
});
