//===========头部热门搜索标签
function hotTag(){
    var url = '/search_top.json';
    T.restGet(url, {}, function(data){
        var html="";
        var bgcolor=["42b5ff","0096ff","2775f7","0096ff","0096ff","42b5ff"];
        for(i=0;i<data.length;i++){
            html+='<li><a href="/info/'+ data[i].id+'.html"';
            html+='style="background: #'+bgcolor[i]+'" href="searchResult.html">'+data[i].name+'</a></li>';
        }
        $("#HotTag").html(html);
    })

}

//返回上一页方法
function goBack(){
    if(document.referrer ==''|| document.referrer.indexOf(window.location.host) == -1){
        window.location = '/'
    }else{
        window.history.go(-1);
    }
}


//当前漫画是否订阅
function isSubscribe(sub_id){
    UserCookie();
    if(m_global.isLogin==true) {
        var localStorag = localStorage.mySubscribeData;
        if (localStorag == undefined || JSON.parse(localStorag) == ""){
            var url = '/mysubscribe';
            T.restGet(url, {}, function (data) {
                localStorag = JSON.stringify(data);//存储
                var subScribeArry = data;
            });
        } else {
            var subScribeArry = JSON.parse(localStorag);
        }
        var is_exist = false;
        for(var sub=0;sub<subScribeArry.length;sub++){
            if(subScribeArry[sub]['sub_id'] == sub_id){
                is_exist=true;
                break;
            }
        }
        if (is_exist){
            $("#Subscribe").html("取消订阅");
            $("#Subscribe").attr("onclick", "unSubscribe('" + sub_id + "')");
            $("#subject_"+sub_id).html("已订阅").attr("onclick","");
        } else {
            $("#Subscribe").html("订阅漫画");
            $("#Subscribe").attr("onclick", "addSubscribe('" + sub_id + "')");
            $("#subject_"+sub_id).html("订阅漫画").attr("onclick","addSubscribe("+sub_id+")");
        }
    }else{
        localStorage.removeItem("mySubscribeData");
    }
}
//alert(localStorage.readHistory)
//console.log(localStorage.readHistory);



/**
 * 取消订阅
 * @param subId  漫画id
 * @param subType 漫画类型 mh=0  dh=1 xs=2
 */
function unSubscribe(subId){
    var html = '';
    html += '<div class="layerIcon02" id="subWindow"></div>';
    html += '<p class="LinHei">您确定要取消该漫画订阅吗？</p>';
    html += '<a class="PubBtn look" id="okBtn" onclick="subscribeDel('+subId+')">确定</a>';
    html += '<a class="PubBtn can" id="Cancel">取消</a>';
    openwindow(html);
}
function subscribeRmove(subId){
    var subScribeArry = JSON.parse(localStorage.mySubscribeData);
    var SubscribeKeyArry = [];
    for(i=0;i<subScribeArry.length;i++){
        for(var key in subScribeArry[i]){
            SubscribeKeyArry.push(parseInt(subScribeArry[i][key]));
        }
    }
    var subScribe_index = $.inArray(subId,SubscribeKeyArry);
    subScribeArry.remove(subScribeArry[subScribe_index]);
    $("#subWindow").parent().remove();
    $(".show").remove();
    $("#Subscribe").html("订阅漫画").attr("onclick","addSubscribe('"+subId+"')");
    $("#mysub_"+subId).html("订阅漫画").attr("onclick","addSubscribe('"+subId+"')");
    localStorage.mySubscribeData=JSON.stringify(subScribeArry);
}
function subscribeDel(subId){
    UserCookie();
    var url = "https://"+domain_name+"interface.dmzj.com/api/subscribe/del";
    T.ajaxJsonp(url,{sub_id:subId,sub_type:0}, function (data) {
        if(data.result==1000){
            subscribeRmove(subId);
            $("#sub_"+subId).remove();
            if($(".itemBox").length==0){
                if($(".Introduct_Sub").length<0){
                  no_conten();
                }
            }
        }else if(data.result==700){
            subscribeRmove(subId);
            $("#Subscribe").html("订阅漫画").attr("onclick","addSubscribe('"+subId+"')");
            $("#mysub_"+subId).html("订阅漫画").attr("onclick","addSubscribe('"+subId+"')");
           console.log(data.msg);
        }
    })
}
//=====================取消订阅  end  ===========================//

//订阅已读
var update_read_status = function(subid){
    url = 'https://'+domain_name+'interface.dmzj.com/api/subscribe/upread';
    T.ajaxJsonp(url,{'sub_id':subid},function(data){
        //console.log(data)
        location.href="/info/"+subid+".html";
    });
};

/**
 * 推荐 换一批
 * @param obj
 * @param type_id
 */
function updateRecommends(type_id) {
    var url_suffix = '/recommend/batch/'+type_id;
    T.restGet(url_suffix, {}, function(data){
        var html = '';
        for (var i = 0; i < data.length; i++) {
            var comic = data[i];
            html += '<li><a class="ImgA autoHeight" href="' + comic['comic_url'] + '"><img src="' + comic['cover_url'] + '" width="100%"/></a>' +
            '<a class="txtA">'+ comic['title'] +'</a>';

            if(comic['comic_author']) {
                html += '<span class="info">作者:' + comic['comic_author'] + '</span>'
            }
            if(comic['status'] == "已完结") {
                html += '<span class="wan"></span>';
            }

            html += '</li>';
        }

        $("#"+type_id).html(html);
    });
}

//==============================头部搜索 star====================//
function headSerch(obj){
    $(obj).bind('input propertychange',function() {
        var keyword = $.trim($(obj).val());
        var messageBox = $("#messagelist");
        var url ="https://"+domain_name+"interface.dmzj.com/api/wap_search"
        messageBox.show();
        if (keyword != '') {
            T.ajaxJsonp(url,{"keywords":keyword}, function (data) {
                var html = "";
                if(data.result==1000){
                    for(i=0;i<data.data.length;i++){
                        html += '<li><a href="/comic/search?kw='+data.data[i].name+'">'+data.data[i].name+'</a></li>';
                    }
                }else{
                    html = '<li><a href="javascript:;">无搜索结果</a></li>';
                }
                messageBox.html(html);
                $('form[id=searchForm]').attr('action','/comic/search?kw='+keyword);
            },function(){
                messageBox.hide();
            });
        }else{
            $("#messagelist").html("");
            messageBox.hide();

        }
    });
}
function success(data){}
function serchAction(){
    var keyword = $("#searInput").val();
    if(keyword!=""){
        location.href="/comic/search?kw="+keyword
    }else{
        alert("请输入关键词");
    }
}

//==============================头部搜索 end====================//


//禁止uc浏览器左右滑屏
/*(function uctocu(){
    var control = navigator.control || {};
    if (control.gesture) {
        control.gesture(false);
    }
})();*/
