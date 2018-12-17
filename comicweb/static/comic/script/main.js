/**
 * 时间戳的格式化
 * @param format
 * @returns {*}
 */
Date.prototype.format = function (format) {
    var o = {
        "M+": this.getMonth() + 1, //month
        "d+": this.getDate(), //day
        "h+": this.getHours(), //hour
        "m+": this.getMinutes(), //minute
        "s+": this.getSeconds(), //second
        "q+": Math.floor((this.getMonth() + 3) / 3), //quarter
        "S": this.getMilliseconds() //millisecond
    }

    if (/(y+)/.test(format)) {
        format = format.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    }
    for (var k in o) {
        if (new RegExp("(" + k + ")").test(format)) {
            format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length));
        }
    }
    return format;
}

window.TSB = (function ($, window, document, undefined) {
    var tsb = {
        switchHideShow: function (oChange, oTarget) {
            oChange.click(function () {
                if (oTarget.is(':hidden')) {
                    oTarget.slideDown('fast');
                } else {
                    oTarget.slideUp('normal');
                }
            });
        },

        /**
         * 初始化选择控件
         */
        initSwitchCheckBox: function () {
            if ($('.switch-checkbox')[0]) {
                $(document).find('.switch-checkbox').bootstrapSwitch();
            }
        },

        /*弹框提示信息*/
        modalAlert: function (options) {
            var opt = $.extend({
                status: 'success',
                msg: "Operation is successful !",
                speed: 2000
            }, options || {});
            if (opt.status == 'success') {
                var alertIcon = '<i class="fa fa-check-circle"></i>';
            } else {
                var alertIcon = '<i class="fa fa-times-circle"></i>';
            }
            var alertHtml = '<div class="modal-alert" style="display:none;"><div class="alert alert-' + opt.status + '">' + alertIcon + opt.msg + '</div></div>';
            $(alertHtml).appendTo($('body')).fadeIn().delay(opt.speed).fadeOut(function () {
                $(this).remove()
            });
        },
        /*jquery UI 滑块扩展*/
        slider: function (sel, opt) {
            var $selectors = $(sel);
            return $.each($selectors, function () {
                var $target = $(this);

                opt.start = function (event, ui) {
                    if (typeof opt.startFun == 'function') {
                        opt.startFun.call(this, event, ui);
                    }
                };
                opt.slide = function (event, ui) {
                    if (typeof opt.slideFun == 'function') {
                        opt.slideFun.call(this, event, ui);
                    }
                    if (opt.values != undefined) {
                        rangeWidget.call(this);
                    }
                };
                opt.change = function (event, ui) {
                    if (typeof opt.changeFun == 'function') {
                        opt.changeFun.call(this, event, ui);
                    }
                    if (opt.values != undefined) {
                        rangeWidget.call(this);
                    }
                };
                opt.stop = function (event, ui) {
                    if (typeof opt.stopFun == 'function') {
                        opt.stopFun.call(this, event, ui);
                    }
                };

                var range = $(this).attr('js-range');

                if (opt.range == undefined) {
                    opt.range = range == 'true' ? true : range;
                }
                if (opt.min == undefined) {
                    opt.min = parseInt($(this).parent('div').find('.slider-widget-range').eq(0).text());
                }
                if (opt.max == undefined) {
                    opt.max = parseInt($(this).parent('div').find('.slider-widget-range').eq(1).text());
                }

                if (opt.value == undefined && opt.values == undefined) {
                    var input_target = $(this).attr('js-target-input');
                    var oForm = $(this).closest('form');
                    if (input_target.indexOf(',') > 1) {
                        var input_targets = input_target.split(',');
                        var input_targets_0 = parseInt(oForm.find('input[name="' + input_targets[0] + '"]').val());
                        var input_targets_1 = parseInt(oForm.find('input[name="' + input_targets[1] + '"]').val());
                        opt.values = [input_targets_0, input_targets_1];
                    } else {
                        opt.value = parseInt(oForm.find('input[name="' + input_target + '"]').val());
                    }
                }
                $target.slider(opt);

                if (opt.values != undefined) {
                    var rangeWidget = function () {
                        var widthPer = parseInt($target.find('.ui-slider-range')[0].style.width);
                        var leftPer = parseInt($target.find('.ui-slider-range')[0].style.left);
                        if ($target.find('.ui-widget-range-left')[0] == undefined) {
                            $('<div class="ui-widget-range-left" style="width:' + leftPer + '%;"></div>' +
                                '<div class="ui-widget-range-right" style="width:' + (100 - widthPer - leftPer) + '%;"></div>').appendTo($target);
                        } else {
                            $target.find('.ui-widget-range-left').css('width', leftPer + '%');
                            $target.find('.ui-widget-range-right').css('width', (100 - widthPer - leftPer) + '%');
                        }
                    };
                    rangeWidget();
                }
            });
        },
        /*初始化slider*/
        initSlider: function () {
            $('.js-ui-slider').each(function () {
                TSB.slider(this, {
                    slideFun: function (event, ui) {
                        var oForm = $(this).closest('form');

                        var target_input = $(this).attr('js-target-input');

                        if (target_input.indexOf(',') > 1) {
                            var input_targets = target_input.split(',');

                            oForm.find('.js_data_' + input_targets[0]).text(ui.values[0]);
                            oForm.find('input[name="' + input_targets[0] + '"]').val(ui.values[0]);

                            oForm.find('.js_data_' + input_targets[1]).text(ui.values[1]);
                            oForm.find('input[name="' + input_targets[1] + '"]').val(ui.values[1]);

                        } else {
                            oForm.find('.js_data_' + target_input).text(ui.value);
                            oForm.find('input[name="' + target_input + '"]').val(ui.value);
                            oForm.find('#' + target_input).trigger('change');
                        }

                    }
                });
            });

            $('.js-ui-slider-with-scale').each(function () {
                var oForm = $(this).closest('form');

                var target_input = $(this).attr('js-target-input');
                var target_value = oForm.find('input[name="' + target_input + '"]').val();
                var value;

                var scale = new Array();
                var scale_target = new Array();
                $(this).closest('div').parent('div').find('.sacle').each(function (k) {
                    var _scale_value = $(this).attr('js-data-scale');
                    var _scale_target = $(this).html();
                    scale[k + 1] = _scale_value;
                    scale_target[k + 1] = _scale_target;
                    if (target_value == _scale_value) {
                        value = k + 1;
                        oForm.find('.js_data_' + target_input).text(_scale_target);
                    }
                });

                TSB.slider(this, {
                    min: 1,
                    max: scale.length - 1,
                    value: value,
                    slideFun: function (event, ui) {

                        if (target_input.indexOf(',') > 1) {
                            var input_targets = target_input.split(',');

                            oForm.find('.js_data_' + input_targets[0]).text(scale_target[ui.values[0]]);
                            oForm.find('input[name="' + input_targets[0] + '"]').val(scale[ui.values[0]]);

                            oForm.find('.js_data_' + input_targets[1]).text(scale_target[ui.values[1]]);
                            oForm.find('input[name="' + input_targets[1] + '"]').val(scale[ui.values[1]]);

                        } else {
                            oForm.find('.js_data_' + target_input).text(scale_target[ui.value]);
                            oForm.find('input[name="' + target_input + '"]').val(scale[ui.value]);
                        }

                    }
                });
            });
        },
        /*初始化表单元素*/
        initForm: function (oForm, oValue) {
            function initSwitch(oForm) {
                oForm.find('.switch-checkbox').bootstrapSwitch();
            }

            if (oValue == undefined) {
                initSwitch(oForm);
                return false;
            }

            oForm.find('input').each(function (k, oThis) {
                var lableName = $(oThis).attr('name');

                if (lableName) {
                    switch ($(oThis).attr('type')) {
                        case 'hidden':
                        case 'text':
                        case 'select':
                            if (oValue.hasOwnProperty(lableName)) {
                                $(oThis).val(oValue[lableName]);
                            }
                            break;
                        case 'radio':
                            if (oValue.hasOwnProperty(lableName)) {
                                oForm.find('input[name="' + lableName + '"][value="' + oValue[lableName] + '"]').attr('checked', 'true');
                            }
                            break;
                        case 'checkbox':
                            var _lableName = lableName.substring(0, lableName.length - 2);
                            if (oValue.hasOwnProperty(_lableName) && oValue[_lableName]) {
                                $.each(oValue[_lableName], function (_k, _v) {
                                    oForm.find('input[name="' + lableName + '"][value="' + _v + '"]').attr('checked', 'true');
                                });
                            }

                            if (oValue.hasOwnProperty(lableName) && oValue[lableName]) {

                                if (lableName == 'status' || lableName.indexOf('_check') > 0) {
                                    oForm.find('input[name="' + lableName + '"]').val(oValue[lableName]);
                                }

                                if (oValue[lableName] == app_enum.alert_config_status_normal) {
                                    oForm.find('input[name="' + lableName + '"]').prop('checked', true);
                                } else {
                                    oForm.find('input[name="' + lableName + '"]').prop('checked', false);
                                }

                            }
                            break;
                    }
                    if (lableName.substring(lableName.length - 2, lableName.length) != '[]') {
                        var js_label = oForm.find('.js_data_' + lableName);
                        if (js_label) {
                            js_label.text(oValue[lableName]);
                        }
                    }

                }

            });

            oForm.find('textarea').each(function (k, oThis) {
                var lableName = $(oThis).attr('name');
                if (lableName && oValue.hasOwnProperty(lableName)) {
                    $(oThis).html(oValue[lableName]);
                }
            });

            oForm.find('select').each(function (k, oThis) {
                var lableName = $(oThis).attr('name');
                if (oValue.hasOwnProperty(lableName)) {
                    $(oThis).val(oValue[lableName]);
                }
            });

            initSwitch(oForm);
        },

        /*事件管理*/
        eventManager: {
            events: {
            },
            addListener: function (type, handler, scope, params) {
                this.events = this.events || {};
                this.events[type] = this.events[type] || [];
                this.events[type].push({
                    handler: handler,
                    scope: scope,
                    params: params
                });
            },
            removeListener: function (type, handler, scope) {
                if (!$.isEmptyObject(this.events)) {
                    this.events[type] = $.grep(this.events[type], function (e) {
                        var s = scope || e.scope;
                        var h = handler || e.handler;
                        return e.scope !== s || e.handler !== h;
                    });
                }
            },
            trigger: function (type, params) {
                if (this.events) {
                    var fns = this.events[type], i, fn;
                    if (!fns) {
                        return;
                    }
                    for (i = 0; fn = fns[i]; i++) {
                        if (fn.handler.apply(fn.scope || this, params || fn.params || []) === false) {
                            return false;
                        }
                    }
                }
            }
        },
        /*url锚点值处理*/
        anchorManager:{
            _processHash : function (params)
            {
                var url = window.location;
                var hash = '#';
                $.each(params,function(k,v){
                    hash = hash + k +'=' + v +"&";
                });
                url.hash = hash;
            },
            getParams : function(){
                var url = window.location.hash;
                var params = {};
                if(url){
                    url = url.slice(1);
                    var _params_tmp = url.split('&');

                    if (_params_tmp.length > 0) {
                        $(_params_tmp).each(function (k,v) {
                            var _tmp = v.split('=');
                            if (_tmp[1]) params[_tmp[0]] = _tmp[1];
                        })
                    }
                }
                return params;
            },
            setParam : function (key,value) {
                var params = this.getParams();
                params[key] = value;
                this._processHash(params);
            },
            removeParam: function (key) {
                var params = this.getParams();
                delete params[key];
                this._processHash(params);
            }
        },
        /**
         * 初始化harViwer
         */
        harViewerInit:function(){
            $(document).ready(function(){
                var har = document.createElement("script");
                har.src = "/resource/js/harviewer/har.js";
                har.setAttribute("id", "har");
                har.setAttribute("async", "true");
                document.documentElement.firstChild.appendChild(har);
            });
            if(typeof(harInitialize)!="undefined"){harInitialize()};
        }

    };
    return tsb;
}(jQuery, window, document, undefined));

$(function () {
    TSB.initSwitchCheckBox();
    TSB.switchHideShow($('.createNewProject'), $('.createNewProjectTarget'));
});
