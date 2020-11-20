<?php
function get_especialidades($db) {
	$sql = "SELECT id, descripcion FROM especialidad";
	$result = $db->query($sql) or die($db->error);
	$especialidades_info = array();
	while ($row = $result->fetch_assoc()) {
		$especialidades_info[] = $row;
	}
	return $especialidades_info;
}
function get_regiones($db) {
	$sql = "SELECT id, nombre FROM region";
	$result = $db->query($sql) or die($db->error);
	$regiones_info = array();
	while ($row = $result->fetch_assoc()) {
		$regiones_info[] = $row;
	}
	return $regiones_info;
}
function get_comunas($db) {
	$sql = "SELECT id, nombre, region_id FROM comuna";
	$result = $db->query($sql) or die($db->error);
	$comunas_info = array();
	while ($row = $result->fetch_assoc()) {
		$comunas_info[] = $row;
	}
	return $comunas_info;
}
function limpiar($db, $str){
	return htmlspecialchars($db->real_escape_string($str));
}
function savePost($db, $nombre, $especialidad_id, $sintomas, $twitter, $email, $celular, $comuna_id, $rutas, $names, $mimes){

	$sql = "INSERT INTO solicitud_atencion (nombre_solicitante, especialidad_id, sintomas, twitter, email, celular, comuna_id) VALUES (?, ?, ?, ?, ?, ?, ?)";
	$stmt = $db->prepare($sql);

	$nombre_db = limpiar($db, $nombre);
	$especialidad_id_db = limpiar($db, $especialidad_id);
	$sintomas_db = limpiar($db, $sintomas);
	$twitter_db = limpiar($db, $twitter);
	$email_db = limpiar($db, $email);
	$celular_db = limpiar($db, $celular);
	$comuna_id_db = limpiar($db, $comuna_id);

	$stmt->bind_param("sissssi", $nombre_db, $especialidad_id_db, $sintomas_db, $twitter_db, $email_db, $celular_db, $comuna_id_db);

	if ($stmt->execute()) {

		$last_id = $db->insert_id;
		$ok = true;

		for($i = 0; $i < sizeof($rutas); $i++) {
			
			$sql = "INSERT INTO archivo_solicitud (ruta_archivo, nombre_archivo, mimetype, solicitud_atencion_id) VALUES (?, ?, ?, ?)";
			$stmt = $db->prepare($sql);

			$ruta_archivo_db = $rutas[$i]; 					// made by the server
			$nombre_archivo_db = limpiar($db, $names[$i]);
			$mime_db = $mimes[$i]; 							// made by the server

			$stmt->bind_param("sssi", $ruta_archivo_db, $nombre_archivo_db, $mime_db, $last_id);
			if($stmt->execute()){
				$ok = false;
			}
		}
		if($ok){ return true; }
	}
	return false;
}
function saveMedico($db, $nombre, $experiencia, $comuna_id, $twitter, $email, $celular, $especialidades, $rutas, $names){

	$sql = "INSERT INTO medico (nombre, experiencia, comuna_id, twitter, email, celular) VALUES (?, ?, ?, ?, ?, ?)";
	$stmt = $db->prepare($sql);

	$nombre_db = limpiar($db, $nombre);
	$experiencia_db = limpiar($db, $experiencia);
	$comuna_id_db = limpiar($db, $comuna_id);
	$twitter_db = limpiar($db, $twitter);
	$email_db = limpiar($db, $email);
	$celular_db = limpiar($db, $celular);

	$stmt->bind_param("ssisss", $nombre_db, $experiencia_db, $comuna_id_db, $twitter_db, $email_db, $celular_db);

	if($stmt->execute()){

		$last_id = $db->insert_id;
		$ok = true;

		for ($i = 0; $i < sizeof($rutas); $i++) { 
			
			$sql = "INSERT INTO foto_medico (ruta_archivo, nombre_archivo, medico_id) VALUES (?, ?, ?)";
			$stmt = $db->prepare($sql);

			$ruta_archivo_db = $rutas[$i]; 					// made by the server
			$nombre_archivo_db = limpiar($db, $names[$i]);

			$stmt->bind_param("ssi", $ruta_archivo_db, $nombre_archivo_db, $last_id);
			if(!$stmt->execute()){
				$ok = false;
			}
		}

		for ($i = 0; $i < sizeof($especialidades); $i++) { 
			
			$sql = "INSERT INTO especialidad_medico (medico_id, especialidad_id) VALUES (?, ?)";
			$stmt = $db->prepare($sql);

			$especialidad_db = limpiar($db, $especialidades[$i]);

			$stmt->bind_param("si", $last_id, $especialidad_db);
			if(!$stmt->execute()){
				$ok = false;
			}
		}
		if($ok){ return true; }
	}
	return false;
}
function get_medicos($db, $offset){
	$sql = "SELECT id, nombre, experiencia, comuna_id, twitter, email, celular FROM medico ORDER BY id DESC LIMIT 5 OFFSET ?";
	$stmt = $db->prepare($sql);

	$stmt->bind_param("i", $offset);
	$stmt->execute() or die("no se pudo obtener la información");

	$result = $stmt->get_result();
	$medicos_info = array();
	while ($row = $result->fetch_assoc()) {
		$medicos_info[] = $row;
	}
	return $medicos_info;
}
function get_nombre_comunas($db, $entities){
	$nombres = array();
	foreach($entities as $entity){
		$id = $entity['comuna_id'];

		$sql = "SELECT region_id, nombre FROM comuna WHERE id=$id";
		$result = $db->query($sql) or die($db->error);

		$nombres[] = $result->fetch_assoc();
	}
	return $nombres;
}
function get_especialidades_medicos($db, $medicos){
	$esps = array();
	foreach($medicos as $medico){
		$id = $medico['id'];

		$sql = "SELECT ESP.descripcion FROM especialidad ESP, especialidad_medico ESPME WHERE ESPME.especialidad_id=ESP.id AND ESPME.medico_id=$id";
		$result = $db->query($sql) or die($db->error);

		$esps_this = array();
		while ($row = $result->fetch_assoc()) {
			$esps_this[] = $row;
		}
		$esps[] = $esps_this;
	}
	return $esps;
}
function count_medicos($db){
	$sql = "SELECT count(id) as count FROM medico";
	$result = $db->query($sql) or die($db->error);
	return $result->fetch_assoc()['count'];
}
function count_solicitudes($db){
	$sql = "SELECT count(id) as count FROM solicitud_atencion";
	$result = $db->query($sql) or die($db->error);
	return $result->fetch_assoc()['count'];
}
function get_solicitudes($db, $offset){
	$sql = "SELECT id, nombre_solicitante, especialidad_id, sintomas, twitter, email, celular, comuna_id FROM solicitud_atencion ORDER BY id DESC LIMIT 5 OFFSET ?";
	$stmt = $db->prepare($sql);

	$stmt->bind_param("i", $offset);
	$stmt->execute() or die("no se pudo obtener la información");

	$result = $stmt->get_result();
	$solicitudes_info = array();
	while ($row = $result->fetch_assoc()) {
		$solicitudes_info[] = $row;
	}
	return $solicitudes_info;
}
function get_descripcion_especialidades($db, $solicitudes){
	$descripciones = array();
	foreach($solicitudes as $solicitud){
		$id = $solicitud['especialidad_id'];

		$sql = "SELECT descripcion FROM especialidad WHERE id=$id";
		$result = $db->query($sql) or die($db->error);

		$descripciones[] = $result->fetch_assoc();
	}
	return $descripciones;
}
function get_allinfo_medico($db, $id){

	$sql = "SELECT id, nombre, experiencia, comuna_id, twitter, email, celular FROM medico WHERE id=?";
	$stmt = $db->prepare($sql);

	$stmt->bind_param("i", $id);
	$stmt->execute() or die("no se pudo obtener la información");

	$result = $stmt->get_result();

	$medico_info = $result->fetch_assoc();



	$sql = "SELECT id, ruta_archivo, nombre_archivo, medico_id FROM foto_medico WHERE medico_id=?";
	$stmt = $db->prepare($sql);

	$stmt->bind_param("i", $id);
	$stmt->execute() or die("no se pudo obtener la información");

	$result = $stmt->get_result();

	$fotos_info = array();
	while ($row = $result->fetch_assoc()) {
		$fotos_info[] = $row;
	}


	return [$medico_info, $fotos_info];

}
function get_allinfo_solicitud($db, $id){

	$sql = "SELECT id, nombre_solicitante, especialidad_id, sintomas, twitter, email, celular, comuna_id FROM solicitud_atencion WHERE id=?";
	$stmt = $db->prepare($sql);

	$stmt->bind_param("i", $id);
	$stmt->execute() or die("no se pudo obtener la información");

	$result = $stmt->get_result();

	$solicitud_info = $result->fetch_assoc();



	$sql = "SELECT ruta_archivo, nombre_archivo, mimetype, solicitud_atencion_id FROM archivo_solicitud WHERE solicitud_atencion_id=?";
	$stmt = $db->prepare($sql);

	$stmt->bind_param("i", $id);
	$stmt->execute() or die("no se pudo obtener la información");

	$result = $stmt->get_result();

	$archivos_info = array();
	while ($row = $result->fetch_assoc()) {
		$archivos_info[] = $row;
	}


	return [$solicitud_info, $archivos_info];
	
}
function check($str){return ($str!=="")?$str:"No ingresado";}
function get_nombre_region($db, $entity){
	$nombres = array();
	$id = $entity['region_id'];

	$sql = "SELECT nombre FROM region WHERE id=$id";
	$result = $db->query($sql) or die($db->error);

	return $result->fetch_assoc();
}
?>