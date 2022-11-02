"use strict";

// variables
const mpBtn = document.getElementById('MYPOST_BTN');
const bmBtn = document.getElementById('BOOKMARK_BTN');

// function activates when DOMtree is organized
$(document).ready(function() {
  // console.log('login.js called');
  showlog();
  showmp();
});

// function to print recent log
function showlog(){
  // console.log("function showlog() called");
  let post = document.querySelector("#LOG");
  while(post.firstChild){
      post.removeChild(post.firstChild);
  }

  let test =
    [
      {like_flag: '1', comment_flag: '1',
       like_user: ['sample14', 'sample2', 'sample3'],
       comment_user: ['sample1', 'sample2']
      },
      {like_flag: '1', comment_flag: '0',
       like_user: ['sample13', 'sample2', 'sample3'],
       comment_user: ['sample17']
      },
      {like_flag: '1', comment_flag: '1',
      like_user: ['sample18', 'sample2', 'sample3', 'sample4'],
      comment_user: ['sample22', 'sample3', 'sample4']
      },
      {like_flag: '0', comment_flag: '0',
      like_user: ['sample13', 'sample2', 'sample3'],
      comment_user: ['sample19']
      },
    ]
  let comments = get_user_comments();
  let likes = get_user_likes();
  to_html_comment(comments, "#LOG");
  to_html_like(likes, "#LOG");
}
// function to bring login user's post
function get_user_posts(){
  let postlist = '';
  $.ajax({
      type: 'GET',
      url: '/mypage/userpost',
      data: {},
      async: false,
      success: function(response) {
        console.log("User Post list");
        console.log(response)
        postlist = response;
      }
  });
  return postlist
}
// function to bring log of comment
function get_user_comments(){
  let commentlist = '';
  $.ajax({
      type: 'GET',
      url: '/mypage/comment',
      data: {},
      async: false,
      success: function(response) {
        console.log("Comment list");
        console.log(response)
        commentlist = response;
      }
  });
  return commentlist
}
// function to bring log of like
function get_user_likes(){
  let likelist = '';
  $.ajax({
      type: 'GET',
      url: '/mypage/like',
      data: {},
      async: false,
      success: function(response) {
        console.log("Like list");
        console.log(response)
        likelist = response;
      }
  });
  return likelist
}
// function to print commtnet log list
function to_html_comment(list, id){
  // console.log('to_html called');
  let post = document.querySelector(id);
  let rows = list;
  for (let i = 0; i<rows.length; i++){
    for(let k = 0; k < rows[i].length; k++){
      if (rows[i][k]['comments_flag']==true){
        let postwrite_pk = rows[i][k]['postwrite_pk'];
        let number = 0;
        let user = '';
        for (let j = k; j<rows[i].length; j++){
          if(postwrite_pk == rows[i][j]['postwrite_pk']){
            number = number + 1;
            rows[i][j]['comments_flag']=false;
            user = rows[i][j]['comments_id'];
          }
        }
        let tmp = '';
        tmp = `<li><a href="postpage?${postwrite_pk}">${user}님 외 ${number}명이 회원님의 게시물에 댓글을 남겼습니다.</a></li>`
        post.insertAdjacentHTML("beforeend", tmp);
      }
    }
  }
}
// function to print like log list
function to_html_like(list, id){
  // console.log('to_html called');
  let post = document.querySelector(id);
  let rows = list;
  for (let i = 0; i<rows.length; i++){
    for(let k = 0; k < rows[i].length; k++){
      if (rows[i][k]['like_flag']==true){
        let postwrite_pk = rows[i][k]['postwrite_pk'];
        let number = 0;
        let user = '';
        for (let j = k; j<rows[i].length; j++){
          if(postwrite_pk == rows[i][j]['postwrite_pk']){
            number = number + 1;
            rows[i][j]['like_flag']=false;
            user = rows[i][j]['like_id'];
          }
        }
        let tmp = '';
        tmp = `<li><a href="postpage?${postwrite_pk}">${user}님 외 ${number}명이 회원님의 게시물을 좋아합니다.</a></li>`
        post.insertAdjacentHTML("beforeend", tmp);
      }
    }
  }
}


