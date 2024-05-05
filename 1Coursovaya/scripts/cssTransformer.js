let loadingScreen = document.querySelector('.loadingScreen')
let levels = document.querySelectorAll('.level')
let currentLvl = document.querySelector('.current')
let lvlBtn = document.querySelector(".next-btn")
let coddingField = document.querySelector(".coding")
let example = document.querySelector("#example")
let code = document.querySelector('#code');
let element = document.querySelector('#text');
let leftArrow = document.querySelector('.left-arrow');
let rightArrow = document.querySelector(".right-arrow");

function changeStyle() {
    element.style.cssText = code.value;
}

function undisable(){
    if(example.style.cssText == element.style.cssText){
        lvlBtn.removeAttribute("disabled")
    }
}

document.addEventListener('keydown', function(evt){
    if(evt.key == "Enter" && example.style.cssText != element.style.cssText){
        coddingField.classList.add('shake');
    }
    setTimeout(undisable, 500); 
    setTimeout(changeStyle, 1000);
})

function hideLoading(){
    loadingScreen.setAttribute("hidden", "hidden")
}
setTimeout(hideLoading, 6000)
leftArrow.addEventListener("click", function(){
    code.value = "";
    lvlBtn.setAttribute("disabled", "disabled")
})


rightArrow.addEventListener("click", function(){
    code.value = "";
    lvlBtn.setAttribute("disabled", "disabled")
})
lvlBtn.addEventListener("click", function(){
    levels[currentLvl.textContent-1].classList.add('level-passed')
    code.value = "";
    lvlBtn.setAttribute("disabled", "disabled")
    code.focus()
})