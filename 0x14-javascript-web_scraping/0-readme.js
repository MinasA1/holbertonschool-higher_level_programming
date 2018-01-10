#!/usr/bin/node
if (!(process.argv.length === 3)) {
  console.log('Usage:.0-readme.js <filepath>');
  process.exit();
}
const fs = require('fs');
let fPath = process.argv[2];
fs.readFile(fPath, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
    process.exit();
  }
  console.log(data);
});
