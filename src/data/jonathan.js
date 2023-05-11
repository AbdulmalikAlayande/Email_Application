// let arr = [1, 2, 3];
// console.log(arr.slice(2, 1))
//
//
// function countBs(string){
//     let count = 0;
//     for (let i of string){
//         if (i === "B")
//             count++;
//     }
//     return count
// }
//
// console.log(countBs("BallingBenBadGraFabConfabBubble"));
//
// function countBCharacters(string, character){
//     let count = 0;
//     for (let i of string){
//         if (i === character)
//             count++;
//     }
//     return count
// }
String.prototype.insert = function(index, string) {
    if (index > 0)
    {
        return this.substring(0, index) + string + this.substring(index, this.length);
    }

    return string + this;
};

let splitString =function splitSentenceIntoWords(sentence){
    return sentence.split(" ")
}
function convertToJadenCase(listOfString){
    let newList = []
    for (let word of listOfString) {
        let firstCharacter = word[0]
        let sliced = word.slice(1, word.length)
         newList.push(sliced)
    }
    return newList
}
// console.log("This is: "+fret.shift())
console.log(splitString("how can mirrors be real if our eyes aren't real"));
console.log(convertToJadenCase(splitString("how can mirrors be real if our eyes aren't real")));
