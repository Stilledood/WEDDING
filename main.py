< html >
< head >
< script
src = "http://code.jquery.com/jquery-1.11.3.min.js" > < / script >

< style >

html
{
    background - color: black;
}

.ball
{
    display: inline - block;
margin: 0;
border - radius: 50 %;
position: absolute;
z - index: 2;
background: radial - gradient(circle
at
50 % 50 %,  # 808080, #000);
}

< / style >

    < script >

    var
Lightning = function(element)
{
    var
_this = this;
var
canvas = element;
var
context = canvas.getContext("2d");

this.clear = function()
{
    canvas.width = canvas.width;
canvas.height = canvas.height;
};

this.strike = function(x1, y1, x2, y2, color1, color2, drawOrbs)
{
    var
x = x2 - x1;
var
y = y2 - y1;
var
segments = 10;
var
distance = Math.sqrt(x * x + y * y);
var
width = distance / segments;
var
prevX = x1;
var
prevY = y1;

if (drawOrbs)
{
// Draw
point
context.strokeStyle = color1;
context.fillStyle = color1;
context.lineWidth = 2;
context.beginPath();
context.arc(x1, y1, 18 + (Math.random() * 4), 0, 2 * Math.PI, false);
context.fill();
}

for (var i = 0; i <= segments; i++) {
    var magnitude = (width * i) /distance;

var x3 = magnitude * x2 + (1 - magnitude) * x1;
var y3 = magnitude * y2 + (1 - magnitude) * y1;

if (i != = 0 & & i != = segments) {
x3 += (Math.random() * width) - (width/ 2);
y3 += (Math.random() * width) - (width/ 2);
}

// Draw line
context.strokeStyle = color1;
context.lineWidth = 12;
context.beginPath();
context.moveTo(prevX, prevY);
context.lineTo(x3, y3);
context.closePath();
context.stroke();

// Draw point
context.strokeStyle = color1;
context.fillStyle = color1;
context.beginPath();
context.arc(x3, y3, 6, 0, 2 * Math.PI, false);
context.fill();

// Draw line
context.strokeStyle = color2;
context.lineWidth = 6;
context.beginPath();
context.moveTo(prevX, prevY);
context.lineTo(x3, y3);
context.closePath();
context.stroke();

// Draw point
context.strokeStyle = color2;
context.fillStyle = color2;
context.beginPath();
context.arc(x3, y3, 3, 0, 2 * Math.PI, false);
context.fill();

prevX = x3;
prevY = y3;
}

if (drawOrbs) {
// Draw point
context.strokeStyle = color2;
context.fillStyle = color2;
context.lineWidth = 2;
context.beginPath();
context.arc(x1, y1, 12 + (Math.random() * 4), 0, 2 * Math.PI, false);
context.fill();
}
};
}

< /script >

< script type="text/javascript" >

$(document).ready(function(){

});

$('html').on('click', function(e){
xCord = e.pageX;
yCord = e.pageY;

console.log(xCord);
console.log(yCord);

createCircle(xCord, yCord);
});

function createCircle(xCord, yCord){

// Generate random radius between 35 and 70
var radius = Math.floor((Math.random() * 45) + 25);
xCord -= radius/ 2;
yCord -= radius/ 2;

console.log("Size Of Square: " + radius);


var ballHTML = "<figure class='ball' style='"
+ "top:" + yCord + ";"
+ "left:" + xCord + ";"
+ "width:" + radius + ";"
+ "height:" + radius + ";"
+ "'></figure>";

console.log(ballHTML);

$('body').append(ballHTML);

loopAnimate($('.ball').last());
// Generate random radius
// Add Div with offset
}

function loopAnimate(lastDiv){
console.log(lastDiv);

var newq = makeNewPosition();

$(lastDiv).animate({
top: newq[0],
left: newq[1]
}, 30000, 'linear', function()
{
    loopAnimate(lastDiv);
});

// lightning();

}

function
makeNewPosition()
{

// Get
viewport
dimensions(remove
the
dimension
of
the
div)
var
h = $(window).height() - 100;
var
w = $(window).width() - 100;

var
nh = Math.floor(Math.random() * h);
var
nw = Math.floor(Math.random() * w);

return [nh, nw];

}

function
lightning()
{
var
lightning = new2
Lightning(document.getElementById("canvas"));
var
timer = setInterval(function()
{
    lightning.clear();
lightning.strike(10, 10, 20, 20, "#557788", "#7799aa");
// lightning.strike(300, 90, 540, 420, "#cfefff", "#ffffff", true);
}, 20);
}

< / script >
    < / head >
        < body >
        < canvas
id = "canvas"
style = "width:100%;height:98%;" > < / canvas >
                                       < / body >
                                           < / html >
