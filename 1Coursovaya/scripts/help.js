let helpBtn = document.querySelector('.help-button')
let hideBtn = document.querySelector('.hide-theory-button')
let theoryWrapper = document.querySelector('.theory-wrapper')
let theory = document.querySelector('.theory')

let levelIndicator = document.querySelector('.level-indicator')
let levelsWrapper = document.querySelector('.levels-wrapper')


helpBtn.onclick = function(){
    theoryWrapper.classList.add('show-theory');
}

hideBtn.onclick = function(){
    theoryWrapper.classList.remove('show-theory');
}

levelIndicator.onclick = function(){
    levelsWrapper.classList.add('levels-wrapper-show')
}

document.addEventListener('mousedown', function(e){
    if(e.target.closest('.levels-wrapper-show') === null){
        levelsWrapper.classList.remove('levels-wrapper-show')
    }
});