var space = {};

(function (namespace, Backbone, $, _, Cookies) {

    "use strict";


    function ModalWindow() {

        this.$wrapper = $("#modal-wrapper");
        this.template = _.template($("#template-modal").html());
        this.modalParams = {};

        this.el = "#modal";

    }


    ModalWindow.prototype = {

        /**
         * Display modal window
         * @param title - modal title
         * @param contents - modal contents (html)
         */

        display: function (title, contents) {

            this.$wrapper
                .empty()
                .html(this.template({
                    modalTitle: title,
                    modalBody: contents
                }));

            $(this.el).modal(this.modalParams);

        }

    };

    /**
     * Store user credentials in cookie,
     * Handle submit with Ctrl + Enter
     */

    var CommentForm = Backbone.View.extend({

        el: "#comment-form",
        credentialFields: ["#id_name", "#id_email"],
        fieldsWildcard: "input:not(:checkbox), textarea",
        events: {
            "keypress #id_name, #id_email": "_storeCredentials",
            "keydown #id_name, #id_email": "_storeCredentials"
        },

        initialize: function () {
            this._render();
        },

        /**
         * 1. Get credential data from cookie and fill in the form fields
         * 2. Apply twitter bootstrap classes to the form fields and display it
         * 3. Setup form shortcuts
         *
         * @private
         */

        _render: function () {

            var form = this.$el,
                enterKeyCodes = [10, 13];

            _.each(this.credentialFields, function (item) {
                var value = Cookies.get(item);
                if(!_.isUndefined(value))
                    $(item).val(value);
            });

            form
                .find(this.fieldsWildcard)
                .addClass("form-control")
                .keydown(function (e) {
                    if (e.ctrlKey && _.contains(enterKeyCodes, e.keyCode))
                        form.submit();
                });

            form.show();
        },

        /**
         * Store credentials in a cookie
         * @private
         */
        _storeCredentials: function () {
            _.each(this.credentialFields, function (item) {
                Cookies.set(item, $(item).val());
            });
        }

    });

    function KasManZvana() {

        this.modal = new ModalWindow;

        new CommentForm();

        this._setupCSRF();
        this._setupGoogleAnalytics();
        this._setUpNewWindowLinks();

        this.$form = $("#number-form");
        this.$number = this.$form.find("#number");
        this.$number.on("keypress", $.proxy(this._validateNumber, this));
        this.$form.on("submit", $.proxy(this._formSubmit, this));

    }

    KasManZvana.prototype = {

        _validateNumber: function(ev) {
            this.$number.val(this.$number.val().slice(0, 8))
        },

        /**
         * Google analytics
         */

        _setupGoogleAnalytics: function () {

            (function (i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r;

                i[r] = i[r] || function () {
                        (i[r].q = i[r].q || []).push(arguments)
                    }, i[r].l = 1 * new Date();
                a = s.createElement(o), m = s.getElementsByTagName(o)[0];
                a.async = 1;
                a.src = g;
                m.parentNode.insertBefore(a, m)
            })(
                window,
                document,
                'script',
                '//www.google-analytics.com/analytics.js', 'ga'
            );

            ga('create', 'UA-71323244-1', 'auto');
            ga('send', 'pageview');

        },

        /**
         * Setup django CSRF token sending for POST requests
         * @private
         */
        _setupCSRF: function () {

            var csrfToken = Cookies.get('csrftoken'),
                regExp = new RegExp("^(GET|HEAD|OPTIONS|TRACE)$");

            $.ajaxSetup({
                beforeSend: function (xhr, settings) {
                    if (!regExp.test(settings.type) && !this.crossDomain)
                        xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
            });

        },

        /**
         * Redirect to phone profile page instead of performing generic
         * form submission
         * @param event
         */
        _formSubmit: function (event) {

            event.preventDefault();

            var host = window.location.host;
            window.location.href = "http://" + host +
                "/numurs/" + this.$number.val() +
                "/";

        },

        _setUpNewWindowLinks: function () {
            $('a[data-target="new-window"]').attr('target', '_blank');
        }

    };

    // Javascript entry point
    namespace.start = function () {
        new KasManZvana();
    };

})(
    space,
    Backbone,
    $,
    _,
    Cookies
);
