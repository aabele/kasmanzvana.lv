/**
 * Handle rating API requests
 * @param url
 * @param plusBlock
 * @param minusBlock
 * @param Buttons jquery objects
 * @constructor
 */
function Rating(url, plusBlock, minusBlock, Buttons, opts) {

    if(!opts.isAuthenticated) {
        Buttons.each(function(){
            LoginPopover($(this));
        })
    }

    Buttons.on("click", function (ev) {
        ev.preventDefault();

        var choice;

        if (!opts.isAuthenticated) {
            return;
        }

        if ($(this).hasClass("btn-plus"))
            choice = "vote_plus";

        if ($(this).hasClass("btn-minus"))
            choice = "vote_minus";

        $.ajax({
            url: url.replace("{0}", opts.id).replace("{1}", choice),
            method: "POST",
            type: "ajax",
            success: function (response) {
                plusBlock.html(response.get_positive_votes);
                minusBlock.html(response.get_negative_votes);
            }
        });

    })

}


function LoginPopover(el) {

    el.popover({
        placement: "top",
        trigger: "hover",
        title: "Autorizējies",
        content: "Lai izmantotu šo servisu nepieciešams pieslēgties ar sociālo tīklu kontu"
    });
}


function Follow(button, opts) {

    if(!opts.isAuthenticated) {
        LoginPopover(button);
    }

    button.on("click", function (ev) {
        ev.preventDefault();
        var action = button.data("action");

        if (!opts.isAuthenticated) {
            return;
        }

        var msgMap = {
            unfollow: "Sekot numuram",
            follow: "Pārtraukt sekošanu"
        };

        $.ajax({
            url: "/api/v1/phone/{0}/{1}/".replace("{0}", opts.id).replace("{1}", action),
            method: "POST",
            type: "ajax",
            success: function (res) {
                console.log(res);
                button.html(msgMap[button.data("action")]);
                button.data("action", action === "follow" ? "unfollow" : "follow");
            }
        });

    })
}
