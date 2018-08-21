(function ($) {

    $.fn.modalUpdate = function (options) {
        var settings = $.extend({
            fields: "__all__",
            callback: "",
            params: ""
        }, options);
        $.ajax("/admin/ajax/get_html_form/", {
            method: "GET",
            data: {
                app_label: $(this).data().app_label,
                model: $(this).data().model,
                fields: settings.fields,
                callback: settings.callback,
                params: settings.params,
                id: $(this).data().id
            },
            success: function (response) {
                var modal = $("#ajax-modal");
                var body = modal.find(".modal-body").empty();
                body.append(response);
                modal.modal("show");
            }
        });
    };

    $.fn.modalCreate = function (options) {
        var settings = $.extend({fields: "__all__"}, options);
        $.ajax("/admin/ajax/get_html_form/", {
            method: "GET",
            data: {
                app_label: $(this).data().app_label,
                model: $(this).data().app_label,
                fields: settings.fields
            },
            success: function (response) {
                var modal = $("#ajax-modal").modal("hide");
                var body = modal.find(".modal-body");
                body.empty().html(response);
                modal.modal("show");
            }
        });
    };
}(jQuery));