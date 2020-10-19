function main(){
    var total = 0;

    for(let i = 0; i < 10; i++){
        total = add(total, i);
    }
}

function add(a, b){
    return a + b;
}

main();