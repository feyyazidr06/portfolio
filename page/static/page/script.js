$(document).ready(function () {
    if(!$("#myCanvas").tagcanvas({
        textColour: "#2aaaf1",
        outlineColour: "transparent",
        reverse: true,
        depth: 0.8,
        maxSpeed: 0.05,
        weight: true,
    }, "tags")) {
        $("#myCanvasContainer");
    }
})

function reveal() {
    var reveals = document.querySelectorAll(".animate__animated");
    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;
        if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("animate__bounceInLeft");
        } else {
        reveals[i].classList.remove("animate__bounceInLeft");
        }
    }
}

window.addEventListener("scroll", reveal);