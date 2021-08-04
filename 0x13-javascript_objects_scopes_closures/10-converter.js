#!/usr/bin/node

exports.converter = function (base) {
  return function (baseTen) {
    return baseTen.toString(base);
  };
};
