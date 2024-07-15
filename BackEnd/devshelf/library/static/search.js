
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
            console.log(btn.id)
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

            let yes = document.querySelector("#btn2");
            yes.addEventListener("click", () => {
                alert("You have requested for the following book - "+ btn.id);
                console.log(document.getElementById("csrf").value);
                let formData = new FormData()
                formData.append("username",document.getElementById("username").value)
                formData.append("borrow", btn.id)
                fetch("/library/borrow/",{
                    method: "POST",
                    body: formData,
                    headers: {
                         "X-CSRFToken": getCookie("csrftoken")
                    },


                    });
                    location.reload();
                    location.reload();
                function getCookie(name) {
                        const value = `; ${document.cookie}`;
                        const parts = value.split(`; ${name}=`);
                        if (parts.length === 2) return parts.pop().split(';').shift();
}

                dialog.style.display="none";

            })


        })
    })
   

});

