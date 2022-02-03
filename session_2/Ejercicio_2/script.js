
function run() {
    console.log('Estoy corriendo el metodo run')
}

function run_1() { 
    console.log('estoy corriendo la funcion run_1')
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) + parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado
    // alert('la suma de ' + number_1 + ' + ' + number_2 + ' = ' + resulatado);
}

function run_2() { 
    console.log('estoy corriendo la funcion run_1')
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) - parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado

    // alert('la resta de ' + number_1 + ' - ' + number_2 + ' = ' + resulatado);
}

function run_3() { 
    console.log('estoy corriendo la funcion run_1')
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) * parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado

    // alert('la multiplicacion de ' + number_1 + ' * ' + number_2 + ' = ' + resulatado);
}

function run_4() { 
    console.log('estoy corriendo la funcion run_1')
    // aca esta la suma 

    let number_1 = document.getElementById("number_1").value;
    let number_2 = document.getElementById("number_2").value;
    let resulatado = parseInt(number_1) / parseInt(number_2);
    document.getElementById('resultado').textContent = resulatado

    // alert('la division de ' + number_1 + ' / ' + number_2 + ' = ' + resulatado);
}
