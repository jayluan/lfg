$(document).ready(function() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function join_group(groupId){
        $.ajax({
            type: "POST",
            url: "/groups/join/",
            data: {"groupId": groupId},
            success: function(data){
                if(!$('#group-leave'+groupId).length)
                    add_button('Leave', groupId);
                $("#group-join-"+groupId).hide();
                $("#group-leave-"+groupId).show();
                $("#members").html(data);
            },
            headers: {
                'X-CSRFToken': csrftoken
            }
        });

        return false;
    }



    $("button.join").on("click", function(){
        var groupId = parseInt(this.id.split("-")[2]);
        join_group(groupId);
    });

    function leave_group(groupId){
        $.ajax({
            type: "POST",
            url: "/groups/leave/",
            data: {"groupId": groupId},
            success: function(data){
                if(!$('#group-join'+groupId).length)
                    add_button('Join', groupId);
                $("#group-leave-"+groupId).hide();
                $("#group-join"+groupId).show();
                $("#members").html(data);
            },
            headers: {
                'X-CSRFToken': csrftoken
            }
        });

        return false;
    }

    $("button.leave").on("click", function(){
        var groupId = parseInt(this.id.split("-")[2]);
        leave_group(groupId);
    });

    function add_button(state, groupId){
        id_name = 'group-' + state.toLowerCase() + '-' + groupId.toString();
        var $something= $('<button/>').attr({ id:id_name, class:state.toLowerCase()});
        $something.html(state + ' Group');
    //    var str = '<button id="group-' + state + '-' + groupId.toString() + 'class="' + state + '">'
        var $btn = $("#manage").append($something);
    }
});