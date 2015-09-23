var terminalContainer = document.getElementById('terminal-container'),
    term = new Terminal();

term.open(terminalContainer);
term.fit();

function getContainer() {
    var url = '/api/terminals/get_or_create/',
        data = {container_image: 'ubuntu'};

    return $.ajax({
        url: url,
        type: 'POST',
        data: data,
    }).done(function(data, textStatus, req) {
        attachToTerminal(data.attach_url);
    }).fail(function(req, textStatus, errorThrown) {
        // Notify user that we have a problem.
    });

}

function attachToTerminal(webSocketUrl) {
    var params = '?logs=1&stream=1',
        ws = new WebSocket(webSocketUrl + params);
    term.attach(ws, true, true);
}

(function(){
    getContainer();
})();
