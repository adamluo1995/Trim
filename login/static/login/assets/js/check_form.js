$(document).ready(function(){

    $("#sub_btn").click(function(){
        var errors = 0;
        $.get("/index/check_email/",{'email': $("#email").val()},function(ret,status){
            if (ret['email'] == '1') {
                $("#signup_mes").text('已经注册过了哟');
                errors += 1;
            }
        })
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
    });

});