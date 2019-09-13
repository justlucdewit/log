let data;

$(document).ready(function(){
	//retrieve json
	$.getJSON("posts.json", function(json){
		data=json
	});

	$('#contentSpace').html("Page is under construction");
});