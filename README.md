### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   502.48ms  477.47ms   1.98s    38.68%
    Req/Sec   303.78    171.08     0.87k    67.75%
  17710 requests in 10.04s, 19.27MB read
  Socket errors: connect 0, read 0, write 0, timeout 515
Requests/sec:   1763.56
Transfer/sec:      1.92MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   516.03ms  458.53ms   2.00s    53.41%
    Req/Sec   317.36    109.49   730.00     71.02%
  18892 requests in 10.04s, 2.94MB read
  Socket errors: connect 0, read 0, write 0, timeout 275
Requests/sec:   1881.83
Transfer/sec:    299.47KB
```

### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   580.34ms  502.65ms   1.98s    44.60%
    Req/Sec   265.69    142.79     0.89k    67.07%
  15497 requests in 10.04s, 16.86MB read
  Socket errors: connect 0, read 0, write 0, timeout 381
Requests/sec:   1543.81
Transfer/sec:      1.68MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   614.94ms  503.38ms   2.00s    49.37%
    Req/Sec   242.51    104.32   686.00     70.52%
  14441 requests in 10.04s, 2.24MB read
  Socket errors: connect 0, read 0, write 0, timeout 447
Requests/sec:   1438.87
Transfer/sec:    228.98KB
```

### Pypika + aiopg

```
Running 10s test @ http://127.0.0.1:8081/pypika-aiopg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   703.49ms  105.63ms   1.34s    87.27%
    Req/Sec   233.66    110.57   575.00     67.64%
  13666 requests in 10.04s, 14.87MB read
Requests/sec:   1361.79
Transfer/sec:      1.48MB

Running 10s test @ http://127.0.0.1:8081/pypika-aiopg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   780.14ms  175.32ms   1.67s    92.32%
    Req/Sec   229.51     90.66   480.00     68.46%
  12253 requests in 10.04s, 1.90MB read
Requests/sec:   1221.00
Transfer/sec:    194.31KB
```

### Pypika + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/pypika-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   765.19ms  181.72ms   1.31s    74.48%
    Req/Sec   234.63    166.34   626.00     57.14%
  12321 requests in 10.04s, 2.67MB read
  Socket errors: connect 0, read 11648, write 0, timeout 0
  Non-2xx or 3xx responses: 11648
Requests/sec:   1227.42
Transfer/sec:    271.88KB

Running 10s test @ http://127.0.0.1:8081/pypika-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   828.31ms  200.73ms   1.45s    88.59%
    Req/Sec   221.65    179.05   717.00     60.00%
  11394 requests in 10.04s, 1.88MB read
  Socket errors: connect 0, read 10699, write 0, timeout 0
  Non-2xx or 3xx responses: 10723
Requests/sec:   1135.40
Transfer/sec:    192.21KB
```

### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   576.60ms  507.35ms   2.00s    46.02%
    Req/Sec   245.35    174.13     0.86k    63.23%
  14280 requests in 10.04s, 15.54MB read
  Socket errors: connect 0, read 0, write 0, timeout 673
Requests/sec:   1422.03
Transfer/sec:      1.55MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   590.08ms  508.30ms   2.00s    49.25%
    Req/Sec   227.36    103.30   626.00     67.22%
  13557 requests in 10.03s, 2.11MB read
  Socket errors: connect 0, read 0, write 0, timeout 841
Requests/sec:   1351.06
Transfer/sec:    215.01KB
```

### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   653.55ms  569.83ms   2.00s    51.37%
    Req/Sec   157.84     71.25   430.00     69.63%
  8910 requests in 10.03s, 9.70MB read
  Socket errors: connect 0, read 0, write 0, timeout 1593
Requests/sec:    888.44
Transfer/sec:      0.97MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   637.84ms  630.13ms   2.00s    84.75%
    Req/Sec   161.18     68.92   410.00     70.05%
  9533 requests in 10.03s, 1.48MB read
  Socket errors: connect 0, read 0, write 0, timeout 1249
Requests/sec:    949.99
Transfer/sec:    151.18KB
```

### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us    -nan%
    Req/Sec     0.00      0.00     0.00      -nan%
  0 requests in 10.05s, 0.00B read
Requests/sec:      0.00
Transfer/sec:       0.00B

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us    -nan%
    Req/Sec     0.00      0.00     0.00      -nan%
  0 requests in 10.05s, 0.00B read
Requests/sec:      0.00
Transfer/sec:       0.00B
```

### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.71s   391.08ms   2.00s    86.29%
    Req/Sec    89.04     60.27   290.00     65.38%
  4806 requests in 10.04s, 0.92MB read
  Socket errors: connect 0, read 4799, write 0, timeout 1078
  Non-2xx or 3xx responses: 4673
Requests/sec:    478.79
Transfer/sec:     93.87KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.80s   209.15ms   2.00s    90.87%
    Req/Sec    81.89     57.59   300.00     62.27%
  3843 requests in 10.03s, 648.39KB read
  Socket errors: connect 0, read 3843, write 0, timeout 2124
  Non-2xx or 3xx responses: 3418
Requests/sec:    382.99
Transfer/sec:     64.62KB
```

### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    45.48ms   69.54ms   2.00s    99.35%
    Req/Sec     1.58k   378.35     2.56k    69.17%
  94199 requests in 10.04s, 13.83MB read
  Socket errors: connect 0, read 0, write 0, timeout 184
  Non-2xx or 3xx responses: 94199
Requests/sec:   9386.27
Transfer/sec:      1.38MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    42.48ms   82.25ms   1.99s    98.97%
    Req/Sec     1.26k   435.58     2.49k    71.64%
  74732 requests in 10.04s, 10.98MB read
  Socket errors: connect 0, read 0, write 0, timeout 208
  Non-2xx or 3xx responses: 74732
Requests/sec:   7444.03
Transfer/sec:      1.09MB
```
