/**
 * Created by chentao on 2016/12/6 0006.
 */
$(document).ready(function () {
    $("#about-btn").click(function (event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + 'o'
        $("#msg").html(msgstr);
    })
})