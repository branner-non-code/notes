## TCP notes

From Rhodes and Goerzen, _Foundations of Python Network Programming_, 2nd ed., 2010. Chapter 3 "TCP".

 1. TCP is ineffective when (p. 36)
   2. a long-term client-server relationship is inappropriate, e.g. there are too many clients to maintain separate a data stream for each one;
   2. simply resending a lost packet is in appropriate, e.g. in audio chat;
 1. Passive socket characterized by
   2. name (= server IP + port) for use by active socket
 1. Active socket is characterized by
   2.  `(local_ip, local_port, remote_ip, remote_port)`
 1. Checking required:
   2. that each message has been fully sent and received
     3. `sendall()` does this automatically, with the GIL released
     4. `recv()` does not do this, and so must be implemented within a loop
 1. Server behavior:
   2. `bind`
   2. `listen`
   2. loop:
     3. `accept` connection
     3. `close` connection
 1. Prevent refused connections while client may still be shutting down:
   2. use option `SO_REUSEADDR`

[end]
