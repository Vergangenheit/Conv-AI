// const persona = document.querySelector('.persona');
// persona.innerHTML = ``;

// const addPersona = (statement) => {
//     let html = `${statement}<br>`;
//     persona.innerHTML += html;
// };

function updatePersona(personality){
    const persona = document.querySelector('.persona');
    persona.innerHTML = ``;
    personality.forEach(element => {
        let html = `${element}<br>`;
        persona.innerHTML += html;
    });
}


// realtime listener
db.collection("personalities").onSnapshot(snapshot => {
    let values = Object.values(snapshot.docChanges()[0].doc.data());
    updatePersona(values[0]);

});