#!/usr/bin/node
// prints the number of movies where the character Wedge Antilles is present

const args = process.argv;
const url = args[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const jsonp = JSON.parse(body);
    const results = jsonp.results;
    let count = 0;

    for (let i = 0; i < results.length; i++) {
      const ch = (results[i].characters);
      for (let j = 0; j < ch.length; j++) {
        const check = ch[j].endsWith('18/');
        if (check) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
