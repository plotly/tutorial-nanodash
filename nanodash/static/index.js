$.ajaxSetup({
    headers: {
        'Content-Type': 'application/json',
    }
});

function isButton(element) {
    return (element.tagName === 'BUTTON');
}

function isCheckbox(element) {
    return (element.type==='checkbox');
}

function isRadio(element) {
    return (element.type==='radio');
}

function initializeButtonHandlers() {
    // Record and send the state when inputs change
    $('input, select, button').each(function(i, element) {
        if (isCheckbox(element) || isRadio(element)) {
            $(element).change(function(){
                sendState(element.id);
            });
        } else if (isButton(element)) {
            element.onclick = function(){
                sendState(element.id);
            };
        } else {
            element.oninput = function(){
                sendState(element.id);
            };
        }
    });
}

$(document).ready(initializeButtonHandlers);

function getInputState(element) {
    if (isRadio(element)) {
        var value = $('input[id='+element.id+']:checked').val();
        if(typeof value === 'undefined'){
            value = null;
        }
        return value;
    } else if (isCheckbox(element)) {
        return $(element).is(':checked');
    } else {
        return element.value;
    }
}

function getSelectState(element) {
    return element.value;
}

function getState() {
    var payload = {};
    $('input').each(function(i, element) {
        payload[element.id] = getInputState(element);
    });
    $('select').each(function(i, element) {
        payload[element.id] = getSelectState(element);
    });
    return payload;
}

function getInputElement(id) {
    return $('input[id="'+id+'"]');
}

function updateValues(newState) {
    for (var id in newState) {
        var value = newState[id];
        if (typeof value === 'boolean') {
            getInputElement(id).prop('checked', value);
        // If the value is an object, it's a graph
        // TODO: This is a hacky way to determine if the value is a graph
        } else if (typeof value === 'object') {
            Plotly.newPlot(id, value.data, value.layout, value.config);
        } else {
            getInputElement(id).val(value);
        }
    }
}

function sendState(id) {
    var state = getState();
    var payload = {
        triggered: id,
        state: state
    }
    $.post('/state', JSON.stringify(payload), updateValues);
}
