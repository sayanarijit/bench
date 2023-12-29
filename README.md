```bash
 bench git:(main) ✗ wrk http://127.0.0.1:8081/piccolo
Running 10s test @ http://127.0.0.1:8081/piccolo
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   419.50ms   60.81ms 577.88ms   73.71%
    Req/Sec    13.07      6.43    30.00     57.01%
  232 requests in 10.01s, 57.77KB read
Requests/sec:     23.18
Transfer/sec:      5.77KB

Running 10s test @ http://127.0.0.1:8081/peewee
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    16.38ms    6.52ms 143.65ms   91.43%
    Req/Sec   311.02     31.27   363.00     78.00%
  6195 requests in 10.00s, 1.51MB read
Requests/sec:    619.25
Transfer/sec:    154.21KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-asyncpg
Running 10s test @ http://127.0.0.1:8081/sqla-asyncpg
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    47.21ms   65.66ms 571.99ms   90.48%
    Req/Sec   169.09    108.16   390.00     48.96%
  3265 requests in 10.01s, 813.06KB read
Requests/sec:    326.26
Transfer/sec:     81.25KB

➜  bench git:(main) ✗ wrk http://127.0.0.1:8081/sqla-psycopg2
Running 10s test @ http://127.0.0.1:8081/sqla-psycopg2
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.33ms    6.38ms  72.84ms   80.79%
    Req/Sec   275.78     32.53   330.00     69.50%
  5497 requests in 10.01s, 1.34MB read
Requests/sec:    549.30
Transfer/sec:    136.79KB
```
