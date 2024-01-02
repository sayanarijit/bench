
### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   698.33ms  508.99ms   2.00s    56.84%
    Req/Sec   195.93    102.92   565.00     67.36%
  11210 requests in 10.05s, 17.48MB read
  Socket errors: connect 0, read 0, write 0, timeout 753
Requests/sec:   1115.92
Transfer/sec:      1.74MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   513.36ms  460.09ms   2.00s    53.20%
    Req/Sec   323.59    117.27   737.00     71.40%
  19300 requests in 10.05s, 3.01MB read
  Socket errors: connect 0, read 0, write 0, timeout 266
Requests/sec:   1921.10
Transfer/sec:    307.00KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   805.34ms  560.55ms   2.00s    59.25%
    Req/Sec   172.62     87.23   460.00     67.19%
  9849 requests in 10.04s, 15.36MB read
  Socket errors: connect 0, read 0, write 0, timeout 677
Requests/sec:    980.50
Transfer/sec:      1.53MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   612.51ms  504.79ms   2.00s    49.98%
    Req/Sec   244.67     86.08   520.00     69.13%
  14557 requests in 10.04s, 2.27MB read
  Socket errors: connect 0, read 0, write 0, timeout 436
Requests/sec:   1449.75
Transfer/sec:    231.68KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.02s   750.53ms   2.00s    61.83%
    Req/Sec    94.99     49.33   320.00     70.19%
  5148 requests in 10.04s, 8.03MB read
  Socket errors: connect 0, read 0, write 0, timeout 1341
Requests/sec:    512.79
Transfer/sec:    818.76KB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   655.41ms  626.53ms   2.00s    41.19%
    Req/Sec   159.78     80.90   414.00     68.60%
  9398 requests in 10.03s, 1.47MB read
  Socket errors: connect 0, read 0, write 0, timeout 1269
Requests/sec:    936.61
Transfer/sec:    149.67KB
```


### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us    -nan%
    Req/Sec     0.00      0.00     0.00      -nan%
  0 requests in 10.06s, 0.00B read
Requests/sec:      0.00
Transfer/sec:       0.00B

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us    -nan%
    Req/Sec     0.00      0.00     0.00      -nan%
  0 requests in 10.06s, 0.00B read
Requests/sec:      0.00
Transfer/sec:       0.00B
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   884.16ms  553.69ms   2.00s    66.11%
    Req/Sec   156.72     83.80   434.00     69.29%
  8854 requests in 10.04s, 13.81MB read
  Socket errors: connect 0, read 0, write 0, timeout 749
Requests/sec:    881.56
Transfer/sec:      1.37MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   622.04ms  499.86ms   2.00s    52.12%
    Req/Sec   225.35     89.48   620.00     69.70%
  13348 requests in 10.04s, 2.08MB read
  Socket errors: connect 0, read 0, write 0, timeout 673
Requests/sec:   1330.12
Transfer/sec:    212.56KB
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.46s   240.64ms   2.00s    75.93%
    Req/Sec   110.26     49.83   333.00     69.64%
  6290 requests in 10.02s, 1.13MB read
  Socket errors: connect 0, read 6286, write 0, timeout 74
  Non-2xx or 3xx responses: 6231
Requests/sec:    627.46
Transfer/sec:    115.02KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.07s   179.20ms   2.00s    92.13%
    Req/Sec   162.70     70.60   480.00     74.95%
  8437 requests in 10.03s, 1.40MB read
  Socket errors: connect 0, read 8436, write 0, timeout 360
  Non-2xx or 3xx responses: 8437
Requests/sec:    841.00
Transfer/sec:    142.90KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    55.61ms   57.91ms   1.99s    98.33%
    Req/Sec     1.04k   403.34     2.38k    69.67%
  61864 requests in 10.03s, 9.09MB read
  Socket errors: connect 0, read 0, write 0, timeout 148
  Non-2xx or 3xx responses: 61864
Requests/sec:   6168.95
Transfer/sec:      0.91MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    42.13ms   84.19ms   1.99s    98.82%
    Req/Sec     1.36k   537.85     3.25k    69.20%
  80485 requests in 10.04s, 11.82MB read
  Socket errors: connect 0, read 0, write 0, timeout 213
  Non-2xx or 3xx responses: 80485
Requests/sec:   8020.25
Transfer/sec:      1.18MB
```

