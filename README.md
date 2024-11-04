# Design question 

Facebook generates events at a rate of 10^5 'like' events per second. 
 Design a system that can handle this volume and produce a report of the top 1,000 users based on the number 
 of 'likes' they've received in the last hour, with a resolution of 1 minute.

 A possible answer.
 
 The Load Balancer (possibly using WebSocket) manages incoming events and routes them to the appropriate pod based on the user GUID. 
 Each pod, running an Accumulator, maintains a sliding window of 60 minutes, aggregating 'like' counts in 1-minute intervals. 
 The accumulator stores these totals in a sharded PostgreSQL (PSQL) database, with shards organized by user GUID.

A separate Report pod handles GET report queries. When queried, the Report pod requests the top 1,000 users from each PSQL shard, 
merges and sorts these results, and returns the overall top 1,000 users.

Follow up questions: 

* Memory constraint in the accumulators: accumulator can keep only one minute counter, and the sliding window is in the PSQL
* What if an accumulator pod fails: backup for the last minute counter in Redis?
