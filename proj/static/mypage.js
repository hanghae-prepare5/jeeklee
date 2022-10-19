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
  // btn style 변경
  mpBtn.style.borderTop = "1px solid #262626";
  mpBtn.style.color = "#262626";
  bmBtn.style.borderTop = "none";
  bmBtn.style.color = "#DBDBDB";

  let test =
    [
      {img: 'https://hollywoodlife.com/wp-content/uploads/2013/08/macmiller.png?w=620',likes: '1'},
      {img: 'https://www.rollingstone.com/wp-content/uploads/2018/09/mac-miller.jpg?w=1581&h=1054&crop=1',likes: '2'},
      {img: 'https://cdn.vox-cdn.com/thumbor/CArdkowtUvnu7MdMSNiOCd9dbVU=/0x0:3000x2000/920x613/filters:focal(1144x362:1624x842):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/61257057/MacTinyDesk02_EslahAttar_NPR_Ringer.0.jpg',likes: '3'},
      {img: 'https://w.namu.la/s/f5999e0e1f85ee971731e5079ba21b9d3bd254286ed57691c672535dab1298197594696b35d7653175f49166e943f052ebb07426d789b93ea8611b7461dcdeafe1f66cba1b14e738f538ddc5dc59497be022f201a0f1d14663980612f831cdd5', likes: '4'},
    ]


  to_html(test, '#WRAP_POST');
}

// function to print bookmarks
function showbm(){
  console.log("function showbm() called");
  // btn style 변경
  bmBtn.style.borderTop = "1px solid #262626";
  bmBtn.style.color = "#262626";
  mpBtn.style.borderTop = "none";
  mpBtn.style.color = "#DBDBDB";

  let test =
    [
      {img: 'http://image.yes24.com/momo/TopCate956/MidCate001/95500703.jpg',likes: '3'},
      {img: 'https://image.xportsnews.com/contents/images/upload/article/2021/1024/1635052092889091.jpg',likes: '1'},
      {img: 'https://image.kmib.co.kr/online_image/2018/1125/611816110012868248_1.jpg',likes: '2'},
      {img: 'https://scontent-ssn1-1.xx.fbcdn.net/v/t1.6435-9/107847148_2553451304872718_1540664845642208434_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=Rgfxk1aCk-sAX9FDxcm&_nc_ht=scontent-ssn1-1.xx&oh=00_AT8GrTZtxoJz51DnGO5RM_ZS3hX_GEv3anewvGl_ms1X6w&oe=6376C3CF', likes: '4'},
    ]
  to_html(test, '#WRAP_POST');
}

// function to print list in html
function to_html(list, id){
  console.log('to_html called');
  let post = document.querySelector(id);
  while(post.firstChild){
      post.removeChild(post.firstChild);
  }
  let rows = list;
  for (let i = 0; i<rows.length; i++){
    let img = rows[i]['img'];
    console.log(img);
    let tmp = '';
    tmp = `<div class="post">
            <a href="#">
              <img src="${img}" alt="">
            </a>
          </div>`;
    post.insertAdjacentHTML("beforeend", tmp);
  }
}

// event Listeners
mpBtn.addEventListener('click', showmp);
bmBtn.addEventListener('click', showbm);
