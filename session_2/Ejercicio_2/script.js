
$(document).ready(function(){
    $("#btn_run_1").click(run_1);
    $("#btn_run_2").click(run_2);
    $("#btn_run_3").click(run_3);
    $("#btn_run_4").click(run_4);
});


function run_1() { 
    // aca esta la suma 

    let number_1 = $("#number_1")[0].value;
    let number_2 = $("#number_2")[0].value;
    let resulatado = parseInt(number_1) + parseInt(number_2);
    $('#resultado')[0].textContent = resulatado

    // alert('la suma de ' + number_1 + ' + ' + number_2 + ' = ' + resulatado);
}

function run_2() { 
    // aca esta la suma 

    let number_1 = $("#number_1")[0].value;
    let number_2 = $("#number_2")[0].value;
    let resulatado = parseInt(number_1) - parseInt(number_2);
    $('#resultado')[0].textContent = resulatado


    // alert('la resta de ' + number_1 + ' - ' + number_2 + ' = ' + resulatado);
}

function run_3() { 
    // aca esta la suma 

    let number_1 = $("#number_1")[0].value;
    let number_2 = $("#number_2")[0].value;
    let resulatado = parseInt(number_1) * parseInt(number_2);
    $('#resultado')[0].textContent = resulatado


    // alert('la multiplicacion de ' + number_1 + ' * ' + number_2 + ' = ' + resulatado);
}

function run_4() { 
    // aca esta la suma 

    let number_1 = $("#number_1")[0].value;
    let number_2 = $("#number_2")[0].value;
    let resulatado = parseInt(number_1) / parseInt(number_2);
    $('#resultado')[0].textContent = resulatado

    // alert('la division de ' + number_1 + ' / ' + number_2 + ' = ' + resulatado);
}
