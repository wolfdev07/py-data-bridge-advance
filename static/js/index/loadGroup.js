"use strict";
const formSelectGroup = document.getElementById("form-select-group");
const buttonAction = document.getElementById("button-action");

buttonAction.addEventListener("click", ()=>{
    // LEER ELEMENTO SELECCIONADO
    const selectElement =  formSelectGroup.querySelector("select");
    // GET THE SELECTED VALUE
    const selectedValue = selectElement.value;
    // VERIFICAR LA SELECCION
    console.info(selectedValue);
    LoadingPage();
    window.location.href="/units-report-group?id_group="+selectedValue;
});