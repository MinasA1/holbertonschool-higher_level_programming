#!/usr/bin/node
let num = Number.parseInt(process.argv[2]);
if (isNaN(num)) {
  return 1;
}
function factorial(n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(num));
