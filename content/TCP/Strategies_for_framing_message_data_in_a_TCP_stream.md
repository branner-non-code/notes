## Strategies for framing message data in a TCP stream

Summarized from Brandon Rhodes and John Goerzen, _Foundations of Python Network Programming_, Second Edition (New York: Apress, 2010), pp. 75–79:

 1. streaming in one direction: receiver calls `recv()` repeatedly until `''` is received; no response required;
 1. streaming in one direction followed by streaming in the other; must be careful to alternate, otherwise deadlock;
 1. fixed-length messages followed by confirmation of receipt;
 1. messages delimited with special characters;
 1. each message prefixed with its length;
 1. break message into parts and send each prefixed with its length; example has structs as messages, with message length packed together with text.

[end]