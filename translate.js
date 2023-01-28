const { translate } = require("@vitalets/google-translate-api")
const fs = require("fs")

const words = fs.readFileSync("./3000word.txt", "utf8").trim().split("\n")

let i = 0
let result_text = []
if(fs.existsSync("./3000word-th.txt")){
    result_text = fs.readFileSync("./3000word-th.txt", "utf8").trim().split("\n")
    
    i = result_text.length
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

const main = async () => {
    let word = words[i]
    const { text } = await translate(word, { to: 'th' });
    console.log({word, text})
    result_text.push(text)
    fs.writeFileSync("./3000word-th.txt", result_text.join("\n"), "utf8")
    i++
    if(i<words.length-1){
        setTimeout(main, 0)
    }
}

main()