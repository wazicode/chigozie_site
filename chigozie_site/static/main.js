// rotating greeting (home page only)
var g = document.getElementById("greet");
if (g) {
  var greetings = ["Hello", "Bonjour", "Ndewo", "Hola", "Ciao", "Olá", "Hallo", "こんにちは"], gi = 0;
  setInterval(function () {
    gi = (gi + 1) % greetings.length;
    g.style.animation = "none"; void g.offsetWidth; g.style.animation = "";
    g.textContent = greetings[gi];
  }, 1800);
}

// Lagos clock
function tick() {
  var c = document.getElementById("clock");
  if (c) c.textContent = new Date().toLocaleTimeString("en-GB",
    { timeZone: "Africa/Lagos", hour: "2-digit", minute: "2-digit" }) + " WAT";
}
tick(); setInterval(tick, 30000);

// mobile menu
var btn = document.getElementById("menuBtn"), ov = document.getElementById("overlay");
function setMenu(o) {
  ov.classList.toggle("open", o);
  btn.setAttribute("aria-expanded", o);
  btn.textContent = o ? "Close" : "Menu";
}
btn.addEventListener("click", function () { setMenu(!ov.classList.contains("open")); });
ov.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
