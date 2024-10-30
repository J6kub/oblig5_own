let ftrE = document.getElementById("ftr")
let ftr_txt_tr = document.getElementById("ftr_txt_tr")

ftrE.addEventListener("click", function (){
    if (ftrE.checked) {
        ftr_txt_tr.style.display = ""
    } else {
        ftr_txt_tr.style.display = "none"
    }
})