	$.ajax({
			data: {query:"many times senbei", id:"73244901"},
			type: "POST",
			url: "http://localhost/raptor/post/track/download",
		})
	 .done(function( data, textStatus, jqXHR ) {
	 		console.log(jQuery.parseJSON(data));	 			
	 })
	  .fail(function( jqXHR, textStatus, errorThrown ) {
		    console.log(errorThrown);
	});