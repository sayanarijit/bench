
### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   693.51ms  522.90ms   2.00s    55.08%
    Req/Sec   194.55     75.45   505.00     69.18%
  11146 requests in 10.04s, 17.38MB read
  Socket errors: connect 0, read 0, write 0, timeout 825
Requests/sec:   1110.68
Transfer/sec:      1.73MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   516.74ms  460.62ms   2.00s    54.00%
    Req/Sec   320.97    127.90   760.00     68.24%
  19039 requests in 10.03s, 2.97MB read
  Socket errors: connect 0, read 0, write 0, timeout 265
Requests/sec:   1898.75
Transfer/sec:    303.43KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   791.36ms  540.79ms   2.00s    61.46%
    Req/Sec   171.12     84.14   570.00     72.33%
  9819 requests in 10.04s, 15.31MB read
  Socket errors: connect 0, read 0, write 0, timeout 754
Requests/sec:    978.07
Transfer/sec:      1.53MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   599.52ms  499.92ms   2.00s    49.35%
    Req/Sec   247.35     91.11   696.00     66.50%
  14730 requests in 10.04s, 2.30MB read
  Socket errors: connect 0, read 0, write 0, timeout 469
Requests/sec:   1466.95
Transfer/sec:    234.42KB
```


### Pypika + aiopg

```
Running 10s test @ http://127.0.0.1:8081/pypika-aiopg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.10s   176.03ms   2.00s    91.35%
    Req/Sec   146.37     68.79   424.00     67.02%
  8362 requests in 10.03s, 13.04MB read
  Socket errors: connect 0, read 0, write 0, timeout 227
Requests/sec:    833.39
Transfer/sec:      1.30MB

Running 10s test @ http://127.0.0.1:8081/pypika-aiopg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   808.87ms  176.64ms   1.67s    91.78%
    Req/Sec   219.66    101.03   600.00     72.61%
  11829 requests in 10.04s, 1.85MB read
Requests/sec:   1178.48
Transfer/sec:    188.33KB
```


### Pypika + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/pypika-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.13s   273.35ms   1.90s    80.36%
    Req/Sec   167.34    117.78   510.00     63.26%
  8261 requests in 10.04s, 1.98MB read
  Socket errors: connect 0, read 7811, write 0, timeout 6
  Non-2xx or 3xx responses: 7826
Requests/sec:    822.67
Transfer/sec:    201.60KB

Running 10s test @ http://127.0.0.1:8081/pypika-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.18s   275.89ms   1.88s    85.77%
    Req/Sec   163.56    112.87   490.00     55.76%
  7575 requests in 10.04s, 1.25MB read
  Socket errors: connect 0, read 7129, write 0, timeout 260
  Non-2xx or 3xx responses: 7132
Requests/sec:    754.52
Transfer/sec:    127.76KB
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   828.78ms  582.58ms   2.00s    60.92%
    Req/Sec   159.22     79.28   460.00     70.23%
  9023 requests in 10.04s, 14.07MB read
  Socket errors: connect 0, read 0, write 0, timeout 847
Requests/sec:    899.08
Transfer/sec:      1.40MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   604.76ms  506.59ms   2.00s    49.83%
    Req/Sec   225.15    100.17   580.00     66.78%
  13450 requests in 10.03s, 2.10MB read
  Socket errors: connect 0, read 0, write 0, timeout 753
Requests/sec:   1340.85
Transfer/sec:    214.27KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.06s   746.15ms   2.00s    64.23%
    Req/Sec    94.44     47.82   270.00     69.42%
  5068 requests in 10.05s, 7.90MB read
  Socket errors: connect 0, read 0, write 0, timeout 1339
Requests/sec:    504.24
Transfer/sec:    805.10KB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   673.38ms  636.76ms   2.00s    46.30%
    Req/Sec   158.15     76.52   484.00     67.69%
  9298 requests in 10.03s, 1.45MB read
  Socket errors: connect 0, read 0, write 0, timeout 1239
Requests/sec:    927.26
Transfer/sec:    148.18KB
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
  0 requests in 10.07s, 0.00B read
Requests/sec:      0.00
Transfer/sec:       0.00B
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.43s   207.89ms   2.00s    79.90%
    Req/Sec   114.35     64.71   320.00     69.89%
  6432 requests in 10.03s, 1.15MB read
  Socket errors: connect 0, read 6431, write 0, timeout 60
  Non-2xx or 3xx responses: 6371
Requests/sec:    641.20
Transfer/sec:    117.63KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.05s   183.61ms   2.00s    89.37%
    Req/Sec   165.85     68.69   430.00     76.29%
  8329 requests in 10.04s, 1.38MB read
  Socket errors: connect 0, read 8328, write 0, timeout 558
  Non-2xx or 3xx responses: 8329
Requests/sec:    829.74
Transfer/sec:    140.99KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    60.92ms   55.53ms   1.99s    99.58%
    Req/Sec     0.99k   335.91     2.01k    63.50%
  59460 requests in 10.04s, 8.73MB read
  Socket errors: connect 0, read 0, write 0, timeout 133
  Non-2xx or 3xx responses: 59460
Requests/sec:   5922.01
Transfer/sec:      0.87MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    43.72ms   84.95ms   2.00s    98.88%
    Req/Sec     1.28k   551.98     4.13k    74.58%
  75963 requests in 10.04s, 11.16MB read
  Socket errors: connect 0, read 0, write 0, timeout 207
  Non-2xx or 3xx responses: 75963
Requests/sec:   7563.59
Transfer/sec:      1.11MB
```

