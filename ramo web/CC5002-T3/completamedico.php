<?php 
require_once('db_config.php');
$db = DbConfig::getConnection();
if(!empty($_GET)){
	$start = $_GET["start"] . "%";
	$sql = "SELECT id, nombre FROM medico WHERE nombre LIKE ?";
	$stmt = $db->prepare($sql);
	$stmt->bind_param("s", $start);
	$stmt->execute() or die("no se pudo obtener el nombre");
	$result = $stmt->get_result();
	$medicos_info = array();
	while ($row = $result->fetch_assoc()) {
		$medicos_info[] = $row;
	}
	if(sizeof($medicos_info)===0){
		echo "no se encontraron medicos";
	}
	foreach ($medicos_info as $medico) {
		echo sprintf("<a href='detallemedico.php?id=%d'>%s</a><br>",$medico["id"],$medico["nombre"]);
	}
}
?>