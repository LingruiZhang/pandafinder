//JavaScript - make a overall rate stars light
const first = document.getElementById("firstStar");
const second = document.getElementById("secondStar");
const third = document.getElementById("thirdStar");
const fourth = document.getElementById("fourthStar");
const fifth = document.getElementById("fifthStar");

let rate = document.getElementById("overallRate");
if (Math.floor(parseInt(rate.innerHTML)) == 1){
    first.classList.add("checked")
}
else if (Math.floor(parseInt(rate.innerHTML)) == 2){
    first.classList.add("checked")
    second.classList.add("checked")
}
else if (Math.floor(parseInt(rate.innerHTML)) == 3){
    first.classList.add("checked")
    second.classList.add("checked")
    third.classList.add("checked")
}
else if (Math.floor(parseInt(rate.innerHTML)) == 4){
    first.classList.add("checked")
    second.classList.add("checked")
    third.classList.add("checked")
    fourth.classList.add("checked")
}
else if (Math.floor(parseInt(rate.innerHTML)) == 5){
    first.classList.add("checked")
    second.classList.add("checked")
    third.classList.add("checked")
    fourth.classList.add("checked")
    fifth.classList.add("checked")
}

//JavaScript - make comment session stars light
const elements = document.querySelectorAll(".stars");
for(let i = 0; i<elements.length;i++){
    rate = document.getElementsByClassName("rate")[i].innerHTML;
    for(let j = 0; j<parseInt(rate); j++){
        elements[i].getElementsByClassName("fa fa-star fa-1x")[j].classList.add("checked")
    }
}

//JavaScript - make comment submit stars light
const stars = document.querySelectorAll(".starRate");
console.log(stars)
for(let i = 0; i<stars.length;i++){
    label = document.getElementsByClassName("label")[i].innerHTML;
    for(let j = 0; j<parseInt(label); j++){
        stars[i].getElementsByClassName("fa fa-star c")[j].classList.add("checked")
    }
}

//JQuery - change the menu size when you click
$('#menu').click(function(){
    $(this).toggleClass('min');
    $(this).toggleClass('max');
});

//JQuery - copy the current URL
function copy_r_link(element) {
  var $input = $("<input>");
  $("body").append($temp);
  $input.val($(element).text()).select();
  document.execCommand("copy");
  $input.remove();
}
