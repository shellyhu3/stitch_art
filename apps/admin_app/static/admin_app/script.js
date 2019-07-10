//Navbar shrink on scroll
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

$(document).ready(()=>{
    // Get the modal
    var modal = $("#myModal");

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var modalImg = $("#img01");
    $(".img").on('click', (e) =>{
        console.log(e.target)
        modal.css('display','block');
        modalImg.attr('src', e.target.src);
    })

    // When the user clicks on <span> (x), close the modal
    $('.close').on('click', () => { 
        modal.css('display','none');
    })

    $('#small_nav').hover(
        () => $('.dropdown').addClass('show_dropdown'),
        () => $('.dropdown').removeClass('show_dropdown')
    )

    $('#nav_icon').on('click', (e) => {
        e.stopPropagation();
        // $('#dropdown').addClass('show_nav');
        // $('#small_nav').addClass('show_nav');
        $('.dropdown').toggleClass('show_dropdown');
    })

    $(document).on('click', () => {
        $('.dropdown').removeClass('show_dropdown');
    })
})