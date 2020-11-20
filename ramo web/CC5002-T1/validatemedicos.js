/*
función de validación del formulario en agregardatosmedico.html
*/

function validate(){

	var region = document.getElementsByName("region-medico")[0].value;
	if(region == "sin-region"){
		alert("El campo región es obligatorio");
		return false;
	}

	var comuna = document.getElementsByName("comuna-medico")[0].value;
	if(comuna == "sin-comuna"){
		alert("El campo comuna es obligatorio");
		return false;
	}

	var nombre = document.getElementsByName("nombre-medico")[0].value;
	if(nombre == ""){
		alert("El campo nombre es obligatorio");
		return false;
	}

	var experiencia = document.getElementsByName("experiencia-medico")[0].value;
	if(experiencia.length > 500){
		alert("El campo experiencia no puede superar los 500 caracteres");
		return false;
	}

	var especialidades = document.getElementsByName("especialidades-medico")[0].selectedOptions;
	if(especialidades.length == 0){
		alert("Debe ingresar al menos una especialidad");
		return false;
	}
	if(especialidades.length > 5){
		alert("Solo puede tener un máximo de 5 especialidades");
		return false;
	}

	var foto = document.getElementsByName("foto-medico")[0].value;
	if(foto == ""){
		alert("Debe ingresar al menos una fotografía");
		return false;
	}

	var twitter = document.getElementsByName("twitter-medico")[0].value;
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

	var email = document.getElementsByName("email-medico")[0].value;
	var regex = /^[a-zA-Z][a-zA-Z]*[a-zA-Z0-9]*@[a-zA-Z][a-zA-Z]*.[a-zA-Z][a-zA-Z]*$/
	if(email == ""){
		alert("El campo email es obligatorio");
		return false;
	}
	if(!regex.test(email)){
			alert("Su mail no sigue el formato correcto: user@domain.country");
			return false;
	}

	var celular = document.getElementsByName("celular-medico")[0].value;
	var regex = /^\+56 9 ?\d{8}$/;
	if(celular != ""){
		if(!regex.test(celular)){
			alert("Su celular no sigue el formato correcto: +56 9 nnnnnnnn");
			return false;
		}
	}

	return true;
}