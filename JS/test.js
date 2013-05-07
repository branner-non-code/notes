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

if (IndexEntries === null) {
  alert("IndexEntries is null");
}
else if (TupleStorage === null) {
  alert("TupleStorage is null");
}

function getSought() {
  var sought = document.getElementById("searchTerm").value.toLowerCase();
  if (sought === null || typeof IndexEntries[sought] === "undefined") {
    alert("Nothing found.");
    location.reload()
  }
//  if (sought !== null) {
  else {
    document.close();
    var tupleIndexes = IndexEntries[sought];
    var indexNum = 0;
    document.getElementById("whereRunning").innerHTML="Enter your next search term below:";
    document.write(
        "<p id=\"whereRunning\"> </p>" +
        "<form><input type=\"text\" name=\"sought\" id=\"searchTerm\" />" +
        "<input type=\"button\" onclick=\"getSought()\" " +
          "value=\"Submit search term\"></form>\n <hr>");
    document.getElementById("searchTerm").focus();
    document.write("<p>Searching for: "+sought+"</p>");
    document.write("<ul>");
    for (var i = 0; i < tupleIndexes.length; i++) {
      var pathHash = tupleIndexes[indexNum++];
      var pathTuple = TupleStorage[String(pathHash)];
      document.write("<li><a href=\""  + urlPrefix + pathTuple[1] + 
          "\" target=\"_blank\">" + pathTuple[2]+ "</a> (<strong>" + 
        pathTuple[0] + "</strong>: " + pathTuple[1] + ")</li>");
    } 
    document.write('</ul>');
  }
}
