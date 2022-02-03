window.onload = function() {
    document.getElementById("btn_run_1").addEventListener(
        "click", run_1
    )
    document.getElementById("btn_run_2").addEventListener(
        "click", run_2
    )
    document.getElementById("btn_run_3").addEventListener(
        "click", run_3
    )
    document.getElementById("btn_run_4").addEventListener(
        "click", run_4
    )
}



function run_1() { 
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) + parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado
    // alert('la suma de ' + number_1 + ' + ' + number_2 + ' = ' + resulatado);
}

function run_2() { 
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) - parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado

    // alert('la resta de ' + number_1 + ' - ' + number_2 + ' = ' + resulatado);
}

function run_3() { 
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) * parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado

    // alert('la multiplicacion de ' + number_1 + ' * ' + number_2 + ' = ' + resulatado);
}

function run_4() { 
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) / parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado

    // alert('la division de ' + number_1 + ' / ' + number_2 + ' = ' + resulatado);
}
