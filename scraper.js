// ==UserScript==
// @name        scraper 
// @namespace   datathon
// @description get the friend graph from fbook
// @include     https://www.facebook.com/events/161836037500120/
// @version     1
// @grant       none
// ==/UserScript==

//Timeout values
MAX_SCROL_TIME_FRIENDS = 30000;
MAX_SCROL_TIME_GOING = 10000;
MAX_PAGE_LOAD_TIME = 10000;
MAX_FRIEND_MINE_TIME = 60000; // at least scrol+load 

get_people = function() {
  // get list of attending people 
  return document.getElementsByClassName("_2akq _1box");
};

var originalWindow = document.defaultView;

// create log 
var logWindow = window.open();
log = function(data) {  
  logWindow.document.writeln(data + "<br>");
};
logf = function(p, f) {
  log("->Starting <" + p +  ">");
  for (var i=0; i<f.length; i++) {
    log(f[i].href);
  } 
  log("->End Person");  
};
originalWindow.alert("ready to start?");

log("All good... starting to play!");


// expand the "Attending" pane
oldClick = document.getElementsByClassName("_3enj")[1].click();

// wait 4 load, then run with results
log("Waiting for people to load...");
log("================== People: =================");


mine_all = function() {
  
  scrol = setInterval(function() {
    document.getElementsByClassName("uiScrollableAreaWrap scrollable")[3].scrollTop = 100000;
  } , 1000); 
  
  setTimeout(function() {

    // can stop scrolling now...
    clearInterval(scrol);
    
    // get and log all people
    people = [];
    data = get_people();
    for (var i=0; i<data.length; i+=2) {
      log(data[i].href);
      people.push(data[i].href);
    }
    
    log("================== /People =================");
    
    var i=0;
    fwin = mine_friends(people[i++]);
    setInterval(function() {
       if (fwin) { fwin.close(); }
       fwin = mine_friends(people[i++]);      
    }, MAX_FRIEND_MINE_TIME);
   
    
  } , MAX_SCROL_TIME_GOING);
  
};

mine_friends = function(url) {
    var newFbookWindow = window.open();
    newFbookWindow.location.href = url;    
  
    setTimeout(function() {
      // click on friends
      log("clicking friends of " + url);
      newFbookWindow.document.getElementsByClassName("_6-6")[2].click();
    
      // scroll down friends of this person 
      scrol = setInterval(function() {
        newFbookWindow.scrollByPages(1);      
      } , 500); 
      
      // save them
      setTimeout(function() {
        clearInterval(scrol);
        
        friends = newFbookWindow.document.getElementsByClassName("_5q6s _8o _8t lfloat _ohe");
        logf(url, friends);     
        
       
      }, MAX_SCROL_TIME_FRIENDS);
      
           
    }, MAX_PAGE_LOAD_TIME);
  
    return newFbookWindow;          
}

mine_all();




