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
        $(".saveKey").hide();
        $(".stateEdit").hide(); 
        $(".stateSave").hide(); 

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
                $(this).parent().parent().find(".editKey").show()
                $(this).parent().parent().find(".saveKey").show()
                $(this).parent().parent().find(".stateEdit").show()
                $(this).parent().parent().find(".stateSave").show()
                $(this).parent().parent().find("#bandTownID").replaceWith("<p class='editLock'>" + bandInfo[1] + "</p>")
                $(this).parent().parent().find("#bandStateID").replaceWith("<p class='editLock'>"+ bandInfo[2] + "</p>")
                $(this).parent().parent().find("#genreID").replaceWith("<p class='editLock'>" + bandInfo[3] + "</p>")
                $(this).parent().parent().find("#bandNameID").replaceWith("<p class='editLock'>" + bandInfo[0] + "</p>")
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

        $("#datePicker").datepicker();
        $("#timePicker").timepicker(    );

//end of (document).ready
});

//emptyRow for adding later
var emptyBandRow =  $("#bandRowID").clone();

//state select for adding later
var stateSelect = $("#bandStateID")

$('#addBandBtn').click(function(){

        emptyRow = emptyBandRow.clone();
        emptyRow.find('.editKey').hide();
        emptyRow.find('.saveKey').hide();
        emptyRow.find('.stateEdit').hide();
        emptyRow.find('.stateSave').hide();

        
        emptyRow.appendTo("#bandListTable");

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

                $(this).parent().parent().find(".editKey").show()
                $(this).parent().parent().find(".saveKey").show()
                $(this).parent().parent().find(".stateEdit").show()
                $(This).parent().parent().find(".stateSave").show()
                $(this).parent().parent().find("#bandTownID").replaceWith("<p class='editLock'>" + bandInfo[1] + "</p>");
                $(this).parent().parent().find("#bandStateID").replaceWith("<p class='editLock'>"+ bandInfo[2] + "</p>");
                $(this).parent().parent().find("#genreID").replaceWith("<p class='editLock'>" + bandInfo[3] + "</p>")
                $(this).parent().parent().find("#bandNameID").replaceWith("<p class='editLock'>" + bandInfo[0] + "</p>");
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


//when editKey is clicked, alert change the related field to 
//a text field with the value that is currently inside of it

$(".editKey").click(function(){
    pValue = $(this).parent().find(".editLock").text();
    $(this).siblings(".editLock").replaceWith("<input class='ui-autocomplete-input openEdit' type='text' value='" + pValue + "'><br class='tempBR'>")
});


$(".saveKey").click(function(){
    nValue = $(this).siblings(".openEdit").val()
    $(this).siblings("br").remove()
    $(this).siblings(".openEdit").replaceWith("<p class='editLock'>" + nValue + "</p>")
});

$(".stateEdit").click(function(){
    
    $(this).parent().find(".editLock").replaceWith(stateSelect)

})


$(".stateSave").click(function(){

    pValue = $(this).parent().find("#bandStateID :selected").text()
    $(this).siblings("#bandStateID").replaceWith("<p class='editLock'>" + pValue + "</p>")

})


$(".bandNumberClass").each(function(index){

    var bandNumber = index + 1;
    $(this).text(bandNumber);
})

