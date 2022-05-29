let summBtn = document.getElementById('summbtn')
let textSum = document.getElementById("textsum")
let textSumRes = document.getElementById("textsumres")
let copyBtn = document.getElementById("copybtn")


async function getSummary(textToBeSummarized) {
    const response = await fetch('/summ', {

        // Declare what type of data we're sending
        headers: {
            'Content-Type': 'application/json'
        },

        // Specify the method
        method: 'POST',

        // A JSON payload
        body: JSON.stringify(textToBeSummarized)
    })
    const summ = await response.json()
    return summ
}

function summarizeText(textToBeSummarized) {
    getSummary(textToBeSummarized).then(summ => {
        textSumRes.value = summ
    })
}

function copyToClipBoard() {
    let summText = textSumRes.value
    navigator.clipboard.writeText(summText)
}
if (summBtn != null) {
    summBtn.addEventListener('click', function () {
        let textToBeSummarized = textSum.value
        textSum.value = " "
        // here goes call to Google Translate to translate this as
        // textToBeSummarized = translate(textToBeSummarized)
        summarizeText(textToBeSummarized)
    })
}
if (copyBtn != null)
    copyBtn.addEventListener("click", copyToClipBoard)