document.addEventListener('DOMContentLoaded', initializeInputHandlers);

function getState() {
    let payload = {};
    // Some helpful pseudo code:
    // for each element in the form
    //     if element is a button
    //         payload[element.id] = element.value
    // EXERCISE 4 START
    const elements = getInputElements();
    for (const element of elements) {
        payload[element.id] = getElementState(element);
    };
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
