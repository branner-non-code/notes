## Encrypt Gmail on Firefox

 1. **[Mailvelope](https://github.com/toberndo/mailvelope/releases)** (20140131) is under active development, and where I am it works today for encryption with my public key. Release is reportedly planned for Firefox v. 27 (v. 26 is current today). Until then, the README describes building from a Git clone of the project — not sure it's advisable to download the `.xpl` file alone and try to install it. To install:

        Tools 
         => Add-ons 
         => Plugins 
         => [gear] Install Add-on from file

   and select `mailvelope.firefox.xpi` file. In order to import private keys, you must click the lock icon — I see it in the "add-on bar" at the bottom of the browser window. (In Chrome, where it also works, the lock icon is in the navigation bar.) From the icon you can bring up settings and there is an "Import Keys" option.
   
   I haven't been sure I wanted to import my private key into Mailevelope to test decryption, though.

 1. **FireGPG** seems to have been discontinued. (20140131)
 1. **WebPG** has only a few reviews, and they're not such happy ones: https://addons.mozilla.org/en-US/firefox/addon/webpg-firefox/reviews/. (20140131)
 1. **GreaseMonkey**. The script at http://www.langenhoven.com/code/emailencrypt/gmailencrypt.php has not been updated since 2010. (20140131)

[end]
