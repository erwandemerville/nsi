const array = [5, 3, 1, 6, 4, 7, 2];
const arrayEl = document.getElementById("array-trii");
const memoryValueEl = document.getElementById("memory-value");
const startSortButton = document.getElementById("start-sort");
const stepSortButton = document.getElementById("step-sort");
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

let ii = 1;
let jj, keyy;
async function stepSort() {
    if (ii < array.length) {
        if (jj >= 0 && array[jj] > keyy) {
            array[jj + 1] = array[jj];
            arrayEl.children[jj + 1].textContent = array[jj];
            arrayEl.children[jj + 1].classList.remove("active");
            arrayEl.children[jj + 1].classList.add("shifting");
            await sleep(300);
            arrayEl.children[jj + 1].classList.remove("shifting");
            arrayEl.children[jj].classList.remove("processed");
            arrayEl.children[jj + 1].classList.add("processed");
            jj = jj - 1;
        } else {
            if (jj !== undefined) {
                array[jj + 1] = keyy;
                arrayEl.children[jj + 1].textContent = keyy;
                arrayEl.children[jj + 1].classList.remove("active", "shifting");
                arrayEl.children[jj + 1].classList.add("processed");
                memoryValueEl.value = "";
            }
            keyy = array[ii];
            jj = ii - 1;
            memoryValueEl.value = keyy;
            arrayEl.children[ii].classList.add("active");
            await sleep(300);
            ii++;
        }
    } else if (ii === array.length && jj >= 0) {
        if (array[jj] > keyy) {
            array[jj + 1] = array[jj];
            arrayEl.children[jj + 1].textContent = array[jj];
            arrayEl.children[jj + 1].classList.remove("active");
            arrayEl.children[jj + 1].classList.add("shifting");
            await sleep(300);
            arrayEl.children[jj + 1].classList.remove("shifting");
            arrayEl.children[jj].classList.remove("processed");
            arrayEl.children[jj + 1].classList.add("processed");
            jj = jj - 1;
        } else {
            array[jj + 1] = keyy;
            arrayEl.children[jj + 1].textContent = keyy;
            arrayEl.children[jj + 1].classList.remove("active", "shifting");
            arrayEl.children[jj + 1].classList.add("processed");
            memoryValueEl.value = "";
        }
    }
}

createArrayElements(array);
arrayEl.children[0].classList.add("processed");
startSortButton.addEventListener("click", insertionSort);
stepSortButton.addEventListener("click", stepSort);
