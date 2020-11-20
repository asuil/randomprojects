<?php 
require_once('db_config.php');
require_once('consultas.php');
require_once('validaciones_medico.php');

$db = DbConfig::getConnection();

$especialidades_info = get_especialidades($db);
$regiones_info = get_regiones($db);
$comunas_info = get_comunas($db);

$db->close();
?>

<?php
$post_is_ok = true;

$photo_names = array();
$photo_filenames = array();

if(!empty($_POST)){
	if(!checkRegion($_POST, $regiones_info)){
    $post_is_ok = false;
	}
	if(!checkComuna($_POST, $comunas_info)){
	    $post_is_ok = false;
	}
	if(!checkNombre($_POST)){
	    $post_is_ok = false;
	}
	if(!checkExp($_POST)){
	    $post_is_ok = false;
	}
	if(!checkEsp($_POST, $especialidades_info)){
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
	// only if the post is ok we'll check if we can upload the photos
	if($post_is_ok){
		if(!checkAndUploadPhoto($_FILES, $photo_names, $photo_filenames)){
			$post_is_ok = false;
		}
	}

	if($post_is_ok){

		//INSERT into $db
		$db = DbConfig::getConnection();
		$res = saveMedico($db, 
			$_POST['nombre-medico'], 
			$_POST['experiencia-medico'], 
			$_POST['comuna-medico'], 
			$_POST['twitter-medico'], 
			$_POST['email-medico'], 
			$_POST['celular-medico'],
			$_POST['especialidades-medico'],
			$photo_filenames,
			$photo_names);
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

		<script src = "validatemedicos.js"></script>
		<script>

			var photo_slots = 1;

			function add_new_photo_slot(){
				if(photo_slots<5){
					photo_slots++;
					previous_html = document.getElementById("image-inputs").innerHTML;
					new_html = previous_html + '<input type="file" name="foto-medico[' + (photo_slots-1) + ']" accept="image/*"><br>';
					document.getElementById("image-inputs").innerHTML = new_html;
				}
				else{
					alert("Máximo 5 fotos")
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

		<title>Agrega Datos de Médico</title>

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

			Región:<br>
			<select id="regiones" name="region-medico" onchange="updateComunas();">
				<option value="0">- Seleccione una región -</option>
				<?php 
				foreach($regiones_info as $region_info){ 
					echo "<option value='" . $region_info["id"] . "'>" . $region_info["nombre"] . "</option>";
				}
				?>
			</select><br>

			Comuna:<br>
			<select id="comunas" name="comuna-medico">
				<option value="0">- Seleccione una comuna -</option>
			</select><br>

			Nombre:<br>
			<input type="text" size="30" name="nombre-medico"><br>

			Experiencia:<br>
			<textarea rows="8" cols="40" name="experiencia-medico"></textarea><br>

			Especialidades:<br>
			<select id="especialidades-medico" name="especialidades-medico[]" multiple>
				<?php 
				foreach($especialidades_info as $esp_info){ 
					echo "<option value='" . $esp_info["id"] . "'>" . $esp_info["descripcion"] . "</option> ";
				}
				?>
			</select><br>

			Foto:<br>
			<div id="image-inputs">
				<input type="file" name="foto-medico[0]" accept="image/*"><br>
			</div>
			<button id="nueva-foto" type="button" onclick="add_new_photo_slot()">Agregar otra foto</button><br>

			Twitter:<br>
			<input type="text" size="80" name="twitter-medico"><br>

			Email:<br>
			<input type="text" size="80" name="email-medico"><br>

			Celular:<br>
			<input type="text" size="15" name="celular-medico"><br>
			
			<button type="button" onclick="validate();">Enviar</button>
			<button type="submit">Enviar sin validar >:)</button>

		</form>
		
	</body>

</html>