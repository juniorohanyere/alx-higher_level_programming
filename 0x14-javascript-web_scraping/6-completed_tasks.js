#!/usr/bin/node
// computes the number of tasks completed by user id

const args = process.argv;
const url = args[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const todos = JSON.parse(body);
    const tkey = {};

    for (let i = 0; i < todos.length; i++) {
      const status = (todos[i].completed);
      const key = todos[i].userId.toString();

      if (status) {
        if (tkey[key]) {
          tkey[key]++;
        } else {
          tkey[key] = 1;
        }
      }
    }
    console.log(tkey);
  }
});
