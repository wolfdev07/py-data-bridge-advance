"use strict";
const formSelectGroup = document.getElementById("form-select-group");
const buttonAction = document.getElementById("button-action");

function processString(inputString) {
    // Convert to lowercase
    let lowercaseString = inputString.toLowerCase();
    // Check if it's a single word
    if (!lowercaseString.includes(' ')) {
        return lowercaseString; // No need to modify single words
    }
    // Remove extra spaces and replace with underscore
    let processedString = lowercaseString.replace(/\s+/g, '_');
    return processedString;
}

buttonAction.addEventListener("click", ()=>{
    // LEER ELEMENTO SELECCIONADO
    const selectElement =  formSelectGroup.querySelector("select");
    // GET THE SELECTED VALUE
    const selectedValue = selectElement.value;
    // GUARDAR NOMBRE DEL GRUPO
    var selectInner = selectElement.querySelector("option:checked").innerText;
    selectInner = processString(selectInner);
    // VERIFICAR LA SELECCION
    LoadingPage();
    window.location.href="/units-report-group?id_group="+selectedValue+"&name_group="+selectInner;
});