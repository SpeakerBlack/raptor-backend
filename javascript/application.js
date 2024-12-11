//Buscar
$.ajax({
		data: {query:"daft punk"},
		type: "POST",
		url:  "http://23.105.70.100/Raptor/post/track/search",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

//Obtener informacion de una cancion
$.ajax({
		data: {id:"67238735"},
		type: "POST",
		url:  "http://23.105.70.100/Raptor/post/track/getInfo",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

//Descargar una cancion
$.ajax({
		data: {id:"67238735", id_user:"-1"},
		type: "POST",
		url:  "http://23.105.70.100/Raptor/post/track/download",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

//Insertar un usuario
$.ajax({
		data: {id:"prueba@prueba.com"}, // Ya existe
		type: "POST",
		url:  "http://23.105.70.100/Raptor/post/user/insertUser",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

//Insertar una FAQ
$.ajax({
		data: {id_user:-1,comentario:"Desde el servicio"},
		type: "POST",
		url:  "http://23.105.70.100/Raptor/post/user/insertFAQ",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

//Obtener sugerencias
$.ajax({
		data: {id_user:"-1"},
		type: "POST",
		url:  "http://23.105.70.100/Raptor/post/track/getSuggested",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});


// Crear una playlist
$.ajax({
		data: {id:"1",nombre:"test"},
		type: "POST",
		url:  "http://localhost:8080/Raptor/post/playlist/newPlaylist",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

// Añadir un item a la playlist
$.ajax({
		data: {id:"1",id_track:"2345654",nombre_track:"test",artist_track:"nro",img_track:"http//:fertyh"},
		type: "POST",
		url:  "http://localhost:8080/Raptor/post/playlist/addItem",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log((data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});


// Listar playlist del usuario
$.ajax({
		data: {id:"1"},
		type: "POST",
		url:  "http://localhost:8080/Raptor/post/playlist/listByUser",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log(jQuery.parseJSON(data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

// Listar elemento de una playlist

$.ajax({
		data: {id:"1"},
		type: "POST",
		url:  "http://localhost:8080/Raptor/post/playlist/listItems",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log((data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

// Eliminar playlist

$.ajax({
		data: {id_playlist:"2"},
		type: "POST",
		url:  "http://localhost:8080/Raptor/post/playlist/dropList",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log((data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});

// Borrar item de una playlist

$.ajax({
		data: {id_playlist:"1",id_track:"2345654"},
		type: "POST",
		url:  "http://localhost:8080/Raptor/post/playlist/dropItem",
	})
 .done(function( data, textStatus, jqXHR ) {
 		console.log((data));		
 })
  .fail(function( jqXHR, textStatus, errorThrown ) {
	    console.log(errorThrown);
});
