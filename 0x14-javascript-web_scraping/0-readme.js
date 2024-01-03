#!/usr/bin/node
// reads and prints the content of a file

const file = process.argv[2];
const fd = require('fs');

fd.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
