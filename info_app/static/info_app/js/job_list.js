if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
  $('.text-block').css("visibility", "visible");
}

else {
  $('img').tooltip('update')
}
