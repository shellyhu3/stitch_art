//Navbar shrink on scroll
$(document).on('scroll', function () {
  return scrollFunction();
});

function scrollFunction() {
  if ($(document).scrollTop() > 100) {
    $('#nav').removeClass('reg_nav');
    $('#nav').addClass('scrolled_nav fixed_nav');
    $('#bg_nav').removeClass('reg_nav_bg');
    $('#bg_nav').addClass('scrolled_nav fixed_nav');
  } else {
    $('#nav').removeClass('scrolled_nav fixed_nav');
    $('#nav').addClass('reg_nav');
    $('#bg_nav').removeClass('scrolled_nav fixed_nav');
    $('#bg_nav').addClass('reg_nav_bg');
  }
}

$(document).ready(function () {
  // Get the modal
  var modal = $("#myModal"); // Get the image and insert it inside the modal - use its "alt" text as a caption

  var modalImg = $("#img01");
  $(".img").on('click', function (e) {
    console.log(e.target);
    modal.css('display', 'block');
    modalImg.attr('src', e.target.src);
  }); // When the user clicks on <span> (x), close the modal

  $('.close').on('click', function () {
    modal.css('display', 'none');
  });
  $('#small_nav').hover(function () {
    return $('.dropdown').addClass('show_dropdown');
  }, function () {
    return $('.dropdown').removeClass('show_dropdown');
  });
  $('#nav_icon').on('click', function (e) {
    e.stopPropagation(); // $('#dropdown').addClass('show_nav');
    // $('#small_nav').addClass('show_nav');

    $('.dropdown').toggleClass('show_dropdown');
  });
  $(document).on('click', function () {
    $('.dropdown').removeClass('show_dropdown');
  });
});