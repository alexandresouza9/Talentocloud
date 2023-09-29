const texto = "Conexão com um arquivo JavaScript"


for(let i=0; i<3; i++){
    // Criar o elemento
    const h2 = document.createElement("h2")

    //Popular esse elemento
    h2.innerText = "Conexão com um arquivo JavaScript"

    // Adicionar elemento na DOM
    const body = document.querySelector("body")
    body.appendChild(h2)
}