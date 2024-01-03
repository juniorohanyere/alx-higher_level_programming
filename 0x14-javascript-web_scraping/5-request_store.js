#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const fd = require('fs');
const request = require('request');

request(process.argv[2]).pipe(fd.createWriteStream(process.argv[3]));
