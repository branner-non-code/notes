## Updatedb and locate deprecated on OS X

For finding currently installed files in readable directories on the system, Linux utilities `updatedb` and `locate` are not readily available n Mac OS X (currently I am on 10.8.3). 

 1. `updatedb` has to be run manually from `/usr/libexec/locate.updatedb`.

 1. `locate` apparently doesn't always find filenames that exist and would be returned on a Linux installation. 

Apple's substitute, `mdfind`, searches the Spotlight metadata store

## Useful flags:

 * `-name` for names only (the default search is for name or content, just like Spotlight)
 * `-onlyin` for limiting the search to specific directories
 * `-live` to initiate live updating of search results

It is also possible to restrict the search to specific fields (keys) of the metadata store.

Man page: https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/mdfind.1.html

[end]
