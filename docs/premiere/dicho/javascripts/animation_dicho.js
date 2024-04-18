function recupererCellulesValides(noeud) {
	listeNoeuds = noeud.children;
	let tableau = [];
	for (let index = 1; index < listeNoeuds.length; index++) {
		tableau.push(listeNoeuds[index]);
	}
	return tableau;
}

function recupererEntiers(noeud) {
	listeNoeuds = noeud.children;
	let tableau = [];
	for (let index = 1; index < listeNoeuds.length; index++) {
		tableau.push(parseInt(listeNoeuds[index].innerHTML));
	}
	return tableau;
}

function supRaisons(visuA) {
	for (let index = 0; index < visuA.bornes.length; index++) {
		visuA.raisons[index].className = "";
		visuA.raisons[index].innerHTML = "";
	}
}

function afficherPiliers(visuA, centre=-1) {
	for (let index = 0; index < visuA.bornes.length; index++) {
		visuA.bornes[index].className = "";
		visuA.bornes[index].innerHTML = "";
		if (index < visuA.gauche || index > visuA.droite) {
			if (index != centre) {
				visuA.numeros[index].className = "txt_w";
				visuA.cellulesVal[index].className = "txt_w";
			}
		} else {
			visuA.numeros[index].className = "ext";
			visuA.cellulesVal[index].className = "val";
		}
	}
	let nom = 'rejet';
	if (visuA.gauche <= visuA.droite) {
		nom = 'ext';
	}
	visuA.bornes[visuA.gauche].className = nom;
	visuA.bornes[visuA.gauche].innerHTML = '<span style="font-size: large">g</span>';
	visuA.bornes[visuA.droite].className = nom;
	visuA.bornes[visuA.droite].innerHTML = '<span style="font-size: large">d</span>';
}

function deplacerPiliers(visuA, centre=-1) {
	for (let index = 0; index < visuA.bornes.length; index++) {
		visuA.bornes[index].className = "";
		visuA.bornes[index].innerHTML = "";
	}
	let nom = 'rejet';
	if (visuA.gauche <= visuA.droite) {
		nom = 'ext';
	}
	visuA.bornes[visuA.gauche].className = nom;
	visuA.bornes[visuA.gauche].innerHTML = '<span style="font-size: large">g</span>';
	visuA.bornes[visuA.droite].className = nom;
	visuA.bornes[visuA.droite].innerHTML = '<span style="font-size: large">d</span>';
}

function afficherCentre1(visuA) {
	let c = visuA.c;
	for (let index = 0; index < visuA.bornes.length; index++) {
		if (index == c) {
			visuA.bornes[c].className = "pilier";
			visuA.bornes[c].innerHTML = '<span style="font-size: large">c</span>';
			visuA.numeros[index].className = "pilier";
		} else if (index != visuA.gauche && index != visuA.droite) {
			visuA.bornes[index].className = "";
		}
	}
}

function afficherCentre2(visuA) {
	let c = visuA.c;
	visuA.cellulesVal[c].className = "pilier";
}


function afficherTestCentre(visuA) {
	let c = visuA.c;
	for (let index = 0; index < visuA.bornes.length; index++) {
		if (index == c) {
			if (visuA.valeurs[index] > visuA.cherche) {
				visuA.numeros[c].className = "rejet";
				visuA.cellulesVal[c].className = "rejet";
				visuA.raisons[c].className = "rejet";
				visuA.raisons[c].innerHTML = '&gt;<br>'+visuA.cherche;
			} else if (visuA.valeurs[index] < visuA.cherche) {
				visuA.cellulesVal[c].className = "rejet";
				visuA.numeros[c].className = "rejet";
				visuA.raisons[c].className = "rejet";
				visuA.raisons[c].innerHTML = '&lt;<br>'+visuA.cherche;
			} else {
				visuA.raisons[c].className = "trouve";
				visuA.raisons[c].innerHTML = 'ok';
			}
		} else {
			visuA.raisons[index].className = "";
			visuA.raisons[index].innerHTML = "";
		}
	}
}

function afficherElementsSup(visuA) {
	let c = visuA.c;
	if (visuA.valeurs[c] > visuA.cherche) {
		for (let index = 0; index < visuA.bornes.length; index++) {
			if (index > c && index <= visuA.droite) {
				visuA.raisons[index].className = "rejet";
				visuA.cellulesVal[index].className = "rejet";
				visuA.numeros[index].className = "rejet";
				visuA.raisons[index].innerHTML = '&gt;<br>'+visuA.cherche;
			}
		}
	} else if (visuA.valeurs[c] < visuA.cherche) {
		for (let index = 0; index < visuA.bornes.length; index++) {
			if (index < c && index >= visuA.gauche) {
				visuA.raisons[index].className = "rejet";
				visuA.cellulesVal[index].className = "rejet";
				visuA.numeros[index].className = "rejet";
				visuA.raisons[index].innerHTML = '&lt;<br>'+visuA.cherche;
			}
		}
	}
}


// <span style="font-size: x-large">&#8595;</span>
function hasard(identifiant) {
	var visuA = document.getElementById(identifiant);
	let noeud = document.querySelector("#" + identifiant + " .trelement");
	visuA.cellulesVal = recupererCellulesValides(noeud);
	let tableau = []
	for (let index = 0; index < visuA.cellulesVal.length; index++) {
		tableau.push(Math.floor(Math.random() * Math.floor(100)));
	}
	const byValue = (a,b) => a - b;
	let tableau_trie = [...tableau].sort(byValue);
	for (let index = 0; index < tableau_trie.length; index++) {
		visuA.cellulesVal[index].innerHTML = tableau_trie[index];
	}
}

