const buttonsEl = document.querySelectorAll('.btn-slide')
const slidesEl = document.querySelector('#second .slides')

document.querySelector('.slider-container#second').addEventListener('click', e => {
    if (e.target === slidesEl) {
        document.querySelector('.slider-container#second').style.display = 'none'
    }
})