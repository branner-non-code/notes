# UDP notes

From Rhodes and Goerzen, _Foundations of Python Network Programming_, 2nd ed., 2010. Chapter 2 "UDP".

 1. function of `bind` (p. 28):
   2. specify internal, external or wildcard IP address;
   2. specify port
 1. avoid reply duplication with:
   2. request IDs
 1. binding vs. connecting (p. 25):
   2. server binds to a port to reserve it for communicating;
   2. client is "implicitly bound" to random ephemeral port number if it tries to connect first;
   2. client connects in order to restrict packets accepted to only those from the "peer" (specified server).
 1. "peer" (p. 17):
   2. "programs cooperating with sockets" (embraces "client" and "server")
 1. IP address `127.0.0.1` is called (p. 19, 39):
   2. "localhost’s loopback interface"

[end]
