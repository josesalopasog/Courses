let label = document.querySelector('label');
console.log(label?.innerText);

let input: HTMLInputElement | null = document.querySelector('input')
let title: HTMLTitleElement = document.querySelector('.title') as HTMLTitleElement;
let button: HTMLButtonElement = document.querySelector('button') as HTMLButtonElement;

console.log(title?.innerText);


if (button) {
    button.addEventListener('click', () => {
        let newMessage = input?.value || 'No message';
        if(label) {
            label.innerText = newMessage;
        }
    })
}