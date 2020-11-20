/*
función de validación del formulario en publicarsolicitudatencion.html
*/

function validate(){

	var nombre = document.getElementsByName("nombre-solicitante")[0].value;
	if(nombre == ""){
		alert("El campo nombre es obligatorio");
		return false;
	}

	var especialidad = document.getElementsByName("especialidad-solicitud")[0].value;
	if(especialidad == "0"){
		alert("El campo especialidad es obligatorio");
		return false;
	}

	var sintomas = document.getElementsByName("sintomas-solicitante")[0].value;
	if(sintomas.length > 500){
		alert("El campo sintomas no puede superar los 500 caracteres");
		return false;
	}

	var twitter = document.getElementsByName("twitter-solicitante")[0].value;
	var regex = /^[a-zA-Z0-9]*$/
	if(twitter != ""){
		if(!regex.test(twitter)){
			alert("Su usuario de twitter no debe contener símbolos especiales");
			return false;
		}
		if(twitter.length < 3){
			alert("Su usuario de twitter debe contener al menos 3 caracteres");
			return false;
		}
		if(twitter.length > 80){
			alert("Su usuario de twitter debe contener al más 80 caracteres");
			return false;
		}
	}

	var email = document.getElementsByName("email-solicitante")[0].value;
	var regex = /^[a-zA-Z][a-zA-Z]*[a-zA-Z0-9]*@[a-zA-Z][a-zA-Z]*.[a-zA-Z][a-zA-Z]*$/
	if(email == ""){
		alert("El campo email es obligatorio");
		return false;
	}
	if(!regex.test(email)){
			alert("Su mail no sigue el formato correcto: user@domain.country");
			return false;
	}

	var celular = document.getElementsByName("celular-solicitante")[0].value;
	var regex = /^\+56 9 ?\d{8}$/;
	if(celular != ""){
		if(!regex.test(celular)){
			alert("Su celular no sigue el formato correcto: +56 9 nnnnnnnn");
			return false;
		}
	}

	var region = document.getElementsByName("region-solicitante")[0].value;
	if(region == "sin-region"){
		alert("El campo región es obligatorio");
		return false;
	}
	
	var comuna = document.getElementsByName("comuna-solicitante")[0].value;
	if(comuna == "sin-comuna"){
		alert("El campo comuna es obligatorio");
		return false;
	}

	return true;
}