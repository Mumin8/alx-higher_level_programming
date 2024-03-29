#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, { encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error(`Error fetching ${url}: ${error}`);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
    if (error) {
      console.error(`Error writing file ${filePath}: ${error}`);
    }
  });
});
