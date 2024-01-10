
### Dict

```
Running 10s test @ http://127.0.0.1:8081/dict
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.68ms  196.92us  18.25ms   93.97%
    Req/Sec     0.88k    19.65     0.91k    49.00%
  17499 requests in 10.01s, 41.35MB read
Requests/sec:   1748.66
Transfer/sec:      4.13MB

Running 10s test @ http://127.0.0.1:8081/dict
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.38ms  145.37us   7.27ms   88.88%
    Req/Sec     3.57k    35.29     3.67k    75.00%
  71140 requests in 10.00s, 13.72MB read
Requests/sec:   7112.77
Transfer/sec:      1.37MB
```


### Dataclass

```
Running 10s test @ http://127.0.0.1:8081/dataclass
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.53ms  141.81us  11.36ms   91.11%
    Req/Sec     1.96k    24.40     2.02k    84.00%
  39050 requests in 10.01s, 92.28MB read
Requests/sec:   3902.89
Transfer/sec:      9.22MB

Running 10s test @ http://127.0.0.1:8081/dataclass
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.35ms  135.17us   7.11ms   89.82%
    Req/Sec     3.66k    32.19     3.74k    73.50%
  72839 requests in 10.00s, 14.05MB read
Requests/sec:   7281.57
Transfer/sec:      1.40MB
```


### Pydantic

```
Running 10s test @ http://127.0.0.1:8081/pydantic
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.60ms  164.00us  11.21ms   91.34%
    Req/Sec     1.92k    20.56     1.99k    80.00%
  38131 requests in 10.00s, 90.11MB read
Requests/sec:   3811.39
Transfer/sec:      9.01MB

Running 10s test @ http://127.0.0.1:8081/pydantic
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.38ms  144.23us   7.24ms   89.69%
    Req/Sec     3.56k    42.71     3.68k    71.50%
  70850 requests in 10.00s, 13.67MB read
Requests/sec:   7083.85
Transfer/sec:      1.37MB
```


### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.30ms    1.73ms  38.17ms   98.43%
    Req/Sec     1.20k    99.10     2.28k    96.52%
  23911 requests in 10.10s, 27.82MB read
Requests/sec:   2367.33
Transfer/sec:      2.75MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.67ms    1.20ms  37.13ms   99.61%
    Req/Sec     1.38k    62.15     1.52k    79.50%
  27562 requests in 10.00s, 4.28MB read
Requests/sec:   2755.36
Transfer/sec:    438.49KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.15ms    1.76ms  38.94ms   99.26%
    Req/Sec     0.99k    54.30     1.09k    92.00%
  19758 requests in 10.00s, 22.99MB read
Requests/sec:   1975.36
Transfer/sec:      2.30MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.90ms  357.23us   9.24ms   70.75%
    Req/Sec     1.02k    32.16     1.13k    72.00%
  20373 requests in 10.00s, 3.17MB read
Requests/sec:   2036.82
Transfer/sec:    324.14KB
```


### Pgmini + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.44ms    1.53ms  39.39ms   99.20%
    Req/Sec     0.94k    57.30     0.98k    98.00%
  18616 requests in 10.00s, 21.66MB read
Requests/sec:   1861.30
Transfer/sec:      2.17MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.50ms    1.38ms  40.44ms   99.47%
    Req/Sec     0.92k    40.74     0.96k    97.00%
  18331 requests in 10.00s, 2.85MB read
Requests/sec:   1832.52
Transfer/sec:    291.63KB
```


### Pgmini + aiopg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.47ms    1.54ms  39.75ms   99.23%
    Req/Sec     0.93k    63.03     0.99k    92.00%
  18526 requests in 10.01s, 21.55MB read
Requests/sec:   1851.62
Transfer/sec:      2.15MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.49ms    1.35ms  39.48ms   99.51%
    Req/Sec     0.92k    40.48     0.98k    93.00%
  18359 requests in 10.00s, 2.85MB read
Requests/sec:   1835.17
Transfer/sec:    292.05KB
```


### Pgmini + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    53.83ms    8.73ms 123.19ms   73.55%
    Req/Sec    92.92      9.92   130.00     78.50%
  1855 requests in 10.01s, 2.16MB read
Requests/sec:    185.40
Transfer/sec:    220.89KB

Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    54.86ms    9.02ms 175.04ms   76.00%
    Req/Sec    91.55      9.11   111.00     66.67%
  1819 requests in 10.01s, 289.46KB read
Requests/sec:    181.73
Transfer/sec:     28.92KB
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.73ms    2.15ms  39.56ms   98.94%
    Req/Sec     0.90k    57.26     0.99k    92.50%
  17858 requests in 10.01s, 20.78MB read
Requests/sec:   1784.85
Transfer/sec:      2.08MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.46ms  370.30us  10.83ms   70.39%
    Req/Sec     0.92k    27.35     1.02k    70.00%
  18284 requests in 10.00s, 2.84MB read
Requests/sec:   1827.51
Transfer/sec:    290.83KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.97ms   25.84ms 318.07ms   97.28%
    Req/Sec   541.57     60.23   600.00     94.90%
  10601 requests in 10.01s, 12.33MB read
Requests/sec:   1059.28
Transfer/sec:      1.23MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.89ms    1.90ms  42.26ms   98.97%
    Req/Sec   641.81     41.33   750.00     78.50%
  12782 requests in 10.00s, 1.99MB read
Requests/sec:   1277.69
Transfer/sec:    203.33KB
```


### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.07ms    3.97ms  51.27ms   91.21%
    Req/Sec   389.48     30.83   450.00     80.50%
  7758 requests in 10.01s, 9.03MB read
Requests/sec:    775.41
Transfer/sec:      0.90MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     9.93ms    1.67ms  26.39ms   70.53%
    Req/Sec   504.63     22.56   565.00     69.00%
  10047 requests in 10.00s, 1.56MB read
Requests/sec:   1004.32
Transfer/sec:    159.87KB
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.49ms    7.44ms  97.02ms   94.14%
    Req/Sec   408.51     65.30   494.00     75.00%
  8137 requests in 10.00s, 1.44MB read
  Socket errors: connect 0, read 8044, write 0, timeout 0
  Non-2xx or 3xx responses: 8045
Requests/sec:    813.30
Transfer/sec:    147.59KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    11.74ms    6.60ms  62.43ms   95.93%
    Req/Sec   429.34     61.24   500.00     88.00%
  8556 requests in 10.01s, 1.42MB read
  Socket errors: connect 0, read 8555, write 0, timeout 0
  Non-2xx or 3xx responses: 8556
Requests/sec:    855.06
Transfer/sec:    145.29KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/peewee
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.61ms    7.52ms  93.47ms   93.53%
    Req/Sec   403.77     67.08   494.00     76.50%
  8042 requests in 10.00s, 1.45MB read
  Socket errors: connect 0, read 7923, write 0, timeout 0
  Non-2xx or 3xx responses: 7923
Requests/sec:    804.07
Transfer/sec:    148.78KB

Running 10s test @ http://127.0.0.1:8081/peewee
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    11.89ms    6.88ms  62.50ms   95.57%
    Req/Sec   427.62     58.37   505.00     87.50%
  8516 requests in 10.00s, 1.41MB read
  Socket errors: connect 0, read 8515, write 0, timeout 0
  Non-2xx or 3xx responses: 8516
Requests/sec:    851.26
Transfer/sec:    144.65KB
```

