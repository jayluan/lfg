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
            success: function(){
                $("group-join-"+groupId).hide();
            },
            headers: {
                'X-CSRFToken': csrftoken
            }
        });

        return false;
    }



    $("button.join").click(function(){
        var groupId = parseInt(this.id.split("-")[2]);
        return join_group(groupId);
    })
});