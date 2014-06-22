## Filtering search hits with JavaScript

Example by Stuart Sandine, 20140209: 

Steps to filter CraigsList output, displaying only most recent day's posts:

 1. Load CraigsList map in Chrome, e.g http://newyork.craigslist.org/search/roo?useMap=1&zoomToPosting=&catAbb=roo&query=&minAsk=&maxAsk=&excats=

 2. Crack open dev tools, sources panel, and navigate to the file at www.craigslist.org/js/searchmaps.min.js

 3. Prettify the js by clicking the `{ }` button then insert a breakpoint at line 24, right inside the `$.getJSON` call

 4. Refresh the page and it'll pause at that point. Hit escape or otherwise open the console and paste this code into the console and run it:

        var temp = a[0].slice();
        var daysBack = 1; //CHANGEME: How many days back displayed?
        a[0] = temp.filter(function( item ) {
          if ( item.PostedDate > Math.round(Date.now()/1000) - daysBack * 86400 ) {
              return true;
              }
          });

 5. Unpause and you'll see filtered results mapped!

The results also include reposted ads within your range but it mostly works.

[end]
