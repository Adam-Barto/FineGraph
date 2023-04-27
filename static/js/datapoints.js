import { sendForm } from "./request.js";

export class Datapoints {
    constructor() {
        this.create = document.querySelectorAll("create-datapoint")
        this.all

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
    }
}