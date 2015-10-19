## Setting up GoDaddy certificates

Placement of original `.key` file and two `.crt` files received from GoDaddy.

Followed instructions at https://www.digitalocean.com/community/tutorials/how-to-install-an-ssl-certificate-from-a-commercial-certificate-authority

### File `sudo vim /etc/apache2/sites-available/000-default.conf`

```
<VirtualHost *:80>
        ServerName sinolexicon.com
        Redirect permanent / https://sinolexicon.com/
</VirtualHost>
 
 
<VirtualHost *:443>
 
        ServerName sinolexicon.com
        ServerAlias www.sinolexicon.com
        ServerAdmin dpb@brannerchinese.com
        DocumentRoot /var/www/html
 
        LogLevel info ssl:warn
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
 
        SSLEngine on
        SSLCertificateFile /etc/ssl/certs/sinolexicon.com.crt
        SSLCertificateKeyFile /etc/ssl/private/sinolexicon.com.key
                                                                                
</VirtualHost>
```

---

### File `sudo vim /etc/apache2/sites-enabled/default-ssl.conf`

```
SSLCertificateFile      /etc/ssl/certs/sinolexicon.com.crt
SSLCertificateKeyFile   /etc/ssl/private/sinolexicon.com.key
SSLCertificateChainFile /etc/ssl/certs/gd_bundle-g2-g1.crt      
```

---

### Finally, issue these two commands

```
sudo a2enmod ssl
sudo service apache2 restart
```

[end]

