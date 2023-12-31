 const dictionary = [
    "apple",
    "banana",
    "cherry",
    "grape",
    "orange",
    "strawberry",
    "watermelon",
];

document.addEventListener("DOMContentLoaded", function() {
    const searchButton = document.getElementById("searchButton");
    const spellCheckButton = document.getElementById("spellCheckButton");
    const output = document.getElementById("output");

    searchButton.addEventListener("click", function() {
        const searchWord = prompt("Enter a word to search for:");
        if (searchWord) {
            if (dictionary.includes(searchWord.toLowerCase())) {
                output.innerText = `'${searchWord}' is in the dictionary.`;
            } else {
                output.innerText = `'${searchWord}' is not in the dictionary.`;
            }
        }
    });

    spellCheckButton.addEventListener("click", function() {
        const spellCheckWord = prompt("Enter a word to spell check:");
        if (spellCheckWord) {
            if (dictionary.includes(spellCheckWord.toLowerCase())) {
                output.innerText = `'${spellCheckWord}' is spelled correctly.`;
            } else {
                output.innerText = `'${spellCheckWord}' might be misspelled.`;
            }
        }
    });
});
