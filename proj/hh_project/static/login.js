"use strict";

// variables
const loginId = document.getElementById('LOGIN_ID');
const loginPw = document.getElementById('LOGIN_PW');
const loginBtn = document.getElementById('LOGIN_BTN');
const veriId = document.getElementById('VERI_ID');
const veriPw = document.getElementById('VERI_PW');

//flags
var flagId = false;
var flagPw = false;

// url replacing with url mapping
$(document).ready(function () {
    console.log('login.js called');
});
function moveToMain() {
    $.ajax({
        type: 'POST',
        url: '/login/session',
        async: false,
        data: {
            id_give: loginId.value
        },
        success: function (response) {
            window.location.reload();
        }
    })
}

// function to veryfi login info
function verify() {
    // ID 확인
    if (loginId.value.length >= 3) {
        loginId.style.backgroundColor = "#FAFAFA";
        veriId.style.color = "#0095F6";
        veriId.innerText = ' ';
        flagId = true;
    } else {
        loginId.style.backgroundColor = "#f5dad7";
        veriId.style.color = "red";
        veriId.innerText = '아이디 형식이 올바르지 않습니다.';
        flagId = false;
    }

    // PW 확인
    if (loginPw.value.length >= 5) {
        loginPw.style.backgroundColor = "#FAFAFA";
        veriPw.style.color = "#0095F6";
        veriPw.innerText = ' ';
        flagPw = true;
    } else {
        loginPw.style.backgroundColor = "#f5dad7";
        veriPw.style.color = "red";
        veriPw.innerText = 'PW 형식이 올바르지 않습니다.';
        flagPw = false;
    }
    // 확인하고 버튼 활성화
    if (flagId == true && flagPw == true) {
        loginBtn.style.backgroundColor = "#0095F6";
        loginBtn.disabled = false;
    } else {
        loginBtn.style.backgroundColor = "#8E8E8E";
        loginBtn.disabled = true;
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

                if (tmpid == loginId.value && tmppw == sha256(loginPw.value)) {
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

loginId.addEventListener('keyup', verify);
loginPw.addEventListener('keyup', verify);
loginBtn.addEventListener('click', verify_DB);