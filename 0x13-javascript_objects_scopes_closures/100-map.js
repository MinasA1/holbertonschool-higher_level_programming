#!/usr/bin/node
const list = require('./100-data.js').list;
var newList = list.map(function (cV, i) {
  return cV * i;
});
console.log(list);
console.log(newList);
