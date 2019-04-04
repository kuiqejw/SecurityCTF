(function() {

}).call(this);

window.onload = function() {
	
  var numButtons = 150;
	
  var docFrag = document.createDocumentFragment();
  var r = Math.floor(Math.random() * numButtons);

  for (var i = 0; i < numButtons; i++) {
	
	if (i == r) {
		
		var elem = document.createElement('input');
		elem.type = 'button';
		elem.value = 'Click Me!';
		//elem.style.margin = "10px";
		elem.style.marginLeft = "10px";
		elem.style.marginTop = "10px";
		elem.style.marginBottom = "10px";
		elem.addEventListener("click", function(e) {
			document.getElementById("wait-text").style.visibility = "visible";
			setTimeout(function(){ window.location.href = "https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Teaser/error-t.jpg"; }, 15000);
		}, false);
		docFrag.appendChild(elem);
		
		var elem = document.createElement('input');
		elem.type = 'button';
		elem.style.width = "17px";
		elem.style.height = "17px";
		elem.style.marginTop = "10px";
		elem.style.marginBottom = "10px";
		elem.style.marginLeft = "1.5px";
		elem.style.marginRight = "1.5px";
		elem.addEventListener("click", function(e) {
			window.location.href = "http://127.0.0.1:5000/template-injection";
		}, false);
		//elem.style.visibility = "hidden";
		elem.style.opacity = "0";
		docFrag.appendChild(elem);
		
		var elem = document.createElement('input');
		elem.type = 'button';
		elem.value = 'Click Me!';
		//elem.style.margin = "10px";
		elem.style.marginTop = "10px";
		elem.style.marginBottom = "10px";
		elem.style.marginRight = "10px";
		elem.addEventListener("click", function(e) {
			document.getElementById("wait-text").style.visibility = "visible";
			setTimeout(function(){ window.location.href = "https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Teaser/error-t.jpg"; }, 15000);
		}, false);
		docFrag.appendChild(elem);
	}
	
	else {
		
		var elem = document.createElement('input');
		elem.type = 'button';
		elem.value = 'Click Me!';
		//elem.style.margin = "10px";
		elem.style.marginLeft = "10px";
		elem.style.marginTop = "10px";
		elem.style.marginBottom = "10px";
		elem.addEventListener("click", function(e) {
			document.getElementById("wait-text").style.visibility = "visible";
			setTimeout(function(){ window.location.href = "https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Teaser/error-t.jpg"; }, 15000);
		}, false);
		docFrag.appendChild(elem);
		
		var elem = document.createElement('input');
		elem.type = 'button';
		elem.style.width = "17px";
		elem.style.height = "17px";
		elem.style.marginTop = "10px";
		elem.style.marginBottom = "10px";
		elem.style.marginLeft = "1.5px";
		elem.style.marginRight = "1.5px";
		elem.style.visibility = "hidden";
		docFrag.appendChild(elem);
		
		var elem = document.createElement('input');
		elem.type = 'button';
		elem.value = 'Click Me!';
		//elem.style.margin = "10px";
		elem.style.marginTop = "10px";
		elem.style.marginBottom = "10px";
		elem.style.marginRight = "10px";
		elem.addEventListener("click", function(e) {
			document.getElementById("wait-text").style.visibility = "visible";
			setTimeout(function(){ window.location.href = "https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Teaser/error-t.jpg"; }, 15000);
		}, false);
		docFrag.appendChild(elem);
		
	}
  }
  document.body.appendChild(docFrag);
};