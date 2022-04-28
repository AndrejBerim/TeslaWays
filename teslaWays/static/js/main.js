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