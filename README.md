
### No Response Model

```
Running 10s test @ http://127.0.0.1:8081/no-resp-model
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.61ms  225.94us  18.97ms   94.70%
    Req/Sec     0.89k    15.94     0.93k    68.50%
  17736 requests in 10.01s, 41.91MB read
Requests/sec:   1771.87
Transfer/sec:      4.19MB

Running 10s test @ http://127.0.0.1:8081/no-resp-model
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.38ms  136.97us   6.79ms   89.34%
    Req/Sec     3.57k    30.86     3.66k    79.00%
  71059 requests in 10.00s, 13.71MB read
Requests/sec:   7105.18
Transfer/sec:      1.37MB
```


### Dict

```
Running 10s test @ http://127.0.0.1:8081/dict
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.22ms  181.78us   9.55ms   89.78%
    Req/Sec     2.23k    24.93     2.29k    75.00%
  44494 requests in 10.01s, 105.15MB read
Requests/sec:   4446.43
Transfer/sec:     10.51MB

Running 10s test @ http://127.0.0.1:8081/dict
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.31ms  130.71us   6.87ms   88.92%
    Req/Sec     3.73k    36.90     3.84k    73.50%
  74333 requests in 10.00s, 14.34MB read
Requests/sec:   7431.30
Transfer/sec:      1.43MB
```


### Dataclass

```
Running 10s test @ http://127.0.0.1:8081/dataclass
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.59ms  164.27us  10.93ms   91.08%
    Req/Sec     1.92k    23.13     1.97k    80.50%
  38174 requests in 10.01s, 90.21MB read
Requests/sec:   3814.84
Transfer/sec:      9.02MB

Running 10s test @ http://127.0.0.1:8081/dataclass
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.38ms  119.66us   6.42ms   90.96%
    Req/Sec     3.57k    39.16     3.68k    74.00%
  70969 requests in 10.00s, 13.69MB read
Requests/sec:   7094.36
Transfer/sec:      1.37MB
```


### Pydantic

```
Running 10s test @ http://127.0.0.1:8081/pydantic
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.63ms  161.46us   9.32ms   90.30%
    Req/Sec     1.89k    21.05     1.93k    68.00%
  37683 requests in 10.01s, 89.05MB read
Requests/sec:   3765.51
Transfer/sec:      8.90MB

Running 10s test @ http://127.0.0.1:8081/pydantic
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.38ms  112.33us   5.67ms   90.35%
    Req/Sec     3.54k    31.22     3.61k    72.00%
  70406 requests in 10.00s, 13.58MB read
Requests/sec:   7039.19
Transfer/sec:      1.36MB
```


### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.37ms    2.11ms  38.30ms   98.95%
    Req/Sec     1.19k    71.41     1.30k    91.00%
  23678 requests in 10.00s, 27.55MB read
Requests/sec:   2367.08
Transfer/sec:      2.75MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.64ms  233.29us   6.93ms   70.92%
    Req/Sec     1.38k    32.58     1.49k    67.50%
  27418 requests in 10.00s, 4.26MB read
Requests/sec:   2741.26
Transfer/sec:    436.25KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.17ms    2.15ms  39.43ms   98.90%
    Req/Sec     1.00k    52.13     1.08k    86.00%
  19858 requests in 10.00s, 23.10MB read
Requests/sec:   1985.22
Transfer/sec:      2.31MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.92ms  364.15us  10.77ms   71.29%
    Req/Sec     1.02k    37.99     1.14k    65.50%
  20300 requests in 10.01s, 3.15MB read
Requests/sec:   2028.95
Transfer/sec:    322.89KB
```


### Pgmini + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.51ms    1.66ms  39.58ms   99.26%
    Req/Sec     0.93k    56.68     0.99k    97.00%
  18428 requests in 10.00s, 21.44MB read
Requests/sec:   1842.28
Transfer/sec:      2.14MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.42ms    1.37ms  39.85ms   99.44%
    Req/Sec     0.94k    38.04     0.98k    96.00%
  18626 requests in 10.00s, 2.89MB read
Requests/sec:   1861.94
Transfer/sec:    296.31KB
```


