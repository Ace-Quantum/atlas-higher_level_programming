#!/usr/bin/node

$('header').addClass('red');
$('#toggle_header').on('click', function() {
  $('header').toggleClass('green');
})
