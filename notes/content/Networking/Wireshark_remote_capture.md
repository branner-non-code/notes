## Wireshark Remote Capture

At home I see the following options on the start-up screen:
 
 * Cisco remote capture: `cisco`. [I use some Cisco tools on my home network.]
 * Random packet generator: `randpkt`
 * SSH remote capture: `ssh`

The [online manual](https://www.wireshark.org/docs/wsug_html_chunked/ChCapInterfaceRemoteSection.html) explains:

> Besides doing capture on local interfaces Wireshark is capable of reaching out across the network to a so called capture daemon or service processes to receive captured data from.

It says this is only available on Windows, and refers to a `WinPcap` driver, whereas the options seems to be talking about an `extcap` driver, which the [man pages](https://www.wireshark.org/docs/man-pages/extcap.html) describe without specifying Window.

[end]