import { sendForm } from "./request.js";

export class Datapoints {
    constructor() {
        this.create = document.querySelectorAll("create-datapoint")
        this.allDatapoints

    }
    activateAllCreateForms() {
    new}
}

export class DatapointCreateForm {
    constructor(personID) {
    this.personID = personID;

    this.createButton = this.form.querySelector(
    "button[data-action='create'])" );
    this.createButton.addEventListener(
    "click",
    this.handleCreateClick.bind(this));

    }

    handleCreateClick(event) {
    event.preventDefault();
    sendForm(this.form, "POST","/api/datapoints" ,this.addDatapoint);
    this.form.reset();
    }

    addDatapoint(rawData) {
    const data = JSON.parse(rawData);
    console.log(data)
    user_id = data.querySelector(".create-datapoint")
    new_datapoint.querySelector(".paymentType").textContent = data.value
    new_datapoint.querySelector(".digits").textContent = data.value
    new_datapoint.querySelector(".amount").textContent = data.value
    new_datapoint.querySelector(".date").textContent = data.value
    new_datapoint.querySelector(".category").textContent = data.value
    }
}