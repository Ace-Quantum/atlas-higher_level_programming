#!/usr/bin/node
const args = process.argv;

if (args.length === 2) {
  console.log('No argument');
} else {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }
}
