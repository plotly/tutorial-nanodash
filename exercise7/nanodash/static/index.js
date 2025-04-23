document.addEventListener('DOMContentLoaded', initializeInputHandlers);

function getState() {
    const payload = {};
    // Some helpful pseudo code:
    // for each input element in the page:
    //   set the payload at element's id to the element's value.
    
    // HELPER FUNCTIONS:
    // * getInputElements() - returns all input elements on the page
    // * getElementId(element) - returns the id of the element as a string
    // * getElementValue(element) - returns the value of the element

    // Some helpful javascript syntax:
    // * To create a variable:
    //     * const variable = value;
    // * To create a for loop:
    //     * for (const element of elements) { ... }
    // * To set a value in an object:
    //     * object[key] = value;
    // * To print to the console:
    //     * console.log('message', variable);
    //////////////////////////////////////////////////////
    // EXERCISE 4 START
    const elements = getInputElements();
    for (const element of elements) {
        payload[getElementId(element)] = getElementState(element);
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
