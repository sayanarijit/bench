
### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   487.85ms  465.31ms   1.99s    38.69%
    Req/Sec   309.97    200.08     0.87k    63.92%
  18040 requests in 10.03s, 19.23MB read
  Socket errors: connect 0, read 0, write 0, timeout 590
Requests/sec:   1798.17
Transfer/sec:      1.92MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   515.91ms  457.47ms   2.00s    53.97%
    Req/Sec   318.96    116.90   747.00     67.61%
  19038 requests in 10.03s, 2.97MB read
  Socket errors: connect 0, read 0, write 0, timeout 268
Requests/sec:   1897.51
Transfer/sec:    303.23KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   544.43ms  512.35ms   2.00s    39.23%
    Req/Sec   275.28    124.58   610.00     65.31%
  16143 requests in 10.04s, 17.21MB read
  Socket errors: connect 0, read 0, write 0, timeout 509
Requests/sec:   1608.45
Transfer/sec:      1.71MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   585.42ms  489.17ms   1.99s    48.59%
    Req/Sec   258.44    102.08   590.00     69.33%
  15449 requests in 10.03s, 2.41MB read
  Socket errors: connect 0, read 0, write 0, timeout 427
Requests/sec:   1539.72
Transfer/sec:    246.05KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   899.02ms  501.51ms   2.00s    69.83%
    Req/Sec   168.59     97.75   484.00     60.95%
  9539 requests in 10.04s, 10.17MB read
  Socket errors: connect 0, read 0, write 0, timeout 448
Requests/sec:    950.30
Transfer/sec:      1.01MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   805.38ms  432.90ms   2.00s    73.31%
    Req/Sec   170.95     75.59   410.00     65.82%
  10128 requests in 10.04s, 1.58MB read
  Socket errors: connect 0, read 0, write 0, timeout 704
Requests/sec:   1009.01
Transfer/sec:    161.24KB
```


### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   985.37ms  248.40ms   2.00s    75.96%
    Req/Sec   139.86    116.23   626.00     77.99%
  8231 requests in 10.03s, 8.78MB read
  Socket errors: connect 0, read 0, write 0, timeout 440
Requests/sec:    820.56
Transfer/sec:      0.87MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   702.36ms  281.52ms   2.00s    79.89%
    Req/Sec   172.94     61.48   353.00     70.36%
  9601 requests in 10.03s, 1.49MB read
  Socket errors: connect 0, read 0, write 0, timeout 708
Requests/sec:    957.17
Transfer/sec:    152.36KB
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   608.48ms  412.95ms   1.99s    61.46%
    Req/Sec   267.52    161.40   676.00     65.18%
  15577 requests in 10.03s, 16.61MB read
  Socket errors: connect 0, read 0, write 0, timeout 163
Requests/sec:   1552.36
Transfer/sec:      1.66MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   603.55ms  400.95ms   1.99s    62.68%
    Req/Sec   258.92     91.96   550.00     68.28%
  15458 requests in 10.04s, 2.41MB read
  Socket errors: connect 0, read 0, write 0, timeout 262
Requests/sec:   1540.27
Transfer/sec:    246.14KB
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   944.37ms  309.37ms   1.42s    77.44%
    Req/Sec   173.67     95.50   595.00     71.08%
  10036 requests in 10.04s, 2.55MB read
  Socket errors: connect 0, read 9055, write 0, timeout 0
  Non-2xx or 3xx responses: 9055
Requests/sec:    999.72
Transfer/sec:    259.96KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.14s   179.77ms   2.00s    91.90%
    Req/Sec   157.63     72.54   515.00     76.29%
  8203 requests in 10.02s, 1.36MB read
  Socket errors: connect 0, read 8162, write 0, timeout 103
  Non-2xx or 3xx responses: 8163
Requests/sec:    818.47
Transfer/sec:    139.04KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    56.76ms   53.91ms   1.97s    99.60%
    Req/Sec     1.60k   503.83     3.18k    65.17%
  95809 requests in 10.04s, 14.07MB read
  Socket errors: connect 0, read 0, write 0, timeout 143
  Non-2xx or 3xx responses: 95809
Requests/sec:   9545.39
Transfer/sec:      1.40MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    41.60ms   82.50ms   2.00s    98.90%
    Req/Sec     1.38k   532.65     3.48k    76.60%
  81936 requests in 10.03s, 12.03MB read
  Socket errors: connect 0, read 0, write 0, timeout 214
  Non-2xx or 3xx responses: 81936
Requests/sec:   8165.45
Transfer/sec:      1.20MB
```

