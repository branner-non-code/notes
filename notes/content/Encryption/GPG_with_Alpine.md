## Using GPG (GnuPG) with Alpine (formerly Pine)

### Using Topal

 1. Installation successful using `apt-get` (20140202). No dependencies appear to be missing.
 1. Configure following http://sysphere.org/~anrxc/j/archives/2009/06/24/notes_on_alpine_and_gnupg/ (20140202):

   2. Set up Topal configuration file:

        ~~~
$ topal -default > ~/.topal/config 
        ~~~

   2. Revise `.pinerc`. 
   
     * Add `enable-topal-hack` to list following `feature-list=`.
     * Add filters:

        ~~~
display-filters=_BEGINNING("-----BEGIN PGP ")_ /usr/bin/topal -display _TMPFILE_ _RESULTFILE_
sending-filters=/usr/bin/topal -send _TMPFILE_ _RESULTFILE_ _RECIPIENTS_,
                /usr/bin/topal -sendmime _TMPFILE_ _RESULTFILE_ _MIMETYPE_ _RECIPIENTS_
        ~~~

   2. Revise `.mailcap` 

        ~~~
# cat (default) should not be used, e-mail text would just scroll by
text/plain; less '%s'; copiousoutput
# Topal GPG integration for Alpine
multipart/signed; topal -mime '%s' '%t'; needsterminal
multipart/encrypted; topal -mime '%s' '%t'; needsterminal
application/pgp; topal -mimeapgp '%s' '%t'; needsterminal
        ~~~

 1. The first time you send via Topal, you must set your own signing and decryption keys. This is done using `o` (Configuration) => `m` (Own key). Remember to save the changes before continuing.
 1. Problem: I would like to save outgoing messages in cleartext. How?


### Simple decryption set-up

Most of this material follows http://moser-isi.ethz.ch/gpg.html#howtosetuppineforuseiwthgpg (accessed 20140131). There is also other discussion at http://www.washington.edu/alpine/tech-notes/config-notes.html.

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

 1. Recipient's email must match email component of recipient's User-ID. 
 1. Options for encryption and/or signing appear just before a message is sent — use `^-p` or `^-n` to reach `gpg` or others. Their order will follow that of `sending-filters`, above. To use the first of these as a default, check `Compose Send Offers First Filter` in the configuration file. 
 1. Stefan Moser notes:

    > You will have noticed that the setup of the pine filters is such that every mail is encrypted both with the recipient's key and with your own key. The reason behind this is the following: if you only used the recipient's key then the message that is stored in your "Sent"-folder is encrypted such that you will never be able to decrypt it anymore! So the additional encryption with your own public-key makes sure that you will be able to read your own email also after the encryption process. (Many thanks to Clemens Hofmann for this hint!) 

 1. Links:

   * [Pine Privacy Guard](http://quantumlab.net/pine_privacy_guard/), accessed 20140131.

        > Pine Privacy Guard is a small perl script to interface Pine and GnuPG for the secure exchange of email.

   * [pgpenvelope](http://pgpenvelope.sourceforge.net/), accessed 20140131. 

        > pgpenvelope is an interface to meld using Pine with GnuPG, the GNU Privacy Guard. It allows one to sign/encrypt/decrypt/verify one's mail messages using GnuPG from within Pine. Ease of installation and use, and a nice interface are primary goals during development. In addition to being just a Pine filter, pgpenvelope tries to maximize the use of procmail so that signed messages only need to be verified only once. 


### Signing

 * Publishing public key?


[end]
