const ip = document.getElementById('ip');
const num = document.getElementById('num');
const connectingBtn = document.getElementById('connectingBtn');

connectingBtn.addEventListener('click', () => {
    eel.send(ip.value, num.value.toString());
});