#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || typeof (w) === 'undefined' || typeof (h) === 'undefined') {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let str = ''
    while (i < this.width) {
      str = str + 'X'
      i++;
    }

    i = 0;

    while (i < this.height) {
      console.log(str);
      i++;
    }
  }
}

module.exports = Rectangle;
