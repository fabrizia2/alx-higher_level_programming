#!/usr/bin/node
/**
 * This script creates a class Rectangle that defines a rectangle:
 * - The constructor takes 2 arguments w and h
 * - Initializes the instance attribute width with the value of w
 * - Initializes the instance attribute height with the value of h
 */
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
