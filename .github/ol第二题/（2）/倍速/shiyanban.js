console.log("hello bbli")
let v1=document.getElementsByTagName("video")[0]; 
let v2=document.getElementsByTagName("bwp-video")[0];
if(v1!=undefined){
    console.log(v1.src.replace("blob:",""))
    //window.open(v1.src.replace("blob:",""));
}else if(v2!=undefined){
    console.log(v2)
}
//console.log(v1.src)
window.addEventListener("load",f)
function f(){
        //var sendbar=document.getElementsByClassName("bilibili-player-video-sendbar");
        //$(".bilibili-player-video-sendbar").append("<button>这是按钮</button>");
        setTimeout(function(){
        $("#viewbox_report").append("<button id='diybtn' style='z-index: 13;\
            height: 30px;\
            width: 60px;\
            min-width: 60px;\
            line-height: 30px;\
            text-align: center;\
            -webkit-box-sizing: border-box;\
            box-sizing: border-box;\
            border-radius: 0 2px 2px 0;\
            background-color: black;\
            color:white;\
            padding-bottom:30px;'\
            \
             >倍速</button>");

        
            //bilibili-player-video-popup
            document.getElementById("bilibili-player")
            document.getElementsByClassName("bilibili-player-video-popup");
            let video=document.getElementsByTagName("video")[0]; 
            if(video==undefined){
                video=document.querySelector("bwp-video");
                console.log("bwp-video")
            }
            console.log(video)
            // video.addEventListener("playing",function(){
              //   console.log("视频播放中...")
             //})
             if(btn!=null){
                btn.addEventListener("click",function(){
                    console.log("按钮点击")
                    let rate=1;
                    if(isNaN(video.playbackRate)){
                        console.log("非数字进入")
                        document.querySelector("bwp-video").playbackRate=1;
                    }else{
                        let vv=video.playbackRate;
                        if(vv>1)
                            video.playbackRate=vv;
                        else{
                            video.playbackRate=vv;
                        }
                        
                        $("#diybtn").html(""+video.playbackRate);
                    
                    }
                    console.log(video.playbackRate)
    
                })
            }
           
        },5000)   
}





































// console.log("hello bbli")
// let v1=document.getElementsByTagName("video")[0]; 
// let v2=document.getElementsByTagName("bwp-video")[0];

// if(v1!=undefined){
//     console.log(v1.src.replace("blob:",""))
//     //window.open(v1.src.replace("blob:",""));
// }else if(v2!=undefined){
//     console.log(v2)
// }
// //console.log(v1.src)
// window.addEventListener("load",f)
// function f(){
//         //var sendbar=document.getElementsByClassName("bilibili-player-video-sendbar");
//         //$(".bilibili-player-video-sendbar").append("<button>这是按钮</button>");
//         setTimeout(function(){
//             $(".rigth-btn").append("<button id='diybtn' style='z-index: 13;\
//             height: 30px;\
//             width: 60px;\
//             min-width: 60px;\
//             line-height: 30px;\
//             text-align: center;\
//             -webkit-box-sizing: border-box;\
//             box-sizing: border-box;\
//             border-radius: 0 2px 2px 0;\
//             background-color: var(--bpx-primary-color,#00a1d6);\
//             color:white;\
//             margin-left:20px;'\
//             \
//              >倍速</button>");
        
//             $(".rigth-btn").append("<button id='diybtn2' style='z-index: 13;\
//             height: 30px;\
//             width: 60px;\
//             min-width: 60px;\
//             line-height: 30px;\
//             text-align: center;\
//             -webkit-box-sizing: border-box;\
//             box-sizing: border-box;\
//             border-radius: 0 2px 2px 0;\
//             background-color: green;\
//             color:white;\
//             margin-left:20px;'\
//             \
//              >翻转</button>");
//             $(".video-info").css("height","116px");
//             //viewbox_report
//             $("#viewbox_report").append("<button id='diybtn3' style='z-index: 13;\
//             height: 30px;\
//             width: 60px;\
//             min-width: 60px;\
//             line-height: 30px;\
//             text-align: center;\
//             -webkit-box-sizing: border-box;\
//             box-sizing: border-box;\
//             border-radius: 0 2px 2px 0;\
//             background-color: orange;\
//             color:white;\
//             padding-bottom:30px;'\
//             \
//              >下载</button>");



//             //bilibili-player-video-popup
//             document.getElementById("bilibili-player")
//             document.getElementsByClassName("bilibili-player-video-popup");
//             let video=document.getElementsByTagName("video")[0]; 
//             if(video==undefined){
//                 video=document.querySelector("bwp-video");
//                 console.log("bwp-video")
//             }
//             console.log(video)
//             // video.addEventListener("playing",function(){
//               //   console.log("视频播放中...")
//              //})
//             var btn=document.getElementById("diybtn");
//             var btn2=document.getElementById("diybtn2");
//             var btn3=document.getElementById("diybtn3");
//             //console.log(btn);
//             if(btn!=null){
//                 btn.addEventListener("click",function(){
//                     console.log("按钮点击")
//                     let rate=1;
//                     if(isNaN(video.playbackRate)){
//                         console.log("非数字进入")
//                         document.querySelector("bwp-video").playbackRate=1;
//                     }else{
//                         let vv=video.playbackRate;
//                         if(vv>5)
//                             video.playbackRate=0.25;
//                         else{
//                             video.playbackRate=vv+0.25;
//                         }
                        
//                         $("#diybtn").html(""+video.playbackRate);
                    
//                     }
//                     console.log(video.playbackRate)
    
//                 })
//             }
//             if(btn2!=null){   
//                 var i=1;
//                 btn2.addEventListener("click",function(){
//                     console.log(video)
//                     video.style="transform:rotate("+(i++) * 90+"deg)";
//                     //video2.setAttribute("style","transform:rotate(90deg)");
//                     //video2.style.transform="rotate(90deg)";
//                     //video2.css("transform","rotate(90deg)");
//                 })
//             }
//             if(btn3!=null){   
//                 btn3.addEventListener("click",function(){
//                     let url=window.location.href;
//                     url=url.replace("bilibili","ibilibili");
//                     //console.log(url)
//                     window.open(url)
//                 })
//             }
//         },5000)
    
// }
