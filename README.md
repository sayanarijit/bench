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

### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   500.91ms  458.94ms   1.98s    40.85%
    Req/Sec   311.09    203.79     1.11k    70.50%
  18128 requests in 10.04s, 19.33MB read
  Socket errors: connect 0, read 0, write 0, timeout 475
Requests/sec:   1805.49
Transfer/sec:      1.93MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   511.98ms  461.34ms   2.00s    53.27%
    Req/Sec   322.31    115.71   680.00     69.78%
  19241 requests in 10.03s, 3.00MB read
  Socket errors: connect 0, read 0, write 0, timeout 246
Requests/sec:   1918.88
Transfer/sec:    306.64KB
```

### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   555.75ms  493.59ms   2.00s    43.15%
    Req/Sec   275.34     95.24   565.00     70.92%
  16155 requests in 10.03s, 17.22MB read
  Socket errors: connect 0, read 0, write 0, timeout 429
Requests/sec:   1610.44
Transfer/sec:      1.72MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   600.01ms  481.86ms   2.00s    50.36%
    Req/Sec   257.73     87.53   575.00     69.63%
  15317 requests in 10.03s, 2.39MB read
  Socket errors: connect 0, read 0, write 0, timeout 366
Requests/sec:   1526.83
Transfer/sec:    243.99KB
```

### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   864.45ms  570.19ms   2.00s    61.26%
    Req/Sec   165.77     71.70   424.00     68.96%
  9396 requests in 10.03s, 10.02MB read
  Socket errors: connect 0, read 0, write 0, timeout 583
Requests/sec:    937.23
Transfer/sec:      1.00MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   801.08ms  401.35ms   2.00s    75.68%
    Req/Sec   171.38     74.70   393.00     68.52%
  10179 requests in 10.04s, 1.59MB read
  Socket errors: connect 0, read 0, write 0, timeout 724
Requests/sec:   1013.54
Transfer/sec:    161.97KB
```

### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   991.35ms  230.79ms   1.99s    77.42%
    Req/Sec   143.44    106.93   520.00     74.04%
  8360 requests in 10.03s, 8.91MB read
  Socket errors: connect 0, read 0, write 0, timeout 409
Requests/sec:    833.23
Transfer/sec:      0.89MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   696.81ms  280.39ms   1.99s    76.21%
    Req/Sec   176.73     58.85   380.00     74.05%
  9839 requests in 10.03s, 1.53MB read
  Socket errors: connect 0, read 0, write 0, timeout 709
Requests/sec:    981.26
Transfer/sec:    156.20KB
```

### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   613.23ms  392.68ms   1.99s    64.25%
    Req/Sec   266.53    147.58     0.89k    72.38%
  15518 requests in 10.03s, 16.55MB read
  Socket errors: connect 0, read 0, write 0, timeout 109
Requests/sec:   1546.44
Transfer/sec:      1.65MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   606.79ms  404.06ms   2.00s    62.64%
    Req/Sec   258.02     93.10   560.00     68.39%
  15379 requests in 10.04s, 2.40MB read
  Socket errors: connect 0, read 0, write 0, timeout 267
Requests/sec:   1531.86
Transfer/sec:    244.80KB
```

### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   976.84ms  542.19ms   1.95s    61.61%
    Req/Sec   166.61    100.66   585.00     71.73%
  9624 requests in 10.03s, 3.72MB read
  Socket errors: connect 0, read 7269, write 0, timeout 0
  Non-2xx or 3xx responses: 7270
Requests/sec:    959.11
Transfer/sec:    379.24KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.21s   194.58ms   2.00s    91.42%
    Req/Sec   147.82     63.11   480.00     74.95%
  7693 requests in 10.03s, 1.28MB read
  Socket errors: connect 0, read 7615, write 0, timeout 137
  Non-2xx or 3xx responses: 7615
Requests/sec:    766.70
Transfer/sec:    130.20KB
```

### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    50.42ms   60.94ms   1.99s    99.50%
    Req/Sec     1.65k   429.98     2.94k    70.00%
  98481 requests in 10.04s, 14.46MB read
  Socket errors: connect 0, read 0, write 0, timeout 163
  Non-2xx or 3xx responses: 98481
Requests/sec:   9804.19
Transfer/sec:      1.44MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    42.08ms   85.39ms   2.00s    98.87%
    Req/Sec     1.39k   639.14     5.34k    78.02%
  82809 requests in 10.04s, 12.16MB read
  Socket errors: connect 0, read 0, write 0, timeout 213
  Non-2xx or 3xx responses: 82809
Requests/sec:   8244.54
Transfer/sec:      1.21MB
```
