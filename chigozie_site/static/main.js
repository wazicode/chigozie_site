var fine = window.matchMedia("(pointer:fine)").matches;
var reduce = window.matchMedia("(prefers-reduced-motion:reduce)").matches;

// intro: cycling greetings, once per visit, home page only
var intro = document.getElementById("intro"), word = document.getElementById("introWord");
var seen = false; try { seen = sessionStorage.getItem("seen"); } catch (e) {}
if (intro && (seen || reduce || location.pathname.replace(/\/+$/, "").split("/").pop() && document.querySelector(".page"))) {
  intro.remove();
} else if (intro) {
  var list = ["Hello","Bonjour","Ndewo","Hola","Ciao","Olá","Hallå","Guten tag","Hallo"], i = 0;
  var t = setInterval(function () {
    i++;
    if (i >= list.length) { clearInterval(t); intro.classList.add("done"); try { sessionStorage.setItem("seen", "1"); } catch (e) {} setTimeout(function () { intro.remove(); }, 1000); return; }
    word.textContent = list[i];
  }, 220);
}

// page transition
var curtain = document.getElementById("curtain");
document.addEventListener("click", function (e) {
  var a = e.target.closest("a");
  if (!a || a.target === "_blank" || e.metaKey || e.ctrlKey || a.origin !== location.origin || a.hash || a.protocol.indexOf("http") !== 0) return;
  if (a.pathname === location.pathname) return;
  e.preventDefault();
  curtain.classList.add("pre"); void curtain.offsetWidth; curtain.classList.remove("pre"); curtain.classList.add("in");
  setTimeout(function () { location.href = a.href; }, reduce ? 0 : 560);
});
window.addEventListener("pageshow", function (e) { if (e.persisted) curtain.classList.remove("in"); });

// cursor bubble + hover preview
if (fine) {
  var cur = document.getElementById("cursor"), peek = document.getElementById("peek"), pimg = peek.querySelector("img");
  var mx = 0, my = 0, cx = 0, cy = 0, s = 0, target = 0;
  document.addEventListener("mousemove", function (e) { mx = e.clientX; my = e.clientY; });
  (function loop() {
    cx += (mx - cx) * .18; cy += (my - cy) * .18; s += (target - s) * .2;
    cur.style.transform = "translate(" + cx + "px," + cy + "px) scale(" + s + ")";
    peek.style.transform = "translate(" + (cx - 140) + "px," + (cy - 150) + "px)";
    requestAnimationFrame(loop);
  })();
  document.querySelectorAll("[data-cursor]").forEach(function (el) {
    el.addEventListener("mouseenter", function () { target = 1; if (el.dataset.img) { pimg.src = el.dataset.img; peek.style.opacity = 1; } });
    el.addEventListener("mouseleave", function () { target = 0; peek.style.opacity = 0; });
  });
  // magnetic round buttons
  document.querySelectorAll(".mag").forEach(function (el) {
    el.addEventListener("mousemove", function (e) {
      var r = el.getBoundingClientRect();
      el.style.translate = ((e.clientX - r.left - r.width / 2) * .3) + "px " + ((e.clientY - r.top - r.height / 2) * .3) + "px";
    });
    el.addEventListener("mouseleave", function () { el.style.translate = "0 0"; });
  });
}

// Lagos clock
function tick() {
  var c = document.getElementById("clock");
  if (c) c.textContent = new Date().toLocaleTimeString("en-GB", { timeZone: "Africa/Lagos", hour: "2-digit", minute: "2-digit" }) + " WAT";
}
tick(); setInterval(tick, 30000);

// menu
var btn = document.getElementById("menuBtn"), ov = document.getElementById("overlay");
function setMenu(o) { ov.classList.toggle("open", o); btn.setAttribute("aria-expanded", o); btn.textContent = o ? "Close" : "Menu"; }
btn.addEventListener("click", function () { setMenu(!ov.classList.contains("open")); });