function initDicho(identifiant, cherche, gauche=-1, droite=-1) {

	var visuA = document.getElementById(identifiant);
	visuA.etape = 1;
	visuA.cherche = cherche;

	let noeud = document.querySelector("#" + identifiant + " .trindic");
	visuA.bornes = recupererCellulesValides(noeud);

	noeud = document.querySelector("#" + identifiant + " .index");
	visuA.numeros = recupererCellulesValides(noeud);

	noeud = document.querySelector("#" + identifiant + " .trelement");
	visuA.cellulesVal = recupererCellulesValides(noeud);
	visuA.valeurs = recupererEntiers(noeud);

	noeud = document.querySelector("#" + identifiant + " .trraison");
	visuA.raisons = recupererCellulesValides(noeud);

	if (gauche == -1) {
		visuA.gauche = 0;
		visuA.droite = visuA.cellulesVal.length-1;
	} else {
		visuA.gauche = gauche;
		visuA.droite = droite;
	}

	supRaisons(visuA);
	afficherPiliers(visuA);

}

function vitesse(identifiant, vit) {
	var visuA = document.getElementById(identifiant);
	visuA.vit = vit;
}

function pause(identifiant, vit) {
	var visuA = document.getElementById(identifiant);
	visuA.pause = !visuA.pause;
}

function startdicho1(identifiant, cherche, boucle=true, gauche=-1, droite=-1) {
	var visuA = document.getElementById(identifiant);
	visuA.boucle = boucle;
	visuA.ide = Math.floor(Math.random() * 1000000);
	if (!visuA.vit) {
		visuA.vit = 5;
	}
	initDicho(identifiant, cherche,gauche,droite);
	animDicho1(identifiant, visuA.ide);
}

function startdicho2(identifiant, ide) {
	var visuA = document.getElementById(identifiant);
	visuA.boucle = true;
	visuA.ide = Math.floor(Math.random() * 1000000);
	let cherche = document.getElementById('valRecherche').value;
	if (!visuA.vit) {
		visuA.vit = 5;
	}
	initDicho(identifiant, cherche,-1,-1);
	animDicho1(identifiant, visuA.ide);

}

function animDicho1(identifiant, ide) {
	let delai = 400;
	var visuA = document.getElementById(identifiant);
	if (visuA.pause) {
		setTimeout(function() {animDicho1(identifiant, ide);}, delai*visuA.vit);
	} else if (visuA.ide == ide) {
		if (visuA.etape == 1) {
			supRaisons(visuA);
			visuA.c = Math.floor((visuA.gauche+visuA.droite)/2);
			visuA.etape = 2;
			delai = 200;
		} else if (visuA.etape == 2) { // Gestion affichage couleur index c
			afficherCentre1(visuA);
			visuA.etape = 3;
			delai = 200;
		} else if (visuA.etape == 3) { // Gestion affichage couleur valeur et raisons c
			afficherCentre2(visuA);
			visuA.etape = 4;
			delai = 200;
		} else if (visuA.etape == 4) {
			afficherTestCentre(visuA);
			visuA.etape = 5;
			delai = 400;
		} else if (visuA.etape == 5) {
			afficherElementsSup(visuA);
			if (visuA.valeurs[visuA.c] > visuA.cherche) {
				visuA.droite = visuA.c - 1;
				visuA.etape = 6;
			} else if (visuA.valeurs[visuA.c] < visuA.cherche) {
				visuA.gauche = visuA.c + 1;
				visuA.etape = 6;
			} else {
				visuA.etape = 20;
			}
			delai = 400;
		} else if (visuA.etape == 6) {
			deplacerPiliers(visuA, visuA.c);
			visuA.etape = 7;
			delai = 400;

		} else if (visuA.etape == 7) {
			supRaisons(visuA);
			delai = 400;
			if (visuA.gauche <= visuA.droite && visuA.boucle) {
				visuA.etape = 1;
			} else {
				visuA.etape = 15;
			}

		}

		if (visuA.etape < 10) {
			setTimeout(function() {animDicho1(identifiant, ide);}, delai*visuA.vit);
		}
	}
}


function animationDichoVieux(numero) {
	var visuA = document.getElementById("etape" + numero + "A");
	var visuB = document.getElementById("etape" + numero + "B");
	var visuC = document.getElementById("etape" + numero + "C");
	var visuD = document.getElementById("etape" + numero + "D");
	if (visuA.etape == 1) {
		visuA.etape = 2;
		visuA.style.display = 'block';
		visuB.style.display = 'none';
		visuC.style.display = 'none';
		visuD.style.display = 'none';
	} else if (visuA.etape == 2) {
		visuA.etape = 3;
		visuA.style.display = 'none';
		visuB.style.display = 'block';
	} else if (visuA.etape == 3) {
		visuA.etape = 4;
		visuB.style.display = 'none';
		visuC.style.display = 'block';
	} else if (visuA.etape == 4) {
		visuA.etape = 1;
		visuC.style.display = 'none';
		visuD.style.display = 'block';
	}
	setTimeout(function() {animationDicho(numero);}, 3500);
}
