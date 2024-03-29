/**
 * Created by waynejessen on 2/22/15.
 */

var fillIn = function (bandNameList, bandInfoList) {

    var bandName = document.getElementById("bandName").value;

    //fill in the rest of the input fields with the band info
    var bandID = bandNameList[bandName];

    var bandInfo = bandInfoList[bandID];

    //Get values from list
    var townText = bandInfo[1];
    var stateText = bandInfo[2];
    var genreText = bandInfo[3];
    var subGenreText = bandInfo[4];

    //set the inputs to new values
    document.getElementById("bandCity").value = townText;
    document.getElementById("bandState").value = stateText;
    document.getElementById("bandGenre").value = genreText;
    document.getElementById("bandSubGenre").value = subGenreText;


};


$(document).ready(function(){

        //sets the autocomplete source for the bandName text inputs
        $(".bandName").autocomplete({
            source: idDict
        })
        var apples = 'reddit';
        var emptyBandRow =  $("#bandRow").clone();
        // console.log(emptyBandRow);

        //set the function for when an item is selected from autocomplete
        $(".bandName").autocomplete({

            select :function(event, ui){

                event.preventDefault();
                var bandName = ui.item.label;
                var bandId = ui.item.value;
                $(this).val(bandName);
                },
                //Find the sibling elements and set there values 
                //based off of the band lis
            focus :function(event, ui){
                event.preventDefault();
                $(this).val(ui.item.label);
                }
        })
        //get the bandnumber
        $('.bandRowClass').each(function(index, element){
            $(this).children().children().children('.orderNum').text(index +1)
                    })
        //add bandNumber to elements
        $('#addBandBtn').click(function(){
            $('.bandRowClass').each(function(index, element){
                $(this).children().children().children('.orderNum').text(index +1)
                })
        })
//end of (document).ready
});


var emptyBandRow =  $("#bandRow").clone();

$('#addBandBtn').click(function(){
        console.log("apples")
        emptyBandRow.clone().appendTo("#bandPanel");
        $(".bandName").autocomplete({
            source : idDict
        })
})
    

