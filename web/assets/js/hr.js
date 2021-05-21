var capacite = 0 ; 
var items = [] ; 
var nombre_items = 0 ; 
var solution = [] ; 

async function loadFile(file) {
    let text = await (new Response(file)).text();
    var list= text.split('\n') ;
    var list = list.map(function (x) { return parseInt(x); });
    capacite =  list[1]  ; 
    nombre_items = list[0] ; 
    items = list.slice(2 , list[0]+2 ) ;
    var objets = $(".body_objets")[0] ; 
    var nb = $("#NB")[0] ; 
    var c = $("#capacite")[0] ; 
    var poids = $("#Poids")[0] ; 

    poids.innerHTML = Math.min (...items) + " < p < " + Math.max (...items) ; 
    c.innerHTML = capacite ; 
    nb.innerHTML = nombre_items ; 
    for(var i = 0 ; i <items.length ; i++) {
        var tr = document.createElement('tr') ; 
        tr.innerHTML=" <td> " +i + " </td> <td> " + items[i]+ "</td>" ; 
        objets.append (tr) ; 
    }
 
    document.getElementById("sol_bins1").innerHTML = "" ; 
    document.getElementById("time1").innerHTML ="" ; 

}


function ffdjs(){
    eel.ffd_py(capacite,items);
}

eel.expose(jsaffich); // Expose this function to Python
function jsaffich(a,t) {
    document.getElementById("sol_bins1").innerHTML = a ; 
    document.getElementById("time1").innerHTML = t + " secondes" ;
}

function heurisjs(){
    alert('hi') ; 
    eel.ffd_py(capacite,items);
    eel.ffi_py(capacite,items);
    eel.bf_py(capacite,items);
    eel.wf_py(capacite,items);
    eel.awf_py(capacite,items);
    eel.nf_py(capacite,items);

}

eel.expose(jsaffich); // Expose this function to Python
function jsaffich(a,t) {
   // document.getElementById("sol_bins1").innerHTML = a ; 
   // document.getElementById("time1").innerHTML = t + " secondes" ;

    //document.getElementById("sol_bins2").innerHTML = a ; 
    //document.getElementById("time2").innerHTML = t + " secondes" ;
}










      
     
                