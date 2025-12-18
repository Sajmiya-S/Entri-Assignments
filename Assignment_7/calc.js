display = document.getElementById('display')
val = ''

function concatenate(v){
    val = val + v
    display.value = val
}
function calculate(){
    try{
        display.value = eval(val)
        val = display.value
    }
    catch{
        display.value = 'Error'
        val = ''
    }
    
}
function allclear(){
    display.value = ''
    val = ''
}
function deletelast(){
    display.value = display.value.slice(0,-1)
    val = display.value
}
