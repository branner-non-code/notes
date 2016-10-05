## Tools for network packet study

### Command-line tools

 * `text2pcap`: Generate a capture file from an ASCII hexdump of packets.
 * `tshark`: Dump and analyze network traffic. See examples at https://hackertarget.com/tshark-tutorial-and-filter-examples/.
 * `tcpdump`: Dump traffic on a network. See examples at http://www.thegeekstuff.com/2010/08/tcpdump-command-examples/.
 * `wireshark`: Wireshark from the command line. See examples at https://www.wireshark.org/docs/wsug_html_chunked/ChCustCommandLine.html.

### Examples of tcpdump

 * `tcpdump -w capture.pcap -i en8`

### Python tools

 * Python `dpkt` (Python 2 only): `dpkt.ip`, `dpkt.tcp`, `dpkt.pcap`. See examples at http://stackoverflow.com/questions/29040467/how-do-i-generate-a-pcap-file-in-python.

[end]