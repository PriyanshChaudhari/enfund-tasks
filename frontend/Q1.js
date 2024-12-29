document.getElementById('collapse-button').addEventListener('click', function() {
    var leftMenu = document.getElementById('left-menu');
    leftMenu.classList.toggle('collapsed');
});

function adjustPageSize() {
    var width = window.innerWidth;
    var scale = 1;

    if (width >= 992 && width <= 1600) {
        scale = 0.9;
    } else if (width >= 700 && width <= 767) {
        scale = 0.8;
    } else if (width >= 600 && width < 700) {
        scale = 0.75;
    } else if (width <= 600) {
        scale = 0.5;
    }

    document.body.style.transform = 'scale(' + scale + ')';
}

window.addEventListener('load', adjustPageSize);