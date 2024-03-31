#!/bin/usr/node

$('#add_item').on('click', function() {
  $('UL.my_list').append($('<li>Item</li>'))
})
