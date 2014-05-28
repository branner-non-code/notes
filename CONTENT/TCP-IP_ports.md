## TCP/IP ports

### Fingerprinting via port 0

 It seems that Port 0 is sometimes used to probe local configuration. Exclude it from use. On-line discussion:

 1. 

        > This port is technically illegal, but possible. It is often used to fingerprint machines, because 
        > different operating systems respond to this port in different ways.

   [SpeedGuide](http://www.speedguide.net/port.php?port=0), (accessed 20140528)

 1. 

        > TCP MUST NOT allocate port number 0, as its use could lead to
        > interoperability problems.  If a segment is received with port 0 as
        > the Source Port or the Destination Port, a RST segment SHOULD be sent
        > in response (provided that the incomming segment does not have the
        > RST flag set).
        
        > DISCUSSION:
        
        >    While port 0 is a legitimate port number, it has a special meaning
        >    in the UNIX Sockets API.  For example, when a TCP port number of 0
        >    is passed as an argument to the bind() function, rather than
        >    binding port 0, an ephemeral port is selected for the
        >    corresponding TCP end-point.  As a result, the TCP port number 0
        >    is never actually used in TCP segments.
        
        >    Different implementations have been found to respond differently
        >    to TCP segments that have a port number of 0 as the Source Port
        >    and/or the Destination Port.  As a result, TCP segments with a
        >    port number of 0 are usually employed for remote OS detection via
        >    TCP/IP stack fingerprinting [Jones, 2003].
        
        >    Since in practice TCP port 0 is not used by any legitimate
        >    application and is only used for fingerprinting purposes, a number
        >    of host implementations already reject TCP segments that use 0 as
        >    the Source Port and/or the Destination Port.  Also, a number
        >    firewalls filter (by default) any TCP segments that contain a port
        >    number of zero for the Source Port and/or the Destination Port.
        
        >    We therefore recommend that TCP implementations respond to
        >    incoming TCP segments that have a Source Port or a Destination
        >    Port of 0 with an RST (provided these incoming segments do not
        >    have the RST bit set).
        
        >    Responding with an RST segment to incoming segments that have the
        >    RST bit would open the door to RST-war attacks.
        
   [Internet Engineering Task Force](http://tools.ietf.org/html/draft-ietf-tcpm-tcp-security-02), (accessed 20140528)

 1. An [article about this by Jim MacLeod](http://www.lovemytool.com/blog/2013/08/the-strange-history-of-port-0-by-jim-macleod.html), accessed 20140528):

        > Originally, port 0 was the magic number in a BSD socket call to indicate an ephemeral port. The packets on the wire would use a random high port -- not technically random, just the next available one, but you know what I mean. When the software said “open a connection from port 0,” the OS would create packets with an ephemeral (high) port. There were never supposed to be any packets whose L4 headers actually listed the source or destination port as 0. As time went on, network monitoring apps began to use the port 0 shorthand as a placeholder to indicate that there wasn’t a TCP or UDP port, with the assumption that it would be clear from context that of course ICMP didn’t have a port.

[end]
