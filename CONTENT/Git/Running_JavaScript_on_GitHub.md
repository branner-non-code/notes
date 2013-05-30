## Running JavaScript on GitHub

20130528 There is a problem with GitHub forcing `text/plain` in order to prevent scripts from being run from their site, and in Chrome this does indeed prevent them from running (not in Firefox or Safari). 

### Workaround: use `rawgithub.com` instead of `raw.github.com`

https://github.com/jeremyckahn/three.js/commit/c22b7784c09fbba03bf96e7c70b06e1217d2cff0 (accessed 20130529)

 > rawgithub.com and raw.github.com serve files with different MIME types. 
 > Chrome doesn't treat the MIME type served from raw.github.com as  
 > executable JavaScript, so the sample code provided in Creating-a-scene.html 
 > fails.  This patch changes the requested URL to make the sample code 
 > run correctly in all browsers.

I tried this on 20130529, without success. Even though the HTML explicitly states `type="text/javascript"`, even with `rawgithub.com`, it is not working on Firefox. It may be necessary to move everything to `gh-pages`.

[end]
