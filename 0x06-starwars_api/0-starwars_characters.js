#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body).characters;
  exactOrder(data, 0);
});

const exactOrder = (data, x) => {
  if (x === data.length) return;
  request(data[x], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(data, x + 1);
  });
};
