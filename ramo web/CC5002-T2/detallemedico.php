<?php 
require_once('db_config.php');
require_once('consultas.php');

if(isset($_GET['id'])){
	$id = (int)$_GET['id'];
	$db = DbConfig::getConnection();
	$medico_allinfo = get_allinfo_medico($db, $id);
	$medico_info = $medico_allinfo[0];
	$foto_info = $medico_allinfo[1];
	$especialidades = get_especialidades_medicos($db, [$medico_info])[0];
	$comuna = get_nombre_comunas($db, [$medico_info])[0];
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

		<script>

			function resize(id){
				
				fotos = document.getElementsByClassName('foto');

				for(let i = 0; i < fotos.length; i++){
					if(parseInt(fotos[i].id) === id && fotos[i].width === 320){
						fotos[i].width = 800;
						fotos[i].height = 600;
					} else {
						fotos[i].width = 320;
						fotos[i].height = 240;
					}
				}
			}

		</script>

		<title id="title">Detalles de <?php echo $medico_info['nombre'] ?></title>

	</head>

	<body>

		<a href="vermedicos.php?offset=1">Volver a la lista de médicos</a><br>
		<br>
		<?php 
		echo sprintf("Región:<br>%s<br><br>", $region['nombre']);
		echo sprintf("Comuna:<br>%s<br><br>", $comuna['nombre']);
		echo sprintf("Nombre:<br>%s<br><br>", $medico_info['nombre']);
		echo sprintf("Experiencia:<br>%s<br><br>", $medico_info['experiencia']);
		echo "Especialidades:<br>";
		foreach ($especialidades as $esp) {
			echo sprintf("%s<br>", $esp['descripcion']);
		}
		echo "<br>Foto:<br>";
		foreach ($foto_info as $foto) {
			echo sprintf("<img width='320' alt='foto del doctor' style='display:inline' height='240' class='foto' id='%d' src='%s' onclick='resize(%d);'>", $foto['id'], $foto['ruta_archivo'], $foto['id']);
		}
		echo "<br>";
		echo sprintf("Twitter:<br>%s<br><br>", check($medico_info['twitter']));
		echo sprintf("E-mail:<br>%s<br><br>", check($medico_info['email']));
		echo sprintf("Celular:<br>%s<br><br>", check($medico_info['celular']));
		 ?>
	</body>

</html>