const query = document.querySelector('#query');
const category = document.querySelector('#category');
const status = document.querySelector('#status');
const count = document.querySelector('#count');
const empty = document.querySelector('#empty');
const entries = document.querySelectorAll('[data-category]');
const normalize = value => value.normalize('NFKC').toLowerCase().replaceAll(/[^\p{L}\p{N}]+/gu, ' ').trim();

function update() {
  const words = normalize(query.value).split(' ');
  let matches = 0;
  for (const entry of entries) {
    const terms = normalize(entry.dataset.search);
    entry.hidden = !words.every(word => terms.includes(word))
      || (category.value !== '' && entry.dataset.category !== category.value)
      || (status.value !== '' && entry.dataset.status !== status.value);
    matches += Number(!entry.hidden);
  }
  count.textContent = `${matches} ${count.dataset.unit}`;
  empty.hidden = matches !== 0;
}

query.addEventListener('input', update);
category.addEventListener('change', update);
status.addEventListener('change', update);
document.querySelector('#filters').hidden = false;
update();
