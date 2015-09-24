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
        displayContainerInfo(data.container_meta_data);
    }).fail(function(req, textStatus, errorThrown) {
        alert = $('#container-info');
        alert.addClass('alert-danger').removeClass('alert-info');
        alert.html('There was an error!');
    });

}

function attachToTerminal(webSocketUrl) {
    var params = '?logs=1&stream=1',
        ws = new WebSocket(webSocketUrl + params);
    term.attach(ws, true, true);
}

function displayContainerInfo(info) {
    var name = info.Node.Name,
        ip = info.Node.IP,
        alert = $('#container-info');
    
    var htmlMsg = 'Container created at node: <strong>' + name + '</strong> with IP: <strong>' + ip + '</strong>.' + '<a href="#" id="full-icon" onclick="makeFullScreen()" <i class="pull-right glyphicon glyphicon-fullscreen"></i></a>';

    alert.html(htmlMsg);
}

(function(){
    getContainer();
})();

function makeFullScreen(){
    term.toggleFullscreen();
};
