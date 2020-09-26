// navbar side menu
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
});

// slide 
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, {
        indicators: false,
        height: 500,
        transition: 500,
        interval: 6000
    });
});

// messages

document.addEventListener('DOMContentLoaded', function(){
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {});
});


let btnMsg = document.querySelector('.btn-msg');
let btnClose = document.querySelector('.btn-close');

btnClose.addEventListener('click', closeMsg)

function closeMsg(){
    btnMsg.style.display = 'none';        
}




