const formSubmitBttn = document.querySelector('.newsletter-form .submit')
const notification = document.querySelector('.newsletter-notification')
function validateEmail(email) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
    {
        notification.textContent = 'Uspešno ste se prijavili!'
        return (true)
    }
        notification.textContent = 'Email adresa nije validna!'
        return (false)
    }

formSubmitBttn.addEventListener('click', e => {
    e.preventDefault()
    const email = document.querySelector('#newsletter').value
    validateEmail(email)
})