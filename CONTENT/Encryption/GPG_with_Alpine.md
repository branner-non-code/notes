## Using GPG (GnuPG) with Alpine

Following http://moser-isi.ethz.ch/gpg.html#howtosetuppineforuseiwthgpg (accessed 20140131).



 1. Create links to the active version of `gpg` in home directory. E.g.

        ln -s <path_to_gpg> encrypt
        ln -s <path_to_gpg> gpg
        ln -s <path_to_gpg> sign

 1. Add content to `.pinerc`:

        display-filters=_LEADING("-----BEGIN PGP MESSAGE-----")_ <home_dir> --decrypt,
                        _LEADING("-----BEGIN PGP SIGNED MESSAGE-----")_ <home_dir> --decrypt

        sending-filters=<home_dir>/sign --clearsign,
                        <home_dir>/encrypt -a --encrypt -r _RECIPIENTS_ -r <your_User-ID_email>
                        <home_dir>/gpg -a -s --encrypt -r _RECIPIENTS_ -r <your_User-ID_email>

 1. Recipient's email must match email component of his User-ID. 
 1. Options for encryption and/or signing appear just before a message is sent — use `^-p`
 1. Stefan Moser notes:

        > You will have noticed that the setup of the pine filters is such that every mail is encrypted both with the recipient's key and with your own key. The reason behind this is the following: if you only used the recipient's key then the message that is stored in your "Sent"-folder is encrypted such that you will never be able to decrypt it anymore! So the additional encryption with your own public-key makes sure that you will be able to read your own email also after the encryption process. (Many thanks to Clemens Hofmann for this hint!) 

 1. Links:

   * [Pine Privacy Guard](http://quantumlab.net/pine_privacy_guard/), accessed 20140131.

        > Pine Privacy Guard is a small perl script to interface Pine and GnuPG for the secure exchange of email.

   * [pgpenvelope](http://pgpenvelope.sourceforge.net/), accessed 20140131. 

        > pgpenvelope is an interface to meld using Pine with GnuPG, the GNU Privacy Guard. It allows one to sign/encrypt/decrypt/verify one's mail messages using GnuPG from within Pine. Ease of installation and use, and a nice interface are primary goals during development. In addition to being just a Pine filter, pgpenvelope tries to maximize the use of procmail so that signed messages only need to be verified only once. 

[end]
