$(document).ready(function(){
    // Record and send the state when inputs change
    $('input, select, button').each(function(i, obj) {
        if(obj.type==='checkbox' || obj.type==='radio'){
            $(obj).change(function(){
                console.log('getState()', getState());
                sendState({}, {});
            });
        } else if (obj.tagName === 'BUTTON') {
            obj.onclick = function(){
                console.log('getState()', getState());
                sendState({}, {});
            };
        } else {
            obj.oninput = function(){
                if($(obj).hasClass('show-output')){
                    $('output[for='+obj.name+']')[0].value = obj.value;
                }
                console.log('getState()', getState());
                sendState({}, {});
            };
        }
    });
});

function getState(payload) {
    var payload = payload || {};
    $('input').each(function(i, el) {
        if (el.type==='radio') {
            var value = $('input[name='+el.name+']:checked').val();
            if(typeof value === 'undefined'){
                value = null;
            }
            payload[el.name] = value;
        } else if (el.type==='checkbox') {
            payload[el.name] = $(el).is(':checked');
        } else if (el.type==='text') {
            payload[el.name] = el.value;
        } else {
            payload[el.name] = el.value;
        }
    });
    $('select').each(function(i, el) {
        payload[el.name] = el.value;
    });
    return payload;
}

function sendState(that, payload){
    var payload = payload || {};
    payload = getState(payload);
    $.post( '/state', payload, function(data) {
        console.log('response', data);
        for (var key in data) {
            var value = data[key];
            if(typeof value === 'boolean'){
                $('input[name="'+key+'"]').prop('checked', value);
            } else {
                $('input[name="'+key+'"]').val(value);
            }
        }
    });
}
