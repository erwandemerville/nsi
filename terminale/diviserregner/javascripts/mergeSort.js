// Canvas variables
var canvas, canvaswidth, canvasheight, ctrl;

// Call canvasElements() to store height width
// in above canvas variables
canvasElements();

// Length of unsorted array
var len_of_arr = 25;

// 3 array are declared

//1) arr is for storing array element 
//2) itmd for storing intermediate values
//3) visited is for element which has been sorted
var arr, itmd, visited
var executed = false  // permet d'indiquer si la visualisation classique est en cours d'exécution
var executedPap = false // permet d'indiquer si la visualisation "Pas à pas" est en cours d'exécution
var avancer = false  // pour le mode "Pas à pas" : indique si on doit avancer d'une étape

// Init arrays and draw bars
const init = async () => {
	arr = [], itmd = [], visited = []

	// Store random value in arr[]
	
	for (var i = 0; i < len_of_arr; i++) {
		arr.push(Math.round(Math.random() * 250) )
	}

	// Initialize itmd and visited array with 0
	for (var i = 0; i < len_of_arr; i++) {
		itmd.push(0)
		visited.push(0)
	}

	await drawBars()
}
// Merging of two sub array
// https://www.geeksforgeeks.org/merge-two-sorted-arrays/
function mergeArray(start, end) {
	let mid = parseInt((start + end) >> 1);
	let start1 = start, start2 = mid + 1
	let end1 = mid, end2 = end
	
	// Initial index of merged subarray
	let index = start

	while ((start1 <= end1 && start2 <= end2) && (executed || executedPap)) {
		if (arr[start1] <= arr[start2]) {
			itmd[index] = arr[start1]
			index = index + 1
			start1 = start1 + 1;
		}
		else if(arr[start1] > arr[start2]) {
			itmd[index] = arr[start2]
			index = index + 1
			start2 = start2 + 1;
		}
	}

	// Copy the remaining elements of
	// arr[], if there are any
	while ((start1 <= end1) && (executed || executedPap)) {
		itmd[index] = arr[start1]
		index = index + 1
		start1 = start1 + 1;
	}

	while ((start2 <= end2) && (executed || executedPap)) {
		itmd[index] = arr[start2]
		index = index + 1
		start2 = start2 + 1;
	}

	index = start
	while ((index <= end) && (executed || executedPap)) {
		arr[index] = itmd[index];
		index++;
	}
}

// Function for showing visualization 
// effect
function drawBars(start, end) {

	// Clear previous unsorted bars
	ctrl.clearRect(0, 0, canvas.width, canvas.height)

	// Styling of bars
	for (let i = 0; i < len_of_arr; i++) {

		// Changing styles of bars
		ctrl.fillStyle = "black"
		ctrl.shadowOffsetX = 2
		ctrl.shadowColor = "chocolate";
		ctrl.shadowBlur = 3;
		ctrl.shadowOffsetY =5;
		
		
		// Size of rectangle of bars
		ctrl.fillRect(25 * i, 300 - arr[i], 20, arr[i])
		
		if ((executed || executedPap) && visited[i]) {
			ctrl.fillStyle = "#006d13"
			ctrl.fillRect(25 * i, 300 - arr[i], 20, arr[i])
			ctrl.shadowOffsetX = 2
		}
	}

	for (let i = start; i <= end; i++) {
		if (!(executed || executedPap)) {
			return;
		}
		ctrl.fillStyle = "orange"
		ctrl.fillRect(25 * i, 300 - arr[i], 18, arr[i])
		ctrl.fillStyle = "#cdff6c"
		ctrl.fillRect(25 * i,300, 18, arr[i])
		visited[i] = 1
	}
}

// Waiting interval between two bars
function timeout(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

// Attente d'une action (pour poursuivre le tri fusion)
function getPromiseFromEvent() {
	return new Promise((resolve) => {
	  const listener = () => {;
		resolve();
	  }
	  button_mergeSort = document.getElementById("run-mergeSort");
	  button_mergeSortStep = document.getElementById("run-mergeSort-step");
	  button_resetMergeSort = document.getElementById("reset-mergeSort");
	  button_mergeSort.addEventListener("click", listener);
	  button_mergeSortStep.addEventListener("click", listener);
	  button_resetMergeSort.addEventListener("click", listener);
	})
}

// Merge Sorting
const mergeSort = async (start, end) => {
	avancer = false
	if ((start < end) && (executedPap || executed)) {
		let mid = parseInt((start + end) >> 1)
		if (executedPap || executed) await mergeSort(start, mid)
		if (executedPap || executed) await mergeSort(mid + 1, end)
		if (executedPap || executed) await mergeArray(start, end)
		if (executedPap || executed) await drawBars(start, end)

		// Waiting time
		if (executed) await timeout(800)
		if (executedPap) await getPromiseFromEvent()
	}
}

// canvasElements function for storing
// width and height in canvas variable
function canvasElements() {
	canvas = document.getElementById("Canvas")
	canvas.width = 700
	canvas.height = 600
	canvaswidth = canvas.width
	canvasheight = canvas.height
	ctrl = canvas.getContext("2d")
}

// Asynchronous MergeSort function 
const performer = async () => {
	if (executedPap || executed) await mergeSort(0, len_of_arr - 1)
	if (executedPap || executed) await drawBars()

	// Code for change title1 text 
	const title1_changer = document.querySelector(".title1")
	if (executedPap || executed) title1_changer.innerText = "Le tableau est complètement trié"
	executedPap = false
	executed = false
}

document.getElementById("run-mergeSort").addEventListener("click", () => {
	if (!executedPap && !executed) {
		executed = true
		performer();
	}
	if (executedPap && !executed) {
		executedPap = false
		executed = true
		avancer = true
	}
});

document.getElementById("run-mergeSort-step").addEventListener("click", () => {
	if (!executedPap && !executed) {
		executedPap = true
		performer();
	}
	if (!executedPap && executed) {
		executed = false
		executedPap = true
	}
	avancer = true
});

document.getElementById("reset-mergeSort").addEventListener("click", () => {
	executed = false  // interrompre l'exécution normale
	executedPap = false  // interrompre l'exécution "Pas à pas"
	init()  // Réinitialiser les tableaux

	// Code for change title1 text 
	const title1_changer = document.querySelector(".title1")
	title1_changer.innerText = "Le tableau n'est pas trié"
});

init()
