#!/usr/bin/node

const args = process.argv;

const num = (parseInt(args[2]) + 1);

function factorial (num) {
  let i = 1;
  let fact = 1;
  while (i < num) {
    fact = fact * i;
    i++;
  }
  console.log(fact);
}

factorial(num)
