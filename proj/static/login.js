"use strict";

// variables
const LOGIN_ID = document.getElementById('login_id');
const LOGIN_PW = document.getElementById('login_pw');
const LOGIN_BTN = document.getElementById('login_btn');
const VERI_ID = document.getElementById('veri_id');
const VERI_PW = document.getElementById('veri_pw');

//flags

var flagID = false;
var flagPW = false;

// url replacing with url mapping
$(document).ready(function () {
    console.log('login.js called');
});

function moveToMain() {
    $.ajax({
        type: 'POST',
        url: '/login/main',
        async: false,
        data: {
            id_give: LOGIN_ID.value
        },
        success: function (response) {
            window.location.reload();
        }
    })
}

// function to veryfi login info
function verify() {
    // ID format verification
    if (LOGIN_ID.value.length > 0 && LOGIN_ID.value.indexOf("@") !== -1) {
        LOGIN_ID.style.backgroundColor = "#FAFAFA";
        VERI_ID.style.color = "#0095F6";
        VERI_ID.innerText = ' ';
        flagID = true;
    } else {
        LOGIN_ID.style.backgroundColor = "#f5dad7";
        VERI_ID.style.color = "red";
        VERI_ID.innerText = '아이디 형식이 올바르지 않습니다.';
        flagID = false;
    }

    // PW format verification
    if (LOGIN_PW.value.length >= 5) {
        LOGIN_PW.style.backgroundColor = "#FAFAFA";
        VERI_PW.style.color = "#0095F6";
        VERI_PW.innerText = ' ';
        flagPW = true;
    } else {
        LOGIN_PW.style.backgroundColor = "#f5dad7";
        VERI_PW.style.color = "red";
        VERI_PW.innerText = 'PW 형식이 올바르지 않습니다.';
        flagPW = false;
    }
    // verify all conditions and activate button
    if (flagID == true && flagPW == true) {
        LOGIN_BTN.style.backgroundColor = "#0095F6";
        LOGIN_BTN.disabled = false;
    } else {
        LOGIN_BTN.style.backgroundColor = "#8E8E8E";
        LOGIN_BTN.disabled = true;
    }

}

function verify_DB() {
    $.ajax({
        type: 'GET',
        url: '/login',
        data: {},
        success: function (response) {
            let rows = response['user'];
            let flag = false;
            for (let i = 0; i < rows.length; i++) {
                let tmpid = rows[i]['ID'];
                let tmppw = rows[i]['PW'];

                if (tmpid == LOGIN_ID.value && tmppw == sha256(LOGIN_PW.value)) {
                    moveToMain();
                    flag = true;
                }
            }
            if (flag == false) {
                alert('일치하는 계정 정보가 존재하지 않습니다.');
            }
        }
    })
}

LOGIN_ID.addEventListener('keyup', verify);
LOGIN_PW.addEventListener('keyup', verify);
LOGIN_BTN.addEventListener('click', verify_DB);