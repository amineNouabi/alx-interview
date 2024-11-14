#!/usr/bin/node
const util = require('util');
const request = require('request');

const get = util.promisify(request.get);

const API_URL = 'https://swapi-api.alx-tools.com/api';

const filmId = process.argv.slice(2)[0];

async function fetchCharacter (characterId) {
  return JSON.parse((await get(`${API_URL}/people/${characterId}`)).body);
}

request.get(`${API_URL}/films/${filmId}`, {}, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (!response || response.statusCode >= 400) {
    console.error(new Error('Bad Response'));
    return;
  }

  const charactersIds = JSON.parse(body).characters.map((characterURL) => {
    const tokens = characterURL.split('/');
    return tokens[tokens.length - 2];
  });

  charactersIds.forEach(async (characterId) => {
    const character = await fetchCharacter(characterId);
    console.log(character.name);
  });
});
