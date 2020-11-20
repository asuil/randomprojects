<?php 
require_once('db_config.php');
$db = DbConfig::getConnection();
$sql = "SELECT c.nombre AS cnom, fm.ruta_archivo, m.id AS mid, m.nombre AS mnom, m.twitter, m.email FROM comuna AS c, medico AS m, foto_medico AS fm WHERE m.id = fm.medico_id AND m.comuna_id = c.id";
$stmt = $db->prepare($sql);
$stmt->execute() or die("no se pudo obtener el nombre");
$result = $stmt->get_result();
$comuna_info = array();
while ($row = $result->fetch_assoc()) {
	$comuna_info[] = $row;
}
foreach ($comuna_info as $c_i) {
	echo sprintf("%s,%s,%s,%s,%s,%s;",
		$c_i["cnom"],
		$c_i["ruta_archivo"],
		$c_i["mnom"],
		$c_i["twitter"],
		$c_i["email"],
		$c_i["mid"]
	);
}
?>