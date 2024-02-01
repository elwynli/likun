.. title: 简历
.. slug: resume
.. date: 2024-01-23 23:44:08 UTC+08:00
.. tags: resume
.. category:
.. link:
.. description: 我的简历
.. type: text
.. hidetitle: True


.. raw:: html

    <div id='target'></div>
    <script src="https://cdn.jsdelivr.net/npm/underscore@1.13.6/underscore-umd-min.js"></script>
    <script type="text/template" id="tpl">
        <% _.each(obj, function(o, i, l){ %>
            <h3 class="is-size-4 mb-3"><%= o.name %></h3>
            <% _.each(o.items, function(o2, i2, l2){ %>
            <div class="columns">
                <div class="column is-one-third">
                    <%= o2.from %> - <%= o2.to %>
                </div>
                <div class="column content">
                    <h4><%= o2.org %></h4>
                    <% _.each(o2.roles, function(o3, i3, l3){ %>
                    <ul>
                        <li>
                            <strong><%= o3.name %></strong>
                            <ul>
                                <% if (o3.desc) %>
                                    <% _.each(o3.desc, function(o4, i4, l4){ %>
                                    <li><%= o4 %></li>
                                    <% }) %>
                                <% if (o3.desc) %>
                            </ul>
                        </li>
                    </ul>
                    <% }) %>
                </div>
            </div>
            <% }) %>
        <% }) %>
    </script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            var data = [{
                'name': '工作经验',
                'items': [{
                    'from': '2021 年 6 月',
                    'to': '现今',
                    'org': '华为终端BG',
                    'roles': [{'name': '资深项目管理', 'desc': ['通过运作PMO指导和激励服务变革项目集各项目的目标达成，以促进营销服能力提升；']},
                              {'name': '高级工程师', 'desc': ['通过建构CBG合规部合规数字化运营平台，整合内外数据与能力，管理合规各领域风险；']}]
                }, {
                    'from': '2019 年 1 月',
                    'to': '2021 年 6 月',
                    'org': '永拓管理咨询',
                    'roles': [{'name': '项目经理', 'desc': ['通过提供业务数字化转型解决方案使企业利润产生数倍增益；']},
                              {'name': '咨询师', 'desc': ['通过交付IT和业务流程体系文件解决业务问题；']}]
                }, {
                    'from': '2017 年 7 月',
                    'to': '2018 年 12 月',
                    'org': '拉普拉斯',
                    'roles': [{'name': '高级工程师', 'desc': ['通过证券投研平台与AI能力的集成，实现自动挖掘发现交易机会和捕获交易信号；',
                                                             '通过Bot池实现Token资讯的同步分发，反馈和跟踪；']},
                              {'name': '业务分析师', 'desc': ['撰写金融反欺诈项目行业洞察和解决方案以供项目投标；',
                                                             '编写银联数据平台解决方案供投资人路演。']}]
                }, {
                    'from': '2019 年 1 月',
                    'to': '2021 年 6 月',
                    'org': '招银科技',
                    'roles': [{'name': '高级工程师', 'desc': ['作为招行CMMI评估试点项目的项目经理，参照 CMMI 标准要求指导项目组通过 CMMI 三级认证',
                                                             '招行3G项目群的核心解耦、信用卡升级目的IT外购和IT人力资源采购项目',
                                                             '负责招行渠道条线一事通、会计部、审计部各项目项目管理等']},
                              {'name': '项目管理', 'desc': ['通过建设PMO体系，章程、制度、流程和工具，实现项目体系化运作',
                                                           '通过建立IT人力资源外包体系实现按需资源供应，增加灵活性，同时监控与量化外包风险',
                                                           '对IT外购项目持续运营，新增IT外购项目注册机制，盘点和监控存量IT外购项目，以实现评估优化闭环']},
                              {'name': '讲师', 'desc': ['通过TTT项目管理课程设计和授课给项目经理赋能',
                                                        '负责招行项目经理资格认证项目的项目管理、IT外购和人力外包模块']}]
                }, {
                    'from': '2007 年 6 月',
                    'to': '2008 年 12 月',
                    'org': '腾讯公司（实施）',
                    'roles': [{'name': '软件工程师', 'desc': ['设计与研发腾讯O线架构平台部ITIL系统及各子系统，以迎接管理不断增长的基础设施规模的挑战；',
                                                             '作为国内首批实践 Agile 的团队，沉淀研发知识经验，为O线研发流程标准化打样。']},
                              {'name': '团队负责人', 'desc': ['通过监控ITIL各子系统关键路径，确保项目群进展，跟踪和解决风险和问题以满足质量预期；',
                                                             '规划资源、建立团队，及人才的选用育留。']}]
                }, {
                    'from': '2005 年 6 月',
                    'to': '2007 年 5 月',
                    'org': '中广核集团',
                    'roles': [{'name': '软件工程师', 'desc': ['通过开发基于WFMC的工作流引擎以提升业务流程的执行效率，并降低流程的监控成本；',
                                                             '研发和维护项目框架、公共组件和工具集，供项目各模块使用以保证软件质量。']},
                              {'name': '项目组长', 'desc': ['负责中广核工程的软件系统研发和重点模块交付']}]
                }]
            },{
                'name': '教育经历',
                'items': [{
                    'from': '1998 年',
                    'to': '2002 年',
                    'org': '湖北大学',
                    'roles': [{'name': '数学与计算机系', 'desc': ['计算机软件专业']}]
                }, {
                    'from': '1995 年',
                    'to': '1998 年',
                    'org': '<a href="http://www.hbsszx.com/" target="_blank">沙市中学</a>',
                    'roles': []
                }]
            }];
            var template = _.template(document.querySelector("#tpl").innerHTML);
            document.querySelector("#target").outerHTML = template(data);
        });
    </script>

