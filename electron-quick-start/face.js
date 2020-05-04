function detect_faces() {
	document.getElementById("detect").value = "Hang on..."
	var {PythonShell} = require("python-shell")
	var paths = require("path")

	var options = {
		scriptPath : paths.join(__dirname, '/.'),
		pythonPath : '/usr/bin/python3'
	}

	var facedet = new PythonShell("faces.py", options);

	facedet.end(function(err, code, message) {
		document.getElementById("detect").value = "Detect faces";
	})
}

function add_face(){

	var {PythonShell} = require("python-shell")
	var paths = require("path")
	var name = document.getElementById("name").value

	var options = {
		scriptPath : paths.join(__dirname, '/.'),
		pythonPath : '/usr/bin/python3',
		args : ["cam", name]
	}
	var face = new PythonShell("add_face.py", options);

	face.end(function(err, code, message){
		swal("Face added!", "We can now recognize your face", "success")
		document.getElementById("add").innerHTML = "Add a new face";
	})
}