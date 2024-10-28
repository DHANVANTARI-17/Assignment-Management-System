document.querySelectorAll('.inline-btn').forEach(button => {
    button.addEventListener('click', () => {
        document.querySelector('.box-container2').classList.toggle('active');
        
    });
});
var c = document.getElementById("toggleButton");
function myFunction() {
    var x = document.getElementById("inputPassword4");
    if (x.type === "password") {
      x.type = "text";
        c.innerHTML = '<i class="fas fa-eye-slash" onclick="myFunction()"></i>';
    } else {
      x.type = "password";
      c.innerHTML = '<i class="fas fa-eye" onclick="myFunction()"></i>';
    }
  }
  
let toggleBtn = document.querySelector('#toggle-btn');
let darkMode = localStorage.getItem('dark-mode');

const enableDarkMode = () =>{
toggleBtn.classList.replace('fa-sun','fa-moon');
body.classList.add('dark');
localStorage.setItem('dark-mode','enabled')
}

const disableDarkMode = () =>{
    toggleBtn.classList.replace('fa-moon','fa-sun');
    body.classList.remove('dark');
    localStorage.setItem('dark-mode','disabled')
    }
    
if(darkMode === 'enabled')
{
    enableDarkMode();
}
toggleBtn.onclick = (e) =>{
    let darkMode = localStorage.getItem('dark-mode');
    if(darkMode === 'disabled')
    {
        enableDarkMode();
    }else{
        disableDarkMode();
    }
}

let f = document.querySelector('.tbl-container .tbl table td span i');
let b = document.querySelector(' #butn');
let ele = document.querySelectorAll('.tbl-container .tbl table td span');
ele. forEach(a =>
{
    if(a.innerText == "Completed")
    {
        b.innerHTML = '<button class="inline-btn" id="us-btn" >Show</button>'
    }
    else 
    {
        b.innerHTML = '<button class="btn" id="us-btn" >Remind</button>';
    }
    
});
function makeThemWhite () {
    var elements = document.querySelectorAll('.tbl-container i');
  
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      if(element.className=='fas fa-check')
      {  
        e.innerHTML = '<button class="inline-btn" id="us-btn" >Show</button>';
      }
      else
      {
        let e=document.querySelector('#butn');
        e.innerHTML = '<button class="btn" id="us-btn" >Remind</button>';
      }
      
    }
  }
  makeThemWhite();