/* SCRIPT DE TEXTO NA IMAGEM */

const quoteInput = document.getElementById("quote-input");
const quoteOverlay = document.getElementById("quote-overlay");

quoteInput.addEventListener("input", () => {
  quoteOverlay.textContent = quoteInput.value;
});


/* DATA NA TELA */
const data = new Date();
const mes = data.toLocaleString('default', { month: 'long' });
const dia = data.getDate();
const ano = data.getFullYear();
document.getElementById('data').innerHTML = `Dia ${dia} de ${mes}, ${ano}`;

function mudarCor(quadrado) {
    quadrado.style.backgroundColor = "lightblue";
}
function reporCor(quadrado) {
    quadrado.style.backgroundColor = "blue";
}


/* FUNÇÃO DE MUDAR AS CORES */

function toggleDarkMode() {
  const body = document.querySelector('body');
  const footer = document.querySelector('footer');
  const expressao = document.querySelector('#expressao');
  const calculateBtn = document.querySelector('#calculate-btn');
  const clearBtn = document.querySelector('#clear-btn');
  const darkmodeToggle = document.querySelector('#darkmode-toggle');
  body.classList.toggle('darkmode');
  expressao.classList.toggle('darkmode');
  calculateBtn.classList.toggle('darkmode');
  clearBtn.classList.toggle('darkmode');
  footer.classList.toggle('darkmode');
  darkmodeToggle.classList.toggle('darkmode');
}


/* FUNÇÃO DA CALCULADORA */

const display = document.querySelector('.display');
const buttons = document.querySelectorAll('button');
let expression = '';

buttons.forEach(button => {
  button.addEventListener('click', () => {
    if (button.classList.contains('number')) {
      expression += button.value;
      display.value = expression;
    } else if (button.classList.contains('operator')) {
      expression += button.value;
      display.value = expression;
    } else if (button.classList.contains('clear')) {
      expression = '';
      display.value = '';
    } else if (button.classList.contains('calculate')) {
      expression = eval(expression);
      display.value = expression;
      
    }
  });
});



/* FUNÇÃO DE INPUT E ESCREVER NOMES */

const form = document.querySelector('form');
const submitBtn = document.getElementById('submit-btn');
const greeting = document.getElementById('greeting');
const greeting1 = document.getElementById('greeting1');
const greetingUsername = document.getElementById('greeting-username');
const greetingUsername1 = document.getElementById('greeting-username1');
const username = document.getElementById('username');
const separador = document.getElementById('sep');
const usernameText = document.getElementById('username-text');

submitBtn.addEventListener('click', () => {
  const name = document.getElementById('name').value;
  greetingUsername.innerHTML = name;
  greetingUsername1.innerHTML = name;
  usernameText.innerHTML = name;
  
  form.reset();
  separador.classList.remove('hidden');
  greeting.classList.remove('hidden');
  greeting1.classList.remove('hidden');
  username.classList.remove('hidden');
});