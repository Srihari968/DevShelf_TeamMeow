
document.addEventListener('DOMContentLoaded', function() {
    let boxes = document.querySelectorAll(".box1");
    let ans=false;

    boxes.forEach((box) => {
        
        

        
            box.addEventListener("click", () => {
                console.log("info clicked");
                box.classList.toggle("flip");
                
            })
        
    
        
        
        
    });

});

