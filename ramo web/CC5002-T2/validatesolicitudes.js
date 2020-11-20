/*
función de validación del formulario en publicarsolicitudatencion.html
*/

function validate(){

	const nombre = document.getElementsByName("nombre-solicitante")[0].value;
	if(nombre === ""){
		alert("El campo nombre es obligatorio");
		return false;
	}

	const especialidad = document.getElementsByName("especialidad-solicitud")[0].value;
	if(especialidad === "0"){
		alert("El campo especialidad es obligatorio");
		return false;
	}

	const sintomas = document.getElementsByName("sintomas-solicitante")[0].value;
	if(sintomas.length > 500){
		alert("El campo sintomas no puede superar los 500 caracteres");
		return false;
	}

	const twitter = document.getElementsByName("twitter-solicitante")[0].value;
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

	const email = document.getElementsByName("email-solicitante")[0].value;
	let regexe = /^[a-zA-Z][a-zA-Z]*[a-zA-Z0-9]*@[a-zA-Z][a-zA-Z]*.[a-zA-Z][a-zA-Z]*$/;
	if(email === ""){
		alert("El campo email es obligatorio");
		return false;
	}
	if(!regexe.test(email)){
			alert("Su mail no sigue el formato correcto: user@domain.country");
			return false;
	}

	const celular = document.getElementsByName("celular-solicitante")[0].value;
	let regexc = /^\+569?\d{8}$/;
	if(celular !== ""){
		if(!regexc.test(celular)){
			alert("Su celular no sigue el formato correcto: +569nnnnnnnn");
			return false;
		}
	}

	const region = document.getElementsByName("region-solicitante")[0].value;
	if(region === "0"){
		alert("El campo región es obligatorio");
		return false;
	}

	const comuna = document.getElementsByName("comuna-solicitante")[0].value;
	if(comuna === "0"){
		alert("El campo comuna es obligatorio");
		return false;
	}

	document.getElementsByName("mainform")[0].submit();
	return true;
}