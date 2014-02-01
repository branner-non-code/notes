## Encrypt Gmail on Firefox

I'm able to use GnuPG to encrypt and decrypt Gmail messages when accessing my accounts via SMTP. but within the regular Gmail page on my browser — I use Mozilla for various reasons — I haven't found a way to do so.

20140131: [Mailvelope](https://github.com/toberndo/mailvelope/releases) seems to be working. Release is planned for Firefox v. 27 (v. 26 is current today). The README describes building from a Git clone of the project — not sure it's advisable to download the `.xpl` file alone and try to install it. To install, Tools => Add-ons => Plugins => [gear] Install Add-on from file, and select `mailvelope.firefox.xpi` file.

I see that

 * FireGPG seems to have been discontinued. (20140131)
 * WebPG has only a few reviews, and they're not such happy ones: https://addons.mozilla.org/en-US/firefox/addon/webpg-firefox/reviews/. (20140131)
 * The GreaseMonkey script at http://www.langenhoven.com/code/emailencrypt/gmailencrypt.php has not been updated since 2010. (20140131)

[end]
