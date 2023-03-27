var canvas = new fabric.Canvas("page");
var textbox;
var count = 0;

function add_text() {
    var mycount = count + 1;
    count = count + 1;
    textbox = new fabric.Textbox("Enter text",{
        width: 400,
        left: 110,
        top: 70,
        fill: "black",
        stroke: "black",
        textAlign: "left",
    });
    canvas.add(textbox);
    // textbox.addEventListner("clicks", )
    textbox.on('modified', function(){
        console.log("textbox %i is selected", mycount);
        console.log(textbox.left, textbox.width, textbox.top, textbox.text);
    });
}






