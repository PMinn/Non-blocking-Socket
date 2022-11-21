const container = document.getElementById('container');
eel.expose(writeMsg);
function writeMsg(code, msg) {
    if (code == 1) { // recv
        var li = document.createElement('div');
        li.classList.add('li');
        li.innerHTML = `<span class="code recv">recv</span>data: ${msg}`;
        container.appendChild(li);
    } else if (code == 0) { // send
        var li = document.createElement('div');
        li.classList.add('li');
        li.innerHTML = `<span class="code send">send</span>data: ${msg}`;
        container.appendChild(li);
    } else if (code == 2) { // set
        var li = document.createElement('div');
        li.classList.add('li');
        li.innerHTML = `<span class="code set">set</span> ${msg}`;
        container.appendChild(li);
        console.log(container,li)
    } else if (code == 3) { // ok
        var li = document.createElement('div');
        li.classList.add('li');
        li.innerHTML = `<span class="code recv">ok</span> ${msg}`;
        container.appendChild(li);
        console.log(container,li)
    } else if (code == 4) { // error
        var li = document.createElement('div');
        li.classList.add('li');
        li.innerHTML = `<span class="code timeout">error</span> ${msg}`;
        container.appendChild(li);
        console.log(container,li)
    } else if (code == 5) { // waiting
        var li = document.createElement('div');
        li.classList.add('li');
        li.innerHTML = `<span class="code set">error</span> ${msg}`;
        container.appendChild(li);
        console.log(container,li)
    }
}