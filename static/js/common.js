function $(str) {
	return(document.getElementById(str));
} 

function isEmpty() {
	var db = 1;
	var elements_input = document.getElementsByTagName("input");
	for (var i = 0; i < elements_input.length; i++) {
		if ( elements_input[i].value == "") {
			db = 0;
			break;
		}
	}
	/*var elements_textarea = document.getElementsByTagName("textarea");
	for (var i = 0; i < elements_textarea.length; i++) {
		if ( elements_textarea[i].value == "") {
			db = 0;
			break;
		}
	}*/
	if (!db) {
		alert("You have not written some required attributes!");
		return false;
	}
	
}

