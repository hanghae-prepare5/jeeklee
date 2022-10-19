"use strict";

// variables
const mpBtn = document.getElementById('MYPOST_BTN');
const bmBtn = document.getElementById('BOOKMARK_BTN');

// function activates when DOMtree is organized
$(document).ready(function() {
  console.log('login.js called');
  showmp();
});

// function to print recent log
function showlog(){
  console.log("function showlog() called");
}

// function to print recent log
function showmp(){
  console.log("function showmp() called");
  mpBtn.style.borderTop = "1px solid #262626";
  mpBtn.style.color = "#262626";
  bmBtn.style.borderTop = "none";
  bmBtn.style.color = "#DBDBDB";
}

// function to print bookmarks
function showbm(){
  console.log("function showbm() called");
  bmBtn.style.borderTop = "1px solid #262626";
  bmBtn.style.color = "#262626";
  mpBtn.style.borderTop = "none";
  mpBtn.style.color = "#DBDBDB";

}

// event Listeners
mpBtn.addEventListener('click', showmp);
bmBtn.addEventListener('click', showbm);
