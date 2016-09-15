# Kozierok, _TCP/IP Guide_ (2005), Chapter 6: OSI Reference Model Layers (PART I-2: THE OPEN SYSTEMS INTERCONNECTION (OSI) REFERENCE MODEL)


## Physical Layer (Layer 1)

Handles bits.

 * The physical layer defines a number of network functions in addition to interfaces with hardware cables and cards.
 * Hardware devices generally implement multiple layers of the OSI model in addition to the physical layer. Example: Ethernet network interface card.
 * Not possible to define hardware at the physical layer independently from the technology being used at the data link layer.
 * Some technologies perform functions at the physical layer that are normally more closely associated with the data link layer

## Data Link Layer (Layer 2)

Defines the boundaries of what is considered a network. Deals with local networks and low-level messages between them.

 * A.k.a. DLL or "link layer"
 * often divided into two sublayers: logical link control (LLC) and media access control (MAC) following IEEE 802.

   * LLC: logical links between local devices on a network
   * MAC: procedures used by devices to control access to the network medium

 * data-framing: final encapsulation of higher-level messages into "frames"
 * hardware addresses
 * Many types of hardware are associated with the data link layer. Example: Ethernet cards, bridges; partially also network switches.

## Network Layer (Layer 3)

Defines how internetworks (interconnected networks) function. Handles routing between networks.

 * particularly important in terms of separating higher and lower-layer functions
 * logical addressing — IP addresses ("layer 3 addresses")
 * routing
 * datagram encapsulation
 * fragmentation and reassembly
 * Protocols here tend to be connectionless.
 * Hardware: routers (network interconnection devices); partially also brouters (bridge-routers), network switches.

## Transport Layer (Layer 4)

A.k.a. "middle layer". Relies on the lower layers to move data between devices. Responsible for end-to-end or host-to-host transport. Communication between software processes.

 * Tracks data from each application and combines it into a single flow of data to send to lower layers; also performs the reverse operations.
 * Protocols here tend to be connection-oriented.
 * TCP and UDP reside here

   * TCP: has reliability and flow-control features

 * ports
 * multiplexing data: combining data from different applications into a single stream (and demultiplexing)
 * segmenting, packaging, reassembly
 * connection management
 * reliability: acknowledgement and retransmission
 * flow control: throttling back send-rate to prevent receiver from bogging down
 * Transport and network layers are often very closely related in practice, and may be combined in some terms, e.g., TCP/IP. These pairs of protocols are not mix-and-match, however.

## Session Layer (Layer 5)

 * Responds to APIs (application program interfaces) used by higher-level protocols.
 * network sockets

## Presentation Layer (Layer 6)

Data translation. "Syntax layer".

 * converting between different encodings used by different systems
 * compression
 * SSL encryption

## Application Layer (Layer 7)

Informally, often includes session and presentation layers.

 * HTTP
 * FTP
 * SMTP
 * etc.

[end]