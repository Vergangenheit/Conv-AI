function updatePersona(personality){
    const persona = document.querySelector('.persona');
    persona.innerHTML = ``;
    personality.forEach(element => {
        let html = `${element}<br>`;
        persona.innerHTML += html;
    });
}

function updateChat(msg){
    const chat = document.querySelector('.chat');
    //chat.innerHTML = '';
    let html = `${msg}<br>`;
    chat.innerHTML += html;
}

db.collection("history").orderBy('timestamp').onSnapshot(snapshot => {
    snapshot.docChanges().forEach(change => {
        updateChat(change.doc.data().msg);
    });
});

// realtime listener
db.collection("personalities").onSnapshot(snapshot => {
    let values = Object.values(snapshot.docChanges()[0].doc.data());
    updatePersona(values[0]);

});