var terminalContainer = document.getElementById('terminal-container'),
    term = new Terminal(),
    shellprompt = '> ';

term.open(terminalContainer);
term.fit();

term.writeln('Welcome to flocker-sourcelair project!');
term.writeln('Here is your fully functional terminal, have fun.');
term.writeln(" _____                          _           _      \r\n"+
             "/  ___|                        | |         (_)     \r\n"+
             "\\ `--.  ___  _   _ _ __ ___ ___| |     __ _ _ _ __ \r\n"+
             " `--. \\/ _ \\| | | | '__/ __/ _ \\ |    / _` | | '__|\r\n"+
             "/\\__/ / (_) | |_| | | | (_|  __/ |___| (_| | | |   \r\n"+
             "\\____/ \\___/ \\__,_|_|  \\___\\___\\_____/\\__,_|_|_|   \r\n"+
             "                                                   \r\n");



(function(){
    term.toggleFullscreen();
})();