
### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   521.20ms  493.20ms   2.00s    38.84%
    Req/Sec   290.81    130.30   686.00     68.37%
  17079 requests in 10.03s, 24.66MB read
  Socket errors: connect 0, read 0, write 0, timeout 519
Requests/sec:   1702.01
Transfer/sec:      2.46MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   507.99ms  479.09ms   2.00s    51.51%
    Req/Sec   324.73    132.66   767.00     67.50%
  19323 requests in 10.04s, 3.02MB read
  Socket errors: connect 0, read 0, write 0, timeout 324
Requests/sec:   1924.51
Transfer/sec:    307.54KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   591.33ms  528.98ms   2.00s    43.65%
    Req/Sec   251.85    122.84   636.00     68.37%
  14776 requests in 10.04s, 21.33MB read
  Socket errors: connect 0, read 0, write 0, timeout 479
Requests/sec:   1471.91
Transfer/sec:      2.13MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   597.90ms  505.75ms   2.00s    47.76%
    Req/Sec   247.14     91.19   494.00     65.72%
  14741 requests in 10.04s, 2.30MB read
  Socket errors: connect 0, read 0, write 0, timeout 485
Requests/sec:   1468.94
Transfer/sec:    234.74KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   870.61ms  481.44ms   2.00s    72.40%
    Req/Sec   149.79     71.51   343.00     67.08%
  8428 requests in 10.05s, 12.17MB read
  Socket errors: connect 0, read 0, write 0, timeout 1207
Requests/sec:    838.89
Transfer/sec:      1.21MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   833.21ms  390.21ms   2.00s    75.24%
    Req/Sec   169.07     68.50   390.00     66.27%
  9974 requests in 10.03s, 1.56MB read
  Socket errors: connect 0, read 0, write 0, timeout 671
Requests/sec:    993.96
Transfer/sec:    158.84KB
```


### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.10s   286.03ms   1.99s    78.53%
    Req/Sec   121.31    123.16   810.00     85.71%
  7090 requests in 10.04s, 10.24MB read
  Socket errors: connect 0, read 0, write 0, timeout 459
Requests/sec:    706.18
Transfer/sec:      1.02MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   701.43ms  283.91ms   1.99s    77.00%
    Req/Sec   172.46     56.53   390.00     73.18%
  9465 requests in 10.03s, 1.47MB read
  Socket errors: connect 0, read 0, write 0, timeout 730
Requests/sec:    943.73
Transfer/sec:    150.22KB
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   650.52ms  406.96ms   2.00s    66.19%
    Req/Sec   246.30     88.23   515.00     71.43%
  14459 requests in 10.03s, 20.88MB read
  Socket errors: connect 0, read 0, write 0, timeout 191
Requests/sec:   1442.29
Transfer/sec:      2.08MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   617.07ms  409.18ms   2.00s    64.20%
    Req/Sec   250.12     86.48   494.00     66.16%
  14886 requests in 10.03s, 2.32MB read
  Socket errors: connect 0, read 0, write 0, timeout 297
Requests/sec:   1484.08
Transfer/sec:    237.16KB
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   969.43ms  361.65ms   1.77s    75.58%
    Req/Sec   168.77     93.37   555.00     71.88%
  9723 requests in 10.04s, 3.28MB read
  Socket errors: connect 0, read 8413, write 0, timeout 0
  Non-2xx or 3xx responses: 8416
Requests/sec:    968.28
Transfer/sec:    334.86KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.14s   179.88ms   2.00s    91.68%
    Req/Sec   154.62     57.21   300.00     72.12%
  8178 requests in 10.03s, 1.36MB read
  Socket errors: connect 0, read 8145, write 0, timeout 127
  Non-2xx or 3xx responses: 8145
Requests/sec:    815.36
Transfer/sec:    138.51KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    62.07ms   50.07ms   1.96s    99.66%
    Req/Sec     1.58k   501.33     3.03k    60.50%
  94633 requests in 10.04s, 13.90MB read
  Socket errors: connect 0, read 0, write 0, timeout 130
  Non-2xx or 3xx responses: 94633
Requests/sec:   9421.09
Transfer/sec:      1.38MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    42.63ms   84.02ms   1.99s    98.88%
    Req/Sec     1.60k   705.36     5.30k    67.20%
  79966 requests in 10.05s, 11.74MB read
  Socket errors: connect 0, read 0, write 0, timeout 209
  Non-2xx or 3xx responses: 79966
Requests/sec:   7953.69
Transfer/sec:      1.17MB
```

