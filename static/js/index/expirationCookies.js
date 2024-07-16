"use strict";
const mainContainer = document.getElementById("main");

function createToast(message) {
    // Create the main toast container
    const toastContainer = document.createElement('div');
    toastContainer.classList.add('toast', 'role', 'alert', 'aria-live', 'assertive', 'aria-atomic', 'true');

    // Create the toast body
    const toastBody = document.createElement('div');
    toastBody.classList.add('toast-body');

    // Create the toast message content
    const toastMessage = document.createTextNode(message);
    toastBody.appendChild(toastMessage);

    // Create the action button container
    const actionButtonContainer = document.createElement('div');
    actionButtonContainer.classList.add('mt-2', 'pt-2', 'border-top');

    // Create the "Take action" button
    const takeActionButton = document.createElement('button');
    takeActionButton.classList.add('btn', 'btn-primary', 'btn-sm');
    takeActionButton.textContent = 'Take action';
    actionButtonContainer.appendChild(takeActionButton);

    // Create the "Close" button
    const closeButton = document.createElement('button');
    closeButton.classList.add('btn', 'btn-secondary', 'btn-sm');
    closeButton.setAttribute('data-bs-dismiss', 'toast');
    closeButton.textContent = 'Close';
    actionButtonContainer.appendChild(closeButton);

    // Append the action button container to the toast body
    toastBody.appendChild(actionButtonContainer);

    // Append the toast body to the toast container
    toastContainer.appendChild(toastBody);

    // Append the toast container to the main container
    mainContainer.appendChild(toastContainer);
}

async function checkCookiesExpiration() {
    try {
        const response = await fetch('http://127.0.0.1:5000/cookies');
        const data = await response.json();
        if (data.expiration){
            alert(data.info);
            createToast(data.info);
        } else {
            alert(data.info);
            createToast(data.info);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

checkCookiesExpiration();
