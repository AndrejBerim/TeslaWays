// Automatic Slideshow

const automaticSlideshow = () => {
    setInterval((() => {
        changeSlide(1, 'first')
    }), 2000);
}

// Slider

let slideIndex = 0
const bullets = document.querySelectorAll('.bullet')
const prevBttn = document.querySelector('#first .btn-slide.prev')
const nextBttn = document.querySelector('#first .btn-slide.next')
const iconLeft = document.querySelector('i.fa-angle-left')
const iconRight = document.querySelector('i.fa-angle-right.fa-xl')

const changeSlide = (n, id) => {
    showSlides(slideIndex += n, id)
}

const showCurrentSlide = n => {
    showSlides(slideIndex = n, 'first')
}

const showSlides = (n, id) => {
    let sliderImgs = document.querySelectorAll(`#${id} .slides-img`)
    if (n > sliderImgs.length) {
        slideIndex = 1
    } else if (n < 1) {
        slideIndex = sliderImgs.length
    }
    for (let i = 0; i < sliderImgs.length; i++) {
        sliderImgs[i].style.display = 'none'
    }
    sliderImgs[slideIndex-1].style.display = 'block'
}

const openSliderOverlay = () => {
    document.querySelector('.slider-container#second').style.display = "block"
}

prevBttn.addEventListener('click', () => {
    clearInterval(1)
    changeSlide(-1, 'first')
})

nextBttn.addEventListener('click', () => {
    clearInterval(1)
    changeSlide(1, 'first')
})

document.querySelector('#second .btn-slide.prev').addEventListener('click', () => {
    changeSlide(-1, 'second')
})

document.querySelector('#second .btn-slide.next').addEventListener('click', () => {
    changeSlide(1, 'second')
})

bullets.forEach(bullet => {
    bullet.addEventListener('click', () => {
        showCurrentSlide(parseInt(bullet.dataset.number))
    })
})

showSlides(slideIndex = 1, 'first')
showSlides(slideIndex = 1, 'second')
automaticSlideshow()


// Open slider overlay

document.querySelector('.slider-container#first').addEventListener('click', e => {
    if (e.target !== prevBttn && e.target != nextBttn && e.target != iconLeft && e.target != iconRight) {
        openSliderOverlay()
    }
})