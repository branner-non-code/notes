VirtualBox
==========

1.  Using NAT, with ports configured as 2222 for both guest and host.

2.  Initially start up VM with

        vboxheadless -startvm dpb15u --vrde=off &

3.  Log in with

        ssh 127.0.0.1 -p 2222

    Avoid using `localhost`. This works even when there is no internet
    connection.

[end]
