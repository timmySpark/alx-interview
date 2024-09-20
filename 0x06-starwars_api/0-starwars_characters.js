#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  Order(actors, 0);
});
const Order = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    Order(actors, x + 1);
  });
};
