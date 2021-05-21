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
  
}