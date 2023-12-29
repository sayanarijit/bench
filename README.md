Benchmark done with 25 records

### Peewee

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/peewee -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/peewee
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    71.15ms   22.32ms 375.74ms   91.64%
    Req/Sec    71.23     14.55   111.00     74.69%
  2842 requests in 10.01s, 3.03MB read
Requests/sec:    283.89
Transfer/sec:    309.95KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/peewee -c 20 -t 4 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/peewee
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    32.01ms    7.68ms  87.32ms   70.98%
    Req/Sec   156.55     18.57   202.00     73.50%
  6244 requests in 10.01s, 0.97MB read
Requests/sec:    623.95
Transfer/sec:     99.71KB
```

### SQLA + asyncpg

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    90.31ms  117.48ms   1.10s    94.36%
    Req/Sec    77.48     14.66   111.00     75.53%
  2927 requests in 10.02s, 3.12MB read
Requests/sec:    292.25
Transfer/sec:    319.07KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg -c 20 -t 4 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    39.65ms   49.36ms 503.22ms   95.82%
    Req/Sec   161.11     32.07   232.00     88.66%
  6251 requests in 10.01s, 0.98MB read
Requests/sec:    624.49
Transfer/sec:     99.79KB
```

### SQLA + psycopg2

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2 -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    81.36ms   18.34ms 167.40ms   75.62%
    Req/Sec    61.47     12.33   101.00     83.88%
  2450 requests in 10.01s, 2.61MB read
Requests/sec:    244.65
Transfer/sec:    267.11KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2 -c 20 -t 4 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    39.28ms   14.00ms 124.34ms   78.88%
    Req/Sec   128.09     23.04   180.00     73.00%
  5109 requests in 10.01s, 813.25KB read
Requests/sec:    510.46
Transfer/sec:     81.25KB
```

### Piccolo

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/piccolo
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   840.40ms   97.81ms   1.15s    73.91%
    Req/Sec    11.32     11.84    40.00     85.29%
  230 requests in 10.01s, 251.11KB read
Requests/sec:     22.97
Transfer/sec:     25.08KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo -c 20 -t 4 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/piccolo
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   799.82ms  130.25ms   1.15s    78.93%
    Req/Sec     8.72      7.90    40.00     83.33%
  242 requests in 10.02s, 38.66KB read
Requests/sec:     24.16
Transfer/sec:      3.86KB
```
