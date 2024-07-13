"use strict";

document.addEventListener("DOMContentLoaded", function() {
    const bruthTable = document.querySelector(".data_table");

    function buildTable() {
        if (bruthTable) {
            // añadir estilos
            bruthTable.classList.remove("data_table");
            bruthTable.classList.add("display");
            // añadir identificador
            bruthTable.id = "data_table";
        } else {
            console.error("No se encontró ningún elemento con la clase 'data_table'.");
        }
    }

    buildTable();

    if (document.getElementById("data_table")) {
        let tableCRM = new DataTable('#data_table', {
            scrollCollapse: true,
            scrollY: '50vh'
        });
    } else {
        console.error("No se pudo crear la tabla DataTable porque el elemento con el id 'data_table' no existe.");
    }
});
