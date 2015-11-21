// ==UserScript==
// @name        scraper 
// @namespace   datathon
// @description get the friend graph from fbook
// @include     https://www.facebook.com/events/161836037500120/
// @version     1
// @grant       none
// ==/UserScript==

MAX_SCROLL_TIME_GOING = 60000;

var originalWindow = document.defaultView;

// create log 
var logWindow = window.open();
log = function(data) {  
  logWindow.document.writeln(data + "<br>");
};


get_people = function() {
  // get list of attending people 
  return document.getElementsByClassName("_2akq _1box");
};

originalWindow.alert("ready to start? Scroll... ");

log("All good... starting to play!");


// expand the "Attending" pane
oldClick = document.getElementsByClassName("_3enj")[1].click();


// wait 4 load, then run with results
log("Waiting for people to load...");
log("================== People: =================");


mine_all = function() {
  
  setTimeout(function() {

    // get and log all people
    data = get_people();
    
    for (var i=0; i<data.length; i+=2) {
      log(data[i].href + " : " + data[i+1].textContent);
    }
    
    log("================== /People =================");
    
   
  } , MAX_SCROLL_TIME_GOING);
 
  
};


mine_all();




