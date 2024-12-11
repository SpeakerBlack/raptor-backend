import json, sys, cocomo # PELIGRO -- no borrar ##COCOMO##
import urllib2, os, eyed3

def newPlaylist():
	cocomo.execute("INSERT INTO playlist (id_user,nombre) VALUES ( '" + _POST['id'] + "',  '" + _POST['nombre'] + "')")
	cocomo.printJson("1", "success")

def addItem():
	cocomo.execute("INSERT INTO track_playlist (id_playlist,track_json) VALUES ( '" + _POST['id'] + "',  '" + _POST['track'] + "')")
	cocomo.printJson("1", "success")

def listByUser():
	r = cocomo.query("SELECT id_playlist , nombre FROM playlist WHERE id_user = '" + _POST['id'] + "'")
	cocomo.printJson(r, "success")

def listItems():
	r = cocomo.query("SELECT CONCAT('[',CONCAT(GROUP_CONCAT(REPLACE(track_json,\";\",'\"')),']')) FROM track_playlist WHERE id_playlist = '" + _POST['id'] + "'")
	cocomo.printJson(r, "success")

##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##
##
## Por favor, no borrar este codigo
## Necesario para el funcionamineto del script dentro del framework
## copie y pege este codigo en cada script que valla a ser utilizado como servicio
_EXECUTE = sys.argv[1] + "()"
_POST = json.loads(sys.argv[2])

def _MAIN():
	try:
		exec _EXECUTE
	except NameError:
		cocomo.printJson("funtion '"+_EXECUTE+"' not found", "error")


if __name__ == "__main__":
	_MAIN()
##
##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##