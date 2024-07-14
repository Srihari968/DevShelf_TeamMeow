$(window).on("load resize ", function () {
  var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
  $('.tbl-header').css({ 'padding-right': scrollWidth });
}).resize();


$('.Menu').click(function(){
  $(this).toggleClass("click");
  $('.sidebar').toggleClass("show");
});