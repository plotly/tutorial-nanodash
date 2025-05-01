document.addEventListener('DOMContentLoaded', initializeInputHandlers);
document.addEventListener('DOMContentLoaded', () => sendState(''));

function getState() {
    const payload = {};
    // Some helpful pseudocode:
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
        payload[getElementId(element)] = getElementValue(element);
    };
    // EXERCISE 4 END
    return payload;
}

function updateValues(newState) {
    // Some helpful pseudocode:
    // for each key in newState:
    //   if the value is a boolean:
    //     set the value of the input element with that id to the value
    //   else if the value is a plotly figure:
    //     update the plotly figure with that id to the value
    //   else:
    //     set the value of the input element with that id to the value

    // Some helpful javascript syntax:
    // * To create a variable:
    //     * const variable = value;
    // * To create a for loop:
    //     * for (const key in object) { ... }
    // * To access a value in an object:
    //     * const value = object[key];

    // HELPER FUNCTIONS:
    // * isPlotlyFigure(value) - returns true if the value is a plotly figure
    // * Plotly.newPlot(id, value) - updates the plotly figure with the given id
    // * getInputElement(id) - returns the input element with the given id

    // EXERCISE 6 START
    for (const id in newState) {
        let value = newState[id];

        if (isPlotlyFigure(value)) {
            Plotly.newPlot(id, value);
        } else {
            const element = getInputElement(id);
            setElementValue(element, value);
        }
    }
    // EXERCISE 6 END
}

function sendState(id) {
    const state = getState();
    const payload = {
        trigger_id: id,
        state: state
    };
    
    fetch('/handle-change', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(parseResponse)
    .then(updateValues)
    .catch(error => console.error('Error:', error));
}
