"use strict";

// variables
const SIGNUP_ID = document.getElementById('sign_id');
const SIGNUP_PW1 = document.getElementById('sign_pw1');
const SIGNUP_PW2 = document.getElementById('sign_pw2');
const SIGNUP_BTN = document.getElementById('sign_btn');
const VERI_ID = document.getElementById('veri_id');
const VERI_PW1 = document.getElementById('veri_pw1');
const VERI_PW2 = document.getElementById('veri_pw2');

//flags
var flagID = false;
var flagPW1 = false;
var flagPW2 = false;

// html DOM status and site moving functions
$(document).ready(function () {
    console.log('signup.js called');
});

// function moveToLogin() {         //로그인 페이지로 이동 연결시키면 됩니다
//     console.log('move to login page');
//     location.replace("/");
// }

// function to get user_info
function get_userinfo() {
    let rows = ''
    $.ajax({
        type: 'GET',
        url: '/signup/get',
        async: false,
        data: {},
        success: function (response) {
            rows = response['user'];
        }
    })
    return rows;
}

// function for password encryption and register data POST
function post_userinfo() {
    let user_id = SIGNUP_ID.value;
    let user_pw = sha256(SIGNUP_PW2.value);
    $.ajax({
        type: "POST",
        url: "/signup/post",
        async: false,
        data: {
            id_give: user_id,
            pw_give: user_pw
        },
        success: function (response) {
            alert(response["msg"])
        }
    });
}

// function to verify register info
function verify() {
    // ID format verification
    if (SIGNUP_ID.value.length > 0 && SIGNUP_ID.value.indexOf("@") !== -1) {
        SIGNUP_ID.style.backgroundColor = "#FAFAFA";
        VERI_ID.style.color = "#0095F6";
        VERI_ID.innerText = '사용 가능한 ID 형식입니다.';
        flagID = true;
    } else {
        SIGNUP_ID.style.backgroundColor = "#f5dad7";
        VERI_ID.style.color = "red";
        VERI_ID.innerText = '아이디 형식이 올바르지 않습니다.';
        flagID = false;
    }

    // PW format verification
    if (SIGNUP_PW1.value.length >= 5) {
        SIGNUP_PW1.style.backgroundColor = "#FAFAFA";
        VERI_PW1.style.color = "#0095F6";
        VERI_PW1.innerText = '사용 가능한 PW입니다.';
        flagPW1 = true;
    } else {
        SIGNUP_PW1.style.backgroundColor = "#f5dad7";
        VERI_PW1.style.color = "red";
        VERI_PW1.innerText = 'PW 형식이 올바르지 않습니다.';
        flagPW1 = false;
    }

    // PW matching
    if (SIGNUP_PW1.value == SIGNUP_PW2.value) {
        SIGNUP_PW2.style.backgroundColor = "#FAFAFA";
        VERI_PW2.style.color = "#0095F6";
        VERI_PW2.innerText = '비밀번호가 일치합니다.';
        flagPW2 = true;
    } else {
        SIGNUP_PW2.style.backgroundColor = "#f5dad7";
        VERI_PW2.style.color = "red";
        VERI_PW2.innerText = '비밀번호가 일치하지 않습니다';
        flagPW2 = false;
    }

    // verify all conditions and activate button
    if (flagID == true && flagPW1 == true && flagPW2 == true) {
        SIGNUP_BTN.style.backgroundColor = "#0095F6";
        SIGNUP_BTN.disabled = false;
    } else {
        SIGNUP_BTN.style.backgroundColor = "#8E8E8E";
        SIGNUP_BTN.disabled = true;
    }
}

function user_register() {
    let users = get_userinfo();
    for (let i = 0; i < users.length; i++) {
        let tmp_id = users[i]['ID'];
        if (tmp_id == SIGNUP_ID.value) {
            alert('이미 존재하는 계정입니다.');
            window.location.reload();
            return
        }
    }
    post_userinfo();
    moveToLogin();
    return
}

SIGNUP_ID.addEventListener('keyup', verify);
SIGNUP_PW1.addEventListener('keyup', verify);
SIGNUP_PW2.addEventListener('keyup', verify);
SIGNUP_BTN.addEventListener('click', user_register);