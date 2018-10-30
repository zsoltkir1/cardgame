function setCardParameter(cardParameterPlace,cardParameterValue) {
    document.getElementById(cardParameterPlace).innerHTML = '';
    document.getElementById(cardParameterPlace).appendChild(document.createTextNode(cardParameterValue));
}


function resetHandColor(){
    document.getElementById('tabl1').bgColor = 'white';
    document.getElementById('tabl2').bgColor = 'white';
    document.getElementById('tabl3').bgColor = 'white';
    document.getElementById('tabl4').bgColor = 'white';
}

