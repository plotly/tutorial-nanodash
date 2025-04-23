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
        if (isCheckbox(element) || isRadio(element) || isDropdown(element)) {
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
    // EXERCISE 4 START
    getElementByTagName('input, select').forEach(element => {
        payload[element.id] = getInputState(element);
    });
    // EXERCISE 4 END
    return payload;
}

function updateValues(newState) {
    // EXERCISE 6 START
    for (let id in newState) {
        let value = newState[id];
        // Deserialize json
        try {
            value = JSON.parse(value);
        } catch (e) {}

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
    // EXERCISE 6 END
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
