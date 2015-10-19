## Alpine set-up for Pobox.com

1. Set up SMTP configurations for outgoing mail. Enter SC to go to Setup => Config.

   Make the following changes:

   * Find the "Personal Name" key and add your name as the corresponding value.

   * Find the "User Domain" key and add your domain name as the corresponding value.

   * Find the "SMTP Server (for sending)" key and add `smtp.pobox.com:587/tls/user=name@pobox.com` as the corresponding value, replacing `name` with your login-name.

   * Find the "Alternate Addresses" key and add `name@pobox.com` (replacing `name` with your login-name) and any other email addresses of your own as the corresponding values.

   When you are done making any changes, enter E to exit the set-up menu. If you've made changes, you'll be asked to commit them — do so by entering Y.

   Note that everything entered in the Setup=>Config interface can also be seen and edited in the `.pinerc` file, usually saved to your home directory.

2. Set up IMAP (or POP) for incoming mail. Enter SL to go to Setup => collectionLists.

   Enter A to add a "collection" (which will correspond to your Pobox.com account).

   Add the following values:

   * For "Nickname" choose a value such as "pobox" or what have you.
 
   * For "Server", in the case of IMAP, add `mail.pobox.com:993/ssl/user=name@pobox.com`, where `name` is your login-name.
 
     In the case of POP, add `mail.pobox.com:995/ssl/user=name@pobox.com`, where `name` is your login-name.

   Entering control-g will bring up help messages for whatever field the cursor is now in.

   To save and exit, enter control-x. If you've made changes to the pobox.com collection, you'll be asked to commit them — do so by entering Y. 

   After that, enter E to exit the collections set-up menu. If you've made changes, you'll be asked to commit them — do so by entering Y.

[end]
