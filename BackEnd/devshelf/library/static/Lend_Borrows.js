$(window).on("load resize ", function () {
  var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
  $('.tbl-header').css({ 'padding-right': scrollWidth });
}).resize();

//  const Menu = document.querySelector(".Menu");
// $('Menu').click(function(){
//    $(this).toggleClass("click");
// });

// Menu.addEventListener("click",() =>{
//   Menu.toggleClass("click");
// });

$('.Menu').click(function(){
    $(this).toggleClass("click");
    $('.sidebar').toggleClass("show");
});
