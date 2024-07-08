console.log("Welcome to the Login Page");

let msg = document.getElementsByClassName(".message");

const refresh_page = () => {
    msg.style.display = "hide";
}

document.addEventListener("DOMContentLoaded", refresh_page);