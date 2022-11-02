"use strict";

// variables
const regiId = document.getElementById('REGI_ID');
const regiPw1 = document.getElementById('REGI_PW1');
const regiPw2 = document.getElementById('REGI_PW2');
const regiBtn = document.getElementById('REGI_BTN');
const veriId = document.getElementById('VERI_ID');
const veriPw1 = document.getElementById('VERI_PW1');
const veriPw2 = document.getElementById('VERI_PW2');

//flags
var flagID = false;
var flagPW1 = false;
var flagPW2 = false;

// html DOM status and site moving functions
$(document).ready(function () {
    console.log('register.js called');
});

function moveToLogin() {
    console.log('move to login page');
    location.replace("/");
}

// 유저정보 함수
function get_userinfo() {
    let rows = ''
    $.ajax({
        type: 'GET',
        url: '/register/get',
        async: false,
        data: {},
        success: function (response) {
            rows = response['user'];
        }
    })
    return rows;
}

var dataURL;

// 프로필이미지 base64 인코딩
function encodeImageFileAsURL(element) {

    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        dataURL = reader.result;
    }
    reader.readAsDataURL(file);
}

// 암호화 등록, 프로필이미지, 데이터 POST
function post_userinfo() {
    let user_id = regiId.value;
    let user_pw = sha256(regiPw2.value);
    let user_image = dataURL;

    $.ajax({
        type: "POST",
        url: "/register/post",
        async: false,
        data: {
            id_give: user_id,
            pw_give: user_pw,
            image_give: user_image
        },
        success: function (response) {
            alert(response["msg"])
        }
    });
}

// 회원가입 정보 확인
function verify() {
    // ID 형식 확인
    if (regiId.value.length >= 5) {
        regiId.style.backgroundColor = "#FAFAFA";
        veriId.style.color = "#0095F6";
        veriId.innerText = '사용 가능한 ID 형식입니다.';
        flagID = true;
    } else {
        regiId.style.backgroundColor = "#f5dad7";
        veriId.style.color = "red";
        veriId.innerText = '아이디 형식이 올바르지 않습니다.';
        flagID = false;
    }

    // PW 형식 확인
    if (regiPw1.value.length >= 3) {
        regiPw1.style.backgroundColor = "#FAFAFA";
        veriPw1.style.color = "#0095F6";
        veriPw1.innerText = '사용 가능한 PW입니다.';
        flagPW1 = true;
    } else {
        regiPw1.style.backgroundColor = "#f5dad7";
        veriPw1.style.color = "red";
        veriPw1.innerText = 'PW 형식이 올바르지 않습니다.';
        flagPW1 = false;
    }

    // PW 일치 확인
    if (regiPw1.value == regiPw2.value) {
        regiPw2.style.backgroundColor = "#FAFAFA";
        veriPw2.style.color = "#0095F6";
        veriPw2.innerText = '비밀번호가 일치합니다.';
        flagPW2 = true;
    } else {
        regiPw2.style.backgroundColor = "#f5dad7";
        veriPw2.style.color = "red";
        veriPw2.innerText = '비밀번호가 일치하지 않습니다';
        flagPW2 = false;
    }

    // 확인하고 버튼 활성화
    if (flagID == true && flagPW1 == true && flagPW2 == true) {
        regiBtn.style.backgroundColor = "#0095F6";
        regiBtn.disabled = false;
    } else {
        regiBtn.style.backgroundColor = "#8E8E8E";
        regiBtn.disabled = true;
    }

}

// 프로필 사진 미리보기
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('preview').src = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        document.getElementById('preview').src = "";
    }
}


function user_register() {
    let users = get_userinfo();
    for (let i = 0; i < users.length; i++) {
        let tmp_id = users[i]['ID'];
        if (tmp_id == regiId.value) {
            alert('이미 존재하는 계정입니다.');
            window.location.reload();
            return
        }
    }
    moveToLogin();
    post_userinfo();
    return
}

regiId.addEventListener('keyup', verify);
regiPw1.addEventListener('keyup', verify);
regiPw2.addEventListener('keyup', verify);
regiBtn.addEventListener('click', user_register);
