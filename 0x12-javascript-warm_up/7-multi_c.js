#!/usr/bin/node

let num = process.argv[2];
let i = 0;

if (!isNaN(parseInt(process.argv[2]))) {
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
