var crsf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
axios.defaults.transformRequest = [function (data) {

    data = JSON.parse(JSON.stringify(data))
    data.csrfmiddlewaretoken = crsf_token;
    var params = []
    for (var key in data) {
        var value = data[key];
        if (typeof (value) == "undefined" || String(value) == "") {
            continue
        } else if (typeof (value) == "object") {
            for (var k in value) {
                if (value[k + "__gte"] || value[k + "__lt"]) {
                    delete value[k]
                }
                if (typeof (value[k]) == "undefined" || String(value[k]) == "" || value[k] == null) {
                    delete value[k]
                }
            }
            value = JSON.stringify(value)
            if (value == "{}") {
                continue
            }
        }
        params.push(key + "=" + value);

    }
    return params.join("&");
}];
Date.prototype.format = function (fmt) {
    var o = {
        "M+": this.getMonth() + 1,                 //月份
        "d+": this.getDate(),                    //日
        "h+": this.getHours(),                   //小时
        "m+": this.getMinutes(),                 //分
        "s+": this.getSeconds(),                 //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds()             //毫秒
    };
    if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}


function post(params, app, showNotice) {
    app.loading = true;
    if (typeof showNotice == "undefined") {
        showNotice = false;
    }
    return new Promise(((resolve, reject) => {
        axios.post('', params).then(res => {
            if (res.status != 200) {
                //提示网络错误
                app.$notify.error({
                    title: '错误',
                    message: res.statusText
                });
                reject(res);
            } else {
                if (res.data.state) {

                    resolve(res.data.data, res.data);
                    if (showNotice) {

                        if (res.data.messages) {
                            res.data.messages.forEach(item => {
                                setTimeout(function () {
                                    app.$notify({
                                        dangerouslyUseHTMLString: true,
                                        message: item.msg,
                                        type: item.tag
                                    });
                                }, 200)
                            });
                        } else {
                            app.$notify({
                                title: '成功',
                                message: res.data.msg,
                                type: 'success'
                            });
                        }
                    }
                    app.showError = false;
                } else {
                    reject(res.data);
                    app.$notify.error({
                        title: '错误',
                        message: res.data.msg
                    });
                    app.showError = true;
                    app.errorMsg = res.data.msg

                }
            }
        }).catch(function (err) {
            app.$notify.error({
                title: '错误',
                message: err
            });
            app.errorMsg = err;
            app.showError = true;
        }).finally(function () {
            app.loading = false;
            app.search.initialized = true;
            app.$forceUpdate()
        });
    }));
}

var fontConfig = new Vue({
    // el: '#dynamicCss',
    data: {
        fontSize: null
    },
    watch: {
        fontSize: function (newValue) {
            if (newValue != 0) {
                var fontStyle = document.getElementById('fontStyle');
                if (!fontStyle) {
                    fontStyle = document.createElement('style');
                    fontStyle.id = 'fontStyle';
                    fontStyle.type = 'text/css';
                    document.head.append(fontStyle);
                }
                fontStyle.innerHTML = '*{font-size:' + newValue + 'px!important;}'

            } else {
                var fontStyle = document.getElementById('fontStyle');
                if (fontStyle) {
                    fontStyle.remove();
                }
            }
        }
    },
    created: function () {
        var val = getCookie('fontSize');
        if (val) {
            this.fontSize = parseInt(val);
        } else {
            this.fontSize = 0;
        }
    },
    methods: {}
});


new Vue({
    el: '#theme',
    data: {
        theme: '',
    },
    created: function () {
        this.theme = getCookie('theme');

        var self = this;
        //向父组件注册事件
        if (parent.addEvent) {
            parent.addEvent('theme', function (theme) {
                self.theme = theme;
            });

            parent.addEvent('font', function (font) {
                fontConfig.fontSize = font;
            });
        }

    }
})
window.addEventListener('beforeunload', () => {
    if (window.beforeLoad) {
        window.beforeLoad();
    }
});

