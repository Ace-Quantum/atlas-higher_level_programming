#!/usr/bin/node

function ReadFile (InputFile) {
  let file = window.open(InputFile);

  FileReader.readAsText(file);
}
