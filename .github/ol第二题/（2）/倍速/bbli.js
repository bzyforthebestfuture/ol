console.log("hello bbli")
let v1 = document.getElementsByTagName("video")[0];
let v2 = document.getElementsByTagName("bwp-video")[0];
if (v1 != undefined) {
    console.log(v1.src.replace("blob:", ""))
    //window.open(v1.src.replace("blob:",""));
} else if (v2 != undefined) {
    console.log(v2)
}
//console.log(v1.src)
window.addEventListener("load", f)
function f() {
    //var sendbar=document.getElementsByClassName("bilibili-player-video-sendbar");
    //$(".bilibili-player-video-sendbar").append("<button>这是按钮</button>");
    $("#viewbox_report").append($(`<button id='diybtn' style='z-index: 13;
            height: 30px;
            width: 60px;
            min-width: 60px;
            line-height: 30px;
            text-align: center;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            border-radius: 0 2px 2px 0;
            background-color: black;
            color:white;
            padding-bottom:30px;'
            
            >倍速</button>`));


    //bilibili-player-video-popup
    document.getElementById("bilibili-player")
    document.getElementsByClassName("bilibili-player-video-popup");
    let video = document.getElementsByTagName("video")[0];
    if (video == undefined) {
        video = document.querySelector("bwp-video");
        console.log("bwp-video")
    }
    console.log(video)
    // video.addEventListener("playing",function(){
    //   console.log("视频播放中...")
    //})
    let btn = $("#diybtn")[0];
    if (btn != null) {
        btn.addEventListener("click", function () {
            console.log("按钮点击")
            let rate = prompt("请输入想要调整的数字倍率", "1")
            if (isNaN(rate)) {
                console.log("非数字进入")
                document.querySelector("bwp-video").playbackRate = 1;
            } else {
                video.playbackRate = rate;

                $("#diybtn").html("" + video.playbackRate);

            }
            console.log(video.playbackRate)

        })
    }
}