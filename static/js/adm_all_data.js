console.log(detz)
for (tbl of detz) {
    document.getElementById(tbl).hidden = 'true'
}
sel = document.getElementById('selectioo')
sel.addEventListener('click',function(){
    for (tbl of detz) {
        if (tbl == sel.value) {
            document.getElementById(tbl).hidden = ''
        } else {
           document.getElementById(tbl).hidden = 'true'
        }
    }
})
window.onload = function() {
    document.getElementById(detz[0]).hidden = ''
}


