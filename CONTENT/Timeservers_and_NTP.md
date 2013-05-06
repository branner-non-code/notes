Timeservers and NTP
===================

DPB's summary
-------------
 1. Use OpenNTP on my servers — almost always on-line. But I have never experimented with its configuration files, which probably alter a lot of behaviors.
 1. Use Chrony on my laptop installations — often off-line.

pool.ntp.org
------------
 "The pool.ntp.org project is a big virtual cluster of timeservers providing reliable easy to use NTP service for millions of clients. The pool is being used by millions or tens of millions of systems around the world. It's the default "time server" for most of the major Linux distributions and many networked appliances." http://www.pool.ntp.org/en/, accessed 20120414.

Comparing system time to the Pool
---------------------------------
 1. Use
~~~
ntpdate -q -p 8 ntp.ubuntu.com pool.ntp.org
~~~
 This will return the difference ("offset", plus delay) from ubuntu's NTP server and some other nearby servers via the Pool. See http://www.pool.ntp.org/en/use.html for more information.
 1. Other remarks:
  * Make sure that the time zone configuration of your computer is correct. ntpd itself does not do anything about the time zones, it just uses UTC internally.
  * If you are synchronising a network to pool.ntp.org, please set up one of your computers as a time server and synchronize the other computers to that one. (you'll have some reading to do - it's not difficult though. And there's always the comp.protocols.time.ntp newsgroup.)

NTPD
----
 1. "What ntpd does is calculate how far off your clock is from the server and then tells the kernel about the offset using adjtime(). The Linux kernel will then slowly adjust the clock until that error is zero. It makes approx a 5ms change every second; so the clock is always going forwards but 1 Unix second may be 0.995 real seconds, or 1.005 seconds. A lot better than ntpdate and 1 second is 'close enough' for most purposes." (http://forum.linode.com/viewtopic.php?p=30556, by sweh, 20100627, accessed 20120414.
 1. "Incremental updates to the clock (based on the ntp protocol) will occur smoothly, with no risk of moving back in time, but there's no offset for clock frequency drift, which means that systems with slow/fast clocks will consistently drift in between updates. If, instead, the frequency of the clock itself can be adjusted, that in turn helps ensure accurate timing in between updates, and then minimizes actual `adjtime` changes. Note that the difference between something like `ntpdate` and either of `openntpd`/`ntpd` is major. The additional gain from frequency drift correction is a much finer difference." (http://forum.linode.com/viewtopic.php?p=30556, by db3l, 20100627, accessed 20120414.

OpenNTP
-------
 1. "OpenNTPD is a FREE, easy to use implementation of the Network Time Protocol. It provides the ability to sync the local clock to remote NTP servers and can act as NTP server itself, redistributing the local clock. " (http://www.openntpd.org/]], accessed 20120414)
 1. Interesting discussions:
  * (2010): http://forum.linode.com/viewtopic.php?p=30556. NTP listens on every network interface, which OpenNTP does not do; OpenNTP has a smaller footprint.
  * (2007): http://fixunix.com/bsd/267804-ntpd-openntpd.html.

Chrony
------
 1. "Chronyd is a daemon which runs in background on the system. It obtains measurements via the network of the system clock’s offset relative to time servers on other systems and adjusts the system time accordingly. For isolated systems, the user can periodically enter the correct time by hand (using `Chronyc`). In either case, `Chronyd` determines the rate at which the computer gains or loses time, and compensates for this. `Chronyd` implements the NTP protocol and can act as either a client or a server." (http://chrony.tuxfamily.org/, accessed 20120414.
 1. See discussion starting at https://lists.fedoraproject.org/pipermail/devel/2010-May/135679.html. Here is one description of the essential difference that Chrony provides: 
  * "Ntpd is designed for long-uptime servers with good quality, stable clocks, and supports external reference clocks (GPS, WWVB, etc.).  Chrony is targeted more at the desktop systems, where the system is not on 24x7, and may not have as stable of an environment." (https://lists.fedoraproject.org/pipermail/devel/2010-May/135716.html, accessed 20120414.
 1. "If your computer is permanently connected, or connected for long periods (that is, for the several hours it takes ntpd to settle down), or you need to support exotic hardware reference clocks to your computer, then ntpd will work fine. Apart from not supporting many hardware clocks, chrony will work fine too. If your computer connects to the 'net for 5 minutes once a day (or something like that), or you turn your (Linux v2.0) computer off when you're not using it, or you want to use NTP on an isolated network with no hardware clocks in sight, chrony will work much better for you." (http://chrony.tuxfamily.org/FAQ.html#question_2.1, accessed 20120414.

Ubuntu time management
----------------------
 1. Discussion at https://help.ubuntu.com/community/UbuntuTime#Command_Line_ntpdate, accessed 20120414.
 1. DPB's notes at
  * Update Ubuntu server time with ntpdate.
  * Resetting time from external servers on Ubuntu 10.04.
 1. Problem with setting time repeatedly via `ntpdate`: "sawtooth correction algorithm": http://forum.linode.com/viewtopic.php?p=30556, accessed 20120414. It is also bad for the pool if every computer is calling ntpdate every minute.
 1. A 2007 survey showed 31% of users using `ntpdate` regularly, despite the problems with that method. http://www.debian-administration.org/polls/113, accessed 20120414.
 1. Using the following code to report just the time offset:
~~~
ntpdate -q -p 8 ntp.ubuntu.com pool.ntp.org | grep ntpdate | awk '{ print $10 }'
~~~

Time on servers
---------------
 1. Leslie Lamport, "Clocks and the Ordering of Events in a Distributed System" (1978) https://research.microsoft.com/en-us/um/people/lamport/pubs/pubs.html#time-clocks. Paper is posted here: https://research.microsoft.com/en-us/um/people/lamport/pubs/time-clocks.pdf.

[end]
