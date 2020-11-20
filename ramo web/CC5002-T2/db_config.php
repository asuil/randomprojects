<?php
/* Clase que crea una coneción a la base de datos
* Modo de uso: 
$db = DbConfig::getConnection();
$sql = "SELECT id, nombre FROM region"
$result = $db->query($sql); 
$res = array();
while ($row = $result->fetch_assoc()) {
	$res[] = $row;
}
$db->close();
Resultados están en arreglo $res
*/
class DbConfig{
	private static $db_name = "cc500226_db"; //Base de datos de la app
	private static $db_user = "cc500226_u"; //Usuario MySQL
	private static $db_pass = "quesuscipi"; //Password
	private static $db_host = "localhost";//Servidor donde esta alojado, puede ser 'localhost' o una IP (externa o interna).
	private static $db_port = 3306;
	
	public static function getConnection(){
		$mysqli = new mysqli(self::$db_host, self::$db_user, self::$db_pass, self::$db_name, self::$db_port);

		$mysqli->set_charset("utf8"); //Muy importante!!
		return $mysqli;
	}
}
?>
