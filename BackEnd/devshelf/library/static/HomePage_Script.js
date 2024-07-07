console.log("Added some code");

let img = document.querySelector(".lib-aks-img");

const mouseHandler = () => {
    img.classList.add("appear");
};

img.addEventListener("mouseover", mouseHandler);

img.addEventListener("click", () => {
    img.removeEventListener("mouseover", mouseHandler);
    img.classList.remove("appear");
    img.style.opacity = 1;
});

