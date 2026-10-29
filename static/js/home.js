const button = document.getElementById('btn');
const circle = document.getElementById('ring2');
button.addEventListener('click', function() {
  circle.classList.toggle('is-spinning');
});