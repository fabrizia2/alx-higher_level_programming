#!/usr/bin/node

// Import Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Create a class Square that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
