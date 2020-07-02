// ==UserScript==
// @name         Xingtingyi beautify
// @namespace    fz6m
// @version      0.1
// @description  try to take over the world!
// @author       fz6m
// @include      https://xingtingyi.com/material/detail/*
// @grant        none
// @require      https://cdn.jsdelivr.net/npm/jquery/dist/jquery.min.js
// @icon         https://cdn.jsdelivr.net/gh/fz6m/Private-web@1.2.1/image/logo/logo.png
// ==/UserScript==

(function() {
    'use strict';
    function main() {
        const style = '<div style="color:#000000;font-weight:600;">'
        const content = $('.word-content.bg-gray').html()
        let list = content.split('<br>')
        let reg = /[\u3040-\u309F\u30A0-\u30FF]+/
        list = list.map((l) => {
            if(reg.test(l) && l.indexOf('div') == -1) {
                return style + l + '</div>'
            }
            return l
        })
        $('.word-content.bg-gray').html(list.join('<br>'))
    }
    function controlPlayback() {
        // 去除原生空格事件
        document.body.onkeydown = function (event) {
            var e = window.event || event;
            if(e.keyCode == 32){
                return false;
            }
        }
        // 模拟事件
        $(document).keydown((e) => {
            if(e.keyCode == 32) {
                $('.audio-play .bar-left img:nth-child(2)').click()
            }
        })
    }
    function changeFont() {
        const style = {
            'font-size': '16px',
            'line-height': '30px',
            'font-family': 'Meiryo',
            'letter-spacing': '1px'
        }
        $('.word-content.bg-gray').css(style)
    }
    function hiddenHead() {
        $('header').css('position', 'unset')
    }
    setTimeout(function() {
        controlPlayback();
        hiddenHead();
        $('.pannel .tab').click(function(el) {
            if(el.target.innerText == '标准答案') {
                //main();
                changeFont();
            }
        })
    },500)


})();