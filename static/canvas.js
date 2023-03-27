var canvas = new fabric.Canvas("page");

function add_text() {
    var textbox = new fabric.Textbox("Enter text",{
        width: 400,
        left: 110,
        top: 70,
        fill: "black",
        stroke: "black",
        textAlign: "left",
    });
    canvas.add(textbox);
}