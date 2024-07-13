"use strict";

const newcrmButton =  document.getElementById("new-crm");

newcrmButton.addEventListener("click", ()=>{
    // EJECUTAR ANIMACION DE CARGA
    LoadingPage();
    // REDIRECCIONAR AL FORMULARIO
    window.location.href="/crm-manager";
});