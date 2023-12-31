#!/usr/bin/env bash

function bench {
  uvicorn app:app --port 8081 --no-access-log &> /dev/null &
  pid=$!
  sleep 5
  echo
  echo "### $1"
  echo
  echo '```'
  wrk http://127.0.0.1:8081/$2 -c 1000 -t 6
  echo
  wrk http://127.0.0.1:8081/$2 -c 1000 -t 6 -s wrk.lua
  echo '```'
  echo
  kill $pid &> /dev/null
}

bench "Asyncpg" asyncpg
bench 'SQLA + asyncpg' sqla-asyncpg
bench 'SQLA + psycopg2' sqla-psycopg2
bench 'SQLA + psycopg2' sqla-psycopg2
bench 'Piccolo' piccolo
bench 'Peewee no pool' peewee-no-pool
bench 'Peewee'
