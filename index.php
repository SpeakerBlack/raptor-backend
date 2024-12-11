<?php 
	header("Access-Control-Allow-Origin: *");  
	
	$url=$_SERVER['REQUEST_URI'];

	$url = str_replace("%20", " ", $url);

	if(strrpos($url, "?")>-1){
		$url = substr($url, 0, strrpos($url, "?")-1)."<br>";
	}

	if (count($_POST) == 0) {
		$_POST = $_GET;
	}

	$var = explode("/", $url);

	ini_set('max_execution_time', 300);

	#$var[2] = vista o 'post' para invocar el servicio web
	#$var[3] = subvista

	#cuando no hay $var[3] se redirige al home
	#si no existe el $var[3] especificado se va a la pagina 404.php

	if (count($_FILES)>0) {
		$output_dir = "default/";
		$cont = array("file"=>0,"post"=>0);

		#se hace lo que se deba hace en python, una funcion de ayuda para la subida
		#se elimina el archivo temporal

		move_uploaded_file($_FILES["file"]['tmp_name'], $output_dir.$_FILES["file"]['name']);
		$_FILES["file"]['tmp_name'] = $output_dir.$_FILES["file"]['name'];
		$cont['file'] = $_FILES["file"];
		$cont['post'] = $_POST;
		echo shell_exec("python service/".$var[3].".py ".$var[4]." \"".str_replace('"', '\\"', json_encode($cont))."\" 2>&1");
		#echo json_encode($cont);
		exit();
	}

	############################################################
	##
	##Cuando se solicita un archivo activo o un contenido del sitio, se debe especificar el tipo de contenido
	##
	############################################################


	$activos = array(
		".js"=>"application/javascript", 
		".css"=>"text/css", 
		".ttf"=>"application/x-font-ttf", 
		".jpg"=>"image/jpeg", 
		".png"=>"image/png", 
		".gif"=>"image/gif",
		".mp3"=>"audio/MPA");
	foreach ($activos as $key => $value) {
		if (endsWith($url, $key)){
			$url = substr($url, 1);
			$ruta = getcwd()."/view".substr($url,stripos($url, "/"));
			if (!file_exists($ruta)) {
				$ruta = getcwd()."/".substr($url,stripos($url, "/"));
				if (!file_exists($ruta)) {
					echo "404...";
				}
			}
			header("Content-type:".$value);
			include($ruta);
			exit();
		}
	}

	############################################################
	##
	##Cuando se hace una solicitud post, significa que se hace una solictud se servicio web
	##
	############################################################

	#Comando a python:
	#1°		$var[3] = nombre del script python
	#2°		$var[4] = funcion
	#3°		$_POST = parametros enviados desde la vista en formato json

	if (strtolower($var[2]) == "post") {
		if (isset($var[3])) {
			if (!file_exists("service/".$var[3].".py")) {
				echo json_encode(array("message"=>"This service '".$var[3]."' dont exist"));
				exit();
			}
			#echo "python service/".$var[3].".py ".$var[4]." \"".str_replace('"', '\\"', json_encode($_POST))."\" 2>&1";
			echo shell_exec("python service/".$var[3].".py ".$var[4]." \"".str_replace('"', '\\"', json_encode($_POST))."\" 2>&1");
		} else {
			echo shell_exec("python service/default.py \"[]\" 2>&1");
		}		
		exit();
	}

	############################################################
	##
	##Esto para mostrar las vistas
	##
	############################################################
	if ($var[2] == "") {
		includeFile("view/home/index.php");
		exit();
	}

	if (isset($var[3])) {
		includeFile("view/".$var[2]."/".$var[3].".php");
	} else {
		includeFile("view/".$var[2]."/index.php");
	}

	function checkFileExists($file) {
		if (!file_exists($file)) {
			require 'default/404.php';
			exit();
		}
	}

	function includeFile($file) {
		checkFileExists($file);
		require_once("default/header.php"); 
		include_once($file);
		require_once("default/footer.php");
		exit();
	}

	function endsWith($haystack, $needle) {
    	// search forward starting from end minus needle length characters
    	return $needle === "" || (($temp = strlen($haystack) - strlen($needle)) >= 0 && strpos($haystack, $needle, $temp) !== false);
	}

 ?>