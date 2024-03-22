#!/usr/bin/node

const square = require('./5-square');

class Square extends square {

  charPrint (c) {
    let i = 0;
    let str = '';
    if (c === undefined) {
      c = 'X';
    }
    while (i < this.width) {
      str = str + c;
      i++;
    }

    i = 0;

    while (i < this.height) {
      console.log(str);
      i++;
    }
  }
}

module.exports = Square;
