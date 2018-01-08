$(function(){

    // Cookie panels

    var cookieName = "eulawarning";
    var cookieValue = "accepted";
    var cookiePanel = $("#cookiewarning");

    if (Cookies.get(cookieName)!=cookieValue) {
        cookiePanel.show();
    }

    cookiePanel.find("button").on("click", function(){
        Cookies.set(cookieName, cookieValue);
        cookiePanel.hide();
    });

});
