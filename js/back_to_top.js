let scroll_button = document.getElementById("to_top");

scroll_button.onclick = to_top
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
	if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
		scroll_button.style.display = "block";
	} else {
		scroll_button.style.display = "none";
	}
}

function to_top() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}