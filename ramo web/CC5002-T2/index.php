<!DOCTYPE html>

<html lang="es">

	<head>

		<meta charset="utf-8">

		<style>

			body {
				background-color: #40d095;
				font-family: "Helvetica", "Arial";
				color: white;
			}
			h1 {
				text-align: center;
				margin-top: 10%;
				font-size: 350%;
			}
			.mainform {
				text-align: center;
				background-color: white;
				padding-top: 6em;
				padding-bottom: 6em;
			}
			button {
				font-family: "Helvetica", "Arial";
				font-weight: bold;
				font-size: 100%;
				width: 20%;
				height: 2.5em;
				margin-left: 2em;
				margin-right: 2em;
				margin-top: .5em;
				margin-bottom: .5em;
				background-color: #40d095;
				border: 0px;
				color: white;
			}
			button:hover {
				background-color: #35b075;
			}

		</style>
		
		<title>Tarea 2 - CC5002</title>

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

	</body>

</html>