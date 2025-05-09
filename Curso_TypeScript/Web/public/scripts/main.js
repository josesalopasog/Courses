"use strict";
let label = document.querySelector('label');
console.log(label === null || label === void 0 ? void 0 : label.innerText);
let input = document.querySelector('input');
let title = document.querySelector('.title');
let button = document.querySelector('button');
console.log(title === null || title === void 0 ? void 0 : title.innerText);
if (button) {
    button.addEventListener('click', () => {
        let newMessage = (input === null || input === void 0 ? void 0 : input.value) || 'No message';
        if (label) {
            label.innerText = newMessage;
        }
    });
}
