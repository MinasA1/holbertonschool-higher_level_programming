#!/usr/bin/node
const dict = require('./101-data').dict;
let newD = {};

for (let k in dict) {
  if (dict[k] in newD) {
    newD[dict[k]].push(k);
  } else {
    newD[dict[k]] = [k];
  }
}
console.log(newD);
