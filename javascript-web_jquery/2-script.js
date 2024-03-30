#!/usr/bin/node

$('#red_header').on('click', function() {
    $('header').trigger(css('color', 'red'));
})