// function to print my post
function showmp(){
  // console.log("function showmp() called");
  // btn style 변경
  mpBtn.style.borderTop = "1px solid #262626";
  mpBtn.style.color = "#262626";
  bmBtn.style.borderTop = "none";
  bmBtn.style.color = "#DBDBDB";

  // let test =
  //   [
  //     {img: 'https://hollywoodlife.com/wp-content/uploads/2013/08/macmiller.png?w=620',likes: '1'},
  //     {img: 'https://www.rollingstone.com/wp-content/uploads/2018/09/mac-miller.jpg?w=1581&h=1054&crop=1',likes: '2'},
  //     {img: 'https://cdn.vox-cdn.com/thumbor/CArdkowtUvnu7MdMSNiOCd9dbVU=/0x0:3000x2000/920x613/filters:focal(1144x362:1624x842):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/61257057/MacTinyDesk02_EslahAttar_NPR_Ringer.0.jpg',likes: '3'},
  //     {img: 'https://w.namu.la/s/f5999e0e1f85ee971731e5079ba21b9d3bd254286ed57691c672535dab1298197594696b35d7653175f49166e943f052ebb07426d789b93ea8611b7461dcdeafe1f66cba1b14e738f538ddc5dc59497be022f201a0f1d14663980612f831cdd5', likes: '4'},
  //   ]
  //
  //
  // to_html_post(test, '#WRAP_POST');

  let tmp = get_user_posts();
  to_html_post(tmp, '#WRAP_POST');
}
// function to print bookmarks
function showbm(){
  // console.log("function showbm() called");
  // btn style 변경
  bmBtn.style.borderTop = "1px solid #262626";
  bmBtn.style.color = "#262626";
  mpBtn.style.borderTop = "none";
  mpBtn.style.color = "#DBDBDB";

  // let test =
  //   [
  //     {img: 'http://image.yes24.com/momo/TopCate956/MidCate001/95500703.jpg',likes: '3'},
  //     {img: 'https://image.xportsnews.com/contents/images/upload/article/2021/1024/1635052092889091.jpg',likes: '1'},
  //     {img: 'https://image.kmib.co.kr/online_image/2018/1125/611816110012868248_1.jpg',likes: '2'},
  //     {img: 'https://scontent-ssn1-1.xx.fbcdn.net/v/t1.6435-9/107847148_2553451304872718_1540664845642208434_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=Rgfxk1aCk-sAX9FDxcm&_nc_ht=scontent-ssn1-1.xx&oh=00_AT8GrTZtxoJz51DnGO5RM_ZS3hX_GEv3anewvGl_ms1X6w&oe=6376C3CF', likes: '4'},
  //   ]
  // to_html_post(test, '#WRAP_POST');

  let tmp = get_user_bookmarks();
  to_html_post(tmp, '#WRAP_POST');
}
// function to bring login user's bookmarks
function get_user_bookmarks(){
  let bookmarks = '';
  $.ajax({
      type: 'GET',
      url: '/mypage/bookmark',
      data: {},
      async: false,
      success: function(response) {
        console.log("Bookmark list");
        console.log(response);
        bookmarks = response;
      }
  });
  return bookmarks
}
// function to print post list in html
function to_html_post(list, id){
  console.log('to_html called');
  let post = document.querySelector(id);
  while(post.firstChild){
      post.removeChild(post.firstChild);
  }
  let rows = list;
  for (let i = 0; i<rows.length; i++){
    let img = rows[i]['image'];
    let postwrite_pk = rows[i]['postwrite_pk'];
    let tmp = '';
    tmp = `<div class="post">
            <a href="postpage?${postwrite_pk}">
              <img src="${img}" alt="">
            </a>
          </div>`;
    post.innerHTML += tmp;
  }
}

// event Listeners
mpBtn.addEventListener('click', showmp);
bmBtn.addEventListener('click', showbm);
