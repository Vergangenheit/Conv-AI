const persona = document.querySelector('.persona');

const addPersona = (statement) => {
    let html = `${statement}<br>`;
    persona.innerHTML += html;
};

db.collection("personalities").get().then(snapshot => {
    var values = Object.values(snapshot.docs[0].data());
    values.forEach(element => {
        addPersona(element);
    });
}).catch(err => {
    console.log(err);
});