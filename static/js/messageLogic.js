document.addEventListener('DOMContentLoaded', (event) => {
  var socket = io();

  socket.on('connect', function() {
      var username = prompt('Enter your username:');
      var room = 'general';
      socket.emit('join', {'username': username, 'room': room});
  });

  socket.on('message', function(msg) {
      var messageContainer = document.getElementById('messages');
      var messageElement = document.createElement('li');
      messageElement.textContent = msg;
      messageContainer.appendChild(messageElement);
  });

  function sendMessage() {
      var messageInput = document.getElementById('messageInput');
      var message = messageInput.value;
      socket.send(message);
      messageInput.value = '';
  }

  document.getElementById('sendButton').onclick = sendMessage;

  document.getElementById('messageInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
        e.preventDefault();
    }
});
});