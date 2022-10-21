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
};