function setFocus() {
	document.getElementById("search").focus();
}

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
			var pathTuple = TupleStorage[String(pathHash)]
			document.write('<li><a href="'  + pathTuple[1] + '" target="_blank">' + pathTuple[2]+ '</a> (<strong>' + pathTuple[0] + '</strong>: ' + pathTuple[1] + ')</li>');
		}
		document.write('</ul>');
	}
}
