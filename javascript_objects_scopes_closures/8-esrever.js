#!/usr/bin/node

exports.esrever = function (list){
  let i = (list.length)
  let listreturn = []

  while (i > 0) {
    listreturn.push(list[i]);
    i--;
  }
  return listreturn;
}
