<?php 
require_once('db_config.php');
require_once('consultas.php');

if(isset($_GET['offset'])){
	$offset = (int)($_GET['offset']-1)*5;
	$db = DbConfig::getConnection();
	$count = count_solicitudes($db);
	if($offset > $count){
		die("offset fuera de rango");
	}
	$solicitudes = get_solicitudes($db, $offset);
	$comunas = get_nombre_comunas($db, $solicitudes);
	$especialidades = get_descripcion_especialidades($db, $solicitudes);
	$db->close();
} else {
	echo "no se detectó offset, favor vuelva a la página principal";
	die();
}
?>


<!DOCTYPE html>

<html lang="es">

	<head>

		<meta charset="utf-8">

		<style>
			table, tr, td {
	  			border: 1px solid black;
			}
			td:hover {
				cursor: pointer;
			}
		</style>

		<script>
			function get_details(id){
				window.location.replace("detallesolicitud.php?id="+id);
			}
			function loadSolicitantes() {
			  	var xhttp = new XMLHttpRequest();
			  	var value = document.getElementById("rellenasolicitante").value;
			  	var div = document.getElementById("queried_solicitantes");
			  	if(value.length < 3){
			  		div.innerHTML = "";
			  		return;
			  	}
			  	xhttp.onreadystatechange = function() {
				    if (this.readyState == 4 && this.status == 200) {
				     	div.innerHTML = this.responseText;
				    }
			  	};
			  	xhttp.open("GET", `completasolicitante.php?start=${value}`, true);
			  	xhttp.send();
			}
		</script>

		<title>Ver Solicitudes de Atención</title>

	</head>

	<body onload="loadSolicitantes()">

		<a href="index.php">Volver a la página principal</a><br>
		<br>

		<input id="rellenasolicitante" type="text" oninput="loadSolicitantes()"><br>

		<div id="queried_solicitantes"></div><br>

		<table>

			<tr>
				<th>Nombre Solicitante</th>
				<th>Especialidad</th>
				<th>Comuna</th>
				<th>Datos Contacto</th>
			</tr>
			<?php 

			for($i = 0; $i < sizeof($solicitudes); $i++){
				$solicitud = $solicitudes[$i];
				echo sprintf('<tr onclick="get_details(\'%d\')">', (int)$solicitud['id']);
				echo sprintf("<td>%s</td>", $solicitud['nombre_solicitante']);
				echo sprintf("<td>%s</td>", $especialidades[$i]['descripcion']);
				echo sprintf("<td>%s</td>", $comunas[$i]['nombre']);
				echo sprintf("<td>email: %s <br> twitter: %s <br> telefono: %s</td>", check($solicitud['email']), check($solicitud['twitter']), check($solicitud['celular']));
				echo sprintf("</tr>");
			}
			?>
		</table>
		<?php 
		$offset = 1;
		while($count > 0){
			echo sprintf('<form method="get" style="display:inline"><input type="submit" name="offset" value="%d"></form>', $offset);
			$offset+=1;
			$count-=5;
		}
		?>
	</body>

</html>