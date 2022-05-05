// Navigation

const navCities = document.querySelectorAll('.city')
const lists = document.querySelectorAll('.sec-menu ul')

navCities.forEach(city => {
    city.addEventListener('click', () => {
        lists.forEach(list => {
            if(list.classList.contains('show')) {
                list.classList.remove('show')
            }
        })
        city.nextElementSibling.classList.toggle('show')
    })
})

// Slider

let slideIndex = 1

const bullets = document.querySelectorAll('.bullet')
const sliderImgs = document.querySelectorAll('.slides-img')

const changeSlide = n => {
    showSlides(slideIndex += n)
}

const showCurrentSlide = n => {
    showSlides(slideIndex = n)
}

const showSlides = n => {
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

document.querySelector('.btn-slide.prev').addEventListener('click', () => {
    changeSlide(-1)
})

document.querySelector('.btn-slide.next').addEventListener('click', () => {
    changeSlide(-1)
})

bullets.forEach(bullet => {
    bullet.addEventListener('click', () => {
        showCurrentSlide(parseInt(bullet.dataset.number))
    })
})

showSlides(slideIndex)
