## GPG basics

### Configuration file should contain

    # when outputting certificates, view user IDs distinctly from keys:
    fixed-list-mode
    # short-keyids are trivially spoofed; it's easy to create a long-keyid collision; if you care about strong key identifiers, you always want to see the fingerprint: 
    keyid-format 0xlong
    fingerprint
    # when multiple digests are supported by all recipients, choose the strongest one:
    personal-digest-preferences SHA512 SHA384 SHA256 SHA224
    # preferences chosen for new keys should prioritize stronger algorithms: 
    default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 BZIP2 ZLIB ZIP Uncompressed
    # If you use a graphical environment (and even if you don't) you should be using an agent:
    # (similar arguments as  https://www.debian-administration.org/users/dkg/weblog/64)
    use-agent
    # You should always know at a glance which User IDs gpg thinks are legitimately bound to the keys in your keyring:
    verify-options show-uid-validity
    list-options show-uid-validity
    # include an unambiguous indicator of which key made a signature:
    # (see http://thread.gmane.org/gmane.mail.notmuch.general/3721/focus=7234)
    sig-notation issuer-fpr@notations.openpgp.fifthhorseman.net=%g
    # when making an OpenPGP certification, use a stronger digest than the default SHA1:
    cert-digest-algo SHA512

 In `~/.gnupg/gpg.conf`. From https://we.riseup.net/riseuplabs+paow/openpgp-best-practices#self-signatures-must-not-use-md5, accessed 20140201.

### To encrypt a message (assuming you already have GnuPG installed and your own key-pair created).

 1. Given a name, domain, email address, or other identifier of the person you want to connect to, look up associated public keys at http://pool.sks-keyservers.net

 2. Links on the results page will lead to an actual public key, which can be downloaded to disk or copied to a file, say as "friends_key". This key is connected to an email address that the friend supplied on creation of the key-pair.

 3. Import using

        gpg --import friends_key

 4. Encrypt a document "plain_text" as "cipher_text.gpg" for your friend, whose keyID can be found using an email address and confirmed by checking its fingerprint manually, using

        gpg --output cipher_text.gpg --encrypt --recipient friends_keyID plain_text

   You will not be able to decrypt it since you don't have your friend's private key.

[end]
