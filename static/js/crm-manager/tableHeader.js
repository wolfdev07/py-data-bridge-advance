"use strict";
const dataTableBruth = document.querySelector(".data_table");

function removeFirstTbody() {
    const firstTbody = dataTableBruth.querySelector("tbody");
    if (firstTbody) {
        dataTableBruth.removeChild(firstTbody);
    }
}

document.addEventListener("DOMContentLoaded", ()=> {
    if (dataTableBruth){
        var firstRow = dataTableBruth.querySelector("tr");
        // Crear el elemento thead
        var thead = document.createElement("thead");
        thead.classList.add("thead-table");
        thead.appendChild(firstRow);
        // Insertar el thead antes del tbody
        dataTableBruth.insertBefore(thead, dataTableBruth.querySelector("tbody"));
    } else {
        console.error("No se pudo crear la tabla DataTable porque el elemento con el id 'data_table' no existe.");
    }

    // Eliminar el primer tbody si existe
    removeFirstTbody();
});