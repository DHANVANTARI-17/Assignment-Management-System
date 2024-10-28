let body = document.body;

let add= document.querySelector('.box-container');
document.querySelector('#user-btn').onclick=()=>
{
    add.classList.toggle('active');

}



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
