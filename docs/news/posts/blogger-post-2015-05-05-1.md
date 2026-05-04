---
date: 2015-05-05
---

# Network downtime (resolved)
Around 1:15am Tuesday morning, we starting experiencing high latency on our internal network. The high latency resulted in NFS reads/writes blocking for periods of several seconds, causing a backlog of processes on the web server and other servers. This resulted in timeouts when trying to access web pages, and eventually complete downtime when we took the servers offline.<br />
<br />
We had four different volunteer staff in the lab troubleshooting the issue around 1:30am. It was difficult to pin down because the actual cause was intermittent, so downtime was slightly more than 30 minutes. (We tried various steps such as searching for network loops, removing different servers from the network, disconnecting from campus, etc.)<br />
<br />
The ultimate cause was a broken backup script run by one of the student groups we host. From what we can tell, a daily backup script they had scheduled exceeded their disk quota, then continued thrashing the network trying to write blocks (which failed after exceeding the disk quota).<br />
<br />
We're monitoring the network now to ensure everything continues to operate normally, and will work on methods for limiting individual accounts' ability to cripple the network. We'll also improve our ability to monitor the network (our existing tools weren't granular enough for us to see the problem without directly witnessing it in iotop).
