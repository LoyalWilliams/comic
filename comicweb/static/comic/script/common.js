var action_size = 0;

/*登录cookie*/
function UserCookie(){
    if($.cookie("my")!=null){
        var cookie_arr =  $.cookie("my").split("|");
        m_global.userId = cookie_arr[0];
        m_global.username = URLdecode(cookie_arr[1]);
        m_global.userPhoto = "https://avatar.dmzj.com/"+cookie_arr[3].substr(0,2)+"/"+cookie_arr[3].substr(2,2)+"/"+cookie_arr[3]+".png";
        m_global.isLogin = true;

        //登录后存储订阅信息
        if(localStorage.mySubscribeDat==undefined){
            var url = '/mysubscribe';
            T.restGet(url, {}, function (data) {
                //存储
                localStorage.mySubscribeData = JSON.stringify(data);
            });
        }

    }
}

//订阅消息
function subscribeUnread(){
    var url = '/subscribeUnread';
    T.restGet(url, {}, function(data){
        if(data.unreadCount!=0 && m_global.isLogin==true){
            $("#subscribe").show();
        }else{
            $("#subscribe").hide();
        }
    })
}

//用户名转码
function URLdecode(str) {
    var ret = "";
    for(var i=0;i<str.length;i++) {
        var chr = str.charAt(i);
        if(chr == "+") {
            ret += " ";
        }else if(chr=="%") {
            var asc = str.substring(i+1,i+3);
            if(parseInt("0x"+asc)>0x7f) {
                ret += decodeURI("%"+ str.substring(i+1,i+9));
                i += 8;
            }else {
                ret += String.fromCharCode(parseInt("0x"+asc));
                i += 2;
            }
        }else {
            ret += chr;
        }
    }
    return ret;
}

/*退出登录*/
function userSubmit(){
    localStorage.removeItem("mySubscribeData");
    $.cookie("my",null,{path:"/",domain:'.dmzj.com'});
    location.href='/logout.html';
    $.cookie("ismy",null,{path:"/",domain:'.dmzj.com'});
}

