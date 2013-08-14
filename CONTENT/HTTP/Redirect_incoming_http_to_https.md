## Redirect incoming http to https

### Via Python

http://www.elifulkerson.com/projects/http-https-redirect.php

Did not try this.

### Via Apache

Norm Kabir recommends doing it this way, rather than with Python.

### Procedure for single site

20100916. Turned on rewrite_module:

        sudo a2enmod rewrite
        sudo /etc/init.d/apache2 restart

Then confirmed it was on by using:

        apache2ctl -M

into file `/etc/apache2/sites-enabled/default-ssl` (20120212), placed:

        RewriteEngine on
        RewriteCond %{SERVER_PORT} !^443$
        RewriteRule ^.*$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]

at end. 

Finally, restarted apache2 , no error and pointing browser to http://www.sinolexicon.com/ led to https version of page.

(This was taken from discussion at http://ubuntuforums.org/showthread.php?t=895633 . Many other solutions failed. For comparison, also see http://www.sslshopper.com/apache-redirect-http-to-https.html and http://www.askapache.com/htaccess/ssl-example-usage-in-htaccess.html . Most solutions failed to explain where to place this code, or omitted the  tags.)

WORKS. 20100916.

### Procedure for multiple domains on a single server with UCC certificate

20120212. As above, but in file `/etc/apache2/sites-enabled/default-ssl` use 


        NameVirtualHost *:80                                                            
        
                RewriteEngine on
                RewriteCond %{HTTPS} !=on
                RewriteRule .* https://%{SERVER_NAME}%{REQUEST_URI} [R,L]
        ...

The `NameVirtualHost` line is vital; it won't work without this. When you reload or restart Apache2, you'll get multiple remarks about `VirtualHost *:443 -- mixing * ports and non-* ports with a NameVirtualHost address is not supported, proceeding with undefined results` but the redirect works, so just ignore the errors and warnings.

[end]
