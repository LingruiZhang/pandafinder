

const first = document.getElementById("firstStar");
const second = document.getElementById("secondStar");
const third = document.getElementById("thirdStar");
const fourth = document.getElementById("fourthStar");
const fifth = document.getElementById("fifthStar");

const rate = document.getElementById("overallRate");
console.log("i am here")
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
console.log("zahuishi4");


const c_first = document.getElementById("c_first");
const c_second = document.getElementById("c_second");
const c_third = document.getElementById("c_third");
const c_fourth = document.getElementById("c_fourth");
const c_fifth = document.getElementById("c_fifth");


const comment_rate = document.getElementById("commentRate").innerHTML
console.log(comment_rate)
const starList = [c_first, c_second, c_third, c_fourth, c_fifth]
for (let i = 0; i<Math.floor(parseInt(comment_rate)); i++){
    console.log(starList[i])
    starList[i].classList.add("checked")
}
