#!/usr/bin/node

$('#toggle_header').on('click', function() {
    $('header').hasClass('red').toggleClass('green')
    $('header').hasClass('green').toggleClass('red')
})
