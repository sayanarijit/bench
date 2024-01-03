### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.27ms    7.98ms 138.20ms   97.93%
    Req/Sec     1.14k   169.97     1.26k    97.00%
  22715 requests in 10.00s, 24.72MB read
Requests/sec:   2270.42
Transfer/sec:      2.47MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.90ms  364.28us   6.22ms   69.31%
    Req/Sec     1.28k    42.02     1.42k    66.50%
  25556 requests in 10.01s, 3.97MB read
Requests/sec:   2554.27
Transfer/sec:    406.49KB
```

### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.97ms    7.63ms 140.95ms   97.89%
    Req/Sec     0.97k   138.89     1.05k    96.00%
  19279 requests in 10.01s, 20.98MB read
Requests/sec:   1926.43
Transfer/sec:      2.10MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.18ms  452.34us   9.97ms   68.55%
    Req/Sec     0.97k    21.17     1.03k    67.50%
  19260 requests in 10.00s, 2.99MB read
Requests/sec:   1925.42
Transfer/sec:    306.41KB
```

### Pgmini + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.78ms    1.60ms  41.91ms   99.14%
    Req/Sec     0.88k    61.02     0.98k    92.00%
  17524 requests in 10.01s, 19.07MB read
Requests/sec:   1750.81
Transfer/sec:      1.91MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.99ms    1.35ms  39.89ms   99.43%
    Req/Sec   844.61     50.08     0.96k    71.50%
  16812 requests in 10.00s, 2.61MB read
Requests/sec:   1680.88
Transfer/sec:    267.50KB
```

### Pgmini + aiopg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.01ms    1.55ms  39.51ms   99.06%
    Req/Sec   845.97     54.26     0.92k    97.50%
  16842 requests in 10.01s, 18.33MB read
Requests/sec:   1683.32
Transfer/sec:      1.83MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.62ms    1.33ms  39.98ms   99.58%
    Req/Sec     0.90k    44.44     1.00k    71.50%
  17907 requests in 10.01s, 2.78MB read
Requests/sec:   1789.79
Transfer/sec:    284.83KB
```

### Pgmini + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    28.33ms    8.27ms  74.04ms   66.38%
    Req/Sec   176.89     25.10   262.00     67.50%
  3527 requests in 10.01s, 3.84MB read
Requests/sec:    352.44
Transfer/sec:    392.71KB

Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    30.51ms    8.03ms  81.43ms   64.43%
    Req/Sec   163.98     19.16   220.00     77.50%
  3271 requests in 10.01s, 520.54KB read
Requests/sec:    326.92
Transfer/sec:     52.03KB
```

### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.64ms    8.67ms 143.60ms   97.66%
    Req/Sec     0.89k   134.66     0.97k    96.00%
  17647 requests in 10.00s, 19.20MB read
Requests/sec:   1763.84
Transfer/sec:      1.92MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.58ms    1.36ms  39.03ms   98.52%
    Req/Sec     0.91k    40.74     0.99k    85.00%
  18024 requests in 10.00s, 2.80MB read
Requests/sec:   1801.74
Transfer/sec:    286.73KB
```

### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    14.75ms   36.46ms 456.30ms   96.96%
    Req/Sec   554.40     78.76   620.00     93.88%
  10834 requests in 10.01s, 11.79MB read
Requests/sec:   1082.42
Transfer/sec:      1.18MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.80ms    1.47ms  41.45ms   95.81%
    Req/Sec   646.18     28.09   700.00     87.00%
  12867 requests in 10.01s, 2.00MB read
Requests/sec:   1285.95
Transfer/sec:    204.65KB
```

### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.90ms    3.72ms  52.08ms   85.32%
    Req/Sec   393.07     30.08   450.00     81.50%
  7830 requests in 10.01s, 8.52MB read
Requests/sec:    782.33
Transfer/sec:      0.85MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.07ms    2.37ms  48.27ms   81.52%
    Req/Sec   499.86     28.11   560.00     71.50%
  9955 requests in 10.01s, 1.55MB read
Requests/sec:    994.92
Transfer/sec:    158.37KB
```

### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    11.27ms    6.66ms  88.68ms   94.42%
    Req/Sec   446.70     79.52   555.00     80.00%
  8897 requests in 10.00s, 1.63MB read
  Socket errors: connect 0, read 8847, write 0, timeout 0
  Non-2xx or 3xx responses: 8730
Requests/sec:    889.51
Transfer/sec:    166.91KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.58ms    5.44ms  59.96ms   97.17%
    Req/Sec   470.27     55.31   550.00     89.50%
  9366 requests in 10.00s, 1.55MB read
  Socket errors: connect 0, read 9364, write 0, timeout 0
  Non-2xx or 3xx responses: 9366
Requests/sec:    936.26
Transfer/sec:    159.09KB
```

### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.08ms    1.91ms  34.21ms   99.07%
    Req/Sec     5.35k   302.00     5.99k    92.08%
  107480 requests in 10.10s, 15.79MB read
  Non-2xx or 3xx responses: 107480
Requests/sec:  10641.67
Transfer/sec:      1.56MB

Running 10s test @ http://127.0.0.1:8081/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.27ms    1.61ms  34.78ms   99.36%
    Req/Sec     4.20k   194.78     4.37k    97.52%
  84455 requests in 10.10s, 12.40MB read
  Non-2xx or 3xx responses: 84455
Requests/sec:   8362.31
Transfer/sec:      1.23MB
```
