#!/usr/bin/node

$(function (){
    $.ajax({
        url: "https://swapi-api.hbtn.io/api/films/?format=json",
        success: function(result) {
            let all_data = result.results;
            $.each(all_data, function(
                
            ))
        }
    })
})
