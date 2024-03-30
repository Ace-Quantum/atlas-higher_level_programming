#!/usr/bin/node

$('DIV#red_header').on('click', function() {
    $('header').trigger(css('color', 'red'));
})
