var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");
    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length} ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndex-1].style.display = "block";
}

var myElement = document.getElementById('indexSlidShow');

var mc = new Hammer(myElement);

mc.on("swipeleft swiperight", function(ev) {
    if (ev.type == "swipeleft") {
      plusDivs(+1)
    }
    if (ev.type == "swiperight") {
      plusDivs(-1)
    }
});
