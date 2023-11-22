// var hungry = false;
// if(hungry){
//     document.write("我就去吃飯");
// }else{
//     document.write("我就不吃飯")
// }
// var score = 60;
// var rainy = true;
// if(score == 100 || !rainy){
//     document.write("我給你1000元");
// }
// else{
//     document.write("你給我100元");
// }

// function max_num(num1, num2, num3){
//     if(num1 >= num2 && num1>=num3){
//         return num1;
//     }else if (num2 >= num1 && num2 >=num3){
//         return num2;
//     }else{
//         return num3;
//     }
// }

// document.write(max_num(9,13,4)+"<br>");
// document.write(max_num(9,8,4)+"<br>");
// document.write(max_num(2,3,4)+"<br>");

// var person = {
//     name: "Alvin",
//     age: 26,
//     is_male: true,
//     print_name: function(){
//         document.write(this.name+"<br>");
//     }
// };
// person.print_name();
// document.write(person.age+"歲<br>");

// var movie = {
//     title:"<h1>刻在你心底的名字</h1><br>",
//     maker:"氧氣電影",
//     duration:114,
//     actors:[
//         {
//             name:"陳昊森",
//             age:24,
//             is_male:true
//         },
//         {
//             name:"曾敬驊",
//             age:23,
//             is_male:true
//         }
//     ]
// };

// document.write(movie.title);
// document.write(movie.actors[0].name);

// var i = 1;

// do{
//     document.write(i);
//     document.write("<br>");
//     i++;
// }while(i<=3)

// 密碼檢驗程式

// var password = 123456;
// var input;
// var entry_count = 0;
// var entry_limit = 3;
// var out_ot_limit = false;


// while(password!=input && !out_ot_limit){
//     entry_count++;
//     if(entry_count<=entry_limit){
//         input=prompt("請輸入您的密碼");
//     }
//     else{
//         out_ot_limit=true;
//     }
// }

// if(out_ot_limit){
//     alert("超出輸入次數");
// }
// else{
//     alert("登入成功");
// }

// for 迴圈

// var i = 0;
// while(i<10){
//     document.write(i);
//     document.write("<br/>");
//     i++;
// }

// var friends = ["Alvin","Mike","YoWei","Blue","阿橘"];
// for(var q = 0 ; q < friends.length ; q++){
//     document.write(friends[q]);
//     document.write("<br/>");
// }

// 製作一個問答程式

// var questions = [
//     {
//         prompt:"香蕉是什麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色",
//         answer:"c"
//     },
//     {
//         prompt:"草莓是什麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色",
//         answer:"a"
//     },
//     {
//         prompt:"1公尺等於幾公分?\n(a)10\n(b)1\n(c)100",
//         answer:"c"
//     }
// ];

// var score = 0;
// for(var i =0 ; i<=questions.length;i++){
//     var input=prompt(questions[i].prompt);
//     if(input==questions[i].answer){
//         score++;
//         alert("你答對了!");
//     }
//     else{
//         alert("你答錯了!");
//     }
// }
// alert("總共答對了"+score +"題!");

// 2維陣列、巢狀迴圈

// var number = [
//     [1,2,3],
//     [4,5,6],
//     [7,8,9],
//     [0]
// ];

// for(var i = 0; i<number.length;i++){
//     for(var j=0;j<number[i].length;j++){
//         document.write(number[i][j]);
//         document.write("<br/>");
//     }
// }

// class

// var phone1 ={
//     number:"123",
//     year:2020,
//     is_waterproof:false,
//     phone_age:function(){
//         return 2023 - this.year;
//     }
// }
// var phone2 ={
//     number:"456",
//     year:2021,
//     is_waterproof:false,
//     phone_age:function(){
//         return 2023 - this.year;
//     }
// }
// var phone3 ={
//     number:"789",
//     year:2022,
//     is_waterproof:true,
//     phone_age:function(){
//         return 2023 - this.year;
//     }
// }

// class Phone{
//     constructor(number, year, is_waterproof){
//         this.number = number;
//         this.year = year;
//         this.is_waterproof = is_waterproof;
//     }
//     phone_age(){
//         return  2023 - this.year;
//     }
// }

// var phone1 = new Phone("123", 2020, false);
// var phone2 = new Phone("456", 2021, false);
// var phone3 = new Phone("780", 2022, true);

// document.write(phone1.phone_age());
// document.write(phone2.number);
// document.write(phone3.is_waterproof);

// //如何取得html元素
// var h1 = document.getElementById("header");
// // console.log(h1);
// h1.innerText = "你好不好啊?";
// h1.style.backgroundColor = "red";
// h1.style.color = "blue";
// var link = document.getElementById("link");
// link.href = "https://amazon.com";

//even listener
// function handle_click(element){
//     // alert("叫你按就按啊?");
//     console.log(element);
//     element.innerText="按屁啊!";
//     element.style.color="red";
// }
// var btn = document.getElementById("btn");
// btn.addEventListener("click",function(){
//     // alert("叫你按就按啊?");
//     this.innerText = "按屁啊?";
//     this.style.color = "red";
// })
// var img = document.getElementById("img");
// img.addEventListener("mouseover",function(){
//     this.src = "R1.jpg";
// })

// img.addEventListener("mouseout",function(){
//     this.src = "R.jpg";
// })

//部落格
var title = document.getElementById("title");
var content = document.getElementById("content");
var btn = document.getElementById("btn");
var list = document.getElementById("list");

btn.addEventListener("click", function(){
    list.innerHTML = list.innerHTML + `
    <div class="article">
        <h2>${title.value}</h2>
        <p>${content.value}</p>
    </div>
    `;
    title.value ="";
    content.value ="";
})