
document.addEventListener('DOMContentLoaded', function() {
    let boxes = document.querySelectorAll(".box1");
    let ans=false;

    boxes.forEach((box) => {
            box.addEventListener("click", () => {
                console.log("info clicked");
                box.classList.toggle("flip");
                
            })

    });
    let buttons = document.querySelectorAll(".box-btn");
    

    buttons.forEach((btn) => {
        btn.addEventListener("click", (event) => {
            event.stopPropagation();
            let dialog=document.querySelector(".dialog");
            dialog.style.display="block";
        

            let close = document.querySelector(".close");
            close.addEventListener("click", () => {
                dialog.style.display="none";
            })
            let cancel = document.querySelector("#btn1");
            cancel.addEventListener("click", () => {
                dialog.style.display="none";
            })


        })
    })
   

});

