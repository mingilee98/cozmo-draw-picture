const server_uri = 'http://127.0.0.1:5000/submit-image'

// create canvas object for drawing
const canvas = document.getElementById('drawingCanvas');
const context = canvas.getContext('2d');

let isDrawing = false;
let lastX = 0;
let lastY = 0;

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

// draw when the mouse is pressed
function startDrawing(e) {
    isDrawing = true;
    [lastX, lastY] = [e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop];
}

// draw when the mouse is moved
function draw(e) {
    if (!isDrawing) return;
    context.beginPath();
    context.moveTo(lastX, lastY);
    context.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    context.stroke();
    [lastX, lastY] = [e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop];
}

// stop drawing when the mouse is released or leaves the canvas
function stopDrawing() {
    isDrawing = false;
}

// for button that submits the canvas
function runScript() {

    var canvas = document.getElementById('drawingCanvas');
    var context = canvas.getContext('2d');
    var drawingData = canvas.toDataURL();

    // create a FormData object to send to the server
    var formData = new FormData();
    formData.append('drawing', drawingData);

    // make a POST request to the server
    fetch(server_uri, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            // handle the response from the server
            console.log('Server response:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
