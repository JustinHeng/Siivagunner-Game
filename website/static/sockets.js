var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

var currentRoom = sessionStorage.getItem("currentRoom");

socket.on('connect', function(){
    socket.emit("join_room", currentRoom);
});

socket.on('disconnect', function(){
    socket.emit("leave_room", currentRoom);
});

window.onbeforeunload = function () {
    socket.disconnect();
}

socket.on('message', function(msg){
    $("#allMessages").append('<li>' + msg + '</li>');
    var elem = document.getElementById('textScroll');
    elem.scrollTop = elem.scrollHeight;
});

//$('#sendButton').on('click', function(){
//    if ($('#myMessage').val() != ''){
//        socket.emit("message", "{{user.first_name}}: " + $('#myMessage').val().substr(0,500), currentRoom);
//        $('#myMessage').val('');
//    }
//});

// Get the input field
var myMessage = document.getElementById("myMessage");

// Execute a function when the user presses a key on the keyboard
myMessage.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("sendButton").click();
    }
});

var volume = 0.8;
var sfxSlider = document.getElementById("sfxVolume");
sfxSlider.oninput = function() {
    volume = this.value / 100;
}

function playSound(url) {
  const audio = new Audio(url);
  audio.volume = volume;
  audio.play();
}

$('#startButton').on('click', function(){
    socket.emit("start_game", currentRoom);
});