//全局
var m_global={
    document_hei:200,
    userPhoto:"",//用户头像
    username:"",//用户名
    userId:"",//用户ID
    isLogin:false,//是否登录
    isHead:false,
    comicId :"",//订阅漫画Id
    Open:function(obj){
        $('#'+obj).show();
    },
    closed:function(obj){
        $('#'+obj).hide();
        $("#HotTag").hide();
        $("#hotTit").hide();
        $("#messagelist").hide();
        $("#searInput").val("");
        $(".show").remove();
        $(".messagSjr").css("padding-bottom","0px");
    },
    //点开搜索
    serchAction:function(obj){
        $("body").append("<div class='show'></div>");
        $(".show").show().css("top","92px");
        $("#hotTit").show();
        $("#HotTag").show();
        $('#'+obj).show();
        headSerch("#searInput");
        $(".messagSjr").css("padding-bottom","20px");
        hotTag();
    },
    //返回顶部
    toTop:function(){
        $("html,body").animate({
            "scrollTop": $("body").offset().top
        })
    },
    //个人首页点击我的订阅进入订阅页面
    subAction:function(){
        UserCookie();
        location.href='/subscribe.html';
    },
    //截取标题长度方法
    character:function(obj,maxstr) {
        $("." + obj).each(function () {
            var maxwidth = maxstr;
            if ($(this).text().length > maxwidth) {
                $(this).text($(this).text().substring(0, maxwidth));
            }
        })
    },
    headPhotoClick:function(){
        UserCookie();
        if(m_global.isLogin==true){
            location.href="my.html"
        }else{
            $.cookie("ismy",1,{path:"/",domain:'.dmzj.com'});
            location.href="login.html";
        }

    },
    //导航样式
    navStyle:function(index){
        switch(index){
            case 0:{
                $(".nav li").eq(0).find("a").addClass("cur").parent("li").siblings().find("a").removeClass("cur");
                break;
            }
            case 1:{
                $(".nav li").eq(1).find("a").addClass("cur").parent("li").siblings().find("a").removeClass("cur");
                break;
            }
            case 2:{
                $(".nav li").eq(2).find("a").addClass("cur").parent("li").siblings().find("a").removeClass("cur");
                break;
            }
            case 3:{
                $(".nav li").eq(3).find("a").addClass("cur").parent("li").siblings().find("a").removeClass("cur");
                break;
            }
            case 4:{
                $(".nav li").eq(4).find("a").addClass("cur").parent("li").siblings().find("a").removeClass("cur");
                break;
            }
            case 5:{
                $(".nav li").find("a").removeClass("cur");
                break;
            }
        }
    }
};
// 对Date的扩展，将 Date 转化为指定格式的String
// 月(M)、日(d)、小时(h)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符，
// 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字)
// 例子：
// (new Date()).Format("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423
// (new Date()).Format("yyyy-M-d h:m:s.S")      ==> 2006-7-2 8:9:4.18
Date.prototype.Format = function(fmt)
{ //author: meizz
    var o = {
        "M+" : this.getMonth()+1,                 //月份
        "d+" : this.getDate(),                    //日
        "h+" : this.getHours(),                   //小时
        "m+" : this.getMinutes(),                 //分
        "s+" : this.getSeconds(),                 //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt))
        fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    for(var k in o)
        if(new RegExp("("+ k +")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
    return fmt;
};


Array.prototype.lastObject = function () {
    var arr_len = this.length;
    if(arr_len == 0) {
        return null;
    }

    return this[arr_len - 1];
};

Array.prototype.firstObject = function () {
    var arr_len = this.length;
    if(arr_len == 0) {
        return null;
    }
    return this[0];
};

//删除数组元素
Array.prototype.indexOf = function(val) {
    for (var i = 0; i < this.length; i++) {
        if (this[i] == val) return i;
    }
    return -1;
};
Array.prototype.remove = function(val) {
    var index = this.indexOf(val);
    if (index > -1) {
        this.splice(index, 1);
    }
};


//弹层定位
function openwindow(html) {
    var showBg = $('<div class="show">')
    var layerHtml = $('<div class="layer">');
    $("body").append(showBg).append(layerHtml);
    var top = ($(window).height() - layerHtml.height()) / 2;
    var left = ($(window).width() - layerHtml.width()) / 2;
    layerHtml.css({top:top,left: left});
    showBg.show();
    layerHtml.show().append(html);
    /*
     }else if(cla==2){//订阅弹层
     layerHtml.append($('<div>').addClass("layerIcon02"))
     .addClass("layerz")
     .append('<p class="LinHei">您确定要取消该漫画订阅吗？</p>')
     .append('<a class="PubBtn look" id=okBtn>确定</a><a class="PubBtn can" id="Cancel">取消</a>')
     }else if(cla==3){//清空浏览记录
     layerHtml.append($('<div>').addClass("layerIcon03"))
     .addClass("layerz")
     .append('<p class="LinHei">您确定要清空所有浏览记录吗？</p>')
     .append('<a class="PubBtn look" id=okBtn>确定</a><a class="PubBtn can" id="Cancel">取消</a>')
     }else if(cla==4){//删除书签
     layerHtml.append($('<div>').addClass("layerIcon04"))
     .addClass("layerz")
     .append('<p class="LinHei">您确定要删除书签吗？</p>')
     .append('<a class="PubBtn look" id=okBtn>确定</a><a class="PubBtn can" id="Cancel">取消</a>')
     }else if(cla==5){//删除收藏书单
     layerHtml.append($('<div>').addClass("layerIcon05"))
     .addClass("layerz")
     .append('<p class="LinHei">您确定要删除该书单收藏吗？</p>')
     .append('<a class="PubBtn look" id=okBtn>确定</a><a class="PubBtn can" id="Cancel">取消</a>')
     }*/
    layerHtml.find("#Cancel").click(function(){
        showBg.remove();
        layerHtml.remove();
    })
}


//分享弹层
function sharwindow(){
    var showBg = $('<div class="show">');
    var sharWin= $(".sharWin");
    var window_h = $(window).height();
    var window_w = $(window).width();
    $("body").append(showBg);
    showBg.show();
    var top = (window_h - sharWin.height()) / 2;
    var left = (window_w - sharWin.width()) / 2;
    sharWin.css({top:top}).css({left: left}).show().addClass("layerz");
    sharWin.find(".sharClose").click(function(){
        $(".sharWin").removeClass("layerz").hide();
        showBg.remove();
    })
}

//图片尺寸
function imgStyle(){
    var divWidth = $(".imgBox li").width();
    var divHeight = Math.floor(divWidth/0.76);
    $(".imgBox li img").css("height",divHeight);
}


var app_ad={
    close_appAD:function(){
        $("#khdDown").hide();
        $.cookie("app_ad",0,{path:'/'});
    },
    app_ad_cookie:function(){
        if($.cookie("app_ad")==null){
            if($.cookie("app_home_ad")==null){
                $("#khdDown").hide();
            }else{
                $("#khdDown").show();
            }
        }else{
            $("#khdDown").hide();
        }
    },
    in_home:function(){
        $("#app_home_ad").hide();
        $.cookie("app_home_ad",0,{path:'/'});
        app_ad.app_ad_cookie();
        $('html,body').removeClass('ovfHiden');

    },
    app_home_ad:function(){
        $(".app_btn").css("left",($(window).width()-270)/2+"px");
        if($.cookie("app_home_ad")==null){
            $("#app_home_ad").show(function(){
                $('html,body').addClass('ovfHiden')
            });

        }else{
            $("#app_home_ad").hide();
            $('html,body').removeClass('ovfHiden');
        }
        app_ad.app_ad_cookie()
    },
    openApp:function(){
        setTimeout(function() {
            window.location = "https://www.dmzj.com/app/mobile.html";
        }, 25);

        var iOS = /iPad|iPhone|iPod/.test( navigator.userAgent );
//            console.log(navigator.userAgent);
        if(iOS) {
//                console.log('调用ios');
            window.location = "dmzj://";
        } else {
//                console.log('调用android');
            window.location = "dmzjandroid://www.dmzj.com/app/";
        }
    }
};

$(function(){
    // app_ad.app_home_ad();
});



//选项卡函数
function tab(titId, conId, titClass, conClass, showbg, type) {
    var tabTits = $('#' + titId).children(),
        tabCons = $('#' + conId).children(),
        len = tabTits.length;
    $('.'+showbg).height($(document).height());
    for (var i = 0; i < len; i++) {
        tabTits[i].index = i;
        tabTits[i].onclick = function() {
            $('#' + conId).show();
            for (var i = 0; i < len; i++) {
                tabTits[i].className = '';
                tabCons[i].className = '';
            };
            tabTits[this.index].className = titClass;
            tabCons[this.index].className = conClass;
            $('.' + showbg).show();
        };
        $('.' + showbg).click(function() {
            if (type == 1) {
                $('#' + titId).parent().hide();
                $('.' + showbg).hide()
            } else {
                $('#' + conId).hide();
                $('.' + showbg).hide();
            }
        })
    }
}