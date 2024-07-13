console.log("Welcome to the Sign Up Page");



document.addEventListener("keypress", function (event) {
  const messageElement = document.querySelector(".message");
  if (event.key== "F5" || (event.key.ctrlKey==true && event.key=="R"))
    messageElement.style.display = "none";
});


document.addEventListener("keydown", function (event) {
  const messageElement = document.querySelector(".message");
  if (event.key == "F5"  || (event.key.ctrlKey==true && event.key=="R"))
    messageElement.style.display = "none";
});


document.addEventListener("keyup", function (event) {
  const messageElement = document.querySelector(".message");
  if (event.key == "F5"  || (event.key.ctrlKey==true && event.key=="R"))
    messageElement.style.display = "none";
});