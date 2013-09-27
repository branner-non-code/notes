## Running JavaScript on GitHub

20130528 There is a problem with GitHub forcing `type="text/plain"` in order to prevent scripts from being run from their site, and in Chrome this does indeed prevent them from running (not in Firefox or Safari). 

### STATUS 20130609: Chrome (Version 27.0.1453.110) reports:

        Refused to execute script from 
        'https://raw.github.com/brannerchinese/JsPlay/master/JS/rotate_table.js' 
        because its MIME type ('text/plain') is not executable, and 
        strict MIME type checking is enabled. 

 But in fact Chrome then does execute the script. On this date I have not trouble running the script on Firefox (v. 21.0) or Safari (Version 6.0.5 [8536.30.1]).

### PAST NOTES, 20130529: Workaround: use `rawgithub.com` instead of `raw.github.com`

https://github.com/jeremyckahn/three.js/commit/c22b7784c09fbba03bf96e7c70b06e1217d2cff0 (accessed 20130529)

 > rawgithub.com and raw.github.com serve files with different MIME types. 
 > Chrome doesn't treat the MIME type served from raw.github.com as  
 > executable JavaScript, so the sample code provided in Creating-a-scene.html 
 > fails.  This patch changes the requested URL to make the sample code 
 > run correctly in all browsers.

I tried this on 20130529, without success. Even though the HTML explicitly states `type="text/javascript"`, even with `rawgithub.com`, it is not working on Firefox. It may be necessary to move everything to `gh-pages`.

[end]
