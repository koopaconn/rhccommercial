$('.col-md-3').hide();

if ($('.w3-serif').text().trim().length) {
    $('.col-md-3').show();
}

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
    showDivs(slideIndex += n);
}

$(document).keydown(function(event){
  if (String.fromCharCode(event.which) == '%') {
    plusDivs(-1)
  }
  if (String.fromCharCode(event.which) == "'") {
    plusDivs(+1)
  }
});

var myElement = document.getElementById('jobpiclightrow');

var mc = new Hammer(myElement);

mc.on("swipeleft swiperight", function(ev) {
    if (ev.type == "swipeleft") {
      plusDivs(+1)
    }
    if (ev.type == "swiperight") {
      plusDivs(-1)
    }
});

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

// $(document).addEventListener("keyleft", function() {
//   plusDivs(-1)
// });
// $(document).addEventListener("keyright", function() {
//   plusDivs(+1)
// });
