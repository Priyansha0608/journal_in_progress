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
        sendElementInfo(mycount,'textbox',textbox.width, textbox.top, textbox.left, textbox.text);
    });
    
    sendElementInfo(mycount,'textbox',textbox.width, textbox.top, textbox.left, textbox.text);
}

function sendElementInfo(mycount, type, width, top, left, text){
    // Creates a dictionary with element info and sends it to py file
    const formData = new FormData()
    formData.append("id", mycount)
    formData.append("type_element", type)
    formData.append("w", width)
    formData.append("t", top)
    formData.append("l", left)
    formData.append("txt", text)

    const request = new XMLHttpRequest();
    request.open("POST", "/getElement", true);
    request.send(formData);
}





