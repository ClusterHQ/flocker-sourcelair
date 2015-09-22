console.log('Add terminal related code here!');
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
term.writeln('');
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