#!/usr/bin/node

let counter = 0;

exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
}

    //     let counter = 0;

//     function printit () {
//         console.log('${counter}: {item}');
//         counter++;
//     }

//     return printit();
// }

