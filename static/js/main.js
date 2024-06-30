function view(x) {
  document.getElementById('gallery' + x).style.opacity = "0.3";
  document.getElementById('btn' + x).style.display = "block";
}
function viewout(x) {
  document.getElementById('gallery' + x).style.opacity = "1";
  document.getElementById('btn' + x).style.display = "none";
}
function submit(x) {
  var stylebtn = x.style;
  stylebtn.width = "20%";
  stylebtn.border = "none";
  stylebtn.backgroundColor = "transparent";
  stylebtn.color = "#f4f4f4";
  x.innerHTML = "Submitted";
}

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {

      document.getElementById("navbar").style.top = "0";

  } else {
      document.getElementById("navbar").style.top = "-150px";
  }
  
  prevScrollpos = currentScrollPos;
}
function myFunction(x) {
  x.classList.toggle("change");
  if(document.getElementById("links").style.display == "block"){
      document.getElementById("links").style.display = "none !important";
  }else{
      document.getElementById("links").style.display = "block !important"
  }
}
function myFunctionHide(){
  document.getElementById("links").style.display = "none !important";
  document.getElementById("fa-bar").classList.toggle("change");
}
var theme = document.getElementById("checktheme");
if (theme.checked == true){
  document.getElementById("aboutus").style.setProperty('background-color','#333','important');
}
