const slides = [...document.querySelectorAll('.slide')];
let i = 0;
const bar = document.querySelector('#bar'), num = document.querySelector('#num'), hint = document.querySelector('#hint');
function show(n) {
  i = Math.max(0, Math.min(slides.length - 1, n));
  slides.forEach((s,k) => {
    s.classList.toggle('on', k === i);
    const foot = s.querySelector('.foot span:last-child');
    if (foot) foot.textContent = String(k+1).padStart(2,'0') + ' / ' + slides.length;
  });
  document.body.dataset.slideDark = String(slides[i].classList.contains('dark'));
  bar.style.width = ((i+1)/slides.length*100) + '%';
  num.textContent = (i+1) + ' / ' + slides.length;
  hint.style.opacity = i ? '0' : '.6';
  history.replaceState(null, '', '#slide='+(i+1));
}
addEventListener('keydown', e => {
  if (document.body.classList.contains('refs-open')) return;
  if (['ArrowRight','PageDown',' '].includes(e.key)) { e.preventDefault(); show(i+1); }
  else if (['ArrowLeft','PageUp'].includes(e.key)) { e.preventDefault(); show(i-1); }
  else if (e.key==='Home') show(0);
  else if (e.key==='End') show(slides.length-1);
});
addEventListener('click', e => {
  if (!e.target.closest('a,button,#refsPanel')) show(i+1);
});
const initial = Number(new URLSearchParams(location.hash.slice(1)).get('slide'));
show(Number.isFinite(initial) && initial > 0 ? initial-1 : 0);
addEventListener('hashchange', () => {
  const target = Number(new URLSearchParams(location.hash.slice(1)).get('slide'));
  if (Number.isFinite(target) && target > 0) show(target - 1);
});
