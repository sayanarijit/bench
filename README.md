Benchmark done with 25 records

### Peewee

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/peewee -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/peewee
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   919.93ms  424.69ms   2.00s    58.65%
    Req/Sec    35.04     26.99   202.00     85.45%
  1808 requests in 10.06s, 3.23MB read
  Socket errors: connect 0, read 0, write 0, timeout 241
Requests/sec:    179.76
Transfer/sec:    328.79KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/peewee -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/peewee
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   722.99ms  391.72ms   2.00s    55.08%
    Req/Sec    95.75     45.91   343.00     79.92%
  4788 requests in 10.05s, 765.13KB read
  Socket errors: connect 0, read 0, write 0, timeout 676
Requests/sec:    476.39
Transfer/sec:     76.13KB
```

### SQLA + asyncpg

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   685.35ms  659.41ms   1.99s    76.97%
    Req/Sec    36.04     18.98   111.00     70.19%
  1909 requests in 10.06s, 3.41MB read
  Socket errors: connect 0, read 0, write 0, timeout 1566
Requests/sec:    189.68
Transfer/sec:    346.95KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.05s   459.53ms   2.00s    78.29%
    Req/Sec   128.43     54.14   270.00     65.71%
  7633 requests in 10.05s, 1.19MB read
  Socket errors: connect 0, read 0, write 0, timeout 751
Requests/sec:    759.31
Transfer/sec:    121.34KB
```

### SQLA + psycopg2

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2 -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.76s   158.58ms   2.00s    59.32%
    Req/Sec    34.84     32.09   212.00     82.69%
  1416 requests in 10.06s, 2.53MB read
  Socket errors: connect 0, read 0, write 0, timeout 1298
Requests/sec:    140.82
Transfer/sec:    257.58KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2 -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.61s   556.24ms   2.00s    85.57%
    Req/Sec    84.10     56.81   242.00     69.91%
  4528 requests in 10.05s, 720.77KB read
  Socket errors: connect 0, read 0, write 0, timeout 945
Requests/sec:    450.74
Transfer/sec:     71.75KB
```

### Piccolo

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   806.28ms  618.21ms   1.95s    53.53%
    Req/Sec    45.63     29.04   202.00     75.09%
  2589 requests in 10.05s, 4.62MB read
  Socket errors: connect 0, read 0, write 0, timeout 2107
Requests/sec:    257.62
Transfer/sec:    471.21KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   998.82ms  308.57ms   2.00s    87.21%
    Req/Sec   149.90     60.81   333.00     68.89%
  8827 requests in 10.05s, 1.38MB read
  Socket errors: connect 0, read 0, write 0, timeout 503
Requests/sec:    878.13
Transfer/sec:    140.33KB
```
