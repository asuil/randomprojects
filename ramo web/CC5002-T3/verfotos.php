<?php 
require_once('db_config.php');
$db = DbConfig::getConnection();
if(!empty($_GET)){
	$id = $_GET["id"];
	$sql = "SELECT id, ruta_archivo FROM foto_medico WHERE medico_id=?";
	$stmt = $db->prepare($sql);
	$stmt->bind_param("s", $id);
	$stmt->execute() or die("no se pudo obtener las fotos");
	$result = $stmt->get_result();
	$fotos_info = array();
	while ($row = $result->fetch_assoc()) {
		$fotos_info[] = $row;
	}
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
	<title>Ver Fotos</title>
</head>
<body>
	<div>
		<?php 
		foreach ($fotos_info as $foto) {
			echo sprintf("<img width='320' style='display:inline' height='240' class='foto' id='%d' src='%s' onclick='resize(%d);' alt='foto de medico'>", $foto['id'], $foto['ruta_archivo'], $foto['id']);
		}
		?>
	</div>
</body>
</html>