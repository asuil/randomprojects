<?php 
require_once('db_config.php');
require_once('consultas.php');

if(isset($_GET['id'])){
	$id = (int)$_GET['id'];
	$db = DbConfig::getConnection();
	$solicitud_allinfo = get_allinfo_solicitud($db, $id);
	$solicitud_info = $solicitud_allinfo[0];
	$archivos_info = $solicitud_allinfo[1];
	$especialidad = get_descripcion_especialidades($db, [$solicitud_info])[0];
	$comuna = get_nombre_comunas($db, [$solicitud_info])[0];
	$region = get_nombre_region($db, $comuna);
	$db->close();
} else {
	echo "no se detectó id, favor vuelva a la página principal";
	die();
}
?>
<!DOCTYPE html>

<html lang="es">

	<head>

		<meta charset="utf-8">

		<title id="title">a</title>

	</head>

	<body>

		<a href="versolicitudesatencion.php?offset=1">Volver a la lista de solicitudes</a><br>
		<br>
		
		
		<?php 
		echo sprintf("Nombre:<br>%s<br><br>", $solicitud_info['nombre_solicitante']);
		echo sprintf("Especialidad:<br>%s<br><br>", $especialidad['descripcion']);
		echo sprintf("Descripción de síntomas:<br>%s<br><br>", check($solicitud_info['sintomas']));
		echo "Archivos Complementarios:<br>";
		if(!empty($archivos_info)){
			foreach ($archivos_info as $archivo) {
				echo sprintf("<a href='%s' download>%s</a>( MIMETYPE: %s )<br>", $archivo['ruta_archivo'], $archivo['nombre_archivo'], $archivo['mimetype']);
			}
		} else {
			echo "No se adjuntaron archivos.<br>";
		}
		echo sprintf("<br>Twitter:<br>%s<br><br>", check($solicitud_info['twitter']));
		echo sprintf("E-mail:<br>%s<br><br>", check($solicitud_info['email']));
		echo sprintf("Celular:<br>%s<br><br>", check($solicitud_info['celular']));
		echo sprintf("Región:<br>%s<br><br>", $region['nombre']);
		echo sprintf("Comuna:<br>%s<br><br>", $comuna['nombre']);
		?>
	</body>

</html>