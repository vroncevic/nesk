# -*- coding: UTF-8 -*-

"""
    Both MAC Address and IP Address are used to uniquely identify a machine
    on the internet. MAC address is provided by the chip maker while
    IP Address is provided by the Internet Service Provider.

    ===> Important differences between MAC Address and IP Address.

    #Definition
    MAC Address stands for Media Access Control Address.
    IP Address stands for Internet Protocol Address.

    #Usage
    MAC Address ensure that physical address of the computer is unique.
    IP Address is a logical address of the computer and is used to uniquely
    locate computer connected via a network.

    #Format
    IPv4 is 32-Bit IP address whereas IPv6 is a 128-Bit IP address.
    IPv4 is a numeric addressing method whereas IPv6 is an alphanumeric
    addressing method.
    IPv4 binary bits are separated by a dot(.) whereas IPv6 binary bits are
    separated by a colon(:).
    IPv4 offers 12 header fields whereas IPv6 offers 8 header fields.
    IPv4 supports broadcast whereas IPv6 doesn’t support broadcast.
    IPv4 has checksum fields while IPv6 doesn’t have checksum fields.
    When we compare IPv4 and IPv6, IPv4 supports VLSM (Variable Length Subnet
    Mask) whereas IPv6 doesn’t support VLSM.
    IPv4 ===> MAC Address is of six byte hexadecimal address.
    IPv4 ===> IP Address is of 4 bytes.
    IPv6 ===> MAC address is of eight byte hexadecimal address.
    IPv6 ===> IP Address is of 16 bytes.

    #Number of classes
    IPv4 offers five different classes of IP Address. Class A to E.
    IPv6 allows storing an unlimited number of IP Address.

    #Access Protocol
    MAC Address can be retrieved using ARP protocol
    (Address Resolution Protocol).
    IP Address can be retrieved using RARP protocol
    (Reverse Address Resolution Protocol).

    #Provider
    Chip maker manufacturer provides the MAC Address.
    Internet Service Provider, ISP provides the IP Address.

    #Mapping
    IPv4 uses ARP (Address Resolution Protocol) to map to MAC address whereas
    IPv6 uses NDP (Neighbour Discovery Protocol) to map to MAC address.

    #Type of Addresses
    IPv4 ===> Unicast, broadcast, and multicast.
    IPV6 ===> Unicast, multicast, and anycast.

    #Dual Stack
    IPv4 and IPv6 cannot communicate with other but can exist together on the
    same network.
"""
