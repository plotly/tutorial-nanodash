function getElementValue(element) {
    return element.value;
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
    getInputElements().forEach(element => {
        // Use 'input' event for text inputs and 'change' for select elements
        // (Selenium seems to not trigger 'input' events for select elements for some reason)
        if (element.tagName === 'SELECT') {
            element.addEventListener('change', () => sendState(element.id));
        }
        else {
            element.addEventListener('input', () => sendState(element.id));
        }
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