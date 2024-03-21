#!/usr/bin/node

const args = process.argv;

let isanumber = parseInt(args[2]);

if (typeof isanumber === 'number') {
  console.log('My number: ' + args[2]);
} else {
  console.log('Not a number');
}
