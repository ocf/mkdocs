---
date: 2011-09-19
---

# Some incoming mail rejected
Between September 1 and September 15, some incoming mail was incorrectly rejected as spam. A blacklist incorrectly included all mail servers, raising the score of incoming messages, and causing some high-scoring messages to be rejected at the SMTP stage. See <a href="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=641227">Debian bug #641227</a>.<br /><br />Since these messages were rejected before their contents could be accepted, they cannot be recovered.<br /><br />Email senders should have received a non-delivery report (bounce message) that stated:<br /><br /><blockquote>Client host rejected: Mail appeared to be SPAM or forged. Ask your Mail/DNS-Administrator to correct HELO and DNS MX settins or to get removed from DNSBLs;</blockquote><br /><br />or<br /><br /><blockquote>Client host rejected: temporarily blocked because of previous errors - retrying too fast.</blockquote><br /><br />We apologize for the inconvenience.
