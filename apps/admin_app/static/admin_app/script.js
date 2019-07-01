window.onscroll = () => scrollFunction();

function scrollFunction(){
    if (document.documentElement.scrollTop > 200){
        document.getElementById('nav').style.background = 'rgb(73, 87, 104)';
        document.getElementById('nav').style.height = '80px';
        document.getElementById('home').style.fontSize = '50px';
        // document.getElementById('home').style.gridColumn = '1/3';
        // document.getElementById('links').style.gridTemplateColumns = 'repeat(7, 1fr)';
    } else{
        document.getElementById('nav').style.background = 'url("/static/admin_app/thread.jpeg") no-repeat fixed';
        document.getElementById('nav').style.backgroundSize = 'cover';
        document.getElementById('nav').style.height = '120px';
        document.getElementById('home').style.fontSize = '70px';
        // document.getElementById('home').style.gridColumn = '1/-1';
        // document.getElementById('links').style.gridTemplateColumns = 'repeat(5, 1fr)';
    }
}
