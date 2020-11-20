<?php
function checkRegion($post, $regiones){
	if(isset($post['region-solicitante'])){
	    foreach($regiones as $region){
	        if ($post['region-solicitante'] === $region["id"]){
	            return true;
	        }
	    }
	}
	return false;
}
function checkComuna($post, $comunas){
	if(isset($post['comuna-solicitante'])){
	    foreach($comunas as $comuna){
	        if ($post['comuna-solicitante'] === $comuna["id"]){
	        	if($post['region-solicitante'] === $comuna["region_id"]){
	        		return true;
	        	}
	        }
	    }
	}
	return false;
}
function checkNombre($post){
	if(isset($post['nombre-solicitante'])){
		if($post['nombre-solicitante'] !== ""){
			return true;
		}
	}
	return false;
}
function checkSintomas($post){
	if(isset($post['sintomas-solicitante'])){
		if(strlen($post['sintomas-solicitante']) < 500){
			return true;
		}
	}
	return false;
}
function checkEsp($post, $especialidades){
	if(isset($post['especialidad-solicitud'])){
		if($post['especialidad-solicitud'] === ""){
			return false;
		}
		foreach($especialidades as $especialidad) {
	        if ($especialidad['id'] === $post['especialidad-solicitud']){
	            return true;
	        }
		}
		return true;
	}
	return false;
}

function checkTwitter($post){
	if(isset($post['twitter-solicitante'])){
		if($post['twitter-solicitante'] !== ""){
			$regex = "/^[a-zA-Z0-9]*$/";
			if(!preg_match($regex, $post['twitter-solicitante'])){
				return false;
			}
			if(strlen($post['twitter-solicitante']) < 3){
				return false;
			}
			if(strlen($post['twitter-solicitante']) > 80){
				return false;
			}
		}
	}
	return true;
}
function checkEmail($post){
	if(isset($post['email-solicitante'])){
		if($post['email-solicitante'] == ""){
			return false;
		}
		$regex = "/^[a-zA-Z][a-zA-Z]*[a-zA-Z0-9]*@[a-zA-Z][a-zA-Z]*.[a-zA-Z][a-zA-Z]*$/";
		if(preg_match($regex, $post['email-solicitante'])){
			return true;
		}
	}
	return false;
}
function checkCelular($post){
	if(isset($post['celular-solicitante'])){
		if($post['celular-solicitante'] !== ""){
			$regex = "/^\+569?\d{8}$/";
			if(!preg_match($regex, $post['celular-solicitante'])){
				return false;
			}
		}
	}
	return true;
}
function checkAndUploadFiles($files, &$f_names, &$f_filenames, &$f_mime){

	// check if dir exists
	if(!file_exists("archivos-solicitantes")){
	    mkdir("archivos-solicitantes");
	}

	// get file name
	$target_dir = "archivos-solicitantes/";

	// check if not empty
	if(isset($files['archivos-solicitante'])){

		$n = sizeof($files['archivos-solicitante']['name']);

		for($i = 0; $i < $n; $i++) {

			if($files['archivos-solicitante']['name'][$i] !== ""){

				$file_is_ok = true;

				// we create a new filename using date and rand
				$target_name = basename($files['archivos-solicitante']["name"][$i]);
				$extention = substr($target_name, strrpos($target_name, '.', -1));
				$target_file = $target_dir . date("YmdHis") . rand(1000,9999) . $extention;

				// check if filename exists in the server
				if(file_exists($target_file)){
				    $file_is_ok = false;
				}

		    	if($file_is_ok){
		    		// upload the file
				    if (move_uploaded_file($files['archivos-solicitante']["tmp_name"][$i], $target_file)) {
				        array_push($f_filenames, $target_file);
				        array_push($f_names, $target_name);
				        array_push($f_mime , mime_content_type($target_file));
				    } else {
				    	echo "No se pudo subir el archivo: " . $target_name . ", favor intentar más tarde.";
				    	return false;
				    }
		    	} else {
		    		echo "No se pudo subir el archivo: " . $target_name . "; ARCHIVO INVALIDO.";
		    		return false;
		    	}
	    	}
		}
		return true;
	}
	return true;
}
?>