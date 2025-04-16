function isButton(element) {
    return element.tagName === 'BUTTON';
}

function isCheckbox(element) {
    return element.type === 'checkbox';
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
        } else if (isButton(element)) {
            element.addEventListener('click', () => sendState(element.id));
        } else {
            element.addEventListener('input', () => sendState(element.id));
        }
    });
}

document.addEventListener('DOMContentLoaded', initializeButtonHandlers);

function getState() {
    let payload = {};
    // EXERCISE 4A START
    getElementByTagName('input').forEach(element => {
        payload[element.id] = getInputState(element);
    });
    // EXERCISE 4A END
    return payload;
}

function updateValues(newState) {
    // EXERCISE 4C START
    for (let id in newState) {
        let value = newState[id];
        // Deserialize json
        value = JSON.parse(value);

        if (typeof value === 'boolean') {
            let element = getInputElement(id);
            if (!element) continue;
            element.checked = value;
        } else if (typeof value === 'object') {
            Plotly.newPlot(id, value.data, value.layout, value.config);
        } else {
            let element = getInputElement(id);
            if (!element) continue;
            element.value = value;
        }
    }
    // EXERCISE 4C END
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
    .then(response => response.json())
    .then(updateValues)
    .catch(error => console.error('Error:', error));
}
