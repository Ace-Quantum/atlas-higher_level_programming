#!/usr/bin/node

const args = process.argv;

let isanumber = args[2];

if (isNaN(isanumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[2]);
}
