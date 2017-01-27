/**$(document).ready(function () {
    $('#submit_button').on("click", function() {
        $('#main_container').stop().animate({backgroundColor: '#8699CC', "slow");
    });
});*/

window.onload = function() {
    if (window.jQuery) {
        // jQuery is loaded
        alert("Yeah!");
    } else {
        // jQuery is not loaded
        alert("Doesn't Work");
    }
}