#!/usr/bin/node
let numA = Number.parseInt(process.argv[2]);
if (isNaN(numA)) {
  console.log('NaN');
  process.exit();
}
let numB = Number.parseInt(process.argv[3]);
if (isNaN(numB)) {
  console.log('NaN');
  process.exit();
}
function add (a, b) {
  return a + b;
}
console.log(add(numA, numB));
