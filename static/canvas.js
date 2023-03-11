var canvas = document.getElementById("page");
var ctx=canvas.getContext("2d");
ctx.font="30px Comic Sans MS";
ctx.fillStyle = "red";
ctx.textAlight = "center";
ctx.fillText("Hello World", canvas.width/2, canvas.height/2);