const h2 = document.querySelector("h2")
h2.style.color = "blue"
h2.style.fontSize = "50px"

const button = document.querySelector("button")

button.style.backgroundColor = "blue"
button.style.color = "white"
button.style.fontSize = "12px"
button.style.borderRadius = "5px"


const userNameInput = document.querySelector("#login-usuario")
userNameInput.classList.add("error")

 
const errorMensagens = document.querySelectorAll(".error-text")
console.log(errorMensagens)
for (let i = 0; i < errorMensagens.length; i++) {
  console.log(i)
  errorMensagens[i].classList.add("visible")

}

const senhaInput = document.querySelector("#login-senha")
senhaInput.classList.add("error")