var app = new Vue({
    el: '#app',
    data: {
        formInline: {},
        form: {
            show: true
        },
        loading: false,
        errorMsg: null,
        search: {
            current_page: 1,
            action: 'list',
            order_by: null,
            all: 0,
            filters: {},
            search: '',
            page_size: 0,
            initialized: false
        },
        dialog: {
            visible: false,
            title: 'dialog',
            url: null
        },
        toolbars: {
            isActive: true,
            customButtons: [],
            showAll: false
        },
        backupSearch: {},
        exportFormat: 0,
        exts: {},
        table: {
            headers: [],
            rows: [],
            actionFixed: false,
            selection: []
        },
        pageSizes: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200],
        paginator: {},
        showError: false
    },
    watch: {
        'table.headers': function (newValue, oldValue) {
            //如果列大于8列，才显示固定列，否则页面布局很诡异
            if (!newValue) {
                return
            }
            if (newValue.length <= 8) {
                this.table.actionFixed = false
            } else {
                this.table.actionFixed = 'right'
            }
        },
        'loading': function (newValue) {
            if (parent.progress) {

                if (newValue) {
                    parent.progress.start();
                } else {
                    parent.progress.done();
                }
            }
        }
    },
    methods: {
        post: function (params) {
            return post(params, this)
        },
        handleSizeChange: function (val) {
            this.search.page_size = val;
            this.onSubmit();
        },
        onSubmit() {
            var self = this;
            post(self.search, self).then(function (res) {

                //在后续分页数据中不返回该字段，减少网络传输开销
                //headers在当前生命周期内部更新，除非刷新页面
                if (self.table.headers.length == 0 && res.headers) {
                    res.headers.forEach(item => {
                        item.show = true
                    });
                    self.table.headers = res.headers

                }
                if (res.exts) {
                    self.exts = res.exts;
                }
                self.table.rows = res.rows
                self.paginator = res.paginator
                if (self.pageSizes.indexOf(res.paginator.page_size) == -1) {
                    self.pageSizes.unshift(res.paginator.page_size);
                }
                self.search.page_size = res.paginator.page_size;
                if (res.custom_button) {
                    self.toolbars.customButtons = res.custom_button
                }

                //调用sdk
                if (window.SIMPLEAPI && window.SIMPLEAPI.loadData) {
                    window.SIMPLEAPI.loadData(self);
                }

                //表格清空
                self.clearSelect();
            });
        },
        pageChange: function (page) {
            this.search.current_page = page;
            this.$nextTick(function () {
                this.onSubmit();
            })
        }, sortChange: function ({column, prop, order}) {
            var mappers = {
                'ascending': '',
                'descending': '-'
            }
            if (!order) {
                this.search.order_by = null;
            } else {
                this.search.order_by = mappers[order] + prop;
            }
            this.$nextTick(function () {
                this.onSubmit();
            });
        },
        refreshData: function () {
            this.search = JSON.parse(JSON.stringify(this.backupSearch));
            this.$nextTick(function () {
                this.onSubmit();
                this.toolbars.isActive = true;
            });
        },
        add: function (title) {
            if (window.SIMPLEAPI && window.SIMPLEAPI.toolbar) {
                var rs = window.SIMPLEAPI.toolbar.call({}, 'add', this);
                if (!rs) {
                    return;
                }
            }
            //页内打开
            location.href = location.pathname + 'add';

            //对话框打开
            // this.dialog.url = location.pathname + 'add';
            // this.dialog.title = title;
            // this.dialog.visible = true;
        },
        edit: function (title, id) {

            if (window.SIMPLEAPI && window.SIMPLEAPI.toolbar) {
                var rs = window.SIMPLEAPI.toolbar.call({}, 'edit', this);
                if (!rs) {
                    return;
                }
            }

            if (!id) {
                id = this.table.selection[0]._id
            }
            //页内打开
            location.href = location.pathname + id + '/change/';//页内打开
        },
        dialogClose: function () {
            this.dialog.visible = false;
        },
        selectAll: function (selection, row) {
            this.select(selection, row);
            //显示全部按钮
            this.toolbars.showAll = selection.length != 0;
        },
        select: function (selection, row) {
            this.table.selection = selection;
            this.toolbars.isActive = selection.length <= 0;
        },
        exports: function (btn, key) {
            document.getElementById('export_form').submit()
        },
        go_url: function (url, icon, name) {
            if (parent.app.openTab) {
                parent.app.openTab({
                    url: url,
                    icon: icon,
                    name: name
                })
            } else {
                window.location.href = url;
            }
        },
        customButtonClick: function (btn, key) {
            if (window.SIMPLEAPI && window.SIMPLEAPI.toolbar) {
                var rs = window.SIMPLEAPI.toolbar.call(btn, key, this);
                if (!rs) {
                    return;
                }
            }

            //如果是导出按钮，处理导出的数据
            //action: export_admin_action
            // select_across: 0
            // file_format: 0
            // index: 0
            // _selected_action: 15
            if (btn.isExport) {
                return this.exports(btn, key);
            }
            var self = this;
            if (btn.confirm) {
                this.$confirm(btn.confirm, '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    done.call(self);
                });
            } else {
                done.call(self);
            }

            function done() {
                if (btn.action_type) {
                    if (!parent.window.app.openTab) {
                        //没有在父框架内打开，就直接跳转
                        btn.action_type = 0;
                    }
                    //打开tab
                    switch (btn.action_type) {
                        case 0:
                            window.location.href = btn.action_url;
                            break;
                        case 1:
                            parent.window.app.openTab({
                                url: btn.action_url,
                                icon: btn.icon || 'fa fa-file',
                                name: btn.short_description,
                                breadcrumbs: []
                            });
                            break;
                        case 2:
                            window.open(btn.action_url)
                            break;
                    }
                } else {

                    //action执行 分为选中某些，和全表选中

                    var all = this.search.all;

                    var data = {
                        action: 'custom_action',
                        all: all,
                        key: key
                    }

                    if (all != 1) {
                        var rows = this.table.selection;
                        var ids = []
                        for (i in rows) {
                            ids.push(rows[i]._id);
                        }
                        data['ids'] = ids.join(',');
                    }
                    var self = this;
                    post(data, this, true).then(function (data) {
                        //刷新界面
                        self.refreshData();

                    });
                }
            }


        },
        clearSelect: function () {
            if (this.$refs.table) {
                this.$refs.table.clearSelection();
            }
            this.table.selection = [];
            this.toolbars.showAll = false;
        },
        selectAllBtnClick: function () {
            if (this.search.all == 1) {
                this.$refs.table.clearSelection();
                this.toolbars.showAll = false;
            }
            this.search.all = this.search.all == 0 ? 1 : 0
        },
        changeDate: function (dateList, field, type) {
            if (dateList) {
                if (type == 'date') {
                    this.search.filters[field + '__gte'] = dateList[0].format('yyyy-MM-dd');
                    this[field + '__lt'] = dateList[1].format('yyyy-MM-dd');
                } else if (type == 'datetime') {
                    this.search.filters[field + '__gte'] = dateList[0].format('yyyy-MM-dd hh:mm:ss' + window.tz);
                    this.search.filters[field + '__lt'] = dateList[1].format('yyyy-MM-dd hh:mm:ss' + window.tz);
                }
            } else {
                this.search.filters[field + '__gte'] = null;
                this.search.filters[field + '__lt'] = null;
            }
        }, onSearch: function () {
            this.search.current_page = 1;
            this.$nextTick(function () {
                this.onSubmit();
            });
        },
        showDropdown: function (e) {
            //elementui的坑
            var btn = e.target;
            if (btn.tagName == 'BUTTON') {
                //除非i的事件
                btn.getElementsByClassName('el-dropdown-link')[0].click();
            }
        },
        deleteData: function (id) {
            if (window.SIMPLEAPI && window.SIMPLEAPI.toolbar) {
                var rs = window.SIMPLEAPI.toolbar.call({}, 'delete', this);
                if (!rs) {
                    return;
                }
            }
            var self = this;

            var target = self;

            if (parent.app) {
                target = parent.app;
            }
            target.$confirm('此操作将永久删除，是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {

                var ids = [];
                if (id) {
                    ids.push(id);
                } else {
                    var rows = self.table.selection;

                    for (var item in rows) {
                        ids.push(rows[item]._id);
                    }
                }
                post({
                    action: 'delete',
                    ids: ids.join(',')
                }, self).then(res => {

                    if (res.state) {
                        self.$notify({
                            title: '成功',
                            message: res.msg,
                            type: 'success'
                        });
                        self.refreshData();

                    } else {
                        app.$notify.error({
                            title: '错误',
                            message: res.msg
                        });
                    }
                }).catch(res => {

                });
            }).catch(() => {

            });
        },
        openDialog: function (title, url) {
            this.dialog.url = url;
            this.dialog.title = title;
            this.dialog.visible = true;
        }

    },
    mounted: function () {
        //调用sdk
        if (window.SIMPLEAPI && window.SIMPLEAPI.init) {
            window.SIMPLEAPI.init(this);
        }
        if (parent.progress) {
            parent.progress.done();
        }
        if (window.messages) {
            window.messages.forEach(item => {
                setTimeout(function () {
                    app.$notify({
                        dangerouslyUseHTMLString: true,
                        message: item.msg,
                        type: item.tag
                    });
                }, 200)
            });
        }
    },
    created: function () {

        for (var i in window.seachModels) {
            this.search.filters[window.seachModels[i]] = ''
        }
        this.backupSearch = JSON.parse(JSON.stringify(this.search));
        this.onSubmit();

    }
});