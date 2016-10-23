## SSL Certificate Formats

 * **PEM** Governed by RFCs, it's used preferentially by open-source software. It can have a variety of extensions (.pem, .key, .cer, .cert, more)
 * **PKCS7** An open standard used by Java and supported by Windows. Does not contain private key material.
 * **PKCS12** A private standard that provides enhanced security versus the plain-text PEM format. This can contain private key material. It's used preferentially by Windows systems, and can be freely converted to PEM format through use of openssl.
 * **DER** The parent format of PEM. It's useful to think of it as a binary version of the base64-encoded PEM file. Not routinely used by much outside of Windows.

Source: http://serverfault.com/a/9717/152014 (accessed 20161022)

[end]