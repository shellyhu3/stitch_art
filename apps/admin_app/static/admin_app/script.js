$(document).on('scroll', () => scrollFunction());

function scrollFunction(){  
    if ($(document).scrollTop() > 100){
        $('#nav').removeClass('reg_nav');
        $('#nav').addClass('scrolled_nav');
        $('#bg_nav').removeClass('reg_nav_bg');
        $('#bg_nav').addClass('scrolled_nav');
    } else{
        $('#nav').removeClass('scrolled_nav');
        $('#nav').addClass('reg_nav');
        $('#bg_nav').removeClass('scrolled_nav');
        $('#bg_nav').addClass('reg_nav_bg');
    }
}
