const array = [5, 3, 1, 6, 4, 7, 2];
const arrayEl = document.getElementById("array-trii");
const memoryValueEl = document.getElementById("memory-value");
const startSortButton = document.getElementById("start-sort");
// const attente = 3000;
memoryValueEl.value = "";

function createArrayElements(arr) {
    arrayEl.innerHTML = "";
    arr.forEach((value) => {
        const li = document.createElement("li");
        li.textContent = value;
        arrayEl.appendChild(li);
    });
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function insertionSort() {
    startSortButton.disabled = true;
    for (let i = 1; i < array.length; i++) {
        let key = array[i];
        let j = i - 1;
        memoryValueEl.value = key;
        arrayEl.children[i].classList.add("active");
        await sleep(1000);

        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            arrayEl.children[j + 1].textContent = array[j];
            arrayEl.children[j + 1].classList.remove("active");
            arrayEl.children[j + 1].classList.add("shifting");
            arrayEl.children[j].classList.remove("processed");
            await sleep(1000);
            arrayEl.children[j + 1].classList.remove("shifting");
            arrayEl.children[j + 1].classList.add("processed");
            j = j - 1;
        }
        array[j + 1] = key;
        arrayEl.children[j + 1].textContent = key;
        arrayEl.children[j + 1].classList.remove("active", "shifting");
        arrayEl.children[j + 1].classList.add("processed");
        memoryValueEl.value = "";
        await sleep(1000);
    }
    startSortButton.disabled = false;
}

let i = 1;
let j, key;

async function stepSort() {
    if (i < array.length) {
        if (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            arrayEl.children[j + 1].textContent = array[j];
            arrayEl.children[j + 1].classList.remove("active");
            arrayEl.children[j + 1].classList.add("shifting");
            await sleep(300);
            arrayEl.children[j + 1].classList.remove("shifting");
            arrayEl.children[j].classList.remove("processed");
            arrayEl.children[j + 1].classList.add("processed");
            j = j - 1;
        } else {
            if (j !== undefined) {
                array[j + 1] = key;
                arrayEl.children[j + 1].textContent = key;
                arrayEl.children[j + 1].classList.remove("active", "shifting");
                arrayEl.children[j + 1].classList.add("processed");
                memoryValueEl.value = "";
            }
            key = array[i];
            j = i - 1;
            memoryValueEl.value = key;
            arrayEl.children[i].classList.add("active");
            await sleep(300);
            i++;
        }
    } else if (i === array.length && j >= 0) {
        if (array[j] > key) {
            array[j + 1] = array[j];
            arrayEl.children[j + 1].textContent = array[j];
            arrayEl.children[j + 1].classList.remove("active");
            arrayEl.children[j + 1].classList.add("shifting");
            await sleep(300);
            arrayEl.children[j + 1].classList.remove("shifting");
            arrayEl.children[j].classList.remove("processed");
            arrayEl.children[j + 1].classList.add("processed");
            j = j - 1;
        } else {
            array[j + 1] = key;
            arrayEl.children[j + 1].textContent = key;
            arrayEl.children[j + 1].classList.remove("active", "shifting");
            arrayEl.children[j + 1].classList.add("processed");
            memoryValueEl.value = "";
        }
    }
}

createArrayElements(array);
arrayEl.children[0].classList.add("processed");
startSortButton.addEventListener("click", insertionSort);

const stepSortButton = document.getElementById("step-sort");
stepSortButton.addEventListener("click", stepSort);