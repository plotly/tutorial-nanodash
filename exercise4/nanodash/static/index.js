function isButton(element) {
    return element.tagName === 'BUTTON';
}

function isCheckbox(element) {
    return element.type === 'checkbox';
}

function isDropdown(element) {
    return element.tagName === 'SELECT';
}

function isRadio(element) {
    return element.type === 'radio';
}

function getInputState(element) {
    if (isRadio(element)) {
        const checkedRadio = document.querySelector(`input[id='${element.id}']:checked`);
        return checkedRadio ? checkedRadio.value : null;
    } else if (isCheckbox(element)) {
        return element.checked;
    } else {
        return element.value;
    }
}

function getElementByTagName(tagName) {
    return document.querySelectorAll(tagName);
}

function getInputElement(id) {
    return document.querySelector(`input[id='${id}']`);
}

function initializeButtonHandlers() {
    document.querySelectorAll('input, select, button').forEach(element => {
        if (isCheckbox(element) || isRadio(element)) {
            element.addEventListener('change', () => sendState(element.id));
        } else if (isButton(element) || isDropdown(element)) {
            element.addEventListener('click', () => sendState(element.id));
        } else {
            element.addEventListener('input', () => sendState(element.id));
        }
    });
}

document.addEventListener('DOMContentLoaded', initializeButtonHandlers);

function getState() {
    let payload = {};
    // EXERCISE 4 START
    
    // EXERCISE 4 END
    return payload;
}

function sendState(id) {
    let state = getState();
    let payload = {
        trigger_id: id,
        state: state
    };
    
    fetch('/handle-change', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .catch(error => console.error('Error:', error));
}
