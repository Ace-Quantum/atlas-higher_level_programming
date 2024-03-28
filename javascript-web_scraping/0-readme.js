#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

// console.log('hello');

fs.readFile(args[2], (err, content) => {
    if (err) throw err;

    console.log(content.toString());

});


// console.log('hello?');
// const fs = require('fs');
// let InputFile = new FileReader();

// function TaskReadFile (InputFile) {
//   fs.readFile(InputFile, (err, content) => {
//     if (err) {
//         console.error('error', err);
//         return
//     }
//     console.log(content.toString());
//     console.log('heck');
//   })
  
// }

// exports.TaskReadFile = TaskReadFile;
