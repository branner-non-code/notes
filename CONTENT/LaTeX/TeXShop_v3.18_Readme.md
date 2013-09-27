## TeXShop v. 3.18 Readme

 > Version 3.18 has only a single change:
 > 
 > TeXShop contains an obsolete sync method called Search Sync, and a modern replacement by Jerome Laurens called SyncTeX. In recent versions of TeXShop, the obsolete Search Sync from the Preview Window to the Source Window randomly hangs, making TeXShop unresponsive This was supposed to be fixed in version 3.17, but it wasn't. Unfortunately, when the modern SyncTeX cannot find a match, it calls the old Search Sync, so SyncTeX can indirectly hang as well.
 > 
 > It is silly to waste time on an obsolete method, so in TeXShop 3.18, Search Sync from the Preview Window to the Source Window is disabled and does nothing. Most users will notice no change. Users who misconfigured SyncTeX will lose synchronization.
 > 
 > Users should check that
 > 
 > 1) in TeXShop Preferences under the Typesetting tab, the "Sync Method" is set to SyncTeX;
 > 
 > 2) in TeXShop Preferences under the Engine tab, the two configuration lines for "pdfTeX" each contain the following flags
 >   
 >      --file-line-error --syncTeX=1
 > 
 > 3) in TeXShop Preferences on the same page, the two "TeX + dvips + distiller" lines contain the following instruction
 > 
 >      --extratexopts "-file-line-error -synctex=1"
 > 
 > The easy way to do this is to push the four "Default" buttons beside these four entries.
 
 [end]
