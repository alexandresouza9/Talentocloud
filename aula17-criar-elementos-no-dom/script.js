const arrayPostagens = [
  {
    titulo: "Pop Vegan",
    subtitulo: "Comida vegana para todos!",
    data: "06/07/2022",
    texto: "Restaurante em Consolação com comida por kilo no almoço e rodízio de pizzas à noite, tudo 100% vegano. Vale muito a pena conhecer :)"
  },
  {
    titulo: "Make Hommus. Not War",
    subtitulo: "Só delivery, para curtir em casa!",
    data: "18/08/2022",
    texto: "Neste restaurante não só pode, como é encorajado comer o antepasto como prato principal. Recomendamos os kibes e a kafta bonina."
  },
  {
    titulo: "Churrascada do Mar",
    subtitulo: "Melhor do que estar na praia!",
    data: "30/08/2022",
    texto: "Todos conhecemos e amamos um bom churrasco, mas o que você acha de experimentar um churrasco focado em frutos do mar? Nós gostamos, experimente e nos conte o que você achou!"
  },
]

// InnerText InnenHtml
//const paragrafo = document.querySelector("p")
//console.log(paragrafo.innerText)

//Criar elemento
const article = document.createElement("article")

// Popular esse elemeto
article.innerHTML = `<h3>Pop Vegan</h3>
<p class="subtitulo">Comida vegana para todos!</p>
<div class="data">06/07/2022</div>
<p>Restaurante em Consolação com comida por kilo no almoço e rodízio de pizzas à noite, tudo 100% vegano. Vale muito a pena conhecer :)</p>`

const artigo = document.createElement("artigo")

// Popular esse elemeto
artigo.innerHTML = `<h3>Pop Vegan</h3>
<p class="subtitulo">Comida vegana para todos!</p>
<div class="data">06/07/2022</div>
<p>Restaurante em Consolação com comida por kilo no almoço e rodízio de pizzas à noite, tudo 100% vegano. Vale muito a pena conhecer :)</p>`
// Adicionar elemento na DOM
const main = document.querySelector("main")
main.appendChild(article, artigo)









