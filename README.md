
### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   485.93ms  474.36ms   2.00s    37.77%
    Req/Sec   309.79    111.99   710.00     69.27%
  18213 requests in 10.03s, 19.42MB read
  Socket errors: connect 0, read 0, write 0, timeout 625
Requests/sec:   1816.13
Transfer/sec:      1.94MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   505.33ms  460.93ms   2.00s    53.63%
    Req/Sec   326.37    113.95   740.00     67.61%
  19482 requests in 10.04s, 3.04MB read
  Socket errors: connect 0, read 0, write 0, timeout 268
Requests/sec:   1940.12
Transfer/sec:    310.04KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   557.21ms  500.69ms   2.00s    42.22%
    Req/Sec   274.44    166.52   797.00     64.96%
  16038 requests in 10.04s, 17.10MB read
  Socket errors: connect 0, read 0, write 0, timeout 467
Requests/sec:   1598.01
Transfer/sec:      1.70MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   586.90ms  482.24ms   2.00s    49.62%
    Req/Sec   259.68    105.62   575.00     67.95%
  15500 requests in 10.02s, 2.42MB read
  Socket errors: connect 0, read 0, write 0, timeout 388
Requests/sec:   1546.44
Transfer/sec:    247.13KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   886.27ms  545.82ms   2.00s    65.04%
    Req/Sec   164.98     70.81   410.00     70.37%
  9356 requests in 10.04s, 9.98MB read
  Socket errors: connect 0, read 0, write 0, timeout 562
Requests/sec:    931.57
Transfer/sec:      0.99MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   803.64ms  438.12ms   2.00s    73.69%
    Req/Sec   173.38     66.13   400.00     66.84%
  10189 requests in 10.03s, 1.59MB read
  Socket errors: connect 0, read 0, write 0, timeout 743
Requests/sec:   1015.70
Transfer/sec:    162.31KB
```


### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.04s   217.91ms   1.99s    78.80%
    Req/Sec   142.58    123.73   616.00     76.23%
  8250 requests in 10.04s, 8.80MB read
  Socket errors: connect 0, read 0, write 0, timeout 349
Requests/sec:    821.71
Transfer/sec:      0.88MB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   704.95ms  274.06ms   2.00s    79.89%
    Req/Sec   173.65     64.68   444.00     73.45%
  9614 requests in 10.04s, 1.49MB read
  Socket errors: connect 0, read 0, write 0, timeout 704
Requests/sec:    957.57
Transfer/sec:    152.43KB
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   615.36ms  393.89ms   2.00s    65.01%
    Req/Sec   262.00     98.53   515.00     66.44%
  15374 requests in 10.03s, 16.39MB read
  Socket errors: connect 0, read 0, write 0, timeout 147
Requests/sec:   1533.29
Transfer/sec:      1.63MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   611.77ms  415.91ms   2.00s    61.69%
    Req/Sec   254.19     92.89   515.00     71.19%
  15135 requests in 10.03s, 2.36MB read
  Socket errors: connect 0, read 0, write 0, timeout 286
Requests/sec:   1509.26
Transfer/sec:    241.18KB
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   929.56ms  641.68ms   2.00s    56.54%
    Req/Sec   170.67     89.90   545.00     70.19%
  9987 requests in 10.03s, 4.44MB read
  Socket errors: connect 0, read 6894, write 0, timeout 123
  Non-2xx or 3xx responses: 6895
Requests/sec:    995.54
Transfer/sec:    453.31KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.12s   185.46ms   2.00s    91.67%
    Req/Sec   158.76     75.29   595.00     80.52%
  8274 requests in 10.04s, 1.37MB read
  Socket errors: connect 0, read 8230, write 0, timeout 135
  Non-2xx or 3xx responses: 8230
Requests/sec:    824.41
Transfer/sec:    140.04KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    52.12ms   58.56ms   1.97s    99.53%
    Req/Sec     1.64k   432.97     2.91k    67.83%
  97740 requests in 10.04s, 14.35MB read
  Socket errors: connect 0, read 0, write 0, timeout 157
  Non-2xx or 3xx responses: 97740
Requests/sec:   9739.01
Transfer/sec:      1.43MB

Running 10s test @ http://127.0.0.1:8081/
  6 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    41.45ms   83.19ms   1.99s    98.90%
    Req/Sec     1.40k   523.03     4.15k    70.97%
  82876 requests in 10.03s, 12.17MB read
  Socket errors: connect 0, read 0, write 0, timeout 216
  Non-2xx or 3xx responses: 82876
Requests/sec:   8261.62
Transfer/sec:      1.21MB
```

