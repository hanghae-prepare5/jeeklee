"use strict";

// variables
const mpBtn = document.getElementById('MYPOST_BTN');
const bmBtn = document.getElementById('BOOKMARK_BTN');

// function activates when DOMtree is organized
$(document).ready(function() {
  console.log('login.js called');
});

// function to print recent log
function showlog(){
  console.log("function showlog() called")
}

// function to print recent log
function showmp(){
  console.log("function showmp() called")
}

// function to print bookmarks
function showbm(){
  console.log("function showbm() called")
}

// event Listeners
mpBtn.addEventListener('click', showmp);
bmBtn.addEventListener('click', showbm);
