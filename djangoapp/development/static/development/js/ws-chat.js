const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
const chatWsPath = ws_scheme + '://' + window.location.host + '/ws/chat/';

const chatSocket = new WebSocket(chatWsPath);

const messageInputDom = document.querySelector('#chat-message-input');
const submitButtonDom = document.querySelector('#chat-message-submit');

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log(data);
    addMessage(data.message, 'bot');
    messageInputDom.disabled = false;
    submitButtonDom.disabled = false;
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({ 'message': message }));
    addMessage(message, 'user');
    messageInputDom.value = '';
    messageInputDom.disabled = true;
    submitButtonDom.disabled = true;
};

function addMessage(message, sender) {
    var chatBox = document.querySelector('.chat-box-area');
    var chatContent = document.createElement('div');
    chatContent.className = 'chat-content' + (sender === 'user' ? ' user' : '');
    var messageItem = document.createElement('div');
    messageItem.className = 'message-item';
    var bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.innerText = message;
    var messageTime = document.createElement('div');
    messageTime.className = 'message-time';
    // Aqui você pode formatar a data como desejar
    messageTime.innerText = new Date().toLocaleTimeString();

    messageItem.appendChild(bubble);
    messageItem.appendChild(messageTime);
    chatContent.appendChild(messageItem);
    chatBox.appendChild(chatContent);
    // Auto-scroll para a mensagem mais recente
    chatBox.scrollTop = chatBox.scrollHeight;
}
