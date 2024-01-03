#!/usr/bin/env bash

function bench {
  uvicorn app:app --port 8081 --no-access-log &> /dev/null &
  pid=$!
  sleep 5
  echo
  echo "### $1"
  echo
  echo '```'
  wrk http://127.0.0.1:8081/$2
  echo
  wrk http://127.0.0.1:8081/$2 -s wrk.lua
  echo '```'
  echo
  kill $pid &> /dev/null
}

bench "Asyncpg" asyncpg
bench "Pypika + asyncpg" pypika-asyncpg
bench "Pgmini + asyncpg" pgmini-aiopg
bench "Pgmini + aiopg" pgmini-aiopg
bench "Pgmini + psycopg2" pgmini-psycopg2
bench 'Piccolo' piccolo
bench 'SQLAlchemy + asyncpg' sqla-asyncpg
bench 'SQLAlchemy + psycopg2' sqla-psycopg2
bench 'Peewee no pool' peewee-no-pool
bench 'Peewee'
