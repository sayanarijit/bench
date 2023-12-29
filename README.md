```bash
➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/piccolo
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.63s   102.31ms   1.96s    81.67%
    Req/Sec     6.96      7.91    40.00     85.71%
  120 requests in 10.02s, 29.88KB read
Requests/sec:     11.98
Transfer/sec:      2.98KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/peewee -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/peewee
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    32.01ms   15.15ms 268.19ms   95.32%
    Req/Sec   161.06     25.25   250.00     79.75%
  6427 requests in 10.01s, 1.56MB read
Requests/sec:    641.99
Transfer/sec:    159.87KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    51.59ms   92.25ms 712.65ms   94.87%
    Req/Sec   158.20     23.74   191.00     95.24%
  5980 requests in 10.01s, 1.45MB read
Requests/sec:    597.43
Transfer/sec:    148.77KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2 -c 20 -t 4
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    40.34ms   13.24ms 112.25ms   79.53%
    Req/Sec   124.82     22.02   180.00     67.42%
  4973 requests in 10.01s, 1.21MB read
Requests/sec:    496.66
Transfer/sec:    123.68KB
```
