#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, sys, cocomo # PELIGRO -- no borrar ##COCOMO##
import urllib2, os, eyed3, random
from pytube import YouTube 

# def login():
# 	__object = _POST	
# 	__data = cocomo.query("select * from user where email = '"+__object['user']+"' and pass = '"+__object['password']+"'")
# 	if len(__data) == 0:
# 		cocomo.printJson("Datos no encontrados", "error")
# 	else:
# 		cocomo.printJson(__data, "success")

def search():
	query = _POST['query'].replace(" ", "%20")
	cocomo.printJson ( smartGet ( "http://api.deezer.com/search?q=" + query ) , "success" )

def getInfo(service=True):
	f = smartGet( "http://api.deezer.com/track/" + str ( _POST['id'] ) , service )
	if service:
		cocomo.printJson(f, "success")
	else:
		return f

def download():
	try:
		###saber si ya existe el archivo en el servidor para no hacer todo el proceso
		if os.path.exists("../audio/"+_POST['id']+"/"):
			trackName = os.listdir("../audio/"+_POST['id']+"/")[0]
			cocomo.printJson( { "trackURL":"audio/"+_POST['id']+"/"+trackName.replace(" ", "%20") } , "success")
			return
	
		track = getInfo(service=False)
		##Recordatorio de la estrutura del json
		#track['title']
		#track['id']
		#track['position']
		#track['artist']['name']
		#track['album']['title']
		#track['album']['cover_big']
		youtubeId = getIdByYoutube(track['title'].encode('utf-8') + " - " + track['artist']['name'].encode('utf-8'))
		downloadFisicalFile(youtubeId, track['id'])
	
		os.makedirs("../audio/"+str(track['id']))
		import subprocess
		subprocess.call("ffmpeg -i tempvideo/"+str(track['id'])+".mp4 -b:a 192K -vn \"../audio/"+str(track['id'])+"/"+track['title']+".mp3\" -loglevel quiet 2>tempvideo/output", shell=True, stdout=subprocess.PIPE)
		os.remove("tempvideo/"+str(track['id'])+".mp4")
	
		#descargar imagen
		#getImage(track['album']['cover'], str(track['id']))
		#completar archivo mp3
		setInfo(track)
		
		#cocomo.execute("CALL insertDownload ( '" + _POST['id_user'] + "' , '" + _POST['id'] + "' )")
		
		cocomo.printJson({"trackURL":"../audio/"+_POST['id']+"/"+track['title']+".mp3"}, "success")
	except Exception, ex:
		cocomo.printJson("No se puede obtener el archivo descargado, El motor dice: " + str(ex), "error")

def getIdByYoutube(searchTerms):
		url = r"https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + ( searchTerms ) + "&type=video&key=AIzaSyAfXxWUUZ1nxII62vg-XR0Shuv_ikuVT2A"
		url = url.replace(" ", "+")
		req = urllib2.Request(url)
		opener = urllib2.build_opener()
		f = opener.open(req)
		json_data = json.load(f)
		return json_data['items'][0]['id']['videoId']

def downloadFisicalFile(youtubeId, idName):
	yt = YouTube()
	yt.url = ("http://www.youtube.com/watch?v=" + youtubeId)
	yt.filename = idName
	video = 0
	if len(yt.filter('mp4')) > 0:
		if len(yt.filter(resolution='720p')) > 0:
			video = yt.get('mp4','720p')
		else:
			video = yt.get('mp4')

		video.download("tempvideo/")
	else:
		cocomo.printJson("no se puede descargar el archivo", "error")
	
	#cocomo.printJson(yt.videos, "test")

def setInfo(track):
	audiofile = eyed3.load("../audio/"+str(track["id"])+"/"+track["title"]+".mp3")
	audiofile.tag.artist = track['artist']['name']
	audiofile.tag.album = track['album']['title']
	audiofile.tag.album_artist = track['artist']['name']
	audiofile.tag.title = track['title']
	audiofile.tag.track_num = int(track['track_position'])
	#imagedata = open("../audio/"+str(track['id'])+"/"+str(track['id'])+".jpg","rb").read()
	#audiofile.tag.images.set(3,imagedata,"image/jpeg",u"By Raptor")
	audiofile.tag.save()
	#os.remove("../audio/"+str(track['id'])+"/"+str(track['id'])+".jpg")


def getImage(url, idname):
	import urllib
	urllib.urlretrieve(url, "../audio/"+str(idname)+"/"+str(idname)+".jpg")

def getSuggested():
	# _POST['id'] = cocomo.query("CALL getLastDownload (" + _POST['id_user'] + ")")[0][0]
	# id_artist = getInfo(False)['artist']['id']
	# cocomo.printJson( smartGet( "http://api.deezer.com/artist/" + str ( id_artist ) + "/top" ) , "success")
	h = smartGet( "http://api.deezer.com/radio" , False )
	r = random.randrange(10)
	h = h['data'][r]['id']
	smartGet( "https://api.deezer.com/radio/" + str ( h ) + "/tracks" )

def smartGet( url, service=True ):
	# cache = cocomo.query("CALL getCache ( '" + url + "' )")
	# n = len(cache)
	# if n != 0:
	# 	if service:
	# 		cocomo.printJson( json.loads( cache[0][0].decode("hex") ) , "success" )
	# 		return
	# 	else:
	# 		return json.loads( cache[0][0].decode("hex") )
	# else:
	# 	f = urllib2.urlopen(url)
	# 	f = json.loads(f.read())
	# 	cocomo.execute("CALL setCache ( '" + url + "', '" + json.dumps(f).encode("hex") + "' )")
	# 	return f
	f = urllib2.urlopen(url)
	f = json.loads(f.read())
	if service:
		cocomo.printJson( f , "success" )
		return
	else:
		return f
		


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
