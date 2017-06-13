$(document).ready(function(){

    $("#sub_btn").click(function(e){
        e.preventDefault();
        $.post("/index/check_email/",{'email': $("#email").val()},function(ret,status){
            var errors = 0;
            if (ret['email'] == '1') {
                $("#signup_mes").text('已经注册过了哟');
                errors += 1;
            }
            if( $("#pwd").val().length > 20) {
                $("#signup_mes").text('密码过长啦');
                errors += 1;

            }
            if ( $("#pwd").val() != $("#pwd2").val() ) {
                $("#signup_mes").text('两次密码不一致哟');
                errors += 1;
            }
            if ( $("#nickname").val().length > 20 || $("#nickname").val().length == 0) {
                $("#signup_mes").text('尼克！');
                errors += 1;
            }
            if (errors != 0) {
                return false;
            }
            else {
                $("#signup_form").submit()
            }
        })
    });

    $("#signin_sub_btn").click(function(e){
        e.preventDefault();
        $.post("/index/check_signin/",{'email': $("#_email").val(),'pwd': $("#_pwd").val()},function(ret,status){
            var errors = 0;
            if (ret['error'] == '1') {
                $("#signin_mes").text('密码不对');
                errors += 1;
//                return false;
            }
            else if (ret['error'] == '2') {
                $("#signin_mes").text('找不到该帐号');
                errors += 1;
//                return false;
            }
            if (errors != 0) {
                return false;
            }
            else {
                $("#signin_form").submit()
            }
        })
    });

//    $(window).unload(function(){
//        $.get("/index/close/",{},function(ret,status){})
//    });


});