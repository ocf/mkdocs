# New ASUC Subdomain

1. create a group account as normal using `approve`, you can ask henry if he wants it to be associated with a callink group/asuc finance or just put 0
2. set up vhosting as usual but put the asuc domain in there
3. add the dns records to [db.asuc.org](https://github.com/ocf/dns/blob/master/etc/zones/db.asuc.org) and make sure to bump the serial on line 5 (we typically do yyyymmdd01)
4. also run `make check_zones` to make sure nothings borked
5. merge the pr and it should be all deployed