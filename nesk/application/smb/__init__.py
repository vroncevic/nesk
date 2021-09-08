"""
Server Message Block provides file sharing, network browsing, printing,
and inter-process communication (IPC) over a network.

The SMB protocol relies on lower-level protocols for transport.

The SMB Inter-Process Communication (IPC) system provides named pipes and was
one of the first inter-process mechanisms commonly available to programmers
that provides a means for services to inherit the authentication carried out
when a client first connects to an SMB server.

Samba is a free software re-implementation of the SMB networking protocol.
SMB (Server Message Block) and CIFS (Common Internet File System) are
protocols. Samba implements CIFS network protocol. This is what allows Samba
to communicate with (newer) MS Windows systems. Typically you will see it
referred to as SMB/CIFS. However, CIFS is the extension of the SMB protocol,
so if someone is sharing out SMB via Samba to a legacy system still using
NetBIOS, it will typically connect to the Samba server via ports 137, 138
and 139 and CIFS is strictly port 445.

"""