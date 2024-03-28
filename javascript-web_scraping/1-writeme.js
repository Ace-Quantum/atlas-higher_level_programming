#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const InputText = args[3];

fs.writeFile(args[2], InputText, (err) => {
  if (err) throw err;
}
);
