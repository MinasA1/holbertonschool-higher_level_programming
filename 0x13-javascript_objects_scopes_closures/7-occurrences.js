#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let oc = 0;
  for (let i of list) {
    if (i === searchElement) {
      oc++;
    }
  }
  return oc;
};
