var currentURL = window.location.href;
if (currentURL.search(/http/) === 0) {
  var urlPrefix = "https://github.com/brannerchinese/notes/blob/master/";
  var whereWeAre = "via HTTP.";
}
else {
  var urlPrefix = "";
  var whereWeAre = "from the filesystem.";
}
document.getElementById("whereRunning").innerHTML="This page was read "+whereWeAre+"<br/><br/>Enter your search term below:";

document.getElementById("searchTerm").focus();

function getSought() {
  var sought = document.getElementById("searchTerm").value;
  if (sought === null || typeof IndexEntries[sought] === "undefined") {
    location.reload()
  }
  document.getElementById("heading").innerHTML="searching for: "+sought;
  if (sought !== null) {
    var tupleIndexes = IndexEntries[sought];
    var indexNum = 0;
    document.write("<form><input type=\"text\" name=\"sought\"" +
          "id=\"searchTerm\"/>" +
          "<input type=\"button\" onclick=\"getSought()\" " +
          "value=\"Enter search term.\"></form>\n <ul>");
    for (var i = 0; i < tupleIndexes.length; i++) {
      var pathHash = tupleIndexes[indexNum++];
      var pathTuple = TupleStorage[String(pathHash)];
      document.write("<li><a href=\""  + urlPrefix + pathTuple[1] + 
          "\" target=\"_blanki\">" + pathTuple[2]+ "</a> (<strong>" + 
        pathTuple[0] + "</strong>: " + pathTuple[1] + ")</li>");
    } 
    document.write('</ul>');
  }
}
