<?php 
require_once('db_config.php');
$db = DbConfig::getConnection();
if(!empty($_GET)){
	$start = $_GET["start"] . "%";
	$sql = "SELECT id, nombre_solicitante FROM solicitud_atencion WHERE nombre_solicitante LIKE ?";
	$stmt = $db->prepare($sql);
	$stmt->bind_param("s", $start);
	$stmt->execute() or die("no se pudo obtener el nombre");
	$result = $stmt->get_result();
	$solicitantes_info = array();
	while ($row = $result->fetch_assoc()) {
		$solicitantes_info[] = $row;
	}
	if(sizeof($solicitantes_info)===0){
		echo "no se encontraron pacientes";
	}
	foreach ($solicitantes_info as $solicitante) {
		echo sprintf("<a href='detallesolicitud.php?id=%d'>%s</a><br>",$solicitante["id"],$solicitante["nombre_solicitante"]);
	}
}
?>