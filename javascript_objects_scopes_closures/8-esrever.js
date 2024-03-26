#!/usr/bin/node

exports.esrever = function (list) {
  let i = (list.length - 1);
  const listreturn = [];

  while (i > -1) {
    listreturn.push(list[i]);
    i--;
  }
  return listreturn;
};
