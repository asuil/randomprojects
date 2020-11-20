<?php 
require_once('db_config.php');
$db = DbConfig::getConnection();
$sql = "SELECT em.medico_id AS id, e.descripcion AS nom FROM especialidad_medico AS em, especialidad AS e WHERE em.especialidad_id=e.id";
$stmt = $db->prepare($sql);
$stmt->execute() or die("no se pudo obtener el nombre");
$result = $stmt->get_result();
$em_info = array();
while ($row = $result->fetch_assoc()) {
	$em_info[] = $row;
}
?>

<!DOCTYPE html>

<html lang="es">

	<head>

		<meta charset="utf-8">
		
		<title>Tarea 3 - CC5002</title>

		<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
   		<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
   integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
   crossorigin=""></script>

   		<style>
   			#mapid {
   				height: 25rem;
   				width: 35rem;
   			}
   		</style>

	</head>
	

	<body>

		<?php
		session_start();

	    if (isset($_SESSION['message'])) {
	       echo '<div>' . $_SESSION['message'] . '</div>';
	       unset($_SESSION['message']);
	    }
		?>

		<h1>Sistema médico</h1>

		<div class="mainform">

			<div id="comunafoto" style="display:none"></div>
			<div id="coordinates" style="display:none"></div>
			<div id="especialidades" style="display:none"><?php foreach ($em_info as $em) {
				echo $em["id"] . "," . $em["nom"] . ";";
			} ?></div>

			<form id="agregadatosmedico" action="agregadatosmedico.php"></form>
			<form id="vermedicos" action="vermedicos.php" method="get">
				<input hidden="hidden" name="offset" value="1">
			</form>
			<form id="publicasolicitud" action="publicarsolicitudatencion.php"></form>
			<form id="versolicitud" action="versolicitudesatencion.php" method="get">
				<input hidden="hidden" name="offset" value="1">
			</form>
			
			<button form="agregadatosmedico">Agrega Datos de Médico</button>
			<button form="vermedicos">Ver Médicos</button>
			<br>
			<button form="publicasolicitud">Publicar Solicitud de Atención</button>
			<button form="versolicitud">Ver Solicitudes de Atención</button>

		</div>

		<div id="mapid"></div>
		<script>

			var especialidades = document.getElementById("especialidades").innerHTML.split(";");
			document.getElementById("especialidades").innerHTML = "";
			for (var i = especialidades.length - 1; i >= 0; i--) {
				especialidades[i] = especialidades[i].split(",");
			}

			var mymap = L.map('mapid').setView([-33.4, -70.7], 5);
				L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYXN1aWwiLCJhIjoiY2tiOXN6eGFhMGJjdTJ4cGczYTd5b3RodiJ9.SSr8FSwEQPbDxisgMG3BMg', {
			    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
			    maxZoom: 18,
			    id: 'mapbox/streets-v11',
			    tileSize: 512,
			    zoomOffset: -1,
			    accessToken: 'your.mapbox.access.token'
			}).addTo(mymap);
			loadComunaFoto();

   			function loadComunaFoto() {
			  	var xhttp = new XMLHttpRequest();
			  	xhttp.onreadystatechange = function() {
				    if (this.readyState == 4 && this.status == 200) {
				     	document.getElementById("comunafoto").innerHTML = this.responseText;
				     	loadCoordinates();
				    }
			  	};
			  	xhttp.open("GET", "comunafoto.php", true);
			  	xhttp.send();
			}

			function loadCoordinates() {
				var xhttp2 = new XMLHttpRequest();
			  	xhttp2.onreadystatechange = function() {
				    if (this.readyState == 4 && this.status == 200) {
				     	document.getElementById("coordinates").innerHTML = this.responseText;
				     	mergeDatos();
				    }

			  	};
			  	xhttp2.open("GET", "chile.json", true);
			  	xhttp2.send();
			}

			function mergeDatos(){
				comunafoto = document.getElementById("comunafoto").innerHTML.split(";");
				coordinates = JSON.parse(document.getElementById("coordinates").innerHTML);
				document.getElementById("comunafoto").innerHTML = "";
				document.getElementById("coordinates").innerHTML = "";

				// pedir diccionario con todas las medico id + especialidad nombre

				let filtered_comunafoto = []; // comunafoto con agrupaciones por comuna
		     	for (var i = comunafoto.length - 2; i >= 0; i--) {
		     		comunafoto[i] = comunafoto[i].split(",");
		     		already_filtered = false;
		     		for (var j = filtered_comunafoto.length - 1; j >= 0; j--) {
		     			if(filtered_comunafoto[j][0][0] === comunafoto[i][0]){
		     				already_filtered = true;
		     				if(!filtered_comunafoto[j][5].includes(comunafoto[i][5])){
			     				for (var n = filtered_comunafoto[j].length - 2; n >= 0; n--) {
			     					filtered_comunafoto[j][n].push(comunafoto[i][n]);
			     				}
			     				filtered_comunafoto[j][filtered_comunafoto[j].length - 1]++;
		     				}
		     				// else 
		     				//	 añadir solo foto [j][1]
		     				// y en marker_text añadirlas todas con un 
		     				//	 for sobre [i]["files"]
		     				// 		concat(<img>)
		     				// ? quizás pero de momento no
		     			}
		     		}
		     		if(!already_filtered){
		     			new_elem = [];
		     			for (var k = 0; k < comunafoto[i].length; k++) {
		     				new_elem.push([comunafoto[i][k]]);
		     			}
		     			new_elem.push(1);
		     			filtered_comunafoto.push(new_elem);
		     		}
		     	}
				let coordfoto = []; // comunafoto but using coords that can be used on the map
		     	for (var i = filtered_comunafoto.length - 1; i >= 0; i--) {
		     		for (var j = coordinates.length - 1; j >= 0; j--) {
		     			if(coordinates[j]["name"] === filtered_comunafoto[i][0][0]){
		     				coordfoto[i] = {
		     					"lat" : coordinates[j]["lat"],
		     					"lng" : coordinates[j]["lng"],
		     					"file" : filtered_comunafoto[i][1],
		     					"nombre" : filtered_comunafoto[i][2],
		     					"twitter" : filtered_comunafoto[i][3],
		     					"email" : filtered_comunafoto[i][4],
		     					"counter" : filtered_comunafoto[i][filtered_comunafoto[i].length - 1],
		     					"id" : filtered_comunafoto[i][5]
		     				}
		     			}
		     		}
		     	}

		     	for (var i = coordfoto.length - 1; i >= 0; i--) {
		     		var marker = L.marker([coordfoto[i]["lat"], coordfoto[i]["lng"]], {title: coordfoto[i]["counter"]}).addTo(mymap);
		     		var marker_text = "";
		     		for (var h = coordfoto[i]["nombre"].length - 1; h >= 0; h--) {
		     			especialidades_id = "";
		     			for (var m = especialidades.length - 1; m >= 0; m--) {
		     				if(especialidades[m][0]===coordfoto[i]["id"][h]){
		     					especialidades_id = especialidades_id.concat(` --- ${especialidades[m][1]}<br>`);
		     				}
		     			}
			     		new_text = `
			     			<img style='center: center' width='30' height='30' src='${coordfoto[i]["file"][h]}' alt='foto de medico'><br>
				     		Info de ${coordfoto[i]["nombre"][h]}:<br>
				     		 - twitter: ${(coordfoto[i]["twitter"][h]==="")?"No se ingresó.":coordfoto[i]["twitter"][h]}<br>
				     		 - email: ${coordfoto[i]["email"][h]}<br>
				     		 - especialidades:<br>
				     		 ${especialidades_id}
				     		 <a href="verfotos.php?id=${coordfoto[i]["id"][h]}">link a fotos</a><br>
				     	`;
				     	marker_text = marker_text.concat(new_text);
				    }
		     		marker.bindPopup(marker_text).openPopup();
		     	}
			}

		</script>

	</body>

</html>