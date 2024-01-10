
### Dict

```
Running 10s test @ http://127.0.0.1:8081/dict
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.91ms  237.91us  20.38ms   97.23%
    Req/Sec   845.96     14.48     0.87k    74.50%
  16844 requests in 10.01s, 39.81MB read
Requests/sec:   1683.18
Transfer/sec:      3.98MB

Running 10s test @ http://127.0.0.1:8081/dict
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.44ms  109.57us   3.73ms   90.37%
    Req/Sec     3.39k    27.49     3.46k    71.00%
  67551 requests in 10.00s, 13.03MB read
Requests/sec:   6753.85
Transfer/sec:      1.30MB
```


### Dataclass

```
Running 10s test @ http://127.0.0.1:8081/dataclass
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.83ms  200.49us  10.64ms   90.27%
    Req/Sec     1.76k    16.60     1.80k    79.50%
  34957 requests in 10.00s, 82.61MB read
Requests/sec:   3494.88
Transfer/sec:      8.26MB

Running 10s test @ http://127.0.0.1:8081/dataclass
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.42ms  129.37us   6.65ms   90.33%
    Req/Sec     3.46k    36.26     3.55k    72.00%
  68884 requests in 10.00s, 13.29MB read
Requests/sec:   6885.81
Transfer/sec:      1.33MB
```


### Pydantic

```
Running 10s test @ http://127.0.0.1:8081/pydantic
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.88ms  175.38us  11.95ms   91.68%
    Req/Sec     1.73k    18.34     1.77k    64.00%
  34446 requests in 10.01s, 81.40MB read
Requests/sec:   3442.47
Transfer/sec:      8.14MB

Running 10s test @ http://127.0.0.1:8081/pydantic
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.43ms  122.97us   7.25ms   90.90%
    Req/Sec     3.42k    39.45     3.51k    71.50%
  68044 requests in 10.00s, 13.13MB read
Requests/sec:   6803.35
Transfer/sec:      1.31MB
```


### Asyncpg

```
Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.78ms    2.71ms  38.93ms   98.40%
    Req/Sec     1.11k    83.27     1.19k    93.50%
  22017 requests in 10.00s, 25.62MB read
Requests/sec:   2201.00
Transfer/sec:      2.56MB

Running 10s test @ http://127.0.0.1:8081/asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.80ms  266.98us   8.07ms   70.80%
    Req/Sec     1.32k    36.08     1.43k    70.50%
  26302 requests in 10.00s, 4.09MB read
Requests/sec:   2629.81
Transfer/sec:    418.51KB
```


### Pypika + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.54ms    2.14ms  39.37ms   99.01%
    Req/Sec     0.93k    49.42     1.01k    85.50%
  18502 requests in 10.00s, 21.53MB read
Requests/sec:   1849.45
Transfer/sec:      2.15MB

Running 10s test @ http://127.0.0.1:8081/pypika-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.05ms  354.06us   9.90ms   70.40%
    Req/Sec     0.99k    36.78     1.11k    72.00%
  19784 requests in 10.00s, 3.07MB read
Requests/sec:   1977.55
Transfer/sec:    314.71KB
```


### Pgmini + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.94ms    1.69ms  40.58ms   99.21%
    Req/Sec     0.86k    59.16     0.91k    95.00%
  17058 requests in 10.01s, 19.85MB read
Requests/sec:   1704.93
Transfer/sec:      1.98MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.13ms    1.41ms  40.47ms   99.44%
    Req/Sec   825.21     38.46     0.88k    87.50%
  16431 requests in 10.00s, 2.55MB read
Requests/sec:   1642.64
Transfer/sec:    261.41KB
```


### Pgmini + aiopg

```
Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.12ms  435.47us  15.79ms   83.77%
    Req/Sec   820.56     32.27     0.90k    72.00%
  16343 requests in 10.01s, 19.01MB read
Requests/sec:   1633.18
Transfer/sec:      1.90MB

Running 10s test @ http://127.0.0.1:8081/pgmini-aiopg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.65ms    1.35ms  40.03ms   99.40%
    Req/Sec     0.89k    54.43     1.02k    79.00%
  17804 requests in 10.01s, 2.77MB read
Requests/sec:   1779.23
Transfer/sec:    283.15KB
```


