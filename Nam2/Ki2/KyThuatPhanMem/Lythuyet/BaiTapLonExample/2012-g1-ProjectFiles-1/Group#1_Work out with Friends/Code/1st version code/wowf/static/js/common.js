var features = {};

features['form'] = function() {
    var config = {'maxFields': 10};
    var $searchForms = $('.search-bar, .search-form');
    var $addClone = $('.add-clone');
    var $removeClone = $('.remove-clone');
    var $clearDate = $('.clear-date');
    var $buddies = $('.create-challenge-form .buddies a');
    var $competitor = $('.create-challenge-form #competitor');

    var showHiddenButtons = function() {
        var $tabs = $addClone.closest('.metadata');
        var $form = $tabs.closest('form');
        var cloneLen = $('.clonable', $form).length;

        if (cloneLen >= config.maxFields) {
            $('.add-clone', $form).addClass('disabled');
        }
        else if (cloneLen <= 1) {
            $('.remove-clone', $form).addClass('disabled');
        }

        $tabs.show();
        $clearDate.before(' &ndash; ').show();
    }
    var disableEmptyForms = function(e) {
        if ($(':text', $(this)).val() == '') {
            e.preventDefault();
        }
    }
    var addClone = function(e) {
        e.preventDefault();

        var $form = $(this).closest('form');
        var $lastClone = $('.clonable:last', $form);
        var $clone = $lastClone.clone(true);
        var cloneId = $clone.find(':input')[0].id;
        var cloneNum = parseInt(cloneId.replace(/.*-(\d{1,4})/m, '$1')) + 1;
        var cloneLen = $('.clonable', $form).length;

        $clone.find(':input, label, .error').each(function() {
            var $this = $(this);

            if ($this.is('.error')) {
                $this.remove();
            }
            else {
                var id = $this.attr('id').replace('-' + (cloneNum - 1), '-' + cloneNum);

                if ($this.is('input')) {
                    $this.attr({'name': id, 'id': id}).val('').removeAttr('checked');
                }
                else if ($this.is('label')) {
                    $this.attr('for', id);
                }
            }

        });

        if (cloneLen + 1 >= config.maxFields) {
            $addClone.addClass('disabled');
        }
        else {
            $addClone.removeClass('disabled');
        }

        $removeClone.removeClass('disabled');

        if (cloneLen < config.maxFields) {
            $lastClone.after($clone);
        }
    }
    var removeClone = function(e) {
        e.preventDefault();

        var $form = $(this).closest('form');
        var $lastClone = $('.clonable:last', $form);
        var cloneLen = $('.clonable', $form).length;

        if (cloneLen - 1 <= 1) {
            $removeClone.addClass('disabled');
        }
        else {
            $removeClone.removeClass('disabled');
        }

        $addClone.removeClass('disabled');

        if (cloneLen > 1) {
            $lastClone.remove();
        }
    }
    var setUsername = function(e) {
        e.preventDefault();

        $competitor.val($(this).data('username'));
    }

    return {
        init: function() {
            showHiddenButtons();
            $searchForms.submit(disableEmptyForms);
            $addClone.click(addClone);
            $removeClone.click(removeClone);
            $buddies.click(setUsername);
        }
    };
}();

features['dropdown'] = function() {
    var $menus = null;
    Response.action(function () {
        if (Response.band(1000)) {
            $('#header .dropdown .menu').show();
            $menus = $('.dropdown .menu').not('#header .dropdown .menu');
        }
        else {
            $menus = $('.dropdown .menu');
        }
    });

    var $toggles = $('.dropdown .toggle');
    var $document = $(document);

    var hideAllMenus = function() {
        $menus.css({'display': 'none'});
    }
    var displayMenu = function() {
        $(this).siblings('.menu').css({'display': 'block'});
    }
    var hideMenu = function() {
        $(this).siblings('.menu').css({'display': 'none'});
    }

    return {
        init: function() {
            hideAllMenus();
            $toggles.toggle(displayMenu, hideMenu);
            $menus.find(':text').click(function() { return false; });
            $document.one('click', function() { hideAllMenus(); });
        }
    };
}();

features['messages'] = function() {
    var config = {'delay': 800};
    var $notifications = $('.notice, .success, .warning, .error, .notification');

    return {
        init: function() {
            $notifications.click(function() {
                $(this).fadeOut(config.delay);
            });
        }
    }
}();

features['tabs'] = function() {
    var $selected = $('.selected, .disabled');

    return {
        init: function() {
            $selected.click(function(e) {
                e.preventDefault();
            });
        }
    }
}();

$(function() {
    for (var key in features) {
        var obj = features[key];
        obj.init();
    }
});