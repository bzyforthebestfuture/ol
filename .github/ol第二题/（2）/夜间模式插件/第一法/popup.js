function darkBtnStyleInit() {
    chrome.storage.sync.get(['isDark'], function(result) {
        if (result.isDark == true) {
            $("#darkBtn").text("关闭夜间模式");
        } else {
            $("#darkBtn").text("开启夜间模式");
        }
    });
}

function settingDark() {
    if ($("#darkBtn").text() == "开启夜间模式") {
        chrome.storage.sync.set({ isDark: true }, function() {});
        $("#darkBtn").text("关闭夜间模式");
    } else {
        chrome.storage.sync.set({ isDark: false }, function() {});
        $("#darkBtn").text("开启夜间模式");
    }
}

function popupSearchInit() {
    chrome.storage.sync.get(['popupSearch'], function(result) {
        if (result.popupSearch == false) {
            $("input").attr("hidden", "hidden");
            $("#searchBtn").css("display", "none");
        }
    });
}

(function() {
    darkBtnStyleInit();
    popupSearchInit();
    $("#darkBtn").click(settingDark);
    //为主站按钮添加事件
    $("#indexPage").click(goToIndexPage);
    $("#searchBtn").click(searchWithBilibili);
    $("#setting").click(goToSettingPage);
})

function bilibiliDarkStart(easyDark) {
    $(window).scroll(function() { toDark(); });
    $(window).click(function() { toDark(); });
    $(function() { toDark(); });
    if (!easyDark) {
        $(window).mousemove(function() { toDark(); });
    }
}


function toDark() {
    let url = window.location.href;
    if (url.startsWith("https://www.bilibili.com/video/")) {
        console.log("视频播放页面dark")
        totalFontColor();
        dynamicAndUserHeader();
        videoBody();
    } else if (url.startsWith("https://www.bilibili.com/")) {
        console.log("主页dark")
        totalFontColor();
        mainHeaderDark();
        mainBodyDark();
        mainFooterDark();
    } else if (url.startsWith("https://t.bilibili.com")) {
        console.log("动态页dark")
        totalFontColor();
        dynamicAndUserHeader();
        dynamicBody();
    } else if (url.startsWith("https://space.bilibili.com")) {
        console.log("用户页面")
        totalFontColor();
        dynamicAndUserHeader();
        userBody();
    } else {
        // console.log("其他页面暂时没做,请联系作者，qq：9711813137，邮箱：971181317@qq.com")
    }
}

function itemSelect() {
    $(this).css("background", "rgb(2,157,208)");
}

function itemNotSelect() {
    $(this).css("background", "#2d2d2d");
}

function totalFontColor() {
    //总字体颜色更改
    $("body").css("color", "#ffffff");
    $("a").css("color", "#ffffff");
    $("p").css("color", "#ffffff");
    $("span").css("color", "#ffffff");
}

function mainFooterDark() {
    $(".international-footer").css("background", "#1c1c1c");
}

function mainBodyDark() {
    $("#app").css("background", "#1c1c1c");
    $("#primary-menu-itnl").css("color", "#ffffff");
    //最上面一行
    $("div.user-con.signin .mini-vip").css("background", "");
    $("div.user-con.signin .mini-favorite").css("background", "");
    $("div.user-con.signin .mini-history").css("background", "");
    //最上方广告
    $("a.name.no-link").css("color", "#ffffff");
    $(".bypb-window").css("color", "#ffffff");
    $(".bypb-window .online")
        .css("background", "#2d2d2d")
        .css("border", "1px solid #2d2d2d");

    $(".list-box").css("background", "#2d2d2d");
    $(".list-box div").css("background", "#2d2d2d");

    //排行榜弹出抽屉
    $(".popover-video-card.pvc").css("background", "#2d2d2d");

    //杂项
    $(".btn.btn-change").css("color", "#ffffff");
    $(".contact-help")
        .css("color", "#ffffff");
    let btnArr = [
        ".btn.more", ".more", ".btn.btn-change", ".change-btn", ".tl-link", "rank-number", "div.item.sortable", ".contact-help"
    ];
    btnArr.forEach((e) => {
        $(e)
            .mousemove(itemSelect)
            .mouseup(itemSelect)
            .mousedown(itemSelect)
            .mouseleave(itemNotSelect);
    });
    $(".tl-link").css("background", "#2d2d2d");
    $(".rank-number").css("background", "#2d2d2d");
    //排行榜数字
    $(".number")
        .css("background", "#2d2d2d")
        .css("color", "#ffffff");
    $(".number.on")
        .css("background", "rgb(2,157,208)")
        .css("color", "#ffffff");
}

