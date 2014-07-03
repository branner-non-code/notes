## TCP notes

From Rhodes and Goerzen, _Foundations of Python Network Programming_, 2nd ed., 2010. Chapter 3 "TCP".

 1. TCP is ineffective when (p. 36)
   2. a long-term client-server relationship is inappropriate, e.g. there are too many clients to maintain separate a data stream for each one;
   2. simply resending a lost packet is in appropriate, e.g. in audio chat;
 1. Passive socket characterized by
   2. name (= server IP + port) for use by active socket
 1. Active socket is characterized by
   2.  `(local_ip, local_port, remote_ip, remote_port)`

[end]
