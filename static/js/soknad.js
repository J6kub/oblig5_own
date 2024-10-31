let ftrE = document.getElementById("ftr")
let ftr_txt_tr = document.getElementById("ftr_txt_tr")

ftrE.addEventListener("click", function (){
    if (ftrE.checked) {
        ftr_txt_tr.style.display = ""
    } else {
        ftr_txt_tr.style.display = "none"
    }
})
/*
0-5 From start
all filled ->
6-9
all filled ->
10-13
*/
function AllFilled(arr) {
    for (let tr of arr) {
        let input = tr.getElementsByTagName('input')[0];
        if (input == undefined) input = tr.getElementsByTagName('select')[0]
        if (input && input.value === '') {
            return false;
        }

    }
    return true;
}


let trs = document.getElementsByTagName('tr');
let tbl = document.getElementsByTagName('table');
let subtn = document.getElementsByClassName('subbit')[0]
set1 = [trs[0],trs[1],trs[2],trs[3],trs[4],trs[5]]
set2 = [trs[6],trs[7],trs[8],trs[9]]
set3 = [trs[10],trs[11],trs[12],trs[13],subtn] // add submit button !!!!!!!
function visiblifier() {
        if (AllFilled(set1)) {
            for (let tr of set2) {
                tr.style.opacity = "100%";
            }
        }
        if (AllFilled(set2)) {
            for (let tr of set3) {
                tr.style.opacity = "100%";
            }
        }
}

window.onload = function() {
    subtn.style.opacity = "0%";
    for (let tr of trs) {
        tr.style.opacity = "0%";
        tr.addEventListener('keydown', visiblifier)
        tr.addEventListener('click', visiblifier)

    }
    for (let tr of set1) {
        tr.style.opacity = "1";
    }
}

