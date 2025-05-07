const NUM_BARS = 30; // Nombre de barres
const MIN_HEIGHT = 10; // Hauteur minimale des barres
const MAX_HEIGHT = 300; // Hauteur maximale des barres
let stepDelay = 100; // Délai entre chaque étape de la simulation (en ms)
let currentIndex = 0; // Index courant de la barre sélectionnée
let isRunning = false; // Indique si la simulation est en cours
let stop = false; // Permet d'arrêter la simulation
let bars = []; // Tableau contenant les barres

function init() {
  const container = document.getElementById("bars-container");
  for (let i = 0; i < NUM_BARS; i++) {
    const height = getRandomHeight();
    const $bar = document.createElement("div");
    $bar.classList.add("bar");
    $bar.style.height = `${height}px`;
    $bar.setAttribute("data-value", height);
    bars.push($bar);
    container.appendChild($bar);
  }
}

function getRandomHeight() {
  return Math.floor(Math.random() * (MAX_HEIGHT - MIN_HEIGHT + 1)) + MIN_HEIGHT;
}

async function run() {
  if (isRunning) {
    return;
  }
  stop = false;
  isRunning = true;
  for (let i = 0; i < NUM_BARS; i++) {
    if (stop) {
        return;
    }
    await selectMin(i);
    await swap(i, currentIndex);
    highlight(i, "green");
  }
  isRunning = false;
}

async function selectMin(startIndex) {
  if (stop) {
      return;
  }
  let minIndex = startIndex;
  highlight(minIndex, "red");
  await sleep(stepDelay);
  for (let i = startIndex + 1; i < NUM_BARS; i++) {
    if (stop) {
        return;
    }
    highlight(i, "blue");
    await sleep(stepDelay);
    if (parseInt(bars[i].getAttribute("data-value")) < parseInt(bars[minIndex].getAttribute("data-value"))) {
      highlight(minIndex, "#2196F3");
      minIndex = i;
      highlight(minIndex, "red");
      await sleep(stepDelay);
    } else {
      highlight(i, "#2196F3");
      await sleep(stepDelay);
    }
  }
  highlight(minIndex, "#2196F3");
  await sleep(stepDelay);
  currentIndex = minIndex;
}

async function swap(index1, index2) {
  if (stop) {
    return;
  }
  if (index1 == index2) {
    return;
  }
  highlight(index1, "purple");
  highlight(index2, "purple");
  await sleep(stepDelay);
  const tempHeight = bars[index1].style.height;
  const tempValue = bars[index1].getAttribute("data-value");
  bars[index1].style.height = bars[index2].style.height;
  bars[index1].setAttribute("data-value", bars[index2].getAttribute("data-value"));
  bars[index2].style.height = tempHeight;
  bars[index2].setAttribute("data-value", tempValue);
  highlight(index1, "#2196F3");
  highlight(index2, "#2196F3");
  await sleep(stepDelay);
}

function highlight(index, color) {
  bars[index].style.backgroundColor = color;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

document.getElementById("run-button").addEventListener("click", () => {
  run();
});

document.getElementById("speed-up-button").addEventListener("click", () => {
  if (stepDelay > 50) {
    stepDelay -= 50;
  }
});

document.getElementById("speed-down-button").addEventListener("click", () => {
  if (stepDelay < 1000) {
    stepDelay += 50;
  }
});

document.getElementById("reinit-button").addEventListener("click", () => {
    stop = true;
    document.getElementById("bars-container").innerHTML = "";
    stepDelay = 100; // Délai entre chaque étape de la simulation (en ms)
    currentIndex = 0; // Index courant de la barre sélectionnée
    isRunning = false; // Indique si la simulation est en cours
    bars = []; // Tableau contenant les barres
    //document.getElementById("bars-container").getElementsByClassName("bar").style.color = "#2196F3";
    init();
  });

init();
