#!/usr/bin/node

const square = require('./5-square')

class Square extends square {
  constructor (size) {
    super(size, size)
  }
  charPrint(c) {
    let i = 0;
    let str = '';
    if (c === 'undefined') {
      c = 'X';
    }
    while (i < this.size) {
      str = str + 'X';
      i++;
    }

    i++;

    while (i < this.size) {
      console.log(str);
      i++;
    }
  }
}
module.exports = Square;
  