#!/usr/bin/node
exports.addMeMaybe = function (x, f) {
  x++;
  f(x);
};
