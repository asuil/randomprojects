<?php
function checkRegion($post, $regiones){
	if(isset($post['region-medico'])){
	    foreach($regiones as $region){
	        if ($post['region-medico'] === $region["id"]){
	            return true;
	        }
	    }
	}
	return false;
}
function checkComuna($post, $comunas){
	if(isset($post['comuna-medico'])){
	    foreach($comunas as $comuna){
	        if ($post['comuna-medico'] === $comuna["id"]){
	        	if($post['region-medico'] === $comuna["region_id"]){
	        		return true;
	        	}
	        }
	    }
	}
	return false;
}
function checkNombre($post){
	if(isset($post['nombre-medico'])){
		if($post['nombre-medico'] !== ""){
			return true;
		}
	}
	return false;
}
function checkExp($post){
	if(isset($post['experiencia-medico'])){
		if(strlen($post['experiencia-medico']) < 500){
			return true;
		}
	}
	return false;
}
function checkEsp($post, $especialidades){
	if(isset($post['especialidades-medico'])){
		if(sizeof($post['especialidades-medico']) === 0){
			return false;
		}
		if(sizeof($post['especialidades-medico']) > 5){
			return false;
		}
		foreach ($post['especialidades-medico'] as $especialidad_medico) {
			$exists = false;
			foreach($especialidades as $especialidad){
		        if ($especialidad['id'] === $especialidad_medico){
		            $exists = true;
		        }
	    	}
	    	if(!$exists){
	    		return false;
	    	}
		}
		return true;
	}
	return false;
}
function checkTwitter($post){
	if(isset($post['twitter-medico'])){
		if($post['twitter-medico'] !== ""){
			$regex = "/^[a-zA-Z0-9]*$/";
			if(!preg_match($regex, $post['twitter-medico'])){
				return false;
			}
			if(strlen($post['twitter-medico']) < 3){
				return false;
			}
			if(strlen($post['twitter-medico']) > 80){
				return false;
			}
		}
	}
	return true;
}
function checkEmail($post){
	if(isset($post['email-medico'])){
		if($post['email-medico'] == ""){
			return false;
		}
		$regex = "/^[a-zA-Z][a-zA-Z]*[a-zA-Z0-9]*@[a-zA-Z][a-zA-Z]*.[a-zA-Z][a-zA-Z]*$/";
		if(preg_match($regex, $post['email-medico'])){
			return true;
		}
	}
	return false;
}
function checkCelular($post){
	if(isset($post['celular-medico'])){
		if($post['celular-medico'] !== ""){
			$regex = "/^\+569?\d{8}$/";
			if(!preg_match($regex, $post['celular-medico'])){
				return false;
			}
		}
	}
	return true;
}
function checkAndUploadPhoto($files, &$p_names, &$p_filenames){

	// check if dir exists
	if(!file_exists("fotos-medicos")){
	    mkdir("fotos-medicos");
	}

	// get file name
	$target_dir = "fotos-medicos/";

	// check if not empty
	if(isset($files['foto-medico'])){

		$n = sizeof($files['foto-medico']['name']);
		$at_least_one = false;

		for($i = 0; $i < $n; $i++) {

			if($files['foto-medico']['name'][$i] !== ""){

				$at_least_one = true;
				$file_is_ok = true;

				// we create a new filename using date and rand
				$target_name = basename($files['foto-medico']["name"][$i]);
				$extention = substr($target_name, strrpos($target_name, '.', -1));
				$target_file = $target_dir . date("YmdHis") . rand(1000,9999) . $extention;

				// check if filename exists in the server
				if(file_exists($target_file)){
				    $file_is_ok = false;
				}

				// check if file is an image
		    	$image_data = getimagesize($files['foto-medico']["tmp_name"][$i]);

		    	if($image_data === false) {
			        $file_is_ok = false;
		    	}

		    	if($file_is_ok){
		    		// upload the file
				    if (move_uploaded_file($files['foto-medico']["tmp_name"][$i], $target_file)) {
				        array_push($p_filenames, $target_file);
				        array_push($p_names, $target_name);
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
		if($at_least_one){
			return true;
		}
	}
	return false;
}
?>