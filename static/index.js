const phoneInput = document.getElementById('phone');

phoneInput.addEventListener('focus', function (e) {
    if (!e.target.value) {
        e.target.value = '+7';
    }
});

phoneInput.addEventListener('blur', function (e) {
    if (e.target.value === '+7') {
        e.target.value = '';
    }
});

const openAuth = document.getElementById('openAuth')
const closeAuth = document.getElementById('closeAuth')
const AuthPopup = document.getElementById('authPopup')


function switchPopup () {
    if (AuthPopup.classList.contains('hidden')) {
        AuthPopup.classList.remove('hidden')
    }   
    else {
        AuthPopup.classList.add('hidden')
    }
}

closeAuth.addEventListener('click', function (e) {
    switchPopup()
})
openAuth.addEventListener('click', function (e) {
    switchPopup()
})