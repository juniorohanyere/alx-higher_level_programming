#!/usr/bin/node
let num = process.argv[2];
let msg;


if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    msg = '';
    for (let j = 0; j < num; j++) {
      msg = msg + 'X';
    }
    console.log(msg);
  }
}
