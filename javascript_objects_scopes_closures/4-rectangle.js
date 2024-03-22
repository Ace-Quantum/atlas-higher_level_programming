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
    let str = '';
    while (i < this.width) {
      str = str + 'X';
      i++;
    }

    i = 0;

    while (i < this.height) {
      console.log(str);
      i++;
    }
  }

  rotate () {
    const h = this.height;
    const w = this.width;

    this.height = w;
    this.width = h;
  }

  double () {
    const h = this.height;
    const w = this.width;

    this.height = (h * 2);
    this.width = (w * 2);
  }
}

module.exports = Rectangle;
