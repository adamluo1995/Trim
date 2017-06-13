$(document).ready(function(){

    $("#check_goal_btn").click(function(event){
        event.preventDefault();
        $("#_log_message").val($("#log_message").val());
        var goal_score = $("[name='goal_score']");
//        alert(goal_score.length)
        var _goal_score = $("select[name^='_goal_score']");
//        alert(_goal_score.length)
        for (var i=0; i<goal_score.length; i++) {
            _goal_score.eq(i).val(goal_score.eq(i).val());
        }
        $("#hid_form").submit();
    });

    $(window).unload(function(){
        $.get("/index/close/",{},function(ret,status){})
    });


});