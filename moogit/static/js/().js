/**
 * Created by waynejessen on 2/22/15.
 */


$(document).ready(function( ){


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

    };

        //when document is loaded, edit button is hidden
        $(".editKey").hide();    

        //sets the autocomplete source for the bandName text inputs
        $(".bandName").autocomplete({
            source: idDict
        });

        //set the function for when an item is selected from autocomplete
        $(".bandName").autocomplete({

            select :function(event, ui){
                event.preventDefault();
                var bandName = ui.item.label;
                var bandId = ui.item.value;
                $(this).val(bandName);
                var bandInfo = bandNames[bandId];
                console.log(bandInfo)
                console.log($(this).parent()    )
                $(this).parent().parent().find("#bandTownID").replaceWith("<p>" + bandInfo[1] + "</p>")
                $(this).parent().parent().find("#bandStateID").replaceWith("<p>"+ bandInfo[2] + "</p>")
                $(this).parent().parent().find("#bandNameID").replaceWith("<p>" + bandInfo[0] + "</p>")


                //when band is selected edit button becomes unhidden
                //.show()
                },
                //Find the sibling elements and set there values 
                //based off of the band lis
            focus :function(event, ui){
                event.preventDefault();
                $(this).val(ui.item.label);
                }
        });


        $(".bandNumberClass").each(function(index){

            var bandNumber = index + 1;
            $(this).text(bandNumber);
        })

//end of (document).ready
});

var emptyBandRow =  $("#bandRowID").clone();

$('#addBandBtn').click(function(){

        // var emptyBandRow =  $("#bandRowID").clone();

        emptyBandRow.clone().appendTo("#bandListTable");

        $(".bandName").autocomplete({
            source : idDict
        });
        // console.log(emptyBandRow);

        //set the function for when an item is selected from autocomplete
        $(".bandName").autocomplete({

            select :function(event, ui){
                event.preventDefault();
                var bandName = ui.item.label;
                var bandId = ui.item.value;
                $(this).val(bandName);
                var bandInfo = bandNames[bandId];
                console.log(bandInfo)
                $(this).parent().parent().find("#bandTownID").replaceWith("<p>" + bandInfo[1] + "</p>");
                $(this).parent().parent().find("#bandStateID").replaceWith("<p>"+ bandInfo[2] + "</p>");
                $(this).parent().parent().find("#bandNameID").replaceWith("<p>" + bandInfo[0] + "</p>");
                console.log($(this).parent())
                },
                //Find the sibling elements and set there values 
                //based off of the band lis
            focus :function(event, ui){
                event.preventDefault();
                $(this).val(ui.item.label);

                }
        });

        $(".bandNumberClass").each(function(index){

            var bandNumber = index + 1;
            $(this).text(bandNumber);
            });
});


$(".bandNumberClass").each(function(index){

    var bandNumber = index + 1;
    $(this).text(bandNumber);
    })

//do it inside a function
$(".bandNumberClass").text($(".bandTableRow").index(this))

