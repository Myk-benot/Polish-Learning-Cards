let cards = [];
let currentIndex = 0;

document.getElementById('nextButton').addEventListener('click', showNextCard);
document.getElementById('playAudio').addEventListener('click', playAudio);

// Fetch the phrases from the JSON file
fetch('phrases.json')
  .then(response => response.json())
  .then(data => {
    cards = data;
    showNextCard();
  });

function showNextCard() {
  if (currentIndex >= cards.length) {
    currentIndex = 0;
  }

  const card = cards[currentIndex];
  document.getElementById('word').textContent = card.polish;
  document.getElementById('meaning').textContent = card.english;
  document.getElementById('playAudio').dataset.audio = `audio/${card.polish}.mp3`;

  currentIndex++;
}

function playAudio() {
  const audio = new Audio(document.getElementById('playAudio').dataset.audio);
  audio.play();
}
