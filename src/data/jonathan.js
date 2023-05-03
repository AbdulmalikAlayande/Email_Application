let arr = [1, 2, 3];
console.log(arr.slice(2, 1))


function countBs(string){
    let count = 0;
    for (let i of string){
        if (i === "B")
            count++;
    }
    return count
}

console.log(countBs("BallingBenBadGraFabConfabBubble"));

function countBCharacters(string, character){
    let count = 0;
    for (let i of string){
        if (i === character)
            count++;
    }
    return count
}
console.log(countBCharacters("BallingBenBadGraFabConfabBubble", "a"));
