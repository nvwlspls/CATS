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


}