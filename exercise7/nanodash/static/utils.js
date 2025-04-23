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

function getElementValue(element) {
    if (isRadio(element)) {
        const checkedRadio = document.querySelector(`input[id='${element.id}']:checked`);
        return checkedRadio ? checkedRadio.value : null;
    } else if (isCheckbox(element)) {
        return element.checked;
    } else {
        return element.value;
    }
}

function getElementId(element) {
    return element.id;
}

function getInputElements() {
    return document.querySelectorAll('input, select');
}

function getInputElement(id) {
    return document.querySelector(`input[id='${id}']`);
}

function initializeInputHandlers() {
    document.querySelectorAll('input, select').forEach(element => {
        element.addEventListener('input', () => sendState(element.id));
    });
}

function parseResponse(data) {
    for (const key in data) {
        const value = data[key];
        // Deserialize json
        try {
            data[key] = JSON.parse(value);
        } catch (e) {}
    }
    return data;
}

function isPlotlyFigure(value) {
    return value && value.data && value.layout;
}

function setElementValue(element, value) {
    if (element) {
        element.value = value;
    }
}