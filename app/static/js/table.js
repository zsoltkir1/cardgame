function tableCreate() {
    var body = document.body,
        first = document.getElementById('first'); //.appendChild(element);
    tbl = document.createElement('table');
    tbl.style.width = '500px';
    tbl.style.height = '500px';
    tbl.style.border = '1px solid black';

    for (var i = 0; i < 5; i++) {
        var tr = tbl.insertRow();
        for (var j = 0; j < 5; j++) {
            if (i == 4 && j == 4) {
                var td = tr.insertCell();


                var tabl = document.createElement('table');
                tabl.id = 'tabl' + (i+1) + (j+1);
                let x = i;
                let y = j;
                tabl.onclick = function() {
                    putCard(x,y);
                }
                tabl.style.width = '100px';
                tabl.style.height = '100px';
                tabl.style.border = '1px solid black';
                //tabl.onclick = function (){asd(i);}

                for (var k = 0; k < 3; k++) {
                    var intr = tabl.insertRow();
                    for (var l = 0; l < 3; l++) {
                        if (k == 2 && l == 2) {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (i + 1) + (j + 1) + (k + 1) + (l + 1);
                            intd.className += 'classintd' + (k + 1) + (l + 1);
                            break;
                        } else {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (i + 1) + (j + 1) + (k + 1) + (l + 1);
                            intd.className += 'classintd' + (k + 1) + (l + 1);
                        }
                    }
                }


                td.appendChild(tabl);
                td.style.border = '1px solid black';
                td.id = 'td' + (i + 1) + (j + 1);
                break;
            } else {
                var td = tr.insertCell();


                //var body = document.body,
                var tabl = document.createElement('table');
                tabl.id = 'tabl' + (i+1) + (j+1);
                let x = i;
                let y = j;
                tabl.onclick = function() {
                    putCard(x,y);
                }
                tabl.style.width = '100px';
                tabl.style.height = '100px';
                tabl.style.border = '1px solid black';
                //tabl.onclick = function (){asd(i,j);}

                for (var k = 0; k < 3; k++) {
                    var intr = tabl.insertRow();
                    for (var l = 0; l < 3; l++) {
                        if (k == 2 && l == 2) {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (i + 1) + (j + 1) + (k + 1) + (l + 1);
                            intd.className += 'classintd' + (k + 1) + (l + 1);
                            break;
                        } else {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (i + 1) + (j + 1) + (k + 1) + (l + 1);
                            intd.className += 'classintd' + (k + 1) + (l + 1);
                        }
                    }
                }


                td.appendChild(tabl);
                td.style.border = '1px solid black';
                td.id = 'td' + (i + 1) + (j + 1);
            }
        }
    }
    return first.appendChild(tbl);
}

function tableCreateForAvailableCards() {
    var body = document.body,
        availableCards = document.getElementById('availableCards'); //.appendChild(element);
    tbl = document.createElement('table');
    tbl.style.width = '400px';
    tbl.style.height = '100px';
    tbl.style.border = '1px solid black';

    for (var i = 0; i < 1; i++) {
        var tr = tbl.insertRow();
        for (var j = 0; j < 4; j++) {
            if (i == 4 && j == 4) {
                var td = tr.insertCell();


                var tabl = document.createElement('table');
                tabl.id = 'tabl' + (j+1);
                let y = j;
                tabl.onclick = function() {
                    chooseCard(y);
                }
                tabl.style.width = '100px';
                tabl.style.height = '100px';
                tabl.style.border = '1px solid black';

                for (var k = 0; k < 3; k++) {
                    var intr = tabl.insertRow();
                    for (var l = 0; l < 3; l++) {
                        if (k == 2 && l == 2) {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (j + 1) +(k + 1)+ (l + 1);
                            intd.className += 'classintd' +(k + 1)+ (l + 1);



                            break;
                        } else {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (j + 1) +(k + 1)+ (l + 1);
                            intd.className += 'classintd' +(k + 1)+ (l + 1);
                        }
                    }
                }


                td.appendChild(tabl);
                td.style.border = '1px solid black';
                td.id = 'td' + (i + 1) + (j + 1);
                break;
            } else {
                var td = tr.insertCell();


                //var body = document.body,
                var tabl = document.createElement('table');
                tabl.id = 'tabl' + (j+1);
                let y = j;
                tabl.onclick = function() {
                    chooseCard(y);
                }
                tabl.style.width = '100px';
                tabl.style.height = '100px';
                tabl.style.border = '1px solid black';

                for (var k = 0; k < 3; k++) {
                    var intr = tabl.insertRow();
                    for (var l = 0; l < 3; l++) {
                        if (k == 2 && l == 2) {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (j + 1) +(k + 1)+ (l + 1);
                            intd.className += 'classintd' +(k + 1)+ (l + 1);
                            break;
                        } else {
                            var intd = intr.insertCell();
                            intd.appendChild(document.createTextNode('a'));
                            //intd.style.border = '1px solid black';
                            intd.id = 'intd' + (j + 1) +(k + 1)+ (l + 1);
                            intd.className += 'classintd' +(k + 1)+ (l + 1);
                        }
                    }
                }


                td.appendChild(tabl);
                td.style.border = '1px solid black';
                td.id = 'td' + (i + 1) + (j + 1);
            }
        }
    }
    return availableCards.appendChild(tbl);
}