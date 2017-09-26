function tableCreate(){
    var body = document.body,
        tbl  = document.createElement('table');
    tbl.style.width  = '500px';
    tbl.style.height  = '500px';
    tbl.style.border = '1px solid black';

    for(var i = 0; i < 5; i++){
        var tr = tbl.insertRow();
        for(var j = 0; j < 5; j++){
            if(i == 4 && j == 4){
            		var td = tr.insertCell();
                
                
                var tabl  = document.createElement('table');
    tabl.style.width  = '100px';
    tabl.style.height  = '100px';
    tabl.style.border = '1px solid black';

    for(var k = 0; k < 3; k++){
        var intr = tabl.insertRow();
        for(var l = 0; l < 3; l++){
            if(k == 2 && l == 2){
            		var intd = intr.insertCell();
                intd.appendChild(document.createTextNode('a'));
                //intd.style.border = '1px solid black';
                intd.id='intd'+(k+1)+(l+1);
                break;
            } else {
                var intd = intr.insertCell();
                intd.appendChild(document.createTextNode('a'));
                //intd.style.border = '1px solid black';
                intd.id='intd'+(k+1)+(l+1);
            }
        }
    }
                
                
                td.appendChild(tabl);
                td.style.border = '1px solid black';
                td.id='td'+(i+1)+(j+1);
                break;
            } else {
                var td = tr.insertCell();
                
                
                //var body = document.body,
        var tabl  = document.createElement('table');
    tabl.style.width  = '100px';
    tabl.style.height  = '100px';
    tabl.style.border = '1px solid black';

    for(var k = 0; k < 3; k++){
        var intr = tabl.insertRow();
        for(var l = 0; l < 3; l++){
            if(k == 2 && l == 2){
            		var intd = intr.insertCell();
                intd.appendChild(document.createTextNode('a'));
                //intd.style.border = '1px solid black';
                intd.id='intd'+(k+1)+(l+1);
                break;
            } else {
                var intd = intr.insertCell();
                intd.appendChild(document.createTextNode('a'));
                //intd.style.border = '1px solid black';
                intd.id='intd'+(k+1)+(l+1);
            }
        }
    }
                
                
                td.appendChild(tabl);
                td.style.border = '1px solid black';
                td.id='td'+(i+1)+(j+1);
            }
        }
    }
    return tbl;
}