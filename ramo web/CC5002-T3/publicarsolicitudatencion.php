<?php 
require_once('db_config.php');
require_once('consultas.php');
require_once('validaciones_solicitud.php');

$db = DbConfig::getConnection();

$especialidades_info = get_especialidades($db);
$regiones_info = get_regiones($db);
$comunas_info = get_comunas($db);

$db->close();
?>

<?php
$post_is_ok = true;

$files_names = array();
$files_filenames = array();
$files_MIME = array();

if(!empty($_POST)){
	if(!checkNombre($_POST)){
	    $post_is_ok = false;
	}
	if(!checkEsp($_POST, $especialidades_info)){
	    $post_is_ok = false;
	}
	if(!checkSintomas($_POST)){
	    $post_is_ok = false;
	}
	if(!checkTwitter($_POST)){
		$post_is_ok = false;
	}
	if(!checkEmail($_POST)){
		$post_is_ok = false;
	}
	if(!checkCelular($_POST)){
		$post_is_ok = false;
	}
	if(!checkRegion($_POST, $regiones_info)){
	    $post_is_ok = false;
	}
	if(!checkComuna($_POST, $comunas_info)){
	    $post_is_ok = false;
	}
	// only if the post is ok we'll check if we can upload the photos
	if($post_is_ok){
		if(!checkAndUploadFiles($_FILES, $files_names, $files_filenames, $files_MIME)){
			$post_is_ok = false;
		}
	}

	if($post_is_ok){

		//INSERT into $db
		$db = DbConfig::getConnection();
		$res = savePost($db, 
			$_POST['nombre-solicitante'], 
			$_POST['especialidad-solicitud'], 
			$_POST['sintomas-solicitante'], 
			$_POST['twitter-solicitante'], 
			$_POST['email-solicitante'], 
			$_POST['celular-solicitante'], 
			$_POST['comuna-solicitante'],
			$files_filenames,
			$files_names,
			$files_MIME);
		$db->close();

		// redirect
		session_start();
		if($res){
			$_SESSION['message'] = 'Su solicitud se subió con éxito al servidor.';
		} else {
			$_SESSION['message'] = 'Su solicitud no pudo ser procesada por el servidor, intente de nuevo.';
		}

		header("Location: index.php");

	}
}
?>


<!DOCTYPE html>

<html lang="es">

	<head>

		<meta charset="utf-8">
		
		<script src = "validatesolicitudes.js"></script>
		<script>

			var file_slots = 1;

			function add_new_file_slot(){
				if(file_slots<5){
					file_slots++;
					previous_html = document.getElementById("file-inputs").innerHTML;
					new_html = previous_html + '<input type="file" name="archivos-solicitante[' + (file_slots-1) + ']"><br>';
					document.getElementById("file-inputs").innerHTML = new_html;
				}
				else{
					alert("Máximo 5 archivos")
				}
			}

			var comunas = [<?php 
					$string = "";
					foreach($comunas_info as $comuna_info){ 
						$string = $string."[".$comuna_info["region_id"].",".$comuna_info["id"].",\"".$comuna_info["nombre"]."\"],";
					}
					echo substr($string, 0, -1);
				?>];

			function updateComunas(){

				region_id = document.getElementById("regiones").value;
				comunas_select = document.getElementById("comunas");
				comunas_select.innerHTML = "<option value='0'>- Seleccione una comuna -</option>";

				for (const comuna of comunas){
					if(comuna[0]==region_id){
						comunas_select.innerHTML += "<option value='" + comuna[1] + "'>" + comuna[2] + "</option>";
					}
				}
			}

		</script>

		<title>Publicar Solicitud de Atención</title>

	</head>

	<body>

		<?php
		if(!$post_is_ok){
			echo "No se cumplieron las validaciones de parte del servidor, intente con otro navegador para una experiencia más guiada.<br>";
		}
		?>

		<a href="index.php">Volver a la página principal</a><br>
		<br>

		<form name="mainform" method="POST" enctype="multipart/form-data">
			
			Nombre:<br>
			<input type="text" size="30" name="nombre-solicitante"><br>
			
			Especialidad:<br>
			<select name="especialidad-solicitud">
				<option value="0">- Selecciona una especialidad-</option>
				<?php 
				foreach($especialidades_info as $esp_info){ 
					echo "<option value='" . $esp_info["id"] . "'>" . $esp_info["descripcion"] . "</option> ";
				}
				?>
			</select><br>

			Descripción de Síntomas:<br>
			<textarea rows="8" cols="40" name="sintomas-solicitante"></textarea><br>

			Archivos Complementarios:<br>
			<div id="file-inputs">
				<input type="file" name="archivos-solicitante[0]"><br>
			</div>
			<button id="nueva-archivo" type="button" onclick="add_new_file_slot()">Agregar otro archivo</button><br>

			Twitter:<br>
			<input type="text" size="80" name="twitter-solicitante"><br>

			Email:<br>
			<input type="text" size="80" name="email-solicitante"><br>

			Celular:<br>
			<input type="text" size="15" name="celular-solicitante"><br>

			Región:<br>
			<select id="regiones" name="region-solicitante" onclick="updateComunas();">
				<option value="0">- Seleccione una región -</option>
				<?php 
				foreach($regiones_info as $region_info){ 
					echo "<option value='" . $region_info["id"] . "'>" . $region_info["nombre"] . "</option>";
				}
				?>
			</select><br>

			Comuna:<br>
			<select id="comunas" name="comuna-solicitante">
				<option value="0">- Seleccione una comuna -</option>
			</select><br>

			<button type="button" onclick="validate()">Enviar</button>
			<button type="submit">Enviar sin validar >:)</button>

		</form>
		
	</body>

</html>