#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
  process.exit();
}
let numbers = process.argv.slice(2).map(n => parseInt(n));
numbers.sort(function (a, b) {
  return a < b;
});
console.log(numbers[1]);
