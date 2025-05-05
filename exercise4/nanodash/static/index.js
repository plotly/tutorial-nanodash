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
    throw new Error('The getState function is not implemented yet!');
    // EXERCISE 4 END
    return payload;
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
    .catch(error => console.error('Error:', error));
}
