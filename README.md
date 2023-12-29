Benchmark done with 25 records

### SQLA + asyncpg

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   494.30ms  621.36ms   2.00s    77.61%
    Req/Sec    35.28     17.07   100.00     76.88%
  1900 requests in 10.06s, 3.39MB read
  Socket errors: connect 0, read 0, write 0, timeout 1315
Requests/sec:    188.81
Transfer/sec:    345.35KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   986.13ms  438.21ms   2.00s    71.84%
    Req/Sec   134.46     78.30   404.00     66.44%
  7882 requests in 10.07s, 1.23MB read
  Socket errors: connect 0, read 0, write 0, timeout 896
Requests/sec:    782.92
Transfer/sec:    125.11KB
```

### SQLA + psycopg2

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2 -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.54s   337.59ms   1.98s    72.93%
    Req/Sec    36.21     38.52   252.00     85.92%
  1694 requests in 10.06s, 3.03MB read
  Socket errors: connect 0, read 0, write 0, timeout 848
Requests/sec:    168.42
Transfer/sec:    308.06KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2 -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   578.71ms  303.95ms   1.14s    63.26%
    Req/Sec   103.35     52.60   404.00     71.22%
  4326 requests in 10.06s, 688.61KB read
  Socket errors: connect 0, read 0, write 0, timeout 643
Requests/sec:    430.14
Transfer/sec:     68.47KB
```

### Piccolo

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   712.28ms  679.30ms   2.00s    75.87%
    Req/Sec    44.74     23.30   160.00     63.11%
  2507 requests in 10.06s, 4.48MB read
  Socket errors: connect 0, read 0, write 0, timeout 1703
Requests/sec:    249.17
Transfer/sec:    455.75KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   794.01ms  374.33ms   2.00s    77.93%
    Req/Sec   198.84     84.15   430.00     67.52%
  11700 requests in 10.05s, 1.83MB read
  Socket errors: connect 0, read 0, write 0, timeout 185
Requests/sec:   1164.13
Transfer/sec:    186.03KB
```

### Peewee

NOTE: Most requests errored

```
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/peewee -c 1000 -t 6
Running 10s test @ http://127.0.0.1:8081/peewee
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.24s   286.14ms   2.00s    87.19%
    Req/Sec   116.34     69.55   464.00     71.01%
  6505 requests in 10.06s, 1.59MB read
  Socket errors: connect 0, read 6190, write 0, timeout 885
  Non-2xx or 3xx responses: 6190
Requests/sec:    646.65
Transfer/sec:    161.83KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/peewee -c 1000 -t 6 -s wrk.lua
Running 10s test @ http://127.0.0.1:8081/peewee
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.31s   277.39ms   1.62s    84.01%
    Req/Sec   125.56     60.65   383.00     73.08%
  7098 requests in 10.05s, 1.18MB read
  Socket errors: connect 0, read 7098, write 0, timeout 0
  Non-2xx or 3xx responses: 7098
Requests/sec:    706.23
Transfer/sec:    120.00KB
```
