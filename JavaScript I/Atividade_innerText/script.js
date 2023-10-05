let titulo = document.getElementById("titulo")
let ulElement = document.querySelector("ul")
let aElement = document.querySelector("a")
let olElement = document.getElementById("lista-ordenada")

titulo.innerText = "Título da Página"
aElement.innerText = "Visite o site da Prozeducação"

ulElement.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
`

olElement.innerHTML = `
    <li><a href="https://exemplo1.com">Link 1</a></li>
    <li><a href="https://exemplo2.com">Link 2</a></li>
    <li><a href="https://exemplo3.com">Link 3</a></li>
`