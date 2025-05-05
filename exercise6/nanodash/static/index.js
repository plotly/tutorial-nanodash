document.addEventListener('DOMContentLoaded', initializeInputHandlers);

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
    console.log('Input to updateValues:', newState);
    // Some helpful pseudocode:
    // for each id in newState:
    //   * get the value of newState at that id
    //   * if the value is a plotly figure:
    //       create a new plotly figure from the value, using the id
    //     else:
    //       set the value of the input element with that id to the value

    // Some helpful javascript syntax:
    //   * To create a variable:
    //       const variable = value;
    //   * To create a for loop:
    //       for (const key in object) { ... }
    //   * To access a value in an object:
    //       const value = object[key];

    // HELPER FUNCTIONS:
    //   * isPlotlyFigure(value) - returns true if the value is a plotly figure
    //   * Plotly.newPlot(id, value) - updates the plotly figure with the given id
    //   * getInputElement(id) - returns the input element with the given id
    
    // EXERCISE 6 START
    throw new Error('The updateValues function is not implemented yet!');
    // EXERCISE 6 END
}

function sendState(id) {
    const state = getState();
    console.log('Output of getState:', state);
    const payload = {
        trigger_id: id,
        state: state
    };
    console.log('Payload to send to server:', payload);
    
    fetch('/handle-change', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .then(response => {
        console.log('Response from server:', response);
        return response.json()
    })
    .then(parseResponse)
    .then(updateValues)
    .catch(error => console.error('Error:', error));
}
