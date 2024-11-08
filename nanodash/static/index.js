$.ajaxSetup({
    headers: {
        'Content-Type': 'application/json',
    }
});

$(document).ready(function(){
    // Record and send the state when inputs change
    $('input, select, button').each(function(i, obj) {
        if(obj.type==='checkbox' || obj.type==='radio'){
            $(obj).change(function(){
                sendState(obj.name);
            });
        } else if (obj.tagName === 'BUTTON') {
            obj.onclick = function(){
                sendState(obj.name);
            };
        } else {
            obj.oninput = function(){
                sendState(obj.name);
            };
        }
    });
});

function getState() {
    var payload = {};
    $('input').each(function(i, el) {
        if (el.type==='radio') {
            var value = $('input[name='+el.name+']:checked').val();
            if(typeof value === 'undefined'){
                value = null;
            }
            payload[el.name] = value;
        } else if (el.type==='checkbox') {
            payload[el.name] = $(el).is(':checked');
        } else {
            payload[el.name] = el.value;
        }
    });
    $('select').each(function(i, el) {
        payload[el.name] = el.value;
    });
    return payload;
}

function sendState(name) {
    var state = getState();
    var payload = {
        triggered: name,
        state: state
    }
    $.post('/state', JSON.stringify(payload), function(data) {
        for (var key in data) {
            var value = data[key];
            if(typeof value === 'boolean') {
                $('input[name="'+key+'"]').prop('checked', value);
            // If the value is an object, it's a graph
            } else if (typeof value === 'object') {
                Plotly.newPlot(key, value.data, value.layout, value.config);
            } else {
                $('input[name="'+key+'"]').val(value);
            }
        }
    });
}
