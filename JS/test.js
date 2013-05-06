function setFocus() {
  document.getElementById("search").focus();
}

var currentURL = window.location.href;

if (currentURL.search(/http/) === 0) {
  alert("http");
  var urlPrefix = "https://github.com/brannerchinese/notes/blob/master/";
}
else {
  var urlPrefix = "";
  alert("file");
}

//alert(currentURL)

function getSought() {
  var sought = document.getElementById("searchTerm").value;
  if (sought === null || typeof IndexEntries[sought] === "undefined") {
    location.reload()
  }
  document.getElementById("heading").innerHTML="searching for: "+sought;
  if (sought !== null) {
    var tupleIndexes = IndexEntries[sought];
    var indexNum = 0;
    document.write('<ul>');
    for (var i = 0; i < tupleIndexes.length; i++) {
      var pathHash = tupleIndexes[indexNum++];
      var pathTuple = TupleStorage[String(pathHash)];
      document.write('<li><a href="'  + urlPrefix + pathTuple[1] + 
          '" target="_blank">' + pathTuple[2]+ '</a> (<strong>' + 
        pathTuple[0] + '</strong>: ' + pathTuple[1] + ')</li>');
    } 
    document.write('</ul>');
  }
}
