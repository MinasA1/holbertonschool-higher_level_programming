#!/usr/bin/node
if (!(process.argv.length === 4)) {
  console.log('Usage:.1-writeme.js <filepath> <content>');
  process.exit();
}
const fs = require('fs');
let fPath = process.argv[2];
let content = process.argv[3];
fs.writeFile(fPath, content, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
    process.exit();
  }
});