### Pgmini + aiopg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.83ms    1.66ms  42.05ms   99.22%
    Req/Sec     0.87k    49.34     0.93k    95.50%
  17389 requests in 10.01s, 20.23MB read
Requests/sec:   1738.01
Transfer/sec:      2.02MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.67ms    1.40ms  39.73ms   99.48%
    Req/Sec     0.89k    50.89     0.96k    78.50%
  17777 requests in 10.00s, 2.76MB read
Requests/sec:   1777.21
Transfer/sec:    282.82KB
```


### Pgmini + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    55.65ms    9.65ms 137.06ms   82.41%
    Req/Sec    89.81     11.85   120.00     88.50%
  1794 requests in 10.01s, 2.09MB read
Requests/sec:    179.25
Transfer/sec:    213.56KB

Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    81.71ms   14.57ms 200.56ms   77.58%
    Req/Sec    61.43     14.25   101.00     74.24%
  1221 requests in 10.01s, 194.30KB read
Requests/sec:    121.99
Transfer/sec:     19.41KB
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     8.86ms    5.54ms 101.55ms   99.06%
    Req/Sec   592.16     73.37     0.85k    89.00%
  11794 requests in 10.01s, 13.72MB read
Requests/sec:   1178.70
Transfer/sec:      1.37MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.66ms    1.27ms  38.58ms   99.57%
    Req/Sec     0.89k    42.57     1.01k    73.50%
  17789 requests in 10.00s, 2.76MB read
Requests/sec:   1778.10
Transfer/sec:    282.97KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    23.95ms   54.11ms 517.91ms   95.93%
    Req/Sec   362.22     56.04   505.00     89.58%
  6961 requests in 10.01s, 8.10MB read
Requests/sec:    695.65
Transfer/sec:    828.80KB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.95ms    1.95ms  43.16ms   98.51%
    Req/Sec   637.20     42.68   730.00     81.50%
  12688 requests in 10.00s, 1.97MB read
Requests/sec:   1268.48
Transfer/sec:    201.87KB
```


### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    21.80ms    6.57ms  91.35ms   86.58%
    Req/Sec   231.59     34.55   290.00     78.50%
  4614 requests in 10.01s, 5.37MB read
Requests/sec:    461.12
Transfer/sec:    549.38KB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    15.71ms    2.75ms  29.21ms   71.46%
    Req/Sec   319.01     18.45   363.00     63.50%
  6355 requests in 10.01s, 0.99MB read
Requests/sec:    634.77
Transfer/sec:    101.04KB
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    19.20ms   12.22ms 162.87ms   93.33%
    Req/Sec   266.48     59.83   353.00     75.50%
  5309 requests in 10.01s, 0.97MB read
  Socket errors: connect 0, read 5221, write 0, timeout 0
  Non-2xx or 3xx responses: 5222
Requests/sec:    530.59
Transfer/sec:     99.04KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    17.37ms    8.81ms  92.97ms   91.84%
    Req/Sec   288.17     54.63   414.00     72.00%
  5739 requests in 10.00s, 0.95MB read
  Socket errors: connect 0, read 5631, write 0, timeout 0
  Non-2xx or 3xx responses: 5633
Requests/sec:    573.79
Transfer/sec:     97.38KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/peewee
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    20.26ms   11.96ms 156.19ms   93.23%
    Req/Sec   250.90     47.22   340.00     73.50%
  4999 requests in 10.01s, 0.96MB read
  Socket errors: connect 0, read 4873, write 0, timeout 0
  Non-2xx or 3xx responses: 4873
Requests/sec:    499.64
Transfer/sec:     97.76KB

Running 10s test @ http://127.0.0.1:8081/peewee
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    15.07ms    8.66ms  90.12ms   93.17%
    Req/Sec   335.01     86.06   484.00     65.50%
  6673 requests in 10.01s, 1.11MB read
  Socket errors: connect 0, read 6608, write 0, timeout 0
  Non-2xx or 3xx responses: 6608
Requests/sec:    666.97
Transfer/sec:    113.26KB
```