### Pgmini + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    54.63ms    8.60ms 109.00ms   72.59%
    Req/Sec    91.52     10.65   121.00     77.00%
  1828 requests in 10.01s, 2.13MB read
Requests/sec:    182.63
Transfer/sec:    217.59KB

Running 10s test @ http://127.0.0.1:8081/pgmini-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    55.44ms    9.91ms 161.93ms   78.25%
    Req/Sec    90.37     10.71   111.00     95.48%
  1799 requests in 10.01s, 286.29KB read
Requests/sec:    179.69
Transfer/sec:     28.60KB
```


### Piccolo

```
Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.35ms    2.32ms  41.54ms   98.83%
    Req/Sec   809.53     49.33     0.87k    91.50%
  16116 requests in 10.00s, 18.75MB read
Requests/sec:   1610.90
Transfer/sec:      1.87MB

Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.76ms  391.03us  12.16ms   69.76%
    Req/Sec     0.87k    29.23     0.94k    71.00%
  17338 requests in 10.00s, 2.69MB read
Requests/sec:   1733.38
Transfer/sec:    275.85KB
```


### SQLAlchemy + asyncpg

```
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.88ms   26.73ms 325.39ms   97.22%
    Req/Sec   501.71     58.22   560.00     94.39%
  9815 requests in 10.01s, 11.42MB read
Requests/sec:    980.73
Transfer/sec:      1.14MB

Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     8.31ms    1.50ms  43.24ms   98.12%
    Req/Sec   606.59     30.71   670.00     75.00%
  12080 requests in 10.01s, 1.88MB read
Requests/sec:   1207.34
Transfer/sec:    192.14KB
```


### SQLAlchemy + psycopg2

```
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.93ms    4.31ms  55.21ms   91.35%
    Req/Sec   365.65     35.07   420.00     85.50%
  7286 requests in 10.00s, 8.48MB read
Requests/sec:    728.31
Transfer/sec:    867.71KB

Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.37ms    1.75ms  20.04ms   71.56%
    Req/Sec   483.10     22.12   540.00     66.00%
  9625 requests in 10.01s, 1.50MB read
Requests/sec:    962.00
Transfer/sec:    153.13KB
```


### Peewee no pool

```
Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.72ms    7.28ms  86.89ms   94.49%
    Req/Sec   366.15     53.43   440.00     78.00%
  7292 requests in 10.01s, 1.28MB read
  Socket errors: connect 0, read 7222, write 0, timeout 0
  Non-2xx or 3xx responses: 7222
Requests/sec:    728.74
Transfer/sec:    130.97KB

Running 10s test @ http://127.0.0.1:8081/peewee-no-pool
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.28ms    6.70ms  66.40ms   96.18%
    Req/Sec   375.79     50.88   444.00     88.00%
  7482 requests in 10.00s, 1.24MB read
  Socket errors: connect 0, read 7481, write 0, timeout 0
  Non-2xx or 3xx responses: 7482
Requests/sec:    748.01
Transfer/sec:    127.10KB
```


### Peewee

```
Running 10s test @ http://127.0.0.1:8081/peewee
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    14.04ms    7.62ms  93.55ms   93.36%
    Req/Sec   358.57     57.45   444.00     77.50%
  7145 requests in 10.01s, 1.29MB read
  Socket errors: connect 0, read 7044, write 0, timeout 0
  Non-2xx or 3xx responses: 7044
Requests/sec:    714.13
Transfer/sec:    131.66KB

Running 10s test @ http://127.0.0.1:8081/peewee
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.84ms    7.32ms  75.47ms   94.40%
    Req/Sec   362.44     55.53   444.00     86.50%
  7221 requests in 10.01s, 1.20MB read
  Socket errors: connect 0, read 7158, write 0, timeout 0
  Non-2xx or 3xx responses: 7160
Requests/sec:    721.59
Transfer/sec:    122.55KB
```

