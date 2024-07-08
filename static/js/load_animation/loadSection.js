"use strict";
const mainSection = document.getElementById("main");

function LoadingPage(){
    // CREAR CONTAINER
    const container = document.createElement("div");
    container.classList.add("container", "mt-5");

    // CREAR DIV ELEMENTO SPINNER
    const spinner = document.createElement("div");
    spinner.classList.add("d-flex", "justify-content-center", "p-5");
    container.appendChild(spinner);

    // CREAR DIV ELEMENTO SPINNER BORDER
    const spinnerBorder = document.createElement("div");
    spinnerBorder.classList.add("spinner-border", "mt-5");
    spinner.appendChild(spinnerBorder);


    // CREAR SPAN ELEMENTO SPINNER
    const spanInner = document.createElement("span");
    spanInner.classList.add("visually-hidden");
    spanInner.innerHTML = "Loading...";
    spinner.appendChild(spanInner);


    mainSection.innerHTML = "";
    mainSection.appendChild(container);
};


