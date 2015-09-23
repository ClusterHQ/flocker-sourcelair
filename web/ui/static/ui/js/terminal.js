var terminalContainer = document.getElementById('terminal-container'),
    term = new Terminal(),
    shellprompt = '> ';

term.open(terminalContainer);
term.fit();

term.prompt = function () {
  term.write('\r\n' + shellprompt);
};

term.writeln('Welcome to flocker-sourcelair project!');
term.writeln('Here is your fully functional terminal, have fun.');
term.writeln(" _____                          _           _      \r\n"+
"/  ___|                        | |         (_)     \r\n"+
"\\ `--.  ___  _   _ _ __ ___ ___| |     __ _ _ _ __ \r\n"+
" `--. \\/ _ \\| | | | '__/ __/ _ \\ |    / _` | | '__|\r\n"+
"/\\__/ / (_) | |_| | | | (_|  __/ |___| (_| | | |   \r\n"+
"\\____/ \\___/ \\__,_|_|  \\___\\___\\_____/\\__,_|_|_|   \r\n"+
"                                                   \r\n");
term.prompt();

term.on('key', function (key, ev) {
  var printable = (!ev.altKey && !ev.altGraphKey && !ev.ctrlKey && !ev.metaKey);

  if (ev.keyCode == 13) {
    term.prompt();
  } else if (ev.keyCode == 8) {
    /*
     * Do not delete the prompt
     */
    if (term.x > 2) {
      term.write('\b \b');
    }
  } else if (printable) {
    term.write(key);
  }
});

(function(){
    term.toggleFullscreen();
})();