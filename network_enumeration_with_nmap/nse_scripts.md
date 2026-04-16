# NSE Scripts

Click on a script name for more detailed information.

## Scripts

[acarsd-info](https://nmap.org/nsedoc/scripts/acarsd-info.html)Retrieves information from a listening acarsd daemon. Acarsd decodes
ACARS (Aircraft Communication Addressing and Reporting System) data in
real time.  The information retrieved by this script includes the
daemon version, API version, administrator e-mail address and
listening frequency.

[address-info](https://nmap.org/nsedoc/scripts/address-info.html)Shows extra information about IPv6 addresses, such as embedded MAC or IPv4 addresses when available.

[afp-brute](https://nmap.org/nsedoc/scripts/afp-brute.html)Performs password guessing against Apple Filing Protocol (AFP).

[afp-ls](https://nmap.org/nsedoc/scripts/afp-ls.html)Attempts to get useful information about files from AFP volumes.
The output is intended to resemble the output of`ls`.

[afp-path-vuln](https://nmap.org/nsedoc/scripts/afp-path-vuln.html)Detects the Mac OS X AFP directory traversal vulnerability, CVE-2010-0533.

[afp-serverinfo](https://nmap.org/nsedoc/scripts/afp-serverinfo.html)Shows AFP server information. This information includes the server's
hostname, IPv4 and IPv6 addresses, and hardware type (for example`Macmini`or`MacBookPro`).

[afp-showmount](https://nmap.org/nsedoc/scripts/afp-showmount.html)Shows AFP shares and ACLs.

[ajp-auth](https://nmap.org/nsedoc/scripts/ajp-auth.html)Retrieves the authentication scheme and realm of an AJP service (Apache JServ Protocol) that requires authentication.

[ajp-brute](https://nmap.org/nsedoc/scripts/ajp-brute.html)Performs brute force passwords auditing against the Apache JServ protocol.
The Apache JServ Protocol is commonly used by web servers to communicate with
back-end Java application server containers.

[ajp-headers](https://nmap.org/nsedoc/scripts/ajp-headers.html)Performs a HEAD or GET request against either the root directory or any
optional directory of an Apache JServ Protocol server and returns the server response headers.

[ajp-methods](https://nmap.org/nsedoc/scripts/ajp-methods.html)Discovers which options are supported by the AJP (Apache JServ
Protocol) server by sending an OPTIONS request and lists potentially
risky methods.

[ajp-request](https://nmap.org/nsedoc/scripts/ajp-request.html)Requests a URI over the Apache JServ Protocol and displays the result
(or stores it in a file). Different AJP methods such as; GET, HEAD,
TRACE, PUT or DELETE may be used.

[allseeingeye-info](https://nmap.org/nsedoc/scripts/allseeingeye-info.html)Detects the All-Seeing Eye service. Provided by some game servers for
querying the server's status.

[amqp-info](https://nmap.org/nsedoc/scripts/amqp-info.html)Gathers information (a list of all server properties) from an AMQP (advanced message queuing protocol) server.

[asn-query](https://nmap.org/nsedoc/scripts/asn-query.html)Maps IP addresses to autonomous system (AS) numbers.

[auth-owners](https://nmap.org/nsedoc/scripts/auth-owners.html)Attempts to find the owner of an open TCP port by querying an auth
daemon which must also be open on the target system. The auth service,
also known as identd, normally runs on port 113.

[auth-spoof](https://nmap.org/nsedoc/scripts/auth-spoof.html)Checks for an identd (auth) server which is spoofing its replies.

[backorifice-brute](https://nmap.org/nsedoc/scripts/backorifice-brute.html)Performs brute force password auditing against the BackOrifice service. The`backorifice-brute.ports`script argument is mandatory (it specifies ports to run
the script against).

[backorifice-info](https://nmap.org/nsedoc/scripts/backorifice-info.html)Connects to a BackOrifice service and gathers information about
the host and the BackOrifice service itself.

[bacnet-info](https://nmap.org/nsedoc/scripts/bacnet-info.html)Discovers and enumerates BACNet Devices collects device information based off
standard requests. In some cases, devices may not strictly follow the
specifications, or may comply with older versions of the specifications, and
will result in a BACNET error response. Presence of this error positively
identifies the device as a BACNet device, but no enumeration is possible.

[banner](https://nmap.org/nsedoc/scripts/banner.html)A simple banner grabber which connects to an open TCP port and prints out anything sent by the listening service within five seconds.

[bitcoin-getaddr](https://nmap.org/nsedoc/scripts/bitcoin-getaddr.html)Queries a Bitcoin server for a list of known Bitcoin nodes

[bitcoin-info](https://nmap.org/nsedoc/scripts/bitcoin-info.html)Extracts version and node information from a Bitcoin server

[bitcoinrpc-info](https://nmap.org/nsedoc/scripts/bitcoinrpc-info.html)Obtains information from a Bitcoin server by calling`getinfo`on its JSON-RPC interface.

[bittorrent-discovery](https://nmap.org/nsedoc/scripts/bittorrent-discovery.html)Discovers bittorrent peers sharing a file based on a user-supplied
torrent file or magnet link.  Peers implement the Bittorrent protocol
and share the torrent, whereas the nodes (only shown if the
include-nodes NSE argument is given) implement the DHT protocol and
are used to track the peers. The sets of peers and nodes are not the
same, but they usually intersect.

[bjnp-discover](https://nmap.org/nsedoc/scripts/bjnp-discover.html)Retrieves printer or scanner information from a remote device supporting the
BJNP protocol. The protocol is known to be supported by network based Canon
devices.

[broadcast-ataoe-discover](https://nmap.org/nsedoc/scripts/broadcast-ataoe-discover.html)Discovers servers supporting the ATA over Ethernet protocol. ATA over Ethernet
is an ethernet protocol developed by the Brantley Coile Company and allows for
simple, high-performance access to SATA drives over Ethernet.

[broadcast-avahi-dos](https://nmap.org/nsedoc/scripts/broadcast-avahi-dos.html)Attempts to discover hosts in the local network using the DNS Service
Discovery protocol and sends a NULL UDP packet to each host to test
if it is vulnerable to the Avahi NULL UDP packet denial of service
(CVE-2011-1002).

[broadcast-bjnp-discover](https://nmap.org/nsedoc/scripts/broadcast-bjnp-discover.html)Attempts to discover Canon devices (Printers/Scanners) supporting the
BJNP protocol by sending BJNP Discover requests to the network
broadcast address for both ports associated with the protocol.

[broadcast-db2-discover](https://nmap.org/nsedoc/scripts/broadcast-db2-discover.html)Attempts to discover DB2 servers on the network by sending a broadcast request to port 523/udp.

[broadcast-dhcp-discover](https://nmap.org/nsedoc/scripts/broadcast-dhcp-discover.html)Sends a DHCP request to the broadcast address (255.255.255.255) and reports
the results. By default, the script uses a static MAC address
(DE:AD:CO:DE:CA:FE) in order to prevent IP pool exhaustion.

[broadcast-dhcp6-discover](https://nmap.org/nsedoc/scripts/broadcast-dhcp6-discover.html)Sends a DHCPv6 request (Solicit) to the DHCPv6 multicast address,
parses the response, then extracts and prints the address along with
any options returned by the server.

[broadcast-dns-service-discovery](https://nmap.org/nsedoc/scripts/broadcast-dns-service-discovery.html)Attempts to discover hosts' services using the DNS Service Discovery protocol.  It sends a multicast DNS-SD query and collects all the responses.

[broadcast-dropbox-listener](https://nmap.org/nsedoc/scripts/broadcast-dropbox-listener.html)Listens for the LAN sync information broadcasts that the Dropbox.com client
broadcasts every 20 seconds, then prints all the discovered client IP
addresses, port numbers, version numbers, display names, and more.

[broadcast-eigrp-discovery](https://nmap.org/nsedoc/scripts/broadcast-eigrp-discovery.html)Performs network discovery and routing information gathering through
Cisco's Enhanced Interior Gateway Routing Protocol (EIGRP).

[broadcast-hid-discoveryd](https://nmap.org/nsedoc/scripts/broadcast-hid-discoveryd.html)Discovers HID devices on a LAN by sending a discoveryd network broadcast probe.

[broadcast-igmp-discovery](https://nmap.org/nsedoc/scripts/broadcast-igmp-discovery.html)Discovers targets that have IGMP Multicast memberships and grabs interesting information.

[broadcast-jenkins-discover](https://nmap.org/nsedoc/scripts/broadcast-jenkins-discover.html)Discovers Jenkins servers on a LAN by sending a discovery broadcast probe.

[broadcast-listener](https://nmap.org/nsedoc/scripts/broadcast-listener.html)Sniffs the network for incoming broadcast communication and
attempts to decode the received packets. It supports protocols like CDP, HSRP,
Spotify, DropBox, DHCP, ARP and a few more. See packetdecoders.lua for more
information.

[broadcast-ms-sql-discover](https://nmap.org/nsedoc/scripts/broadcast-ms-sql-discover.html)Discovers Microsoft SQL servers in the same broadcast domain.

[broadcast-netbios-master-browser](https://nmap.org/nsedoc/scripts/broadcast-netbios-master-browser.html)Attempts to discover master browsers and the domains they manage.

[broadcast-networker-discover](https://nmap.org/nsedoc/scripts/broadcast-networker-discover.html)Discovers EMC Networker backup software servers on a LAN by sending a network broadcast query.

[broadcast-novell-locate](https://nmap.org/nsedoc/scripts/broadcast-novell-locate.html)Attempts to use the Service Location Protocol to discover Novell NetWare Core Protocol (NCP) servers.

[broadcast-ospf2-discover](https://nmap.org/nsedoc/scripts/broadcast-ospf2-discover.html)Discover IPv4 networks using Open Shortest Path First version 2(OSPFv2) protocol.

[broadcast-pc-anywhere](https://nmap.org/nsedoc/scripts/broadcast-pc-anywhere.html)Sends a special broadcast probe to discover PC-Anywhere hosts running on a LAN.

[broadcast-pc-duo](https://nmap.org/nsedoc/scripts/broadcast-pc-duo.html)Discovers PC-DUO remote control hosts and gateways running on a LAN by sending a special broadcast UDP probe.

[broadcast-pim-discovery](https://nmap.org/nsedoc/scripts/broadcast-pim-discovery.html)Discovers routers that are running PIM (Protocol Independent Multicast).

[broadcast-ping](https://nmap.org/nsedoc/scripts/broadcast-ping.html)Sends broadcast pings on a selected interface using raw ethernet packets and
outputs the responding hosts' IP and MAC addresses or (if requested) adds them
as targets.  Root privileges on UNIX are required to run this script since it
uses raw sockets.  Most operating systems don't respond to broadcast-ping
probes, but they can be configured to do so.

[broadcast-pppoe-discover](https://nmap.org/nsedoc/scripts/broadcast-pppoe-discover.html)Discovers PPPoE (Point-to-Point Protocol over Ethernet) servers using
the PPPoE Discovery protocol (PPPoED).  PPPoE is an ethernet based
protocol so the script has to know what ethernet interface to use for
discovery. If no interface is specified, requests are sent out on all
available interfaces.

[broadcast-rip-discover](https://nmap.org/nsedoc/scripts/broadcast-rip-discover.html)Discovers hosts and routing information from devices running RIPv2 on the
LAN. It does so by sending a RIPv2 Request command and collects the responses
from all devices responding to the request.

[broadcast-ripng-discover](https://nmap.org/nsedoc/scripts/broadcast-ripng-discover.html)Discovers hosts and routing information from devices running RIPng on the
LAN by sending a broadcast RIPng Request command and collecting any responses.

[broadcast-sonicwall-discover](https://nmap.org/nsedoc/scripts/broadcast-sonicwall-discover.html)Discovers Sonicwall firewalls which are directly attached (not routed) using
the same method as the manufacturers own 'SetupTool'. An interface needs to be
configured, as the script broadcasts a UDP packet.

[broadcast-sybase-asa-discover](https://nmap.org/nsedoc/scripts/broadcast-sybase-asa-discover.html)Discovers Sybase Anywhere servers on the LAN by sending broadcast discovery messages.

[broadcast-tellstick-discover](https://nmap.org/nsedoc/scripts/broadcast-tellstick-discover.html)Discovers Telldus Technologies TellStickNet devices on the LAN. The Telldus
TellStick is used to wirelessly control electric devices such as lights,
dimmers and electric outlets. For more information:[http://www.telldus.com/](http://www.telldus.com/)

[broadcast-upnp-info](https://nmap.org/nsedoc/scripts/broadcast-upnp-info.html)Attempts to extract system information from the UPnP service by sending a multicast query, then collecting, parsing, and displaying all responses.

[broadcast-versant-locate](https://nmap.org/nsedoc/scripts/broadcast-versant-locate.html)Discovers Versant object databases using the broadcast srvloc protocol.

[broadcast-wake-on-lan](https://nmap.org/nsedoc/scripts/broadcast-wake-on-lan.html)Wakes a remote system up from sleep by sending a Wake-On-Lan packet.

[broadcast-wpad-discover](https://nmap.org/nsedoc/scripts/broadcast-wpad-discover.html)Retrieves a list of proxy servers on a LAN using the Web Proxy
Autodiscovery Protocol (WPAD).  It implements both the DHCP and DNS
methods of doing so and starts by querying DHCP to get the address.
DHCP discovery requires nmap to be running in privileged mode and will
be skipped when this is not the case.  DNS discovery relies on the
script being able to resolve the local domain either through a script
argument or by attempting to reverse resolve the local IP.

[broadcast-wsdd-discover](https://nmap.org/nsedoc/scripts/broadcast-wsdd-discover.html)Uses a multicast query to discover devices supporting the Web Services
Dynamic Discovery (WS-Discovery) protocol. It also attempts to locate
any published Windows Communication Framework (WCF) web services (.NET
4.0 or later).

[broadcast-xdmcp-discover](https://nmap.org/nsedoc/scripts/broadcast-xdmcp-discover.html)Discovers servers running the X Display Manager Control Protocol (XDMCP) by
sending a XDMCP broadcast request to the LAN. Display managers allowing access
are marked using the keyword Willing in the result.

[cassandra-brute](https://nmap.org/nsedoc/scripts/cassandra-brute.html)Performs brute force password auditing against the Cassandra database.

[cassandra-info](https://nmap.org/nsedoc/scripts/cassandra-info.html)Attempts to get basic info and server status from a Cassandra database.

[cccam-version](https://nmap.org/nsedoc/scripts/cccam-version.html)Detects the CCcam service (software for sharing subscription TV among
multiple receivers).

[cics-enum](https://nmap.org/nsedoc/scripts/cics-enum.html)CICS transaction ID enumerator for IBM mainframes.
This script is based on mainframe_brute by Dominic White
([https://github.com/sensepost/mainframe_brute](https://github.com/sensepost/mainframe_brute)). However, this script
doesn't rely on any third party libraries or tools and instead uses
the NSE TN3270 library which emulates a TN3270 screen in lua.

[cics-info](https://nmap.org/nsedoc/scripts/cics-info.html)Using the CICS transaction CEMT, this script attempts to gather information
about the current CICS transaction server region. It gathers OS information,
Datasets (files), transactions and user ids. Based on CICSpwn script by
Ayoub ELAASSAL.

[cics-user-brute](https://nmap.org/nsedoc/scripts/cics-user-brute.html)CICS User ID brute forcing script for the CESL login screen.

[cics-user-enum](https://nmap.org/nsedoc/scripts/cics-user-enum.html)CICS User ID enumeration script for the CESL/CESN Login screen.

[citrix-brute-xml](https://nmap.org/nsedoc/scripts/citrix-brute-xml.html)Attempts to guess valid credentials for the Citrix PN Web Agent XML
Service. The XML service authenticates against the local Windows server
or the Active Directory.

[citrix-enum-apps](https://nmap.org/nsedoc/scripts/citrix-enum-apps.html)Extracts a list of published applications from the ICA Browser service.

[citrix-enum-apps-xml](https://nmap.org/nsedoc/scripts/citrix-enum-apps-xml.html)Extracts a list of applications, ACLs, and settings from the Citrix XML
service.

[citrix-enum-servers](https://nmap.org/nsedoc/scripts/citrix-enum-servers.html)Extracts a list of Citrix servers from the ICA Browser service.

[citrix-enum-servers-xml](https://nmap.org/nsedoc/scripts/citrix-enum-servers-xml.html)Extracts the name of the server farm and member servers from Citrix XML
service.

[clamav-exec](https://nmap.org/nsedoc/scripts/clamav-exec.html)Exploits ClamAV servers vulnerable to unauthenticated clamav comand execution.

[clock-skew](https://nmap.org/nsedoc/scripts/clock-skew.html)Analyzes the clock skew between the scanner and various services that report timestamps.

[coap-resources](https://nmap.org/nsedoc/scripts/coap-resources.html)Dumps list of available resources from CoAP endpoints.

[couchdb-databases](https://nmap.org/nsedoc/scripts/couchdb-databases.html)Gets database tables from a CouchDB database.

[couchdb-stats](https://nmap.org/nsedoc/scripts/couchdb-stats.html)Gets database statistics from a CouchDB database.

[creds-summary](https://nmap.org/nsedoc/scripts/creds-summary.html)Lists all discovered credentials (e.g. from brute force and default password checking scripts) at end of scan.

[cups-info](https://nmap.org/nsedoc/scripts/cups-info.html)Lists printers managed by the CUPS printing service.

[cups-queue-info](https://nmap.org/nsedoc/scripts/cups-queue-info.html)Lists currently queued print jobs of the remote CUPS service grouped by
printer.

[cvs-brute](https://nmap.org/nsedoc/scripts/cvs-brute.html)Performs brute force password auditing against CVS pserver authentication.

[cvs-brute-repository](https://nmap.org/nsedoc/scripts/cvs-brute-repository.html)Attempts to guess the name of the CVS repositories hosted on the remote server.
With knowledge of the correct repository name, usernames and passwords can be guessed.

[daap-get-library](https://nmap.org/nsedoc/scripts/daap-get-library.html)Retrieves a list of music from a DAAP server. The list includes artist
names and album and song titles.

[daytime](https://nmap.org/nsedoc/scripts/daytime.html)Retrieves the day and time from the Daytime service.

[db2-das-info](https://nmap.org/nsedoc/scripts/db2-das-info.html)Connects to the IBM DB2 Administration Server (DAS) on TCP or UDP port 523 and
exports the server profile.  No authentication is required for this request.

[deluge-rpc-brute](https://nmap.org/nsedoc/scripts/deluge-rpc-brute.html)Performs brute force password auditing against the DelugeRPC daemon.

[dhcp-discover](https://nmap.org/nsedoc/scripts/dhcp-discover.html)Sends a DHCPINFORM request to a host on UDP port 67 to obtain all the local configuration parameters
without allocating a new address.

[dicom-brute](https://nmap.org/nsedoc/scripts/dicom-brute.html)Attempts to brute force the Application Entity Title of a DICOM server (DICOM Service Provider).

[dicom-ping](https://nmap.org/nsedoc/scripts/dicom-ping.html)Attempts to discover DICOM servers (DICOM Service Provider) through a partial C-ECHO request.
 It also detects if the server allows any called Application Entity Title or not.

[dict-info](https://nmap.org/nsedoc/scripts/dict-info.html)Connects to a dictionary server using the DICT protocol, runs the SHOW
SERVER command, and displays the result. The DICT protocol is defined in RFC
2229 and is a protocol which allows a client to query a dictionary server for
definitions from a set of natural language dictionary databases.

[distcc-cve2004-2687](https://nmap.org/nsedoc/scripts/distcc-cve2004-2687.html)Detects and exploits a remote code execution vulnerability in the distributed
compiler daemon distcc. The vulnerability was disclosed in 2002, but is still
present in modern implementation due to poor configuration of the service.

[dns-blacklist](https://nmap.org/nsedoc/scripts/dns-blacklist.html)Checks target IP addresses against multiple DNS anti-spam and open
proxy blacklists and returns a list of services for which an IP has been flagged.  Checks may be limited by service category (eg: SPAM,
PROXY) or to a specific service name.

[dns-brute](https://nmap.org/nsedoc/scripts/dns-brute.html)Attempts to enumerate DNS hostnames by brute force guessing of common
subdomains. With the`dns-brute.srv`argument, dns-brute will also
try to enumerate common DNS SRV records.

[dns-cache-snoop](https://nmap.org/nsedoc/scripts/dns-cache-snoop.html)Performs DNS cache snooping against a DNS server.

[dns-check-zone](https://nmap.org/nsedoc/scripts/dns-check-zone.html)Checks DNS zone configuration against best practices, including RFC 1912.
The configuration checks are divided into categories which each have a number
of different tests.

[dns-client-subnet-scan](https://nmap.org/nsedoc/scripts/dns-client-subnet-scan.html)Performs a domain lookup using the edns-client-subnet option which
allows clients to specify the subnet that queries supposedly originate
from.  The script uses this option to supply a number of
geographically distributed locations in an attempt to enumerate as
many different address records as possible. The script also supports
requests using a given subnet.

[dns-fuzz](https://nmap.org/nsedoc/scripts/dns-fuzz.html)Launches a DNS fuzzing attack against DNS servers.

[dns-ip6-arpa-scan](https://nmap.org/nsedoc/scripts/dns-ip6-arpa-scan.html)Performs a quick reverse DNS lookup of an IPv6 network using a technique
which analyzes DNS server response codes to dramatically reduce the number of queries needed to enumerate large networks.

[dns-nsec-enum](https://nmap.org/nsedoc/scripts/dns-nsec-enum.html)Enumerates DNS names using the DNSSEC NSEC-walking technique.

[dns-nsec3-enum](https://nmap.org/nsedoc/scripts/dns-nsec3-enum.html)Tries to enumerate domain names from the DNS server that supports DNSSEC
NSEC3 records.

[dns-nsid](https://nmap.org/nsedoc/scripts/dns-nsid.html)Retrieves information from a DNS nameserver by requesting
its nameserver ID (nsid) and asking for its id.server and
version.bind values. This script performs the same queries as the following
two dig commands:
  - dig CH TXT bind.version @target
  - dig +nsid CH TXT id.server @target

[dns-random-srcport](https://nmap.org/nsedoc/scripts/dns-random-srcport.html)Checks a DNS server for the predictable-port recursion vulnerability.
Predictable source ports can make a DNS server vulnerable to cache poisoning
attacks (see CVE-2008-1447).

[dns-random-txid](https://nmap.org/nsedoc/scripts/dns-random-txid.html)Checks a DNS server for the predictable-TXID DNS recursion
vulnerability.  Predictable TXID values can make a DNS server vulnerable to
cache poisoning attacks (see CVE-2008-1447).

[dns-recursion](https://nmap.org/nsedoc/scripts/dns-recursion.html)Checks if a DNS server allows queries for third-party names. It is
expected that recursion will be enabled on your own internal
nameservers.

[dns-service-discovery](https://nmap.org/nsedoc/scripts/dns-service-discovery.html)Attempts to discover target hosts' services using the DNS Service Discovery protocol.

[dns-srv-enum](https://nmap.org/nsedoc/scripts/dns-srv-enum.html)Enumerates various common service (SRV) records for a given domain name.
The service records contain the hostname, port and priority of servers for a given service.
The following services are enumerated by the script:
  - Active Directory Global Catalog
  - Exchange Autodiscovery
  - Kerberos KDC Service
  - Kerberos Passwd Change Service
  - LDAP Servers
  - SIP Servers
  - XMPP S2S
  - XMPP C2S

[dns-update](https://nmap.org/nsedoc/scripts/dns-update.html)Attempts to perform a dynamic DNS update without authentication.

[dns-zeustracker](https://nmap.org/nsedoc/scripts/dns-zeustracker.html)Checks if the target IP range is part of a Zeus botnet by querying ZTDNS @ abuse.ch.
Please review the following information before you start to scan:

- [https://zeustracker.abuse.ch/ztdns.php](https://zeustracker.abuse.ch/ztdns.php)
[dns-zone-transfer](https://nmap.org/nsedoc/scripts/dns-zone-transfer.html)Requests a zone transfer (AXFR) from a DNS server.

[docker-version](https://nmap.org/nsedoc/scripts/docker-version.html)Detects the Docker service version.

[domcon-brute](https://nmap.org/nsedoc/scripts/domcon-brute.html)Performs brute force password auditing against the Lotus Domino Console.

[domcon-cmd](https://nmap.org/nsedoc/scripts/domcon-cmd.html)Runs a console command on the Lotus Domino Console using the given authentication credentials (see also: domcon-brute)

[domino-enum-users](https://nmap.org/nsedoc/scripts/domino-enum-users.html)Attempts to discover valid IBM Lotus Domino users and download their ID files by exploiting the CVE-2006-5835 vulnerability.

[dpap-brute](https://nmap.org/nsedoc/scripts/dpap-brute.html)Performs brute force password auditing against an iPhoto Library.

[drda-brute](https://nmap.org/nsedoc/scripts/drda-brute.html)Performs password guessing against databases supporting the IBM DB2 protocol such as Informix, DB2 and Derby

[drda-info](https://nmap.org/nsedoc/scripts/drda-info.html)Attempts to extract information from database servers supporting the DRDA
protocol. The script sends a DRDA EXCSAT (exchange server attributes)
command packet and parses the response.

[duplicates](https://nmap.org/nsedoc/scripts/duplicates.html)Attempts to discover multihomed systems by analysing and comparing
information collected by other scripts. The information analyzed
currently includes, SSL certificates, SSH host keys, MAC addresses,
and Netbios server names.

[eap-info](https://nmap.org/nsedoc/scripts/eap-info.html)Enumerates the authentication methods offered by an EAP (Extensible
Authentication Protocol) authenticator for a given identity or for the
anonymous identity if no argument is passed.

[enip-info](https://nmap.org/nsedoc/scripts/enip-info.html)This NSE script is used to send a EtherNet/IP packet to a remote device that
has TCP 44818 open. The script will send a Request Identity Packet and once a
response is received, it validates that it was a proper response to the command
that was sent, and then will parse out the data. Information that is parsed
includes Device Type, Vendor ID, Product name, Serial Number, Product code,
Revision Number, status, state, as well as the Device IP.

[epmd-info](https://nmap.org/nsedoc/scripts/epmd-info.html)Connects to Erlang Port Mapper Daemon (epmd) and retrieves a list of nodes with their respective port numbers.

[eppc-enum-processes](https://nmap.org/nsedoc/scripts/eppc-enum-processes.html)Attempts to enumerate process info over the Apple Remote Event protocol.
When accessing an application over the Apple Remote Event protocol the
service responds with the uid and pid of the application, if it is running,
prior to requesting authentication.

[fcrdns](https://nmap.org/nsedoc/scripts/fcrdns.html)Performs a Forward-confirmed Reverse DNS lookup and reports anomalous results.

[finger](https://nmap.org/nsedoc/scripts/finger.html)Attempts to retrieve a list of usernames using the finger service.

[fingerprint-strings](https://nmap.org/nsedoc/scripts/fingerprint-strings.html)Prints the readable strings from service fingerprints of unknown services.

[firewalk](https://nmap.org/nsedoc/scripts/firewalk.html)Tries to discover firewall rules using an IP TTL expiration technique known
as firewalking.

[firewall-bypass](https://nmap.org/nsedoc/scripts/firewall-bypass.html)Detects a vulnerability in netfilter and other firewalls that use helpers to
dynamically open ports for protocols such as ftp and sip.

[flume-master-info](https://nmap.org/nsedoc/scripts/flume-master-info.html)Retrieves information from Flume master HTTP pages.

[fox-info](https://nmap.org/nsedoc/scripts/fox-info.html)Tridium Niagara Fox is a protocol used within Building Automation Systems. Based
off Billy Rios and Terry McCorkle's work this Nmap NSE will collect information
from A Tridium Niagara system.

[freelancer-info](https://nmap.org/nsedoc/scripts/freelancer-info.html)Detects the Freelancer game server (FLServer.exe) service by sending a
status query UDP probe.

[ftp-anon](https://nmap.org/nsedoc/scripts/ftp-anon.html)Checks if an FTP server allows anonymous logins.

[ftp-bounce](https://nmap.org/nsedoc/scripts/ftp-bounce.html)Checks to see if an FTP server allows port scanning using the FTP bounce method.

[ftp-brute](https://nmap.org/nsedoc/scripts/ftp-brute.html)Performs brute force password auditing against FTP servers.

[ftp-libopie](https://nmap.org/nsedoc/scripts/ftp-libopie.html)Checks if an FTPd is prone to CVE-2010-1938 (OPIE off-by-one stack overflow),
a vulnerability discovered by Maksymilian Arciemowicz and Adam "pi3" Zabrocki.
See the advisory at[https://nmap.org/r/fbsd-sa-opie](https://nmap.org/r/fbsd-sa-opie).
Be advised that, if launched against a vulnerable host, this script will crash the FTPd.

[ftp-proftpd-backdoor](https://nmap.org/nsedoc/scripts/ftp-proftpd-backdoor.html)Tests for the presence of the ProFTPD 1.3.3c backdoor reported as BID
45150. This script attempts to exploit the backdoor using the innocuous`id`command by default, but that can be changed with the`ftp-proftpd-backdoor.cmd`script argument.

[ftp-syst](https://nmap.org/nsedoc/scripts/ftp-syst.html)Sends FTP SYST and STAT commands and returns the result.

[ftp-vsftpd-backdoor](https://nmap.org/nsedoc/scripts/ftp-vsftpd-backdoor.html)Tests for the presence of the vsFTPd 2.3.4 backdoor reported on 2011-07-04
(CVE-2011-2523). This script attempts to exploit the backdoor using the
innocuous`id`command by default, but that can be changed with
the`exploit.cmd`or`ftp-vsftpd-backdoor.cmd`script
arguments.

[ftp-vuln-cve2010-4221](https://nmap.org/nsedoc/scripts/ftp-vuln-cve2010-4221.html)Checks for a stack-based buffer overflow in the ProFTPD server, version
between 1.3.2rc3 and 1.3.3b. By sending a large number of TELNET_IAC escape
sequence, the proftpd process miscalculates the buffer length, and a remote
attacker will be able to corrupt the stack and execute arbitrary code within
the context of the proftpd process (CVE-2010-4221). Authentication is not
required to exploit this vulnerability.

[ganglia-info](https://nmap.org/nsedoc/scripts/ganglia-info.html)Retrieves system information (OS version, available memory, etc.) from
a listening Ganglia Monitoring Daemon or Ganglia Meta Daemon.

[giop-info](https://nmap.org/nsedoc/scripts/giop-info.html)Queries a CORBA naming server for a list of objects.

[gkrellm-info](https://nmap.org/nsedoc/scripts/gkrellm-info.html)Queries a GKRellM service for monitoring information. A single round of
collection is made, showing a snapshot of information at the time of the
request.

[gopher-ls](https://nmap.org/nsedoc/scripts/gopher-ls.html)Lists files and directories at the root of a gopher service.

[gpsd-info](https://nmap.org/nsedoc/scripts/gpsd-info.html)Retrieves GPS time, coordinates and speed from the GPSD network daemon.

[hadoop-datanode-info](https://nmap.org/nsedoc/scripts/hadoop-datanode-info.html)Discovers information such as log directories from an Apache Hadoop DataNode
HTTP status page.

[hadoop-jobtracker-info](https://nmap.org/nsedoc/scripts/hadoop-jobtracker-info.html)Retrieves information from an Apache Hadoop JobTracker HTTP status page.

[hadoop-namenode-info](https://nmap.org/nsedoc/scripts/hadoop-namenode-info.html)Retrieves information from an Apache Hadoop NameNode HTTP status page.

[hadoop-secondary-namenode-info](https://nmap.org/nsedoc/scripts/hadoop-secondary-namenode-info.html)Retrieves information from an Apache Hadoop secondary NameNode HTTP status page.

[hadoop-tasktracker-info](https://nmap.org/nsedoc/scripts/hadoop-tasktracker-info.html)Retrieves information from an Apache Hadoop TaskTracker HTTP status page.

[hartip-info](https://nmap.org/nsedoc/scripts/hartip-info.html)This NSE script is used to send a HART-IP packet to a HART device that has TCP 5094 open.
The script will establish Session with HART device, then Read Unique Identifier and
Read Long Tag packets are sent to parse the required HART device information.
Read Sub-Device Identity Summary packet with Sub-Device index 00 01 is sent
to request information on Sub-Device, if any available. If the response code
differs from 0 (success), the error code is passed as Sub-Device Information.
Otherwise, the required Sub-Device information is parsed from response packet.

[hbase-master-info](https://nmap.org/nsedoc/scripts/hbase-master-info.html)Retrieves information from an Apache HBase (Hadoop database) master HTTP status page.

[hbase-region-info](https://nmap.org/nsedoc/scripts/hbase-region-info.html)Retrieves information from an Apache HBase (Hadoop database) region server HTTP status page.

[hddtemp-info](https://nmap.org/nsedoc/scripts/hddtemp-info.html)Reads hard disk information (such as brand, model, and sometimes temperature) from a listening hddtemp service.

[hnap-info](https://nmap.org/nsedoc/scripts/hnap-info.html)Retrieve hardwares details and configuration information utilizing HNAP, the "Home Network Administration Protocol".
It is an HTTP-Simple Object Access Protocol (SOAP)-based protocol which allows for remote topology discovery,
configuration, and management of devices (routers, cameras, PCs, NAS, etc.)

[hostmap-bfk](https://nmap.org/nsedoc/scripts/hostmap-bfk.html)Discovers hostnames that resolve to the target's IP address by querying the online database at[http://www.bfk.de/bfk_dnslogger.html](http://www.bfk.de/bfk_dnslogger.html).

[hostmap-crtsh](https://nmap.org/nsedoc/scripts/hostmap-crtsh.html)Finds subdomains of a web server by querying Google's Certificate Transparency
logs database ([https://crt.sh](https://crt.sh/)).

[hostmap-robtex](https://nmap.org/nsedoc/scripts/hostmap-robtex.html)Discovers hostnames that resolve to the target's IP address by querying the online Robtex service at[http://ip.robtex.com/](http://ip.robtex.com/).

[http-adobe-coldfusion-apsa1301](https://nmap.org/nsedoc/scripts/http-adobe-coldfusion-apsa1301.html)Attempts to exploit an authentication bypass vulnerability in Adobe Coldfusion
servers to retrieve a valid administrator's session cookie.

[http-affiliate-id](https://nmap.org/nsedoc/scripts/http-affiliate-id.html)Grabs affiliate network IDs (e.g. Google AdSense or Analytics, Amazon
Associates, etc.) from a web page. These can be used to identify pages
with the same owner.

[http-apache-negotiation](https://nmap.org/nsedoc/scripts/http-apache-negotiation.html)Checks if the target http server has mod_negotiation enabled.  This
feature can be leveraged to find hidden resources and spider a web
site using fewer requests.

[http-apache-server-status](https://nmap.org/nsedoc/scripts/http-apache-server-status.html)Attempts to retrieve the server-status page for Apache webservers that
have mod_status enabled. If the server-status page exists and appears to
be from mod_status the script will parse useful information such as the
system uptime, Apache version and recent HTTP requests.

[http-aspnet-debug](https://nmap.org/nsedoc/scripts/http-aspnet-debug.html)Determines if a ASP.NET application has debugging enabled using a HTTP DEBUG request.

[http-auth](https://nmap.org/nsedoc/scripts/http-auth.html)Retrieves the authentication scheme and realm of a web service that requires
authentication.

[http-auth-finder](https://nmap.org/nsedoc/scripts/http-auth-finder.html)Spiders a web site to find web pages requiring form-based or HTTP-based authentication. The results are returned in a table with each url and the
detected method.

[http-avaya-ipoffice-users](https://nmap.org/nsedoc/scripts/http-avaya-ipoffice-users.html)Attempts to enumerate users in Avaya IP Office systems 7.x.

[http-awstatstotals-exec](https://nmap.org/nsedoc/scripts/http-awstatstotals-exec.html)Exploits a remote code execution vulnerability in Awstats Totals 1.0 up to 1.14
and possibly other products based on it (CVE: 2008-3922).

[http-axis2-dir-traversal](https://nmap.org/nsedoc/scripts/http-axis2-dir-traversal.html)Exploits a directory traversal vulnerability in Apache Axis2 version 1.4.1 by
sending a specially crafted request to the parameter`xsd`(BID 40343). By default it will try to retrieve the configuration file of the
Axis2 service`'/conf/axis2.xml'`using the path`'/axis2/services/'`to return the username and password of the
admin account.

[http-backup-finder](https://nmap.org/nsedoc/scripts/http-backup-finder.html)Spiders a website and attempts to identify backup copies of discovered files.
It does so by requesting a number of different combinations of the filename (eg. index.bak, index.html~, copy of index.html).

[http-barracuda-dir-traversal](https://nmap.org/nsedoc/scripts/http-barracuda-dir-traversal.html)Attempts to retrieve the configuration settings from a Barracuda
Networks Spam & Virus Firewall device using the directory traversal
vulnerability described at[http://seclists.org/fulldisclosure/2010/Oct/119](http://seclists.org/fulldisclosure/2010/Oct/119).

[http-bigip-cookie](https://nmap.org/nsedoc/scripts/http-bigip-cookie.html)Decodes any unencrypted F5 BIG-IP cookies in the HTTP response.
BIG-IP cookies contain information on backend systems such as
internal IP addresses and port numbers.
See here for more info:[https://support.f5.com/csp/article/K6917](https://support.f5.com/csp/article/K6917)

[http-brute](https://nmap.org/nsedoc/scripts/http-brute.html)Performs brute force password auditing against http basic, digest and ntlm authentication.

[http-cakephp-version](https://nmap.org/nsedoc/scripts/http-cakephp-version.html)Obtains the CakePHP version of a web application built with the CakePHP
framework by fingerprinting default files shipped with the CakePHP framework.

[http-chrono](https://nmap.org/nsedoc/scripts/http-chrono.html)Measures the time a website takes to deliver a web page and returns
the maximum, minimum and average time it took to fetch a page.

[http-cisco-anyconnect](https://nmap.org/nsedoc/scripts/http-cisco-anyconnect.html)Connect as Cisco AnyConnect client to a Cisco SSL VPN and retrieves version
and tunnel information.

[http-coldfusion-subzero](https://nmap.org/nsedoc/scripts/http-coldfusion-subzero.html)Attempts to retrieve version, absolute path of administration panel and the
file 'password.properties' from vulnerable installations of ColdFusion 9 and
10.

[http-comments-displayer](https://nmap.org/nsedoc/scripts/http-comments-displayer.html)Extracts and outputs HTML and JavaScript comments from HTTP responses.

[http-config-backup](https://nmap.org/nsedoc/scripts/http-config-backup.html)Checks for backups and swap files of common content management system
and web server configuration files.

[http-cookie-flags](https://nmap.org/nsedoc/scripts/http-cookie-flags.html)Examines cookies set by HTTP services.  Reports any session cookies set
without the httponly flag.  Reports any session cookies set over SSL without
the secure flag.  If http-enum.nse is also run, any interesting paths found
by it will be checked in addition to the root.

[http-cors](https://nmap.org/nsedoc/scripts/http-cors.html)Tests an http server for Cross-Origin Resource Sharing (CORS), a way
for domains to explicitly opt in to having certain methods invoked by
another domain.

[http-cross-domain-policy](https://nmap.org/nsedoc/scripts/http-cross-domain-policy.html)Checks the cross-domain policy file (/crossdomain.xml) and the client-acces-policy file (/clientaccesspolicy.xml)
in web applications and lists the trusted domains. Overly permissive settings enable Cross Site Request Forgery
attacks and may allow attackers to access sensitive data. This script is useful to detect permissive
configurations and possible domain names available for purchase to exploit the application.

[http-csrf](https://nmap.org/nsedoc/scripts/http-csrf.html)This script detects Cross Site Request Forgeries (CSRF) vulnerabilities.

[http-date](https://nmap.org/nsedoc/scripts/http-date.html)Gets the date from HTTP-like services. Also prints how much the date
differs from local time. Local time is the time the HTTP request was
sent, so the difference includes at least the duration of one RTT.

[http-default-accounts](https://nmap.org/nsedoc/scripts/http-default-accounts.html)Tests for access with default credentials used by a variety of web applications
and devices. It detects applications by matching web responses of known paths
and launching a login routine using default credentials when found.

[http-devframework](https://nmap.org/nsedoc/scripts/http-devframework.html)

[http-dlink-backdoor](https://nmap.org/nsedoc/scripts/http-dlink-backdoor.html)Detects a firmware backdoor on some D-Link routers by changing the User-Agent
to a "secret" value. Using the "secret" User-Agent bypasses authentication
and allows admin access to the router.

[http-dombased-xss](https://nmap.org/nsedoc/scripts/http-dombased-xss.html)It looks for places where attacker-controlled information in the DOM may be used
to affect JavaScript execution in certain ways. The attack is explained here:[http://www.webappsec.org/projects/articles/071105.shtml](http://www.webappsec.org/projects/articles/071105.shtml)

[http-domino-enum-passwords](https://nmap.org/nsedoc/scripts/http-domino-enum-passwords.html)Attempts to enumerate the hashed Domino Internet Passwords that are (by
default) accessible by all authenticated users. This script can also download
any Domino ID Files attached to the Person document.  Passwords are presented
in a form suitable for running in John the Ripper.

[http-drupal-enum](https://nmap.org/nsedoc/scripts/http-drupal-enum.html)Enumerates the installed Drupal modules/themes by using a list of known modules and themes.

[http-drupal-enum-users](https://nmap.org/nsedoc/scripts/http-drupal-enum-users.html)Enumerates Drupal users by exploiting an information disclosure vulnerability
in Views, Drupal's most popular module.

[http-enum](https://nmap.org/nsedoc/scripts/http-enum.html)Enumerates directories used by popular web applications and servers.

[http-errors](https://nmap.org/nsedoc/scripts/http-errors.html)This script crawls through the website and returns any error pages.

[http-exif-spider](https://nmap.org/nsedoc/scripts/http-exif-spider.html)Spiders a site's images looking for interesting exif data embedded in
.jpg files. Displays the make and model of the camera, the date the photo was
taken, and the embedded geotag information.

[http-favicon](https://nmap.org/nsedoc/scripts/http-favicon.html)Gets the favicon ("favorites icon") from a web page and matches it against a
database of the icons of known web applications. If there is a match, the name
of the application is printed; otherwise the MD5 hash of the icon data is
printed.

[http-feed](https://nmap.org/nsedoc/scripts/http-feed.html)This script crawls through the website to find any rss or atom feeds.

[http-fetch](https://nmap.org/nsedoc/scripts/http-fetch.html)The script is used to fetch files from servers.

[http-fileupload-exploiter](https://nmap.org/nsedoc/scripts/http-fileupload-exploiter.html)Exploits insecure file upload forms in web applications
using various techniques like changing the Content-type
header or creating valid image files containing the
payload in the comment.

[http-form-brute](https://nmap.org/nsedoc/scripts/http-form-brute.html)Performs brute force password auditing against http form-based authentication.

[http-form-fuzzer](https://nmap.org/nsedoc/scripts/http-form-fuzzer.html)Performs a simple form fuzzing against forms found on websites.
Tries strings and numbers of increasing length and attempts to
determine if the fuzzing was successful.

[http-frontpage-login](https://nmap.org/nsedoc/scripts/http-frontpage-login.html)Checks whether target machines are vulnerable to anonymous Frontpage login.

[http-generator](https://nmap.org/nsedoc/scripts/http-generator.html)Displays the contents of the "generator" meta tag of a web page (default: /)
if there is one.

[http-git](https://nmap.org/nsedoc/scripts/http-git.html)Checks for a Git repository found in a website's document root
/.git/<something>) and retrieves as much repo information as
possible, including language/framework, remotes, last commit
message, and repository description.

[http-gitweb-projects-enum](https://nmap.org/nsedoc/scripts/http-gitweb-projects-enum.html)Retrieves a list of Git projects, owners and descriptions from a gitweb (web interface to the Git revision control system).

[http-google-malware](https://nmap.org/nsedoc/scripts/http-google-malware.html)Checks if hosts are on Google's blacklist of suspected malware and phishing
servers. These lists are constantly updated and are part of Google's Safe
Browsing service.

[http-grep](https://nmap.org/nsedoc/scripts/http-grep.html)Spiders a website and attempts to match all pages and urls against a given
string. Matches are counted and grouped per url under which they were
discovered.

[http-headers](https://nmap.org/nsedoc/scripts/http-headers.html)Performs a HEAD request for the root folder ("/") of a web server and displays the HTTP headers returned.

[http-hp-ilo-info](https://nmap.org/nsedoc/scripts/http-hp-ilo-info.html)Attempts to extract information from HP iLO boards including versions and addresses.

[http-huawei-hg5xx-vuln](https://nmap.org/nsedoc/scripts/http-huawei-hg5xx-vuln.html)Detects Huawei modems models HG530x, HG520x, HG510x (and possibly others...)
vulnerable to a remote credential and information disclosure vulnerability. It
also extracts the PPPoE credentials and other interesting configuration values.

[http-icloud-findmyiphone](https://nmap.org/nsedoc/scripts/http-icloud-findmyiphone.html)Retrieves the locations of all "Find my iPhone" enabled iOS devices by querying
the MobileMe web service (authentication required).

[http-icloud-sendmsg](https://nmap.org/nsedoc/scripts/http-icloud-sendmsg.html)Sends a message to a iOS device through the Apple MobileMe web service. The
device has to be registered with an Apple ID using the Find My Iphone
application.

[http-iis-short-name-brute](https://nmap.org/nsedoc/scripts/http-iis-short-name-brute.html)Attempts to brute force the 8.3 filenames (commonly known as short names) of files and directories in the root folder
of vulnerable IIS servers. This script is an implementation of the PoC "iis shortname scanner".

[http-iis-webdav-vuln](https://nmap.org/nsedoc/scripts/http-iis-webdav-vuln.html)Checks for a vulnerability in IIS 5.1/6.0 that allows arbitrary users to access
secured WebDAV folders by searching for a password-protected folder and
attempting to access it. This vulnerability was patched in Microsoft Security
Bulletin MS09-020,[https://nmap.org/r/ms09-020](https://nmap.org/r/ms09-020).

[http-internal-ip-disclosure](https://nmap.org/nsedoc/scripts/http-internal-ip-disclosure.html)Determines if the web server leaks its internal IP address when sending
an HTTP/1.0 request without a Host header.

[http-joomla-brute](https://nmap.org/nsedoc/scripts/http-joomla-brute.html)Performs brute force password auditing against Joomla web CMS installations.

[http-jsonp-detection](https://nmap.org/nsedoc/scripts/http-jsonp-detection.html)Attempts to discover JSONP endpoints in web servers. JSONP endpoints can be
used to bypass Same-origin Policy restrictions in web browsers.

[http-litespeed-sourcecode-download](https://nmap.org/nsedoc/scripts/http-litespeed-sourcecode-download.html)Exploits a null-byte poisoning vulnerability in Litespeed Web Servers 4.0.x
before 4.0.15 to retrieve the target script's source code by sending a HTTP
request with a null byte followed by a .txt file extension (CVE-2010-2333).

[http-ls](https://nmap.org/nsedoc/scripts/http-ls.html)Shows the content of an "index" Web page.

[http-majordomo2-dir-traversal](https://nmap.org/nsedoc/scripts/http-majordomo2-dir-traversal.html)Exploits a directory traversal vulnerability existing in Majordomo2 to retrieve remote files. (CVE-2011-0049).

[http-malware-host](https://nmap.org/nsedoc/scripts/http-malware-host.html)Looks for signature of known server compromises.

[http-mcmp](https://nmap.org/nsedoc/scripts/http-mcmp.html)Checks if the webserver allows mod_cluster management protocol (MCMP) methods.

[http-method-tamper](https://nmap.org/nsedoc/scripts/http-method-tamper.html)Attempts to bypass password protected resources (HTTP 401 status) by performing HTTP verb tampering.
If an array of paths to check is not set, it will crawl the web server and perform the check against any
password protected resource that it finds.

[http-methods](https://nmap.org/nsedoc/scripts/http-methods.html)Finds out what options are supported by an HTTP server by sending an
OPTIONS request. Lists potentially risky methods. It tests those methods
not mentioned in the OPTIONS headers individually and sees if they are
implemented. Any output other than 501/405 suggests that the method is
if not in the range 400 to 600. If the response falls under that range then
it is compared to the response from a randomly generated method.

[http-mobileversion-checker](https://nmap.org/nsedoc/scripts/http-mobileversion-checker.html)Checks if the website holds a mobile version.

[http-ntlm-info](https://nmap.org/nsedoc/scripts/http-ntlm-info.html)This script enumerates information from remote HTTP services with NTLM
authentication enabled.

[http-open-proxy](https://nmap.org/nsedoc/scripts/http-open-proxy.html)Checks if an HTTP proxy is open.

[http-open-redirect](https://nmap.org/nsedoc/scripts/http-open-redirect.html)Spiders a website and attempts to identify open redirects. Open
redirects are handlers which commonly take a URL as a parameter and
responds with a HTTP redirect (3XX) to the target.  Risks of open redirects are
described at[http://cwe.mitre.org/data/definitions/601.html](http://cwe.mitre.org/data/definitions/601.html).

[http-passwd](https://nmap.org/nsedoc/scripts/http-passwd.html)Checks if a web server is vulnerable to directory traversal by attempting to
retrieve`/etc/passwd`or`\boot.ini`.

[http-php-version](https://nmap.org/nsedoc/scripts/http-php-version.html)Attempts to retrieve the PHP version from a web server. PHP has a number
of magic queries that return images or text that can vary with the PHP
version. This script uses the following queries:

- `/?=PHPE9568F36-D428-11d2-A769-00AA001ACF42`: gets a GIF logo, which changes on April Fool's Day.
- `/?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000`: gets an HTML credits page.
[http-phpmyadmin-dir-traversal](https://nmap.org/nsedoc/scripts/http-phpmyadmin-dir-traversal.html)Exploits a directory traversal vulnerability in phpMyAdmin 2.6.4-pl1 (and
possibly other versions) to retrieve remote files on the web server.

[http-phpself-xss](https://nmap.org/nsedoc/scripts/http-phpself-xss.html)Crawls a web server and attempts to find PHP files vulnerable to reflected
cross site scripting via the variable`$_SERVER["PHP_SELF"]`.

[http-proxy-brute](https://nmap.org/nsedoc/scripts/http-proxy-brute.html)Performs brute force password guessing against HTTP proxy servers.

[http-put](https://nmap.org/nsedoc/scripts/http-put.html)Uploads a local file to a remote web server using the HTTP PUT method. You must specify the filename and URL path with NSE arguments.

[http-qnap-nas-info](https://nmap.org/nsedoc/scripts/http-qnap-nas-info.html)Attempts to retrieve the model, firmware version, and enabled services from a
QNAP Network Attached Storage (NAS) device.

[http-referer-checker](https://nmap.org/nsedoc/scripts/http-referer-checker.html)Informs about cross-domain include of scripts. Websites that include
external javascript scripts are delegating part of their security to
third-party entities.

[http-rfi-spider](https://nmap.org/nsedoc/scripts/http-rfi-spider.html)Crawls webservers in search of RFI (remote file inclusion) vulnerabilities. It
tests every form field it finds and every parameter of a URL containing a
query.

[http-robots.txt](https://nmap.org/nsedoc/scripts/http-robots.txt.html)Checks for disallowed entries in`/robots.txt`on a web server.

[http-robtex-reverse-ip](https://nmap.org/nsedoc/scripts/http-robtex-reverse-ip.html)Obtains up to 100 forward DNS names for a target IP address by querying the Robtex service ([https://www.robtex.com/ip-lookup/](https://www.robtex.com/ip-lookup/)).

[http-robtex-shared-ns](https://nmap.org/nsedoc/scripts/http-robtex-shared-ns.html)Finds up to 100 domain names which use the same name server as the target by querying the Robtex service at[http://www.robtex.com/dns/](http://www.robtex.com/dns/).

[http-sap-netweaver-leak](https://nmap.org/nsedoc/scripts/http-sap-netweaver-leak.html)Detects SAP Netweaver Portal instances that allow anonymous access to the
 KM unit navigation page. This page leaks file names, ldap users, etc.

[http-security-headers](https://nmap.org/nsedoc/scripts/http-security-headers.html)Checks for the HTTP response headers related to security given in OWASP Secure Headers Project
and gives a brief description of the header and its configuration value.

[http-server-header](https://nmap.org/nsedoc/scripts/http-server-header.html)Uses the HTTP Server header for missing version info. This is currently
infeasible with version probes because of the need to match non-HTTP services
correctly.

[http-shellshock](https://nmap.org/nsedoc/scripts/http-shellshock.html)Attempts to exploit the "shellshock" vulnerability (CVE-2014-6271 and
CVE-2014-7169) in web applications.

[http-sitemap-generator](https://nmap.org/nsedoc/scripts/http-sitemap-generator.html)Spiders a web server and displays its directory structure along with
number and types of files in each folder. Note that files listed as
having an 'Other' extension are ones that have no extension or that
are a root document.

[http-slowloris](https://nmap.org/nsedoc/scripts/http-slowloris.html)Tests a web server for vulnerability to the Slowloris DoS attack by launching a Slowloris attack.

[http-slowloris-check](https://nmap.org/nsedoc/scripts/http-slowloris-check.html)Tests a web server for vulnerability to the Slowloris DoS attack without
actually launching a DoS attack.

[http-sql-injection](https://nmap.org/nsedoc/scripts/http-sql-injection.html)Spiders an HTTP server looking for URLs containing queries vulnerable to an SQL
injection attack. It also extracts forms from found websites and tries to identify
fields that are vulnerable.

[http-stored-xss](https://nmap.org/nsedoc/scripts/http-stored-xss.html)Unfiltered '>' (greater than sign). An indication of potential XSS vulnerability.

[http-svn-enum](https://nmap.org/nsedoc/scripts/http-svn-enum.html)Enumerates users of a Subversion repository by examining logs of most recent commits.

[http-svn-info](https://nmap.org/nsedoc/scripts/http-svn-info.html)Requests information from a Subversion repository.

[http-title](https://nmap.org/nsedoc/scripts/http-title.html)Shows the title of the default page of a web server.

[http-tplink-dir-traversal](https://nmap.org/nsedoc/scripts/http-tplink-dir-traversal.html)Exploits a directory traversal vulnerability existing in several TP-Link
wireless routers. Attackers may exploit this vulnerability to read any of the
configuration and password files remotely and without authentication.

[http-trace](https://nmap.org/nsedoc/scripts/http-trace.html)Sends an HTTP TRACE request and shows if the method TRACE is enabled. If debug
is enabled, it returns the header fields that were modified in the response.

[http-traceroute](https://nmap.org/nsedoc/scripts/http-traceroute.html)Exploits the Max-Forwards HTTP header to detect the presence of reverse proxies.

[http-trane-info](https://nmap.org/nsedoc/scripts/http-trane-info.html)Attempts to obtain information from Trane Tracer SC devices. Trane Tracer SC
 is an intelligent field panel for communicating with HVAC equipment controllers
 deployed across several sectors including commercial facilities and others.

[http-unsafe-output-escaping](https://nmap.org/nsedoc/scripts/http-unsafe-output-escaping.html)Spiders a website and attempts to identify output escaping problems
where content is reflected back to the user.  This script locates all
parameters, ?x=foo&y=bar and checks if the values are reflected on the
page. If they are indeed reflected, the script will try to insert
ghz>hzx"zxc'xcv and check which (if any) characters were reflected
back onto the page without proper html escaping.  This is an
indication of potential XSS vulnerability.

[http-useragent-tester](https://nmap.org/nsedoc/scripts/http-useragent-tester.html)Checks if various crawling utilities are allowed by the host.

[http-userdir-enum](https://nmap.org/nsedoc/scripts/http-userdir-enum.html)Attempts to enumerate valid usernames on web servers running with the mod_userdir
module or similar enabled.

[http-vhosts](https://nmap.org/nsedoc/scripts/http-vhosts.html)Searches for web virtual hostnames by making a large number of HEAD requests against http servers using common hostnames.

[http-virustotal](https://nmap.org/nsedoc/scripts/http-virustotal.html)Checks whether a file has been determined as malware by Virustotal. Virustotal
is a service that provides the capability to scan a file or check a checksum
against a number of the major antivirus vendors. The script uses the public
API which requires a valid API key and has a limit on 4 queries per minute.
A key can be acquired by registering as a user on the virustotal web page:

- [http://www.virustotal.com](http://www.virustotal.com/)
[http-vlcstreamer-ls](https://nmap.org/nsedoc/scripts/http-vlcstreamer-ls.html)Connects to a VLC Streamer helper service and lists directory contents. The
VLC Streamer helper service is used by the iOS VLC Streamer application to
enable streaming of multimedia content from the remote server to the device.

[http-vmware-path-vuln](https://nmap.org/nsedoc/scripts/http-vmware-path-vuln.html)Checks for a path-traversal vulnerability in VMWare ESX, ESXi, and Server (CVE-2009-3733).

[http-vuln-cve2006-3392](https://nmap.org/nsedoc/scripts/http-vuln-cve2006-3392.html)Exploits a file disclosure vulnerability in Webmin (CVE-2006-3392)

[http-vuln-cve2009-3960](https://nmap.org/nsedoc/scripts/http-vuln-cve2009-3960.html)Exploits cve-2009-3960 also known as Adobe XML External Entity Injection.

[http-vuln-cve2010-0738](https://nmap.org/nsedoc/scripts/http-vuln-cve2010-0738.html)Tests whether a JBoss target is vulnerable to jmx console authentication bypass (CVE-2010-0738).

[http-vuln-cve2010-2861](https://nmap.org/nsedoc/scripts/http-vuln-cve2010-2861.html)Executes a directory traversal attack against a ColdFusion
server and tries to grab the password hash for the administrator user. It
then uses the salt value (hidden in the web page) to create the SHA1
HMAC hash that the web server needs for authentication as admin. You can
pass this value to the ColdFusion server as the admin without cracking
the password hash.

[http-vuln-cve2011-3192](https://nmap.org/nsedoc/scripts/http-vuln-cve2011-3192.html)Detects a denial of service vulnerability in the way the Apache web server
handles requests for multiple overlapping/simple ranges of a page.

[http-vuln-cve2011-3368](https://nmap.org/nsedoc/scripts/http-vuln-cve2011-3368.html)Tests for the CVE-2011-3368 (Reverse Proxy Bypass) vulnerability in Apache HTTP server's reverse proxy mode.
The script will run 3 tests:

- the loopback test, with 3 payloads to handle different rewrite rules
- the internal hosts test. According to Contextis, we expect a delay before a server error.
- The external website test. This does not mean that you can reach a LAN ip, but this is a relevant issue anyway.
[http-vuln-cve2012-1823](https://nmap.org/nsedoc/scripts/http-vuln-cve2012-1823.html)Detects PHP-CGI installations that are vulnerable to CVE-2012-1823, This
critical vulnerability allows attackers to retrieve source code and execute
code remotely.

[http-vuln-cve2013-0156](https://nmap.org/nsedoc/scripts/http-vuln-cve2013-0156.html)Detects Ruby on Rails servers vulnerable to object injection, remote command
executions and denial of service attacks. (CVE-2013-0156)

[http-vuln-cve2013-6786](https://nmap.org/nsedoc/scripts/http-vuln-cve2013-6786.html)Detects a URL redirection and reflected XSS vulnerability in Allegro RomPager
Web server. The vulnerability has been assigned CVE-2013-6786.

[http-vuln-cve2013-7091](https://nmap.org/nsedoc/scripts/http-vuln-cve2013-7091.html)An 0 day was released on the 6th December 2013 by rubina119, and was patched in Zimbra 7.2.6.

[http-vuln-cve2014-2126](https://nmap.org/nsedoc/scripts/http-vuln-cve2014-2126.html)Detects whether the Cisco ASA appliance is vulnerable to the Cisco ASA ASDM
Privilege Escalation Vulnerability (CVE-2014-2126).

[http-vuln-cve2014-2127](https://nmap.org/nsedoc/scripts/http-vuln-cve2014-2127.html)Detects whether the Cisco ASA appliance is vulnerable to the Cisco ASA SSL VPN
Privilege Escalation Vulnerability (CVE-2014-2127).

[http-vuln-cve2014-2128](https://nmap.org/nsedoc/scripts/http-vuln-cve2014-2128.html)Detects whether the Cisco ASA appliance is vulnerable to the Cisco ASA SSL VPN
Authentication Bypass Vulnerability (CVE-2014-2128).

[http-vuln-cve2014-2129](https://nmap.org/nsedoc/scripts/http-vuln-cve2014-2129.html)Detects whether the Cisco ASA appliance is vulnerable to the Cisco ASA SIP
Denial of Service Vulnerability (CVE-2014-2129).

[http-vuln-cve2014-3704](https://nmap.org/nsedoc/scripts/http-vuln-cve2014-3704.html)Exploits CVE-2014-3704 also known as 'Drupageddon' in Drupal. Versions < 7.32
of Drupal core are known to be affected.

[http-vuln-cve2014-8877](https://nmap.org/nsedoc/scripts/http-vuln-cve2014-8877.html)Exploits a remote code injection vulnerability (CVE-2014-8877) in Wordpress CM
Download Manager plugin. Versions <= 2.0.0 are known to be affected.

[http-vuln-cve2015-1427](https://nmap.org/nsedoc/scripts/http-vuln-cve2015-1427.html)This script attempts to detect a vulnerability, CVE-2015-1427, which  allows attackers
 to leverage features of this API to gain unauthenticated remote code execution (RCE).

[http-vuln-cve2015-1635](https://nmap.org/nsedoc/scripts/http-vuln-cve2015-1635.html)Checks for a remote code execution vulnerability (MS15-034) in Microsoft Windows systems (CVE2015-2015-1635).

[http-vuln-cve2017-1001000](https://nmap.org/nsedoc/scripts/http-vuln-cve2017-1001000.html)Attempts to detect a privilege escalation vulnerability in Wordpress 4.7.0 and 4.7.1 that
allows unauthenticated users to inject content in posts.

[http-vuln-cve2017-5638](https://nmap.org/nsedoc/scripts/http-vuln-cve2017-5638.html)Detects whether the specified URL is vulnerable to the Apache Struts
Remote Code Execution Vulnerability (CVE-2017-5638).

[http-vuln-cve2017-5689](https://nmap.org/nsedoc/scripts/http-vuln-cve2017-5689.html)Detects if a system with Intel Active Management Technology is vulnerable to the INTEL-SA-00075
privilege escalation vulnerability (CVE2017-5689).

[http-vuln-cve2017-8917](https://nmap.org/nsedoc/scripts/http-vuln-cve2017-8917.html)An SQL Injection vulnerability affecting Joomla! 3.7.x before 3.7.1 allows for
unauthenticated users to execute arbitrary SQL commands. This vulnerability was
caused by a new component,`com_fields`, which was introduced in
version 3.7. This component is publicly accessible, which means this can be
exploited by any malicious individual visiting the site.

[http-vuln-misfortune-cookie](https://nmap.org/nsedoc/scripts/http-vuln-misfortune-cookie.html)Detects the RomPager 4.07 Misfortune Cookie vulnerability by safely exploiting it.

[http-vuln-wnr1000-creds](https://nmap.org/nsedoc/scripts/http-vuln-wnr1000-creds.html)A vulnerability has been discovered in WNR 1000 series that allows an attacker
to retrieve administrator credentials with the router interface.
Tested On Firmware Version(s): V1.0.2.60_60.0.86 (Latest) and V1.0.2.54_60.0.82NA

[http-waf-detect](https://nmap.org/nsedoc/scripts/http-waf-detect.html)Attempts to determine whether a web server is protected by an IPS (Intrusion
Prevention System), IDS (Intrusion Detection System) or WAF (Web Application
Firewall) by probing the web server with malicious payloads and detecting
changes in the response code and body.

[http-waf-fingerprint](https://nmap.org/nsedoc/scripts/http-waf-fingerprint.html)Tries to detect the presence of a web application firewall and its type and
version.

[http-webdav-scan](https://nmap.org/nsedoc/scripts/http-webdav-scan.html)A script to detect WebDAV installations. Uses the OPTIONS and PROPFIND methods.

[http-wordpress-brute](https://nmap.org/nsedoc/scripts/http-wordpress-brute.html)performs brute force password auditing against Wordpress CMS/blog installations.

[http-wordpress-enum](https://nmap.org/nsedoc/scripts/http-wordpress-enum.html)Enumerates themes and plugins of Wordpress installations. The script can also detect
 outdated plugins by comparing version numbers with information pulled from api.wordpress.org.

[http-wordpress-users](https://nmap.org/nsedoc/scripts/http-wordpress-users.html)Enumerates usernames in Wordpress blog/CMS installations by exploiting an
information disclosure vulnerability existing in versions 2.6, 3.1, 3.1.1,
3.1.3 and 3.2-beta2 and possibly others.

[http-xssed](https://nmap.org/nsedoc/scripts/http-xssed.html)This script searches the xssed.com database and outputs the result.

[https-redirect](https://nmap.org/nsedoc/scripts/https-redirect.html)Check for HTTP services that redirect to the HTTPS on the same port.

[iax2-brute](https://nmap.org/nsedoc/scripts/iax2-brute.html)Performs brute force password auditing against the Asterisk IAX2 protocol.
Guessing fails when a large number of attempts is made due to the maxcallnumber limit (default 2048).
In case your getting "ERROR: Too many retries, aborted ..." after a while, this is most likely what's happening.
In order to avoid this problem try:
  - reducing the size of your dictionary
  - use the brute delay option to introduce a delay between guesses
  - split the guessing up in chunks and wait for a while between them

[iax2-version](https://nmap.org/nsedoc/scripts/iax2-version.html)Detects the UDP IAX2 service.

[icap-info](https://nmap.org/nsedoc/scripts/icap-info.html)Tests a list of known ICAP service names and prints information about
any it detects. The Internet Content Adaptation Protocol (ICAP) is
used to extend transparent proxy servers and is generally used for
content filtering and antivirus scanning.

[iec-identify](https://nmap.org/nsedoc/scripts/iec-identify.html)Attempts to identify IEC 60870-5-104 ICS protocol.

[iec61850-mms](https://nmap.org/nsedoc/scripts/iec61850-mms.html)Queries a IEC 61850-8-1 MMS server. Sends Initate-Request, Identify-Request and Read-Request to LN0 and LPHD.

[ike-version](https://nmap.org/nsedoc/scripts/ike-version.html)Obtains information (such as vendor and device type where available) from an
IKE service by sending four packets to the host.  This scripts tests with both
Main and Aggressive Mode and sends multiple transforms per request.

[imap-brute](https://nmap.org/nsedoc/scripts/imap-brute.html)Performs brute force password auditing against IMAP servers using either LOGIN, PLAIN, CRAM-MD5, DIGEST-MD5 or NTLM authentication.

[imap-capabilities](https://nmap.org/nsedoc/scripts/imap-capabilities.html)Retrieves IMAP email server capabilities.

[imap-ntlm-info](https://nmap.org/nsedoc/scripts/imap-ntlm-info.html)This script enumerates information from remote IMAP services with NTLM
authentication enabled.

[impress-remote-discover](https://nmap.org/nsedoc/scripts/impress-remote-discover.html)Tests for the presence of the LibreOffice Impress Remote server.
Checks if a PIN is valid if provided and will bruteforce the PIN
if requested.

[informix-brute](https://nmap.org/nsedoc/scripts/informix-brute.html)Performs brute force password auditing against IBM Informix Dynamic Server.

[informix-query](https://nmap.org/nsedoc/scripts/informix-query.html)Runs a query against IBM Informix Dynamic Server using the given
authentication credentials (see also: informix-brute).

[informix-tables](https://nmap.org/nsedoc/scripts/informix-tables.html)Retrieves a list of tables and column definitions for each database on an Informix server.

[ip-forwarding](https://nmap.org/nsedoc/scripts/ip-forwarding.html)Detects whether the remote device has ip forwarding or "Internet connection
sharing" enabled, by sending an ICMP echo request to a given target using
the scanned host as default gateway.

[ip-geolocation-geoplugin](https://nmap.org/nsedoc/scripts/ip-geolocation-geoplugin.html)Tries to identify the physical location of an IP address using the
Geoplugin geolocation web service ([http://www.geoplugin.com/](http://www.geoplugin.com/)). There
is no limit on lookups using this service.

[ip-geolocation-ipinfodb](https://nmap.org/nsedoc/scripts/ip-geolocation-ipinfodb.html)Tries to identify the physical location of an IP address using the
IPInfoDB geolocation web service
([http://ipinfodb.com/ip_location_api.php](http://ipinfodb.com/ip_location_api.php)).

[ip-geolocation-map-bing](https://nmap.org/nsedoc/scripts/ip-geolocation-map-bing.html)This script queries the Nmap registry for the GPS coordinates of targets stored
by previous geolocation scripts and renders a Bing Map of markers representing
the targets.

[ip-geolocation-map-google](https://nmap.org/nsedoc/scripts/ip-geolocation-map-google.html)This script queries the Nmap registry for the GPS coordinates of targets stored
by previous geolocation scripts and renders a Google Map of markers representing
the targets.

[ip-geolocation-map-kml](https://nmap.org/nsedoc/scripts/ip-geolocation-map-kml.html)This script queries the Nmap registry for the GPS coordinates of targets stored
by previous geolocation scripts and produces a KML file of points representing
the targets.

[ip-geolocation-maxmind](https://nmap.org/nsedoc/scripts/ip-geolocation-maxmind.html)Tries to identify the physical location of an IP address using a
Geolocation Maxmind database file (available from[http://www.maxmind.com/app/ip-location](http://www.maxmind.com/app/ip-location)). This script supports queries
using all Maxmind databases that are supported by their API including
the commercial ones.

[ip-https-discover](https://nmap.org/nsedoc/scripts/ip-https-discover.html)Checks if the IP over HTTPS (IP-HTTPS) Tunneling Protocol [1] is supported.

[ipidseq](https://nmap.org/nsedoc/scripts/ipidseq.html)Classifies a host's IP ID sequence (test for susceptibility to idle
scan).

[ipmi-brute](https://nmap.org/nsedoc/scripts/ipmi-brute.html)Performs brute force password auditing against IPMI RPC server.

[ipmi-cipher-zero](https://nmap.org/nsedoc/scripts/ipmi-cipher-zero.html)IPMI 2.0 Cipher Zero Authentication Bypass Scanner. This module identifies IPMI 2.0
  compatible systems that are vulnerable to an authentication bypass vulnerability
  through the use of cipher zero.

[ipmi-version](https://nmap.org/nsedoc/scripts/ipmi-version.html)Performs IPMI Information Discovery through Channel Auth probes.

[ipv6-multicast-mld-list](https://nmap.org/nsedoc/scripts/ipv6-multicast-mld-list.html)Uses Multicast Listener Discovery to list the multicast addresses subscribed to
by IPv6 multicast listeners on the link-local scope. Addresses in the IANA IPv6
Multicast Address Space Registry have their descriptions listed.

[ipv6-node-info](https://nmap.org/nsedoc/scripts/ipv6-node-info.html)Obtains hostnames, IPv4 and IPv6 addresses through IPv6 Node Information Queries.

[ipv6-ra-flood](https://nmap.org/nsedoc/scripts/ipv6-ra-flood.html)Generates a flood of Router Advertisements (RA) with random source MAC
addresses and IPv6 prefixes. Computers, which have stateless autoconfiguration
enabled by default (every major OS), will start to compute IPv6 suffix and
update their routing table to reflect the accepted announcement. This will
cause 100% CPU usage on Windows and platforms, preventing to process other
application requests.

[irc-botnet-channels](https://nmap.org/nsedoc/scripts/irc-botnet-channels.html)Checks an IRC server for channels that are commonly used by malicious botnets.

[irc-brute](https://nmap.org/nsedoc/scripts/irc-brute.html)Performs brute force password auditing against IRC (Internet Relay Chat) servers.

[irc-info](https://nmap.org/nsedoc/scripts/irc-info.html)Gathers information from an IRC server.

[irc-sasl-brute](https://nmap.org/nsedoc/scripts/irc-sasl-brute.html)Performs brute force password auditing against IRC (Internet Relay Chat) servers supporting SASL authentication.

[irc-unrealircd-backdoor](https://nmap.org/nsedoc/scripts/irc-unrealircd-backdoor.html)Checks if an IRC server is backdoored by running a time-based command (ping)
and checking how long it takes to respond.

[iscsi-brute](https://nmap.org/nsedoc/scripts/iscsi-brute.html)Performs brute force password auditing against iSCSI targets.

[iscsi-info](https://nmap.org/nsedoc/scripts/iscsi-info.html)Collects and displays information from remote iSCSI targets.

[isns-info](https://nmap.org/nsedoc/scripts/isns-info.html)Lists portals and iSCSI nodes registered with the Internet Storage Name
Service (iSNS).

[jdwp-exec](https://nmap.org/nsedoc/scripts/jdwp-exec.html)Attempts to exploit java's remote debugging port. When remote debugging
port is left open, it is possible to inject java bytecode and achieve
remote code execution.  This script abuses this to inject and execute
a Java class file that executes the supplied shell command and returns
its output.

[jdwp-info](https://nmap.org/nsedoc/scripts/jdwp-info.html)Attempts to exploit java's remote debugging port.  When remote
debugging port is left open, it is possible to inject java bytecode
and achieve remote code execution.  This script injects and execute a
Java class file that returns remote system information.

[jdwp-inject](https://nmap.org/nsedoc/scripts/jdwp-inject.html)Attempts to exploit java's remote debugging port.  When remote debugging port
is left open, it is possible to inject  java bytecode and achieve remote code
execution.  This script allows injection of arbitrary class files.

[jdwp-version](https://nmap.org/nsedoc/scripts/jdwp-version.html)Detects the Java Debug Wire Protocol. This protocol is used by Java programs
to be debugged via the network. It should not be open to the public Internet,
as it does not provide any security against malicious attackers who can inject
their own bytecode into the debugged process.

[knx-gateway-discover](https://nmap.org/nsedoc/scripts/knx-gateway-discover.html)Discovers KNX gateways by sending a KNX Search Request to the multicast address
224.0.23.12 including a UDP payload with destination port 3671. KNX gateways
will respond with a KNX Search Response including various information about the
gateway, such as KNX address and supported services.

[knx-gateway-info](https://nmap.org/nsedoc/scripts/knx-gateway-info.html)Identifies a KNX gateway on UDP port 3671 by sending a KNX Description Request.

[krb5-enum-users](https://nmap.org/nsedoc/scripts/krb5-enum-users.html)Discovers valid usernames by brute force querying likely usernames against a Kerberos service.
When an invalid username is requested the server will respond using the
Kerberos error code KRB5KDC_ERR_C_PRINCIPAL_UNKNOWN, allowing us to determine
that the user name was invalid. Valid user names will illicit either the
TGT in a AS-REP response or the error KRB5KDC_ERR_PREAUTH_REQUIRED, signaling
that the user is required to perform pre authentication.

[ldap-brute](https://nmap.org/nsedoc/scripts/ldap-brute.html)Attempts to brute-force LDAP authentication. By default
it uses the built-in username and password lists. In order to use your
own lists use the`userdb`and`passdb`script arguments.

[ldap-novell-getpass](https://nmap.org/nsedoc/scripts/ldap-novell-getpass.html)Universal Password enables advanced password policies, including extended
characters in passwords, synchronization of passwords from eDirectory to
other systems, and a single password for all access to eDirectory.

[ldap-rootdse](https://nmap.org/nsedoc/scripts/ldap-rootdse.html)Retrieves the LDAP root DSA-specific Entry (DSE)

[ldap-search](https://nmap.org/nsedoc/scripts/ldap-search.html)Attempts to perform an LDAP search and returns all matches.

[lexmark-config](https://nmap.org/nsedoc/scripts/lexmark-config.html)Retrieves configuration information from a Lexmark S300-S400 printer.

[llmnr-resolve](https://nmap.org/nsedoc/scripts/llmnr-resolve.html)Resolves a hostname by using the LLMNR (Link-Local Multicast Name Resolution) protocol.

[lltd-discovery](https://nmap.org/nsedoc/scripts/lltd-discovery.html)Uses the Microsoft LLTD protocol to discover hosts on a local network.

[lu-enum](https://nmap.org/nsedoc/scripts/lu-enum.html)Attempts to enumerate Logical Units (LU) of TN3270E servers.

[maxdb-info](https://nmap.org/nsedoc/scripts/maxdb-info.html)Retrieves version and database information from a SAP Max DB database.

[mcafee-epo-agent](https://nmap.org/nsedoc/scripts/mcafee-epo-agent.html)Check if ePO agent is running on port 8081 or port identified as ePO Agent port.

[membase-brute](https://nmap.org/nsedoc/scripts/membase-brute.html)Performs brute force password auditing against Couchbase Membase servers.

[membase-http-info](https://nmap.org/nsedoc/scripts/membase-http-info.html)Retrieves information (hostname, OS, uptime, etc.) from the CouchBase
Web Administration port.  The information retrieved by this script
does not require any credentials.

[memcached-info](https://nmap.org/nsedoc/scripts/memcached-info.html)Retrieves information (including system architecture, process ID, and
server time) from distributed memory object caching system memcached.

[metasploit-info](https://nmap.org/nsedoc/scripts/metasploit-info.html)Gathers info from the Metasploit rpc service.  It requires a valid login pair.
After authentication it tries to determine Metasploit version and deduce the OS
type.  Then it creates a new console and executes few commands to get
additional info.

[metasploit-msgrpc-brute](https://nmap.org/nsedoc/scripts/metasploit-msgrpc-brute.html)Performs brute force username and password auditing against
Metasploit msgrpc interface.

[metasploit-xmlrpc-brute](https://nmap.org/nsedoc/scripts/metasploit-xmlrpc-brute.html)Performs brute force password auditing against a Metasploit RPC server using the XMLRPC protocol.

[mikrotik-routeros-brute](https://nmap.org/nsedoc/scripts/mikrotik-routeros-brute.html)Performs brute force password auditing against Mikrotik RouterOS devices with the API RouterOS interface enabled.

[mikrotik-routeros-username-brute](https://nmap.org/nsedoc/scripts/mikrotik-routeros-username-brute.html)Attempts to enumerate valid usernames on MikroTik devices running the Winbox service on port 8291 in MikroTik-RouterOS.

[mikrotik-routeros-version](https://nmap.org/nsedoc/scripts/mikrotik-routeros-version.html)Detects MikroTik RouterOS version from devices running the Winbox service on port 8291.

[mmouse-brute](https://nmap.org/nsedoc/scripts/mmouse-brute.html)Performs brute force password auditing against the RPA Tech Mobile Mouse
servers.

[mmouse-exec](https://nmap.org/nsedoc/scripts/mmouse-exec.html)Connects to an RPA Tech Mobile Mouse server, starts an application and
sends a sequence of keys to it. Any application that the user has
access to can be started and the key sequence is sent to the
application after it has been started.

[modbus-discover](https://nmap.org/nsedoc/scripts/modbus-discover.html)Enumerates SCADA Modbus slave ids (sids) and collects their device information.

[mongodb-brute](https://nmap.org/nsedoc/scripts/mongodb-brute.html)Performs brute force password auditing against the MongoDB database.

[mongodb-databases](https://nmap.org/nsedoc/scripts/mongodb-databases.html)Attempts to get a list of tables from a MongoDB database.

[mongodb-info](https://nmap.org/nsedoc/scripts/mongodb-info.html)Attempts to get build info and server status from a MongoDB database.

[mqtt-subscribe](https://nmap.org/nsedoc/scripts/mqtt-subscribe.html)Dumps message traffic from MQTT brokers.

[mrinfo](https://nmap.org/nsedoc/scripts/mrinfo.html)Queries targets for multicast routing information.

[ms-sql-brute](https://nmap.org/nsedoc/scripts/ms-sql-brute.html)Performs password guessing against Microsoft SQL Server (ms-sql). Works best in
conjunction with the`broadcast-ms-sql-discover`script.

[ms-sql-config](https://nmap.org/nsedoc/scripts/ms-sql-config.html)Queries Microsoft SQL Server (ms-sql) instances for a list of databases, linked servers,
and configuration settings.

[ms-sql-dac](https://nmap.org/nsedoc/scripts/ms-sql-dac.html)Queries the Microsoft SQL Browser service for the DAC (Dedicated Admin
Connection) port of a given (or all) SQL Server instance. The DAC port
is used to connect to the database instance when normal connection
attempts fail, for example, when server is hanging, out of memory or
in other bad states. In addition, the DAC port provides an admin with
access to system objects otherwise not accessible over normal
connections.

[ms-sql-dump-hashes](https://nmap.org/nsedoc/scripts/ms-sql-dump-hashes.html)Dumps the password hashes from an MS-SQL server in a format suitable for
cracking by tools such as John-the-ripper. In order to do so the user
needs to have the appropriate DB privileges.

[ms-sql-empty-password](https://nmap.org/nsedoc/scripts/ms-sql-empty-password.html)Attempts to authenticate to Microsoft SQL Servers using an empty password for
the sysadmin (sa) account.

[ms-sql-hasdbaccess](https://nmap.org/nsedoc/scripts/ms-sql-hasdbaccess.html)Queries Microsoft SQL Server (ms-sql) instances for a list of databases a user has
access to.

[ms-sql-info](https://nmap.org/nsedoc/scripts/ms-sql-info.html)Attempts to determine configuration and version information for Microsoft SQL
Server instances.

[ms-sql-ntlm-info](https://nmap.org/nsedoc/scripts/ms-sql-ntlm-info.html)This script enumerates information from remote Microsoft SQL services with NTLM
authentication enabled.

[ms-sql-query](https://nmap.org/nsedoc/scripts/ms-sql-query.html)Runs a query against Microsoft SQL Server (ms-sql).

[ms-sql-tables](https://nmap.org/nsedoc/scripts/ms-sql-tables.html)Queries Microsoft SQL Server (ms-sql) for a list of tables per database.

[ms-sql-xp-cmdshell](https://nmap.org/nsedoc/scripts/ms-sql-xp-cmdshell.html)Attempts to run a command using the command shell of Microsoft SQL
Server (ms-sql).

[msrpc-enum](https://nmap.org/nsedoc/scripts/msrpc-enum.html)Queries an MSRPC endpoint mapper for a list of mapped
services and displays the gathered information.

[mtrace](https://nmap.org/nsedoc/scripts/mtrace.html)Queries for the multicast path from a source to a destination host.

[multicast-profinet-discovery](https://nmap.org/nsedoc/scripts/multicast-profinet-discovery.html)Sends a multicast PROFINET DCP Identify All message and prints the responses.

[murmur-version](https://nmap.org/nsedoc/scripts/murmur-version.html)Detects the Murmur service (server for the Mumble voice communication
client) versions 1.2.X.

[mysql-audit](https://nmap.org/nsedoc/scripts/mysql-audit.html)Audits MySQL database server security configuration against parts of
the CIS MySQL v1.0.2 benchmark (the engine can be used for other MySQL
audits by creating appropriate audit files).

[mysql-brute](https://nmap.org/nsedoc/scripts/mysql-brute.html)Performs password guessing against MySQL.

[mysql-databases](https://nmap.org/nsedoc/scripts/mysql-databases.html)Attempts to list all databases on a MySQL server.

[mysql-dump-hashes](https://nmap.org/nsedoc/scripts/mysql-dump-hashes.html)Dumps the password hashes from an MySQL server in a format suitable for
cracking by tools such as John the Ripper.  Appropriate DB privileges (root) are required.

[mysql-empty-password](https://nmap.org/nsedoc/scripts/mysql-empty-password.html)Checks for MySQL servers with an empty password for`root`or`anonymous`.

[mysql-enum](https://nmap.org/nsedoc/scripts/mysql-enum.html)Performs valid-user enumeration against MySQL server using a bug
discovered and published by Kingcope
([http://seclists.org/fulldisclosure/2012/Dec/9](http://seclists.org/fulldisclosure/2012/Dec/9)).

[mysql-info](https://nmap.org/nsedoc/scripts/mysql-info.html)Connects to a MySQL server and prints information such as the protocol and
version numbers, thread ID, status, capabilities, and the password salt.

[mysql-query](https://nmap.org/nsedoc/scripts/mysql-query.html)Runs a query against a MySQL database and returns the results as a table.

[mysql-users](https://nmap.org/nsedoc/scripts/mysql-users.html)Attempts to list all users on a MySQL server.

[mysql-variables](https://nmap.org/nsedoc/scripts/mysql-variables.html)Attempts to show all variables on a MySQL server.

[mysql-vuln-cve2012-2122](https://nmap.org/nsedoc/scripts/mysql-vuln-cve2012-2122.html)

[nat-pmp-info](https://nmap.org/nsedoc/scripts/nat-pmp-info.html)Gets the routers WAN IP using the NAT Port Mapping Protocol (NAT-PMP).
The NAT-PMP protocol is supported by a broad range of routers including:

- Apple AirPort Express
- Apple AirPort Extreme
- Apple Time Capsule
- DD-WRT
- OpenWrt v8.09 or higher, with MiniUPnP daemon
- pfSense v2.0
- Tarifa (firmware) (Linksys WRT54G/GL/GS)
- Tomato Firmware v1.24 or higher. (Linksys WRT54G/GL/GS and many more)
- Peplink Balance
[nat-pmp-mapport](https://nmap.org/nsedoc/scripts/nat-pmp-mapport.html)Maps a WAN port on the router to a local port on the client using the NAT Port Mapping Protocol (NAT-PMP).  It supports the following operations:

- map - maps a new external port on the router to an internal port of the requesting IP
- unmap - unmaps a previously mapped port for the requesting IP
- unmapall - unmaps all previously mapped ports for the requesting IP
[nbd-info](https://nmap.org/nsedoc/scripts/nbd-info.html)Displays protocol and block device information from NBD servers.

[nbns-interfaces](https://nmap.org/nsedoc/scripts/nbns-interfaces.html)Retrieves IP addresses of the target's network interfaces via NetBIOS NS.
Additional network interfaces may reveal more information about the target,
including finding paths to hidden non-routed networks via multihomed systems.

[nbstat](https://nmap.org/nsedoc/scripts/nbstat.html)Attempts to retrieve the target's NetBIOS names and MAC address.

[ncp-enum-users](https://nmap.org/nsedoc/scripts/ncp-enum-users.html)Retrieves a list of all eDirectory users from the Novell NetWare Core Protocol (NCP) service.

[ncp-serverinfo](https://nmap.org/nsedoc/scripts/ncp-serverinfo.html)Retrieves eDirectory server information (OS version, server name,
mounts, etc.) from the Novell NetWare Core Protocol (NCP) service.

[ndmp-fs-info](https://nmap.org/nsedoc/scripts/ndmp-fs-info.html)Lists remote file systems by querying the remote device using the Network
Data Management Protocol (ndmp). NDMP is a protocol intended to transport
data between a NAS device and the backup device, removing the need for the
data to pass through the backup server. The following products are known
to support the protocol:

- Amanda
- Bacula
- CA Arcserve
- CommVault Simpana
- EMC Networker
- Hitachi Data Systems
- IBM Tivoli
- Quest Software Netvault Backup
- Symantec Netbackup
- Symantec Backup Exec
[ndmp-version](https://nmap.org/nsedoc/scripts/ndmp-version.html)Retrieves version information from the remote Network Data Management Protocol
(ndmp) service. NDMP is a protocol intended to transport data between a NAS
device and the backup device, removing the need for the data to pass through
the backup server. The following products are known to support the protocol:

- Amanda
- Bacula
- CA Arcserve
- CommVault Simpana
- EMC Networker
- Hitachi Data Systems
- IBM Tivoli
- Quest Software Netvault Backup
- Symantec Netbackup
- Symantec Backup Exec
[nessus-brute](https://nmap.org/nsedoc/scripts/nessus-brute.html)Performs brute force password auditing against a Nessus vulnerability scanning daemon using the NTP 1.2 protocol.

[nessus-xmlrpc-brute](https://nmap.org/nsedoc/scripts/nessus-xmlrpc-brute.html)Performs brute force password auditing against a Nessus vulnerability scanning daemon using the XMLRPC protocol.

[netbus-auth-bypass](https://nmap.org/nsedoc/scripts/netbus-auth-bypass.html)Checks if a NetBus server is vulnerable to an authentication bypass
vulnerability which allows full access without knowing the password.

[netbus-brute](https://nmap.org/nsedoc/scripts/netbus-brute.html)Performs brute force password auditing against the Netbus backdoor ("remote administration") service.

[netbus-info](https://nmap.org/nsedoc/scripts/netbus-info.html)Opens a connection to a NetBus server and extracts information about
the host and the NetBus service itself.

[netbus-version](https://nmap.org/nsedoc/scripts/netbus-version.html)Extends version detection to detect NetBuster, a honeypot service
that mimes NetBus.

[nexpose-brute](https://nmap.org/nsedoc/scripts/nexpose-brute.html)Performs brute force password auditing against a Nexpose vulnerability scanner
using the API 1.1.

[nfs-ls](https://nmap.org/nsedoc/scripts/nfs-ls.html)Attempts to get useful information about files from NFS exports.
The output is intended to resemble the output of`ls`.

[nfs-showmount](https://nmap.org/nsedoc/scripts/nfs-showmount.html)Shows NFS exports, like the`showmount -e`command.

[nfs-statfs](https://nmap.org/nsedoc/scripts/nfs-statfs.html)Retrieves disk space statistics and information from a remote NFS share.
The output is intended to resemble the output of`df`.

[nje-node-brute](https://nmap.org/nsedoc/scripts/nje-node-brute.html)z/OS JES Network Job Entry (NJE) target node name brute force.

[nje-pass-brute](https://nmap.org/nsedoc/scripts/nje-pass-brute.html)z/OS JES Network Job Entry (NJE) 'I record' password brute forcer.

[nntp-ntlm-info](https://nmap.org/nsedoc/scripts/nntp-ntlm-info.html)This script enumerates information from remote NNTP services with NTLM
authentication enabled.

[nping-brute](https://nmap.org/nsedoc/scripts/nping-brute.html)Performs brute force password auditing against an Nping Echo service.

[nrpe-enum](https://nmap.org/nsedoc/scripts/nrpe-enum.html)Queries Nagios Remote Plugin Executor (NRPE) daemons to obtain information such
as load averages, process counts, logged in user information, etc.

[ntp-info](https://nmap.org/nsedoc/scripts/ntp-info.html)Gets the time and configuration variables from an NTP server. We send two
requests: a time request and a "read variables" (opcode 2) control message.
Without verbosity, the script shows the time and the value of the`version`,`processor`,`system`,`refid`, and`stratum`variables. With verbosity, all
variables are shown.

[ntp-monlist](https://nmap.org/nsedoc/scripts/ntp-monlist.html)Obtains and prints an NTP server's monitor data.

[omp2-brute](https://nmap.org/nsedoc/scripts/omp2-brute.html)Performs brute force password auditing against the OpenVAS manager using OMPv2.

[omp2-enum-targets](https://nmap.org/nsedoc/scripts/omp2-enum-targets.html)Attempts to retrieve the list of target systems and networks from an OpenVAS Manager server.

[omron-info](https://nmap.org/nsedoc/scripts/omron-info.html)This NSE script is used to send a FINS packet to a remote device. The script
will send a Controller Data Read Command and once a response is received, it
validates that it was a proper response to the command that was sent, and then
will parse out the data.

[openflow-info](https://nmap.org/nsedoc/scripts/openflow-info.html)Queries OpenFlow controllers for information. Newer versions of the OpenFlow
protocol (1.3 and greater) will return a list of all protocol versions supported
by the controller. Versions prior to 1.3 only return their own version number.

[openlookup-info](https://nmap.org/nsedoc/scripts/openlookup-info.html)Parses and displays the banner information of an OpenLookup (network key-value store) server.

[openvas-otp-brute](https://nmap.org/nsedoc/scripts/openvas-otp-brute.html)Performs brute force password auditing against a OpenVAS vulnerability scanner daemon using the OTP 1.0 protocol.

[openwebnet-discovery](https://nmap.org/nsedoc/scripts/openwebnet-discovery.html)OpenWebNet is a communications protocol developed by Bticino since 2000.
Retrieves device identifying information and number of connected devices.

[oracle-brute](https://nmap.org/nsedoc/scripts/oracle-brute.html)Performs brute force password auditing against Oracle servers.

[oracle-brute-stealth](https://nmap.org/nsedoc/scripts/oracle-brute-stealth.html)Exploits the CVE-2012-3137 vulnerability, a weakness in Oracle's
O5LOGIN authentication scheme.  The vulnerability exists in Oracle 11g
R1/R2 and allows linking the session key to a password hash.  When
initiating an authentication attempt as a valid user the server will
respond with a session key and salt.  Once received the script will
disconnect the connection thereby not recording the login attempt.
The session key and salt can then be used to brute force the users
password.

[oracle-enum-users](https://nmap.org/nsedoc/scripts/oracle-enum-users.html)Attempts to enumerate valid Oracle user names against unpatched Oracle 11g
servers (this bug was fixed in Oracle's October 2009 Critical Patch Update).

[oracle-sid-brute](https://nmap.org/nsedoc/scripts/oracle-sid-brute.html)Guesses Oracle instance/SID names against the TNS-listener.

[oracle-tns-version](https://nmap.org/nsedoc/scripts/oracle-tns-version.html)Decodes the VSNNUM version number from an Oracle TNS listener.

[ovs-agent-version](https://nmap.org/nsedoc/scripts/ovs-agent-version.html)Detects the version of an Oracle Virtual Server Agent by fingerprinting
responses to an HTTP GET request and an XML-RPC method call.

[p2p-conficker](https://nmap.org/nsedoc/scripts/p2p-conficker.html)Checks if a host is infected with Conficker.C or higher, based on
Conficker's peer to peer communication.

[path-mtu](https://nmap.org/nsedoc/scripts/path-mtu.html)Performs simple Path MTU Discovery to target hosts.

[pcanywhere-brute](https://nmap.org/nsedoc/scripts/pcanywhere-brute.html)Performs brute force password auditing against the pcAnywhere remote access protocol.

[pcworx-info](https://nmap.org/nsedoc/scripts/pcworx-info.html)This NSE script will query and parse pcworx protocol to a remote PLC.
The script will send a initial request packets and once a response is received,
it validates that it was a proper response to the command that was sent, and then
will parse out the data. PCWorx is a protocol and Program by Phoenix Contact.

[pgsql-brute](https://nmap.org/nsedoc/scripts/pgsql-brute.html)Performs password guessing against PostgreSQL.

[pjl-ready-message](https://nmap.org/nsedoc/scripts/pjl-ready-message.html)Retrieves or sets the ready message on printers that support the Printer
Job Language. This includes most PostScript printers that listen on port
9100. Without an argument, displays the current ready message. With the`pjl_ready_message`script argument, displays the old ready
message and changes it to the message given.

[pop3-brute](https://nmap.org/nsedoc/scripts/pop3-brute.html)Tries to log into a POP3 account by guessing usernames and passwords.

[pop3-capabilities](https://nmap.org/nsedoc/scripts/pop3-capabilities.html)Retrieves POP3 email server capabilities.

[pop3-ntlm-info](https://nmap.org/nsedoc/scripts/pop3-ntlm-info.html)This script enumerates information from remote POP3 services with NTLM
authentication enabled.

[port-states](https://nmap.org/nsedoc/scripts/port-states.html)Prints a list of ports found in each state.

[pptp-version](https://nmap.org/nsedoc/scripts/pptp-version.html)Attempts to extract system information from the point-to-point tunneling protocol (PPTP) service.

[profinet-cm-lookup](https://nmap.org/nsedoc/scripts/profinet-cm-lookup.html)Sends a DCERPC EPM Lookup Request to PROFINET devices. the DCE/RPC Endpoint Mapper (EPM) targeting Profinet Devices.

[puppet-naivesigning](https://nmap.org/nsedoc/scripts/puppet-naivesigning.html)Detects if naive signing is enabled on a Puppet server. This enables attackers
to create any Certificate Signing Request and have it signed, allowing them
to impersonate as a puppet agent. This can leak the configuration of the agents
as well as any other sensitive information found in the configuration files.

[qconn-exec](https://nmap.org/nsedoc/scripts/qconn-exec.html)Attempts to identify whether a listening QNX QCONN daemon allows
unauthenticated users to execute arbitrary operating system commands.

[qscan](https://nmap.org/nsedoc/scripts/qscan.html)Repeatedly probe open and/or closed ports on a host to obtain a series
of round-trip time values for each port.  These values are used to
group collections of ports which are statistically different from other
groups.  Ports being in different groups (or "families") may be due to
network mechanisms such as port forwarding to machines behind a NAT.

[quake1-info](https://nmap.org/nsedoc/scripts/quake1-info.html)Extracts information from Quake game servers and other game servers
which use the same protocol.

[quake3-info](https://nmap.org/nsedoc/scripts/quake3-info.html)Extracts information from a Quake3 game server and other games which use the same protocol.

[quake3-master-getservers](https://nmap.org/nsedoc/scripts/quake3-master-getservers.html)Queries Quake3-style master servers for game servers (many games other than Quake 3 use this same protocol).

[rdp-enum-encryption](https://nmap.org/nsedoc/scripts/rdp-enum-encryption.html)Determines which Security layer and Encryption level is supported by the
RDP service. It does so by cycling through all existing protocols and ciphers.
When run in debug mode, the script also returns the protocols and ciphers that
fail and any errors that were reported.

[rdp-ntlm-info](https://nmap.org/nsedoc/scripts/rdp-ntlm-info.html)This script enumerates information from remote RDP services with CredSSP
(NLA) authentication enabled.

[rdp-vuln-ms12-020](https://nmap.org/nsedoc/scripts/rdp-vuln-ms12-020.html)Checks if a machine is vulnerable to MS12-020 RDP vulnerability.

[realvnc-auth-bypass](https://nmap.org/nsedoc/scripts/realvnc-auth-bypass.html)Checks if a VNC server is vulnerable to the RealVNC authentication bypass
(CVE-2006-2369).

[redis-brute](https://nmap.org/nsedoc/scripts/redis-brute.html)Performs brute force passwords auditing against a Redis key-value store.

[redis-info](https://nmap.org/nsedoc/scripts/redis-info.html)Retrieves information (such as version number and architecture) from a Redis key-value store.

[resolveall](https://nmap.org/nsedoc/scripts/resolveall.html)NOTE: This script has been replaced by the`--resolve-all`command-line option in Nmap 7.70

[reverse-index](https://nmap.org/nsedoc/scripts/reverse-index.html)Creates a reverse index at the end of scan output showing which hosts run a
particular service.  This is in addition to Nmap's normal output listing the
services on each host.

[rexec-brute](https://nmap.org/nsedoc/scripts/rexec-brute.html)Performs brute force password auditing against the classic UNIX rexec (remote exec) service.

[rfc868-time](https://nmap.org/nsedoc/scripts/rfc868-time.html)Retrieves the day and time from the Time service.

[riak-http-info](https://nmap.org/nsedoc/scripts/riak-http-info.html)Retrieves information (such as node name and architecture) from a Basho Riak distributed database using the HTTP protocol.

[rlogin-brute](https://nmap.org/nsedoc/scripts/rlogin-brute.html)Performs brute force password auditing against the classic UNIX rlogin (remote
login) service.  This script must be run in privileged mode on UNIX because it
must bind to a low source port number.

[rmi-dumpregistry](https://nmap.org/nsedoc/scripts/rmi-dumpregistry.html)Connects to a remote RMI registry and attempts to dump all of its
objects.

[rmi-vuln-classloader](https://nmap.org/nsedoc/scripts/rmi-vuln-classloader.html)Tests whether Java rmiregistry allows class loading.  The default
configuration of rmiregistry allows loading classes from remote URLs,
which can lead to remote code execution. The vendor (Oracle/Sun)
classifies this as a design feature.

[rpc-grind](https://nmap.org/nsedoc/scripts/rpc-grind.html)Fingerprints the target RPC port to extract the target service, RPC number and version.

[rpcap-brute](https://nmap.org/nsedoc/scripts/rpcap-brute.html)Performs brute force password auditing against the WinPcap Remote Capture
Daemon (rpcap).

[rpcap-info](https://nmap.org/nsedoc/scripts/rpcap-info.html)Connects to the rpcap service (provides remote sniffing capabilities
through WinPcap) and retrieves interface information. The service can either be
setup to require authentication or not and also supports IP restrictions.

[rpcinfo](https://nmap.org/nsedoc/scripts/rpcinfo.html)Connects to portmapper and fetches a list of all registered programs.  It then
prints out a table including (for each program) the RPC program number,
supported version numbers, port number and protocol, and program name.

[rsa-vuln-roca](https://nmap.org/nsedoc/scripts/rsa-vuln-roca.html)Detects RSA keys vulnerable to Return Of Coppersmith Attack (ROCA) factorization.

[rsync-brute](https://nmap.org/nsedoc/scripts/rsync-brute.html)Performs brute force password auditing against the rsync remote file syncing protocol.

[rsync-list-modules](https://nmap.org/nsedoc/scripts/rsync-list-modules.html)Lists modules available for rsync (remote file sync) synchronization.

[rtsp-methods](https://nmap.org/nsedoc/scripts/rtsp-methods.html)Determines which methods are supported by the RTSP (real time streaming protocol) server.

[rtsp-url-brute](https://nmap.org/nsedoc/scripts/rtsp-url-brute.html)Attempts to enumerate RTSP media URLS by testing for common paths on devices such as surveillance IP cameras.

[rusers](https://nmap.org/nsedoc/scripts/rusers.html)Connects to rusersd RPC service and retrieves a list of logged-in users.

[s7-info](https://nmap.org/nsedoc/scripts/s7-info.html)Enumerates Siemens S7 PLC Devices and collects their device information. This
script is based off PLCScan that was developed by Positive Research and
Scadastrangelove ([https://code.google.com/p/plcscan/](https://code.google.com/p/plcscan/)). This script is meant to
provide the same functionality as PLCScan inside of Nmap. Some of the
information that is collected by PLCScan was not ported over; this
information can be parsed out of the packets that are received.

[samba-vuln-cve-2012-1182](https://nmap.org/nsedoc/scripts/samba-vuln-cve-2012-1182.html)Checks if target machines are vulnerable to the Samba heap overflow vulnerability CVE-2012-1182.

[servicetags](https://nmap.org/nsedoc/scripts/servicetags.html)Attempts to extract system information (OS, hardware, etc.) from the Sun Service Tags service agent (UDP port 6481).

[shodan-api](https://nmap.org/nsedoc/scripts/shodan-api.html)Queries Shodan API for given targets and produces similar output to
a -sV nmap scan. The ShodanAPI key can be set with the 'apikey' script
argument, or hardcoded in the .nse file itself. You can get a free key from[https://developer.shodan.io](https://developer.shodan.io/)

[sip-brute](https://nmap.org/nsedoc/scripts/sip-brute.html)Performs brute force password auditing against Session Initiation Protocol
(SIP) accounts. This protocol is most commonly associated with VoIP sessions.

[sip-call-spoof](https://nmap.org/nsedoc/scripts/sip-call-spoof.html)Spoofs a call to a SIP phone and detects the action taken by the target (busy, declined, hung up, etc.)

[sip-enum-users](https://nmap.org/nsedoc/scripts/sip-enum-users.html)Enumerates a SIP server's valid extensions (users).

[sip-methods](https://nmap.org/nsedoc/scripts/sip-methods.html)Enumerates a SIP Server's allowed methods (INVITE, OPTIONS, SUBSCRIBE, etc.)

[skypev2-version](https://nmap.org/nsedoc/scripts/skypev2-version.html)Detects the Skype version 2 service.

[smb-brute](https://nmap.org/nsedoc/scripts/smb-brute.html)Attempts to guess username/password combinations over SMB, storing discovered combinations
for use in other scripts. Every attempt will be made to get a valid list of users and to
verify each username before actually using them. When a username is discovered, besides
being printed, it is also saved in the Nmap registry so other Nmap scripts can use it. That
means that if you're going to run`smb-brute.nse`, you should run other`smb`scripts you want.
This checks passwords in a case-insensitive way, determining case after a password is found,
for Windows versions before Vista.

[smb-double-pulsar-backdoor](https://nmap.org/nsedoc/scripts/smb-double-pulsar-backdoor.html)Checks if the target machine is running the Double Pulsar SMB backdoor.

[smb-enum-domains](https://nmap.org/nsedoc/scripts/smb-enum-domains.html)Attempts to enumerate domains on a system, along with their policies. This generally requires
credentials, except against Windows 2000. In addition to the actual domain, the "Builtin"
domain is generally displayed. Windows returns this in the list of domains, but its policies
don't appear to be used anywhere.

[smb-enum-groups](https://nmap.org/nsedoc/scripts/smb-enum-groups.html)Obtains a list of groups from the remote Windows system, as well as a list of the group's users.
This works similarly to`enum.exe`with the`/G`switch.

[smb-enum-processes](https://nmap.org/nsedoc/scripts/smb-enum-processes.html)Pulls a list of processes from the remote server over SMB. This will determine
all running processes, their process IDs, and their parent processes. It is done
by querying the remote registry service, which is disabled by default on Vista;
on all other Windows versions, it requires Administrator privileges.

[smb-enum-services](https://nmap.org/nsedoc/scripts/smb-enum-services.html)Retrieves the list of services running on a remote Windows system.
Each service attribute contains service name, display name and service status of
each service.

[smb-enum-sessions](https://nmap.org/nsedoc/scripts/smb-enum-sessions.html)Enumerates the users logged into a system either locally or through an SMB share. The local users
can be logged on either physically on the machine, or through a terminal services session.
Connections to a SMB share are, for example, people connected to fileshares or making RPC calls.
Nmap's connection will also show up, and is generally identified by the one that connected "0
seconds ago".

[smb-enum-shares](https://nmap.org/nsedoc/scripts/smb-enum-shares.html)Attempts to list shares using the`srvsvc.NetShareEnumAll`MSRPC function and
retrieve more information about them using`srvsvc.NetShareGetInfo`. If access
to those functions is denied, a list of common share names are checked.

[smb-enum-users](https://nmap.org/nsedoc/scripts/smb-enum-users.html)Attempts to enumerate the users on a remote Windows system, with as much
information as possible, through two different techniques (both over MSRPC,
which uses port 445 or 139; see`smb.lua`). The goal of this script
is to discover all user accounts that exist on a remote system. This can be
helpful for administration, by seeing who has an account on a server, or for
penetration testing or network footprinting, by determining which accounts
exist on a system.

[smb-flood](https://nmap.org/nsedoc/scripts/smb-flood.html)Exhausts a remote SMB server's connection limit by by opening as many
connections as we can.  Most implementations of SMB have a hard global
limit of 11 connections for user accounts and 10 connections for
anonymous. Once that limit is reached, further connections are
denied. This script exploits that limit by taking up all the
connections and holding them.

[smb-ls](https://nmap.org/nsedoc/scripts/smb-ls.html)Attempts to retrieve useful information about files shared on SMB volumes.
The output is intended to resemble the output of the UNIX`ls`command.

[smb-mbenum](https://nmap.org/nsedoc/scripts/smb-mbenum.html)Queries information managed by the Windows Master Browser.

[smb-os-discovery](https://nmap.org/nsedoc/scripts/smb-os-discovery.html)Attempts to determine the operating system, computer name, domain, workgroup, and current
time over the SMB protocol (ports 445 or 139).
This is done by starting a session with the anonymous
account (or with a proper user account, if one is given; it likely doesn't make
a difference); in response to a session starting, the server will send back all this
information.

[smb-print-text](https://nmap.org/nsedoc/scripts/smb-print-text.html)Attempts to print text on a shared printer by calling Print Spooler Service RPC functions.

[smb-protocols](https://nmap.org/nsedoc/scripts/smb-protocols.html)Attempts to list the supported protocols and dialects of a SMB server.

[smb-psexec](https://nmap.org/nsedoc/scripts/smb-psexec.html)Implements remote process execution similar to the Sysinternals' psexec
tool, allowing a user to run a series of programs on a remote machine and
read the output. This is great for gathering information about servers,
running the same tool on a range of system, or even installing a backdoor on
a collection of computers.

[smb-security-mode](https://nmap.org/nsedoc/scripts/smb-security-mode.html)Returns information about the SMB security level determined by SMB.

[smb-server-stats](https://nmap.org/nsedoc/scripts/smb-server-stats.html)Attempts to grab the server's statistics over SMB and MSRPC, which uses TCP
ports 445 or 139.

[smb-system-info](https://nmap.org/nsedoc/scripts/smb-system-info.html)Pulls back information about the remote system from the registry. Getting all
of the information requires an administrative account, although a user account
will still get a lot of it. Guest probably won't get any, nor will anonymous.
This goes for all operating systems, including Windows 2000.

[smb-vuln-conficker](https://nmap.org/nsedoc/scripts/smb-vuln-conficker.html)Detects Microsoft Windows systems infected by the Conficker worm. This check is dangerous and
it may crash systems.

[smb-vuln-cve-2017-7494](https://nmap.org/nsedoc/scripts/smb-vuln-cve-2017-7494.html)Checks if target machines are vulnerable to the arbitrary shared library load
vulnerability CVE-2017-7494.

[smb-vuln-cve2009-3103](https://nmap.org/nsedoc/scripts/smb-vuln-cve2009-3103.html)Detects Microsoft Windows systems vulnerable to denial of service (CVE-2009-3103).
This script will crash the service if it is vulnerable.

[smb-vuln-ms06-025](https://nmap.org/nsedoc/scripts/smb-vuln-ms06-025.html)Detects Microsoft Windows systems with Ras RPC service vulnerable to MS06-025.

[smb-vuln-ms07-029](https://nmap.org/nsedoc/scripts/smb-vuln-ms07-029.html)Detects Microsoft Windows systems with Dns Server RPC vulnerable to MS07-029.

[smb-vuln-ms08-067](https://nmap.org/nsedoc/scripts/smb-vuln-ms08-067.html)Detects Microsoft Windows systems vulnerable to the remote code execution vulnerability
known as MS08-067. This check is dangerous and it may crash systems.

[smb-vuln-ms10-054](https://nmap.org/nsedoc/scripts/smb-vuln-ms10-054.html)Tests whether target machines are vulnerable to the ms10-054 SMB remote memory
corruption vulnerability.

[smb-vuln-ms10-061](https://nmap.org/nsedoc/scripts/smb-vuln-ms10-061.html)Tests whether target machines are vulnerable to ms10-061 Printer Spooler impersonation vulnerability.

[smb-vuln-ms17-010](https://nmap.org/nsedoc/scripts/smb-vuln-ms17-010.html)Attempts to detect if a Microsoft SMBv1 server is vulnerable to a remote code
 execution vulnerability (ms17-010, a.k.a. EternalBlue).
 The vulnerability is actively exploited by WannaCry and Petya ransomware and other malware.

[smb-vuln-regsvc-dos](https://nmap.org/nsedoc/scripts/smb-vuln-regsvc-dos.html)Checks if a Microsoft Windows 2000 system is vulnerable to a crash in regsvc caused by a null pointer
dereference. This check will crash the service if it is vulnerable and requires a guest account or
higher to work.

[smb-vuln-webexec](https://nmap.org/nsedoc/scripts/smb-vuln-webexec.html)A critical remote code execution vulnerability exists in WebExService (WebExec).

[smb-webexec-exploit](https://nmap.org/nsedoc/scripts/smb-webexec-exploit.html)Attempts to run a command via WebExService, using the WebExec vulnerability.
Given a Windows account (local or domain), this will start an arbitrary
executable with SYSTEM privileges over the SMB protocol.

[smb2-capabilities](https://nmap.org/nsedoc/scripts/smb2-capabilities.html)Attempts to list the supported capabilities in a SMBv2 server for each
 enabled dialect.

[smb2-security-mode](https://nmap.org/nsedoc/scripts/smb2-security-mode.html)Determines the message signing configuration in SMBv2 servers
 for all supported dialects.

[smb2-time](https://nmap.org/nsedoc/scripts/smb2-time.html)Attempts to obtain the current system date and the start date of a SMB2 server.

[smb2-vuln-uptime](https://nmap.org/nsedoc/scripts/smb2-vuln-uptime.html)Attempts to detect missing patches in Windows systems by checking the
uptime returned during the SMB2 protocol negotiation.

[smtp-brute](https://nmap.org/nsedoc/scripts/smtp-brute.html)Performs brute force password auditing against SMTP servers using either LOGIN, PLAIN, CRAM-MD5, DIGEST-MD5 or NTLM authentication.

[smtp-commands](https://nmap.org/nsedoc/scripts/smtp-commands.html)Attempts to use EHLO and HELP to gather the Extended commands supported by an
SMTP server.

[smtp-enum-users](https://nmap.org/nsedoc/scripts/smtp-enum-users.html)Attempts to enumerate the users on a SMTP server by issuing the VRFY, EXPN or RCPT TO
commands. The goal of this script is to discover all the user accounts in the remote
system.

[smtp-ntlm-info](https://nmap.org/nsedoc/scripts/smtp-ntlm-info.html)This script enumerates information from remote SMTP services with NTLM
authentication enabled.

[smtp-open-relay](https://nmap.org/nsedoc/scripts/smtp-open-relay.html)Attempts to relay mail by issuing a predefined combination of SMTP commands. The goal
of this script is to tell if a SMTP server is vulnerable to mail relaying.

[smtp-strangeport](https://nmap.org/nsedoc/scripts/smtp-strangeport.html)Checks if SMTP is running on a non-standard port.

[smtp-vuln-cve2010-4344](https://nmap.org/nsedoc/scripts/smtp-vuln-cve2010-4344.html)Checks for and/or exploits a heap overflow within versions of Exim
prior to version 4.69 (CVE-2010-4344) and a privilege escalation
vulnerability in Exim 4.72 and prior (CVE-2010-4345).

[smtp-vuln-cve2011-1720](https://nmap.org/nsedoc/scripts/smtp-vuln-cve2011-1720.html)Checks for a memory corruption in the Postfix SMTP server when it uses
Cyrus SASL library authentication mechanisms (CVE-2011-1720).  This
vulnerability can allow denial of service and possibly remote code
execution.

[smtp-vuln-cve2011-1764](https://nmap.org/nsedoc/scripts/smtp-vuln-cve2011-1764.html)Checks for a format string vulnerability in the Exim SMTP server
(version 4.70 through 4.75) with DomainKeys Identified Mail (DKIM) support
(CVE-2011-1764).  The DKIM logging mechanism did not use format string
specifiers when logging some parts of the DKIM-Signature header field.
A remote attacker who is able to send emails, can exploit this vulnerability
and execute arbitrary code with the privileges of the Exim daemon.

[sniffer-detect](https://nmap.org/nsedoc/scripts/sniffer-detect.html)Checks if a target on a local Ethernet has its network card in promiscuous mode.

[snmp-brute](https://nmap.org/nsedoc/scripts/snmp-brute.html)Attempts to find an SNMP community string by brute force guessing.

[snmp-hh3c-logins](https://nmap.org/nsedoc/scripts/snmp-hh3c-logins.html)Attempts to enumerate Huawei / HP/H3C Locally Defined Users through the
hh3c-user.mib OID

[snmp-info](https://nmap.org/nsedoc/scripts/snmp-info.html)Extracts basic information from an SNMPv3 GET request. The same probe is used
here as in the service version detection scan.

[snmp-interfaces](https://nmap.org/nsedoc/scripts/snmp-interfaces.html)Attempts to enumerate network interfaces through SNMP.

[snmp-ios-config](https://nmap.org/nsedoc/scripts/snmp-ios-config.html)Attempts to downloads Cisco router IOS configuration files using SNMP RW (v1) and display or save them.

[snmp-netstat](https://nmap.org/nsedoc/scripts/snmp-netstat.html)Attempts to query SNMP for a netstat like output. The script can be used to
identify and automatically add new targets to the scan by supplying the
newtargets script argument.

[snmp-processes](https://nmap.org/nsedoc/scripts/snmp-processes.html)Attempts to enumerate running processes through SNMP.

[snmp-sysdescr](https://nmap.org/nsedoc/scripts/snmp-sysdescr.html)Attempts to extract system information from an SNMP service.

[snmp-win32-services](https://nmap.org/nsedoc/scripts/snmp-win32-services.html)Attempts to enumerate Windows services through SNMP.

[snmp-win32-shares](https://nmap.org/nsedoc/scripts/snmp-win32-shares.html)Attempts to enumerate Windows Shares through SNMP.

[snmp-win32-software](https://nmap.org/nsedoc/scripts/snmp-win32-software.html)Attempts to enumerate installed software through SNMP.

[snmp-win32-users](https://nmap.org/nsedoc/scripts/snmp-win32-users.html)Attempts to enumerate Windows user accounts through SNMP

[socks-auth-info](https://nmap.org/nsedoc/scripts/socks-auth-info.html)Determines the supported authentication mechanisms of a remote SOCKS
proxy server.  Starting with SOCKS version 5 socks servers may support
authentication.  The script checks for the following authentication
types:
  0 - No authentication
  1 - GSSAPI
  2 - Username and password

[socks-brute](https://nmap.org/nsedoc/scripts/socks-brute.html)Performs brute force password auditing against SOCKS 5 proxy servers.

[socks-open-proxy](https://nmap.org/nsedoc/scripts/socks-open-proxy.html)Checks if an open socks proxy is running on the target.

[ssh-auth-methods](https://nmap.org/nsedoc/scripts/ssh-auth-methods.html)Returns authentication methods that a SSH server supports.

[ssh-brute](https://nmap.org/nsedoc/scripts/ssh-brute.html)Performs brute-force password guessing against ssh servers.

[ssh-hostkey](https://nmap.org/nsedoc/scripts/ssh-hostkey.html)Shows SSH hostkeys.

[ssh-publickey-acceptance](https://nmap.org/nsedoc/scripts/ssh-publickey-acceptance.html)This script takes a table of paths to private keys, passphrases, and usernames
and checks each pair to see if the target ssh server accepts them for publickey
authentication. If no keys are given or the known-bad option is given, the
script will check if a list of known static public keys are accepted for
authentication.

[ssh-run](https://nmap.org/nsedoc/scripts/ssh-run.html)Runs remote command on ssh server and returns command output.

[ssh2-enum-algos](https://nmap.org/nsedoc/scripts/ssh2-enum-algos.html)Reports the number of algorithms (for encryption, compression, etc.) that
the target SSH2 server offers. If verbosity is set, the offered algorithms
are each listed by type.

[sshv1](https://nmap.org/nsedoc/scripts/sshv1.html)Checks if an SSH server supports the obsolete and less secure SSH Protocol Version 1.

[ssl-ccs-injection](https://nmap.org/nsedoc/scripts/ssl-ccs-injection.html)Detects whether a server is vulnerable to the SSL/TLS "CCS Injection"
vulnerability (CVE-2014-0224), first discovered by Masashi Kikuchi.
The script is based on the ccsinjection.c code authored by Ramon de C Valle
([https://gist.github.com/rcvalle/71f4b027d61a78c42607](https://gist.github.com/rcvalle/71f4b027d61a78c42607))

[ssl-cert](https://nmap.org/nsedoc/scripts/ssl-cert.html)Retrieves a server's SSL certificate. The amount of information printed about
the certificate depends on the verbosity level. With no extra verbosity, the
script prints the validity period and the commonName, organizationName,
stateOrProvinceName, and countryName of the subject. When present, it also
outputs all the subject alternative names.

[ssl-cert-intaddr](https://nmap.org/nsedoc/scripts/ssl-cert-intaddr.html)Reports any private (RFC1918) IPv4 addresses found in the various fields of
an SSL service's certificate.  These will only be reported if the target
address itself is not private.  Nmap v7.30 or later is required.

[ssl-date](https://nmap.org/nsedoc/scripts/ssl-date.html)Retrieves a target host's time and date from its TLS ServerHello response.

[ssl-dh-params](https://nmap.org/nsedoc/scripts/ssl-dh-params.html)Weak ephemeral Diffie-Hellman parameter detection for SSL/TLS services.

[ssl-enum-ciphers](https://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html)This script repeatedly initiates SSLv3/TLS connections, each time trying a new
cipher or compressor while recording whether a host accepts or rejects it. The
end result is a list of all the ciphersuites and compressors that a server accepts.

[ssl-heartbleed](https://nmap.org/nsedoc/scripts/ssl-heartbleed.html)Detects whether a server is vulnerable to the OpenSSL Heartbleed bug (CVE-2014-0160).
The code is based on the Python script ssltest.py authored by Katie Stafford (katie@ktpanda.org)

[ssl-known-key](https://nmap.org/nsedoc/scripts/ssl-known-key.html)Checks whether the SSL certificate used by a host has a fingerprint
that matches an included database of problematic keys.

[ssl-poodle](https://nmap.org/nsedoc/scripts/ssl-poodle.html)Checks whether SSLv3 CBC ciphers are allowed (POODLE)

[sslv2](https://nmap.org/nsedoc/scripts/sslv2.html)Determines whether the server supports obsolete and less secure SSLv2, and discovers which ciphers it
supports.

[sslv2-drown](https://nmap.org/nsedoc/scripts/sslv2-drown.html)Determines whether the server supports SSLv2, what ciphers it supports and tests for
CVE-2015-3197, CVE-2016-0703 and CVE-2016-0800 (DROWN)

[sstp-discover](https://nmap.org/nsedoc/scripts/sstp-discover.html)Check if the Secure Socket Tunneling Protocol is supported. This is
accomplished by trying to establish the HTTPS layer which is used to
carry SSTP traffic as described in:
    -[http://msdn.microsoft.com/en-us/library/cc247364.aspx](http://msdn.microsoft.com/en-us/library/cc247364.aspx)

[stun-info](https://nmap.org/nsedoc/scripts/stun-info.html)Retrieves the external IP address of a NAT:ed host using the STUN protocol.

[stun-version](https://nmap.org/nsedoc/scripts/stun-version.html)Sends a binding request to the server and attempts to extract version
information from the response, if the server attribute is present.

[stuxnet-detect](https://nmap.org/nsedoc/scripts/stuxnet-detect.html)Detects whether a host is infected with the Stuxnet worm ([http://en.wikipedia.org/wiki/Stuxnet](http://en.wikipedia.org/wiki/Stuxnet)).

[supermicro-ipmi-conf](https://nmap.org/nsedoc/scripts/supermicro-ipmi-conf.html)Attempts to download an unprotected configuration file containing plain-text
user credentials in vulnerable Supermicro Onboard IPMI controllers.

[svn-brute](https://nmap.org/nsedoc/scripts/svn-brute.html)Performs brute force password auditing against Subversion source code control servers.

[targets-asn](https://nmap.org/nsedoc/scripts/targets-asn.html)Produces a list of IP prefixes for a given routing AS number (ASN).

[targets-ipv6-eui64](https://nmap.org/nsedoc/scripts/targets-ipv6-eui64.html)This script runs in the pre-scanning phase to convert 48-bit MAC addresses to
EUI-64 IPv6 addresses, which are often used for auto-configuration. Generated
addresses may be added to the scan queue.

[targets-ipv6-map4to6](https://nmap.org/nsedoc/scripts/targets-ipv6-map4to6.html)This script runs in the pre-scanning phase to map IPv4 addresses onto IPv6
networks and add them to the scan queue.

[targets-ipv6-multicast-echo](https://nmap.org/nsedoc/scripts/targets-ipv6-multicast-echo.html)Sends an ICMPv6 echo request packet to the all-nodes link-local
multicast address (`ff02::1`) to discover responsive hosts
on a LAN without needing to individually ping each IPv6 address.

[targets-ipv6-multicast-invalid-dst](https://nmap.org/nsedoc/scripts/targets-ipv6-multicast-invalid-dst.html)Sends an ICMPv6 packet with an invalid extension header to the
all-nodes link-local multicast address (`ff02::1`) to
discover (some) available hosts on the LAN. This works because some
hosts will respond to this probe with an ICMPv6 Parameter Problem
packet.

[targets-ipv6-multicast-mld](https://nmap.org/nsedoc/scripts/targets-ipv6-multicast-mld.html)Attempts to discover available IPv6 hosts on the LAN by sending an MLD
(multicast listener discovery) query to the link-local multicast address
(ff02::1) and listening for any responses.  The query's maximum response delay
set to 1 to provoke hosts to respond immediately rather than waiting for other
responses from their multicast group.

[targets-ipv6-multicast-slaac](https://nmap.org/nsedoc/scripts/targets-ipv6-multicast-slaac.html)Performs IPv6 host discovery by triggering stateless address auto-configuration
(SLAAC).

[targets-ipv6-wordlist](https://nmap.org/nsedoc/scripts/targets-ipv6-wordlist.html)Adds IPv6 addresses to the scan queue using a wordlist of hexadecimal "words"
that form addresses in a given subnet.

[targets-sniffer](https://nmap.org/nsedoc/scripts/targets-sniffer.html)Sniffs the local network for a configurable amount of time (10 seconds
by default) and prints discovered addresses. If the`newtargets`script argument is set, discovered addresses
are added to the scan queue.

[targets-traceroute](https://nmap.org/nsedoc/scripts/targets-traceroute.html)Inserts traceroute hops into the Nmap scanning queue. It only functions if
Nmap's`--traceroute`option is used and the`newtargets`script argument is given.

[targets-xml](https://nmap.org/nsedoc/scripts/targets-xml.html)Loads addresses from an Nmap XML output file for scanning.

[teamspeak2-version](https://nmap.org/nsedoc/scripts/teamspeak2-version.html)Detects the TeamSpeak 2 voice communication server and attempts to determine
version and configuration information.

[telnet-brute](https://nmap.org/nsedoc/scripts/telnet-brute.html)Performs brute-force password auditing against telnet servers.

[telnet-encryption](https://nmap.org/nsedoc/scripts/telnet-encryption.html)Determines whether the encryption option is supported on a remote telnet
server.  Some systems (including FreeBSD and the krb5 telnetd available in many
Linux distributions) implement this option incorrectly, leading to a remote
root vulnerability. This script currently only tests whether encryption is
supported, not for that particular vulnerability.

[telnet-ntlm-info](https://nmap.org/nsedoc/scripts/telnet-ntlm-info.html)This script enumerates information from remote Microsoft Telnet services with NTLM
authentication enabled.

[tftp-enum](https://nmap.org/nsedoc/scripts/tftp-enum.html)Enumerates TFTP (trivial file transfer protocol) filenames by testing
for a list of common ones.

[tftp-version](https://nmap.org/nsedoc/scripts/tftp-version.html)Obtains information (such as vendor and device type where available) from a
TFTP service by requesting a random filename. Software vendor information is
determined by matching the error message against a database of known software.

[tls-alpn](https://nmap.org/nsedoc/scripts/tls-alpn.html)Enumerates a TLS server's supported application-layer protocols using the ALPN protocol.

[tls-nextprotoneg](https://nmap.org/nsedoc/scripts/tls-nextprotoneg.html)Enumerates a TLS server's supported protocols by using the next protocol
negotiation extension.

[tls-ticketbleed](https://nmap.org/nsedoc/scripts/tls-ticketbleed.html)Detects whether a server is vulnerable to the F5 Ticketbleed bug (CVE-2016-9244).

[tn3270-screen](https://nmap.org/nsedoc/scripts/tn3270-screen.html)Connects to a tn3270 'server' and returns the screen.

[tor-consensus-checker](https://nmap.org/nsedoc/scripts/tor-consensus-checker.html)Checks if a target is a known Tor node.

[traceroute-geolocation](https://nmap.org/nsedoc/scripts/traceroute-geolocation.html)Lists the geographic locations of each hop in a traceroute and optionally
saves the results to a KML file, plottable on Google earth and maps.

[tso-brute](https://nmap.org/nsedoc/scripts/tso-brute.html)TSO account brute forcer.

[tso-enum](https://nmap.org/nsedoc/scripts/tso-enum.html)TSO User ID enumerator for IBM mainframes (z/OS). The TSO logon panel
tells you when a user ID is valid or invalid with the message:`IKJ56420I Userid <user ID> not authorized to use TSO`.

[ubiquiti-discovery](https://nmap.org/nsedoc/scripts/ubiquiti-discovery.html)Extracts information from Ubiquiti networking devices.

[unittest](https://nmap.org/nsedoc/scripts/unittest.html)Runs unit tests on all NSE libraries.

[unusual-port](https://nmap.org/nsedoc/scripts/unusual-port.html)Compares the detected service on a port against the expected service for that
port number (e.g. ssh on 22, http on 80) and reports deviations. The script
requires that a version scan has been run in order to be able to discover what
service is actually running on each port.

[upnp-info](https://nmap.org/nsedoc/scripts/upnp-info.html)Attempts to extract system information from the UPnP service.

[uptime-agent-info](https://nmap.org/nsedoc/scripts/uptime-agent-info.html)Gets system information from an Idera Uptime Infrastructure Monitor agent.

[url-snarf](https://nmap.org/nsedoc/scripts/url-snarf.html)Sniffs an interface for HTTP traffic and dumps any URLs, and their
originating IP address. Script output differs from other script as
URLs are written to stdout directly. There is also an option to log
the results to file.

[ventrilo-info](https://nmap.org/nsedoc/scripts/ventrilo-info.html)Detects the Ventrilo voice communication server service versions 2.1.2
and above and tries to determine version and configuration
information. Some of the older versions (pre 3.0.0) may not have the
UDP service that this probe relies on enabled by default.

[versant-info](https://nmap.org/nsedoc/scripts/versant-info.html)Extracts information, including file paths, version and database names from
a Versant object database.

[vmauthd-brute](https://nmap.org/nsedoc/scripts/vmauthd-brute.html)Performs brute force password auditing against the VMWare Authentication Daemon (vmware-authd).

[vmware-version](https://nmap.org/nsedoc/scripts/vmware-version.html)Queries VMware server (vCenter, ESX, ESXi) SOAP API to extract the version information.

[vnc-brute](https://nmap.org/nsedoc/scripts/vnc-brute.html)Performs brute force password auditing against VNC servers.

[vnc-info](https://nmap.org/nsedoc/scripts/vnc-info.html)Queries a VNC server for its protocol version and supported security types.

[vnc-title](https://nmap.org/nsedoc/scripts/vnc-title.html)Tries to log into a VNC server and get its desktop name. Uses credentials
discovered by vnc-brute, or None authentication types. If`realvnc-auth-bypass`was run and returned VULNERABLE, this script
will use that vulnerability to bypass authentication.

[voldemort-info](https://nmap.org/nsedoc/scripts/voldemort-info.html)Retrieves cluster and store information from the Voldemort distributed key-value store using the Voldemort Native Protocol.

[vtam-enum](https://nmap.org/nsedoc/scripts/vtam-enum.html)Many mainframes use VTAM screens to connect to various applications
(CICS, IMS, TSO, and many more).

[vulners](https://nmap.org/nsedoc/scripts/vulners.html)For each available CPE the script prints out known vulns (links to the correspondent info) and correspondent CVSS scores.

[vuze-dht-info](https://nmap.org/nsedoc/scripts/vuze-dht-info.html)Retrieves some basic information, including protocol version from a Vuze filesharing node.

[wdb-version](https://nmap.org/nsedoc/scripts/wdb-version.html)Detects vulnerabilities and gathers information (such as version
numbers and hardware support) from VxWorks Wind DeBug agents.

[weblogic-t3-info](https://nmap.org/nsedoc/scripts/weblogic-t3-info.html)Detect the T3 RMI protocol and Weblogic version

[whois-domain](https://nmap.org/nsedoc/scripts/whois-domain.html)Attempts to retrieve information about the domain name of the target

[whois-ip](https://nmap.org/nsedoc/scripts/whois-ip.html)Queries the WHOIS services of Regional Internet Registries (RIR) and attempts to retrieve information about the IP Address
Assignment which contains the Target IP Address.

[wsdd-discover](https://nmap.org/nsedoc/scripts/wsdd-discover.html)Retrieves and displays information from devices supporting the Web
Services Dynamic Discovery (WS-Discovery) protocol. It also attempts
to locate any published Windows Communication Framework (WCF) web
services (.NET 4.0 or later).

[x11-access](https://nmap.org/nsedoc/scripts/x11-access.html)Checks if you're allowed to connect to the X server.

[xdmcp-discover](https://nmap.org/nsedoc/scripts/xdmcp-discover.html)Requests an XDMCP (X display manager control protocol) session and lists supported authentication and authorization mechanisms.

[xmlrpc-methods](https://nmap.org/nsedoc/scripts/xmlrpc-methods.html)Performs XMLRPC Introspection via the system.listMethods method.

[xmpp-brute](https://nmap.org/nsedoc/scripts/xmpp-brute.html)Performs brute force password auditing against XMPP (Jabber) instant messaging servers.

[xmpp-info](https://nmap.org/nsedoc/scripts/xmpp-info.html)Connects to XMPP server (port 5222) and collects server information such as:
supported auth mechanisms, compression methods, whether TLS is supported
and mandatory, stream management, language, support of In-Band registration,
server capabilities.  If possible, studies server vendor.