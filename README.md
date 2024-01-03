### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.10ms   13.30ms 180.42ms   97.90%
    Req/Sec     1.12k   167.09     1.22k    97.00%
  22269 requests in 10.00s, 24.23MB read
Requests/sec:   2226.39
Transfer/sec:      2.42MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.78ms  395.70us   8.28ms   66.63%
    Req/Sec     1.32k    36.07     1.44k    72.00%
  26351 requests in 10.00s, 4.10MB read
Requests/sec:   2633.92
Transfer/sec:    419.16KB
```

### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.33ms    9.81ms 168.15ms   97.97%
    Req/Sec     0.94k   136.48     1.03k    96.00%
  18781 requests in 10.01s, 20.44MB read
Requests/sec:   1876.11
Transfer/sec:      2.04MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.43ms    1.36ms  38.89ms   97.59%
    Req/Sec     0.93k    49.54     1.03k    74.00%
  18527 requests in 10.00s, 2.88MB read
Requests/sec:   1851.98
Transfer/sec:    294.72KB
```

### Pypika + aiopg

```
Running 10s test @ http://127.0.0.1:8081/pypika-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.30ms    1.52ms  38.92ms   99.21%
    Req/Sec   806.18     47.61     0.86k    95.50%
  16051 requests in 10.01s, 17.47MB read
Requests/sec:   1604.28
Transfer/sec:      1.75MB

Running 10s test @ http://127.0.0.1:8081/pypika-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.16ms  326.46us  17.83ms   86.49%
    Req/Sec   814.57     26.27     0.86k    75.00%
  16219 requests in 10.01s, 2.52MB read
Requests/sec:   1620.93
Transfer/sec:    257.96KB
```

### Pypika + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/pypika-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    29.63ms    8.83ms  84.20ms   63.35%
    Req/Sec   169.20     24.08   242.00     70.50%
  3374 requests in 10.01s, 3.67MB read
Requests/sec:    337.17
Transfer/sec:    375.70KB

Running 10s test @ http://127.0.0.1:8081/pypika-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    30.85ms    8.24ms  94.38ms   63.72%
    Req/Sec   162.46     22.25   232.00     75.50%
  3239 requests in 10.01s, 515.45KB read
Requests/sec:    323.67
Transfer/sec:     51.51KB
```

### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.59ms    8.42ms 145.52ms   97.65%
    Req/Sec     0.89k   133.96     0.98k    95.00%
  17676 requests in 10.01s, 19.23MB read
Requests/sec:   1766.52
Transfer/sec:      1.92MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.52ms    1.33ms  38.94ms   98.50%
    Req/Sec     0.91k    47.60     0.99k    79.50%
  18201 requests in 10.00s, 2.83MB read
Requests/sec:   1819.51
Transfer/sec:    289.56KB
```

### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    14.75ms   35.00ms 434.39ms   96.90%
    Req/Sec   543.41     82.31   606.00     95.41%
  10615 requests in 10.01s, 11.55MB read
Requests/sec:   1060.74
Transfer/sec:      1.15MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.97ms    1.45ms  42.42ms   96.53%
    Req/Sec   631.29     30.94   696.00     86.00%
  12571 requests in 10.00s, 1.95MB read
Requests/sec:   1256.50
Transfer/sec:    199.96KB
```

### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.15ms    3.71ms  51.20ms   84.07%
    Req/Sec   385.01     33.25   444.00     85.00%
  7671 requests in 10.01s, 8.35MB read
Requests/sec:    766.31
Transfer/sec:    853.87KB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.13ms    2.32ms  45.48ms   79.27%
    Req/Sec   496.35     30.22   565.00     76.00%
  9886 requests in 10.01s, 1.54MB read
Requests/sec:    987.99
Transfer/sec:    157.27KB
```

### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.59ms    6.65ms  99.06ms   93.45%
    Req/Sec   475.34     96.44   600.00     75.50%
  9467 requests in 10.00s, 1.95MB read
  Socket errors: connect 0, read 9349, write 0, timeout 0
  Non-2xx or 3xx responses: 9057
Requests/sec:    946.44
Transfer/sec:    199.53KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     9.51ms    5.50ms  55.87ms   96.72%
    Req/Sec   530.90     67.63   606.00     87.50%
  10579 requests in 10.01s, 1.76MB read
  Socket errors: connect 0, read 10579, write 0, timeout 0
  Non-2xx or 3xx responses: 10579
Requests/sec:   1057.11
Transfer/sec:    179.63KB
```

### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.05ms    1.85ms  33.33ms   99.08%
    Req/Sec     5.47k   293.22     5.83k    92.00%
  108878 requests in 10.00s, 15.99MB read
  Non-2xx or 3xx responses: 108878
Requests/sec:  10886.92
Transfer/sec:      1.60MB

Running 10s test @ http://127.0.0.1:8081/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.25ms    1.54ms  33.79ms   99.37%
    Req/Sec     4.27k   334.38     8.30k    96.52%
  85395 requests in 10.10s, 12.54MB read
  Non-2xx or 3xx responses: 85395
Requests/sec:   8455.20
Transfer/sec:      1.24MB
```
