"use strict";

const inputDatePicker = document.querySelector(".datePicker_input");

const datePicker = new Datepicker(inputDatePicker, {
    'format': 'dd/mm/yyyy',
    'title':  'Seleccione una fecha'
});