/**
 * Created by waynejessen on 2/22/15.
 */

var fillIn = function (bandName, bandList) {

    //fill in the rest of the input fields with the band info
    bandID = bandList[bandName];

    bandInfo = bandList[bandID];

    //Get values from list
    townText = bandInfo[1];
    stateText = bandInfo[2];
    genreText = bandInfo[3];
    subGenreText = bandInfo[4];

    //set the inputs to new values
    document.getElementById("bandCity").value = townText;
    document.getElementById("bandSate").value = stateText;
    document.getElementById("bandGenre").value = genreText;
    document.getElementById("bandSubGenre").value = subGenreText;


}