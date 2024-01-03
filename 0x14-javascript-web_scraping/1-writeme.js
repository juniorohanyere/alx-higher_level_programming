#!/usr/bin/node
// writes a string to a file

const fd = require('fs');
const file = process.argv[2];
const wfile = process.argv[3];

fd.writeFile(file, wfile, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
