# IPMI

IPMI is accessible for each host at `HOSTNAME-mgmt.ocf.berkeley.edu`

For older supermicro X9 boards, use the following command to connect to serial directly without using the java applet:
(example for yuu)
```
ipmitool -I lanplus -H yuu-mgmt.ocf.berkeley.edu -U "ADMIN" sol activate
```
