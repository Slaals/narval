/*
	This file is part of Narval :
	an opensource and free rights static blog generator.
*/

console.log("This blog is generated with Narval, an opensource and free rights static blog generator !\nShow on Github here : https://github.com/yultivert/narval\n\nThe javascript code only suggests switching between two views of the blog, with icon in right corner (dark or light).");

let headTheme = document.getElementById('theme');


// ajout du bouton de contrôle du thème

const bt = document.createElement('div');
bt.id = 'btTheme';
bt.classList.add("btTheme");
bt.title = 'Basculer entre thème sombre et clair';

if (localStorage.getItem("theme") === null || localStorage.getItem("theme") === "dark") {
	bt.classList.add("btThemeLight");
	localStorage.setItem("theme", "dark");
	bt.dataset.theme = 'b';
} else {
	bt.classList.add("btThemeDark");
	bt.dataset.theme = 'w';
	headTheme.href = 'https://yultivert.github.io/theme/light.css';
}
document.body.appendChild(bt);


// changement du thème manuellement

bt.addEventListener('click', function () {
	if (this.dataset.theme === 'b') {
		this.classList.remove('btThemeLight');
		this.classList.add('btThemeDark');
		this.dataset.theme = 'w';
		headTheme.href = 'https://yultivert.github.io/theme/light.css';
		localStorage.setItem("theme", "light");
	} else {
		this.classList.remove('btThemeDark');
		this.classList.add('btThemeLight');
		this.dataset.theme = 'b';
		headTheme.href = 'https://yultivert.github.io/theme/dark.css';
		localStorage.setItem("theme", "dark");
	}
}, false);
