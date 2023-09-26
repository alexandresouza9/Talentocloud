const linkPerfil = document.getElementById("link-perfil");
const navPerfil = document.getElementById("nav-perfil");
const linkPerfilDados = document.getElementById("link-prefil-dados")

linkPerfil.addEventListener("mouseover", ()=> {
  navPerfil.style.display = "block"
})
document.addEventListener("keyup", (e) => {
    console.log(e.key)
    console.log(e.code)

    if (e.code == "Digit" || e.code == "Numpad1"){
        console.log("Vc pressionou a tecla 1!!")
        navPerfil.style.display = "block"
    }
    if(e.code == "Escape"){
        console.log("Vc precionou ESC!!")
        navPerfil.style.display = "nome"
    }
    //if(e.code == "Digit1"){
    //    linkPerfilDados.click()
   // }
    if(navPerfil.style.display == "block"){
        if(e.code == "Digit1"){
            linkPerfilDados.click()
        }
    }else if(e.code == "Digit1"){
        navPerfil.style.display = "block"
    }
})