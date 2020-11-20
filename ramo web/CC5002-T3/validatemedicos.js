/*
función de validación del formulario en agregardatosmedico.html
*/

function validate(){

	const region = document.getElementsByName("region-medico")[0].value;
	if(region === "0"){
		alert("El campo región es obligatorio");
		return false;
	}

	const comuna = document.getElementsByName("comuna-medico")[0].value;
	if(comuna === "0"){
		alert("El campo comuna es obligatorio");
		return false;
	}

	const nombre = document.getElementsByName("nombre-medico")[0].value;
	if(nombre === ""){
		alert("El campo nombre es obligatorio");
		return false;
	}

	const experiencia = document.getElementsByName("experiencia-medico")[0].value;
	if(experiencia.length > 500){
		alert("El campo experiencia no puede superar los 500 caracteres");
		return false;
	}

	const especialidades = document.getElementById("especialidades-medico").selectedOptions;
	if(especialidades.length === 0){
		alert("Debe ingresar al menos una especialidad");
		return false;
	}
	if(especialidades.length > 5){
		alert("Solo puede tener un máximo de 5 especialidades");
		return false;
	}

	const foto = document.getElementsByName("foto-medico[0]")[0].value;
	if(foto === ""){
		alert("Debe ingresar al menos una fotografía");
		return false;
	}

	const twitter = document.getElementsByName("twitter-medico")[0].value;
	let regext = /^[a-zA-Z0-9]*$/;
	if(twitter !== ""){
		if(!regext.test(twitter)){
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

	const email = document.getElementsByName("email-medico")[0].value;
	let regexe = /^[a-zA-Z][a-zA-Z]*[a-zA-Z0-9]*@[a-zA-Z][a-zA-Z]*.[a-zA-Z][a-zA-Z]*$/;
	if(email === ""){
		alert("El campo email es obligatorio");
		return false;
	}
	if(!regexe.test(email)){
			alert("Su mail no sigue el formato correcto: user@domain.country");
			return false;
	}

	const celular = document.getElementsByName("celular-medico")[0].value;
	let regexc = /^\+569?\d{8}$/;
	if(celular !== ""){
		if(!regexc.test(celular)){
			alert("Su celular no sigue el formato correcto: +569nnnnnnnn");
			return false;
		}
	}

	document.getElementsByName("mainform")[0].submit();
	return true;
}