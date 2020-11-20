<?php 
require_once('db_config.php');
require_once('consultas.php');

if(isset($_GET['offset'])){
	$offset = (int)($_GET['offset']-1)*5;
	$db = DbConfig::getConnection();
	$count = count_medicos($db);
	if($offset > $count){
		die("offset fuera de rango");
	}
	$medicos = get_medicos($db, $offset);
	$comunas = get_nombre_comunas($db, $medicos);
	$especialidades = get_especialidades_medicos($db, $medicos);
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
			table, th, td {
	  			border: 1px solid black;
			}
			td:hover {
				cursor: pointer;
			}
		</style>

		<script>
			function get_details(id){
				window.location.replace("detallemedico.php?id="+id);
			}
		</script>

		<title>Ver Médicos</title>

	</head>

	<body>

		<a href="index.php">Volver a la página principal</a><br>
		<br>

		<table>

			<tr>
				<th>Nombre Médico</th>
				<th>Especialidades</th>
				<th>Comuna</th>
				<th>Datos Contacto</th>
			</tr>
			<?php 
			for($i = 0; $i < sizeof($medicos); $i++){
				$medico = $medicos[$i];
				$esps = $especialidades[$i];
				echo sprintf('<tr onclick="get_details(\'%d\')">', (int)$medico['id']);
				echo sprintf("<td>%s</td>", $medico['nombre']);
				echo "<td>";
				foreach ($esps as $esp) {
					echo sprintf("%s<br>", $esp['descripcion']);
				}
				echo "</td>";
				echo sprintf("<td>%s</td>", $comunas[$i]['nombre']);
				echo sprintf("<td>email: %s <br> twitter: %s <br> telefono: %s</td>", check($medico['email']), check($medico['twitter']), check($medico['celular']));
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