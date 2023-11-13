#!/usr/bin/node
let num = process.argv[2];
let msg;
let i;
let j;


if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    msg = '';
    for (j = 0; j < num; j++) {
      msg = msg + 'X';
    }
    console.log(msg);
  }
}
