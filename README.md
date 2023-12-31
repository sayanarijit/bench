### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   503.07ms  477.72ms   1.99s    39.91%
    Req/Sec   301.16    114.14   640.00     67.57%
  17715 requests in 10.03s, 18.89MB read
  Socket errors: connect 0, read 0, write 0, timeout 567
Requests/sec:   1766.05
Transfer/sec:      1.88MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   516.78ms  464.69ms   2.00s    52.20%
    Req/Sec   313.17    116.27   707.00     69.06%
  18673 requests in 10.04s, 2.91MB read
  Socket errors: connect 0, read 0, write 0, timeout 249
Requests/sec:   1860.21
Transfer/sec:    297.27KB
```

### SQLA + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   906.40ms  433.46ms   2.00s    76.89%
    Req/Sec   171.94    114.77   464.00     59.74%
  9510 requests in 10.04s, 10.14MB read
  Socket errors: connect 0, read 0, write 0, timeout 418
Requests/sec:    947.34
Transfer/sec:      1.01MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   766.07ms  474.45ms   2.00s    67.58%
    Req/Sec   176.39     76.73   590.00     72.20%
  10431 requests in 10.04s, 1.63MB read
  Socket errors: connect 0, read 0, write 0, timeout 770
Requests/sec:   1038.59
Transfer/sec:    165.97KB
```

### SQLA + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.00s   239.99ms   1.99s    77.32%
    Req/Sec   141.41     94.80   505.00     68.48%
  8170 requests in 10.03s, 8.71MB read
  Socket errors: connect 0, read 0, write 0, timeout 415
Requests/sec:    814.51
Transfer/sec:      0.87MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   692.27ms  279.85ms   2.00s    78.93%
    Req/Sec   175.54     70.26   484.00     75.76%
  9832 requests in 10.04s, 1.53MB read
  Socket errors: connect 0, read 0, write 0, timeout 708
Requests/sec:    979.49
Transfer/sec:    155.91KB
```

### SQLA + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   967.79ms  271.35ms   1.99s    78.54%
    Req/Sec   137.82    105.60   620.00     78.58%
  8102 requests in 10.03s, 8.64MB read
  Socket errors: connect 0, read 0, write 0, timeout 482
Requests/sec:    807.65
Transfer/sec:      0.86MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   695.57ms  273.70ms   1.99s    76.57%
    Req/Sec   174.49     59.96   363.00     71.82%
  9666 requests in 10.04s, 1.50MB read
  Socket errors: connect 0, read 0, write 0, timeout 715
Requests/sec:    962.75
Transfer/sec:    153.25KB
```

### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   607.23ms  391.33ms   1.99s    63.89%
    Req/Sec   269.03    115.97   696.00     71.53%
  15663 requests in 10.05s, 16.70MB read
  Socket errors: connect 0, read 0, write 0, timeout 128
Requests/sec:   1558.53
Transfer/sec:      1.66MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   608.88ms  405.10ms   2.00s    63.05%
    Req/Sec   257.71     82.01   470.00     69.28%
  15378 requests in 10.04s, 2.40MB read
  Socket errors: connect 0, read 0, write 0, timeout 262
Requests/sec:   1531.51
Transfer/sec:    244.74KB
```

### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   944.12ms  460.97ms   1.64s    64.17%
    Req/Sec   173.23     97.27   570.00     70.20%
  9810 requests in 10.03s, 3.16MB read
  Socket errors: connect 0, read 8107, write 0, timeout 0
  Non-2xx or 3xx responses: 8107
Requests/sec:    978.07
Transfer/sec:    322.72KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.12s   226.61ms   2.00s    90.79%
    Req/Sec   165.86     78.70   520.00     77.98%
  8352 requests in 10.04s, 1.38MB read
  Socket errors: connect 0, read 8201, write 0, timeout 55
  Non-2xx or 3xx responses: 8201
Requests/sec:    831.79
Transfer/sec:    141.19KB
```

### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    44.33ms   67.35ms   1.98s    99.37%
    Req/Sec     1.70k   496.32     3.30k    71.67%
  101349 requests in 10.04s, 14.88MB read
  Socket errors: connect 0, read 0, write 0, timeout 190
  Non-2xx or 3xx responses: 101349
Requests/sec:  10094.33
Transfer/sec:      1.48MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    40.96ms   83.35ms   1.99s    98.88%
    Req/Sec     1.43k   349.58     2.67k    71.19%
  85034 requests in 10.03s, 12.49MB read
  Socket errors: connect 0, read 0, write 0, timeout 220
  Non-2xx or 3xx responses: 85034
Requests/sec:   8474.90
Transfer/sec:      1.24MB
```
