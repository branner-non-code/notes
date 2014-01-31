## GPG basics

### To encrypt a message (assuming you already have GnuPG installed and your own key-pair created).

 1. Given a name, domain, email address, or other identifier of the person you want to connect to, look up associated public keys at http://pool.sks-keyservers.net

 2. Links on the results page will lead to an actual public key, which can be downloaded to disk or copied to a file, say as "friends_key".

 3. Import using

        gpg --import friends_key

 4. Encrypt a document "plain_text" as "cipher_text.gpg" for your friend, whose email is "friend@domain", using

    gpg --output cipher_text.gpg --encrypt --recipient friend@domain plain_text

   You will not be able to decrypt it since you don't have your friend's private key.

[end]
