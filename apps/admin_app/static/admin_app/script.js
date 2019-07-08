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
$(".img").click((e) =>{
    console.log(e.target)
    modal.css('display','block');
    modalImg.attr('src', e.target.src);
})


// When the user clicks on <span> (x), close the modal
$('.close').click(() => { 
    modal.css('display','none');
})

})