function mainHeaderDark() {
    $(".tab-bar").css("background", "#2d2d2d");
    $(".title").css("color", "#ffffff");
    $(".video-list").css("background", "#2d2d2d");
    $(".live-list").css("background", "#2d2d2d");
    $(".article-list").css("background", "#2d2d2d");
    $(".tip-box.no-more-tip").css("background", "#2d2d2d");
    $(".history-tip").css("background", "#2d2d2d");
    $(".list-item").css('color', "#ffffff");
    $(".primary-menu-itnl li span").css("color", "#ffffff");
    $(".primary-menu-itnl li").css("border", "1px solid #1c1c1c");
    $(".international-header a").css("color", "#ffffff");
    $(".item .van-popover__reference").css("background", "#2d2d2d");
    $(".van-popover")
        .css("background", "#2d2d2d")
        .css("border", "1px solid #2d2d2d");
    $(".van-popper")
        .css("background", "#2d2d2d");
    $(".van-popper-channel")
        .css("background", "#2d2d2d");
    //主页左侧联系客服按钮
    $(".contact-help")
        .css("background", "#1c1c1c")
        .css("color", "#2d2d2d");
    $(".link-title").css("color", "#ffffff");
    $(".link-item")
        .mousemove(itemSelect)
        .mouseleave(itemNotSelect);
    $(".contact-tips.email-tips").css("background", "#000000");
    $(".contact-tips.phone-tips").css("background", "#000000");
    $(".level-intro").css("background", "#3c3c3c");
    $(".level-intro__content").css("color", "#ffffff");
    $(".history-item a").css("color", "#000000");
    $("input .nav-search-keyword").css("color", "#000000");
    $(".channel-menu-mini").css("background", "#3d3d3d");
    //消息按钮
    $("div.im-list-box")
        .css("background", "#2d2d2d")
        .children("a")
        .css("color", "#ffffff");
}

function dynamicAndUserHeader() {
    $(".fixed-bg").css("background", "#1c1c1c");
    $(".home-content").css("background", "#1c1c1c");
    //头
    $(".mini-header__content.mini-header--login").css("background", "#2d2d2d");
    mainHeaderDark();
}

function dynamicBody() {
  
    $(".content").css("background", "#2d2d2d");
    $(".bottom").css("background", "#2d2d2d");
    
    $(".live-panel").css("background", "#2d2d2d");
    $(".up-name.line-clamp-1").css("color", "#ffffff");
    $(".live-name.line-clamp-2").css("color", "#ffffff");
    
    $(".userinfo-content").css("background", "#2d2d2d");
    
    $(".section-block").css("background", "#2d2d2d");
    $(".publish-panel").css("background", "#2d2d2d");
    $(".core-style")
        .css("background", "#2d2d2d")
        .css("border", "1px solid #ffffff")
        .css("color", "#ffffff");
    
    $(".notice-panel").css("background", "#2d2d2d");
    
    $(".new-topic-panel").css("background", "#2d2d2d");
    $(".title.tc-black").css("color", "#ffffff");
    
    $(".most-viewed-panel")
        .css("background", "#2d2d2d")
        .css("color", "#ffffff");
    
    $(".card")
        .css("background", "#2d2d2d");
    $(".card dir").css("background", "#2d2d2d");
    $(".live-container").css("background", "#2d2d2d");
    $(".video-wrap").css("background", "#2d2d2d");
    $(".post-content.repost").css("background", "#3d3d3d");
    $(".post-content.repost .content").css("background", "#3d3d3d");
    $(".post-content.repost .video-wrap").css("background", "#3d3d3d");
    $(".post-content.repost .video-wrap .text-area").css("background", "#3d3d3d");
    $(".shop-list").css("background", "#2d2d2d");
    $(".article-container").css("background", "#2d2d2d");
    $(".post-content.repost .text-area").css("background", "#3d3d3d");
    $(".music-container.bg-white.pointer.t-left")
        .css("background", "#2d2d2d")
        .css("color", "#ffffff");
    
    $(".bangumi-container.can-hover").css("background", "#2d2d2d");
    $(".text-content.ff-yahei.tc-black.fs-14.ls-0.line-clamp-1").css("color", "#ffffff");
    
    $("p .message").css("color", "#9b7652");

    
    $(".bb-comment").css("background", "#2d2d2d");
}

