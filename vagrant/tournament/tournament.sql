-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Delete DB if it exists
DROP DATABASE IF EXISTS tournament;

-- Create the tournament database
CREATE DATABASE tournament;

-- connect to tournament database
\c tournament

-- create players table
CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- create matches table
CREATE TABLE matches(
    id SERIAL PRIMARY KEY,
    winner INTEGER REFERENCES players(id),
    loser INTEGER REFERENCES players(id)
);
