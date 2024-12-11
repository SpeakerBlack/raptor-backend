var _server_ = window.location.origin + window.location.pathname;
var cocomo = {
	url : _server_,
	host : window.location.origin,
	path : _server_.substring(0, _server_.lastIndexOf("/")+1),
	setSession : function (key, value){
		localStorage[key] = value;
	},
	getSession : function (key){
		return jQuery.parseJSON(localStorage[key]);
	},
	isHere : function(site){
		return _server_.endsWith(site);
	}
}