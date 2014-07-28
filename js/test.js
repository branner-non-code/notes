;(function IIFE(window, document, undefined) {
  // Variables
  var currentURL,
      urlPrefix,
      whereWeAre,
      sought,
      tupleIndexes,
      indexNum,
      output,
      pathHash,
      pathTuple;

  // Main loop.
  document.addEventListener('DOMContentLoaded', function(){
    'use strict';
    
    // Different settings if running locally or on web.
    currentURL = window.location.href;
    console.log(currentURL);
    if (currentURL.search(/http/) === 0) {
      // Don't use htmlpreview.github.io here; displays markdown, not HTML.
      urlPrefix = "https://github.com/brannerchinese/notes/blob/master/";
      whereWeAre = "via HTTP.";
    }
    else {
      urlPrefix = "";
      whereWeAre = "from the filesystem.";
    }

    document.getElementById("whereRunning").innerHTML="This page was read " + 
        whereWeAre + "<br/><br/>Enter your search term below:" + 
        "<form>" + 
        "<input type='text' id='searchTerm' />" + 
        "<input type='button' onclick='getSought(" + urlPrefix + 
        ")' value='Enter search term'>" +
        "</form>";

    // Set focus.
    document.getElementById("searchTerm").focus();

    // Errors.
    if (IndexEntries === null) {
      alert("IndexEntries is null");
    }
    else if (TupleStorage === null) {
      alert("TupleStorage is null");
    }
  });
})(window, document);

function getSought(urlPrefix) {
  sought = document.getElementById("searchTerm").value.toLowerCase();
  alert(sought);
  if (sought === null || typeof IndexEntries[sought] === "undefined") {
    alert("Nothing found.");
    location.reload();
  }
  else {
    document.close();
    tupleIndexes = IndexEntries[sought];
    indexNum = 0;
    document.getElementById("whereRunning").innerHTML="Enter your next search term below:" + 
        "<p id=\"whereRunning\"> </p>" +
        "<form><input type=\"text\" id=\"searchTerm\" />" +
        "<input type=\"button\" onclick=\"getSought(" + 
        urlPrefix + ")\" " + "value=\"Submit search term\"></form>";
    document.getElementById("searchTerm").focus();
    output = "<p>Results for: "+sought+"</p><ul>";
    for (var i = 0; i < tupleIndexes.length; i++) {
      pathHash = tupleIndexes[indexNum++];
      pathTuple = TupleStorage[String(pathHash)];
      output += "<li><a href=\""  + urlPrefix + pathTuple[1] + 
        "\" target=\"_blank\">" + pathTuple[2]+ "</a> (<strong>" +
        pathTuple[0] + "</strong>: " + pathTuple[1] + ")</li>";
    }
    output += "</ul>";
    document.getElementById("results").innerHTML=output;
  }
}
