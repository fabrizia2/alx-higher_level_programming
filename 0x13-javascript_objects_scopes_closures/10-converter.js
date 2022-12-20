#!/usr/bin/node
/**
 * Write a function that converts a number from base 10 to another base passed as argument:
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base); // toString() method returns a string representing the specified Number object in the specified radix (base).
  };
};