function userBody() {
    $("html").css("background", "#1c1c1c");
    $("#app").css("background", "#1c1c1c");
    
    $(".h").css("background", "#1c1c1c");
    
    $("#navigator").css("background", "#1c1c1c").css("box-shadow", "0 0 0 1px #2d2d2d");
    $(".n-inner.clearfix").css("background", "#2d2d2d").css("box-shadow", "0 0 0 1px #2d2d2d");
    $(".wrapper").css("border-color", "#1c1c1c");
    $("h3").css("color", "#ffffff");
    $("span.count").css("color", "rgb(2,157,208)");

    $(".s-space").css("background", "#1c1c1c");
    $(".col-1").css("background", "#2d2d2d")
        .css("border", "1px solid #1c1c1c");
    $(".col-2").children()
        .css("background", "#2d2d2d")
        .css("border-color", "#1c1c1c");
    $(".row.user-auth.no-auth").css("background", "#2d2d2d");
    $(".section")
        .css("background", "#2d2d2d")
        .css("border-color", "#1c1c1c");
    $("textarea.be-textarea_inner")
        .css("background", "#2d2d2d")
        .css("border-color", "#ffffff");
    
    $(".card")
        .css("background", "#2d2d2d")
        .css("border-color", "#2d2d2d");
    $(".card dir").css("background", "#2d2d2d");
    $(".live-container").css("background", "#2d2d2d");
    $(".video-wrap").css("background", "#2d2d2d");
    $(".post-content.repost").css("background", "#3d3d3d");
    $(".post-content.repost .content").css("background", "#3d3d3d");
    $(".post-content.repost .video-wrap").css("background", "#3d3d3d");
    $(".post-content.repost .video-wrap .text-area").css("background", "#3d3d3d");
    $(".shop-list").css("background", "#2d2d2d");
    $(".article-container").css("background", "#2d2d2d");
    $(".post-content.repost .text-area").css("background", "#3d3d3d");
    $(".music-container.bg-white.pointer.t-left")
        .css("background", "#2d2d2d")
        .css("color", "#ffffff");
    
    $(".bangumi-container.can-hover").css("background", "#2d2d2d");
    $(".text-content.ff-yahei.tc-black.fs-14.ls-0.line-clamp-1").css("color", "#ffffff");
   
    $(".col-full.clearfix").css("background", "#2d2d2d").css("box-shadow", "0 0 0 1px #2d2d2d");
    $(".contribution-sidenav").css("border-color", "#2d2d2d");
    $(".main-content").css("border-color", "#2d2d2d");
    $("#submit-video-type-filter").css("background", "#3c3c3c");
    
    $(".col-full").css("background", "#2d2d2d").css("box-shadow", "0 0 0 1px #2d2d2d").css("border-color", "#2d2d2d");
    $(".channel-option.no-channel").css("background", "#2d2d2d");
    
    $(".small-item").css("border-color", "#2d2d2d");
    $(".be-pager li").css("background", "#2d2d2d");
    
    $(".pgc-item-title").css("color", "#ffffff");
    $(".pgc-item-desc").css("color", "#ffffff");
    $(".bangumi-pagelistbox.clearfix a").css("background", "#2d2d2d");
    
    $("#setting-new-tag-btn").css("background", "#2d2d2d");
    $(".setting-tag-list a").css("background", "#2d2d2d");
    $("input#setting-new-tag").css("background", "#2d2d2d").css("color", "#ffffff");
    
    $(".elec-status-bg-grey").css("background", "#2d2d2d");
}

function videoBody() {
    $("#app").css("background", "#1c1c1c");

    
    $(".btn-panel").children().first().css("background", "#fb7299").css("color", "#ffffff");
    $(".btn-panel").children().last().css("background", "#00b5e5").css("color", "#ffffff");

    
    $(".bui-collapse-header").css("background-color", "#2d2d2d");
    $(".player-auxiliary-danmaku-function").css("background", "#2d2d2d")
        .children().css("background", "#2d2d2d").css("color", "#ffffff");
    $(".player-auxiliary-danmaku-warp li,ul").css("background", "#2d2d2d");
    $(".player-auxiliary-danmaku-btn-history,.player-auxiliary-danmaku-btn-footer").css("background", "#2d2d2d").css("color", "#ffffff");
    $(".player-auxiliary-area relative").css("background", "#2d2d2d");

    
    $(".tag-area li").css("background", "#2d2d2d");

    
    $(".bb-comment").css("background", "#1c1c1c");
    $(".comment-send-lite ").css("background", "#2d2d2d")}

    function aj() {
        'use strict';
        let style = document.createElement("style");
        style.type = "text/css";
        style.id = "COLORSTYLE"
        style.appendChild(document.createTextNode("*:not(a){background-color:#333!important;color:#ccc!important;}img{z-index:999!important;}"));
        var head = document.getElementsByTagName("head")[0];
        let COLORFLAG = false;
        let COLORFLAGHTML = `<div id="COLORDIVCHANGEBTN" style="cursor: pointer;position: fixed;top: 0;right: 0;z-index: 99999999;font-weight: 600;font-size: 12px;background: yellow;user-select: none;">反转</div>`;
        let COLORDIV = document.createElement('div');
        COLORDIV.innerHTML = COLORFLAGHTML;
        document.body.appendChild(COLORDIV)
        document.addEventListener('click', function (e) {
            if (e.target && e.target.id == 'COLORDIVCHANGEBTN') {
                COLORFLAG = !COLORFLAG;
                if (COLORFLAG) {
                    head.appendChild(style);
                } else {
                    head.removeChild(style);
                }
            }
        }, false)
    }