.. title: 项目
.. slug: projects
.. date: 2024-01-24 00:40:43 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. hidetitle: True

.. raw:: html

    <div id='target'></div>
    <script src="https://cdn.jsdelivr.net/npm/underscore@1.13.6/underscore-umd-min.js"></script>
    <script type="text/template" id="tpl">
        <article>
            <h3 class="is-size-4">项目列表</h3>
            <table class="table is-striped is-narrow is-hoverable is-fullwidth">
                <tbody>
                    <% _.each(obj, function(o, i, l){ %>
                    <tr>
                        <td class="p-5">
                            <h5 class="title is-size-5">
                                <a href="<%= o.href %>" target="_blank"><%= o.name %></a>
                            </h5>
                            <div class="tags">
                                <% _.each(o.tags, function(o2, i2, l2){ %>
                                    <span class="tag"><%= o2 %></span>
                                <% }) %>
                            </div>
                            <p class="m-2"><%= o.desc %></p>
                        </td>
                        <td class="p-5" style="width: 120px">
                            <%= o.src %>
                        </td>
                    </tr>
                    <% }) %>
                </tbody>
            </table>
        </article>
    </script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            var data = [{
                'name': 'HW终端BG合规数字化平台',
                'href': '',
                'tags': ['Java', 'SpringBoot', 'Angular', 'HTML', 'CSS', 'JavaScript', 'GaussDB', 'Python', 'Flask', 'MySQL'],
                'desc': '业务合规风险防火墙。按合规领域和合规专项管理合规风险，异构数据 x 多模态AI x 算法，实现全面智能的合规风险管理机制。',
                'src': ''
            }, {
                'name': 'HW终端外包合作可视化平台',
                'href': '',
                'tags': ['Java', 'SpringBoot', 'Angular', 'HTML', 'CSS', 'JavaScript', 'GaussDB', 'MySQL', 'Tabular'],
                'desc': '外包合作业务数字化运营平台，规划、预算、合同、工时、成本、账单、产能，能效度量。',
                'src': ''
            }, {
                'name': 'HW终端财经精细化运营管理平台',
                'href': '',
                'tags': ['Java', 'SpringBoot', 'Angular', 'HTML', 'CSS', 'JavaScript', 'GaussDB', 'MySQL', 'Tabular', '帆软'],
                'desc': '财经数字化运营平台，主要服务中层管理以上和CEO办公室。',
                'src': ''
            }, {
                'name': '万联芯在线商城 Shop + ERP',
                'href': '//www.wlxmall.com',
                'tags': ['PHP', 'VO', 'Layui', 'HTML', 'CSS', 'JavaScript', 'MySQL', 'Elasticsearch'],
                'desc': 'IC元器件芯片领域类JD商城+ERP。搜索规则引擎。',
                'src': ''
            }, {
                'name': '高考与高校招生数据平台',
                'href': '',
                'tags': ['PHP', 'HTML', 'CSS', 'JavaScript', 'C#', 'OCR Service'],
                'desc': '高考数据类垂类 Top App 数据支持服务',
                'src': ''
            }, {
                'name': '超级计算机计算资源管理系统',
                'href': '',
                'tags': ['PHP', 'HTML', 'CSS', 'JavaScript', 'OpenStack', 'Python', 'Redis', 'MySQL', 'FastAPI'],
                'desc': '通过 OpenStack 项目集二开满足对租户计算资源（含 GPU）的管理和控制。',
                'src': ''
            }, {
                'name': '金融大数据反欺平台',
                'href': '',
                'tags': ['HTML', 'CSS', 'JavaScript', 'Python', 'NumPy', 'Pandas', 'Matplotlib'],
                'desc': '集成、管理、存储和分析金融数据，通过模型将金融账户、人、公司，交易行为数据集成分析，形成可交互报告，供金融反欺诈工作人员进行人工分析。<br>对标 IBM i2、Palantir Gotham，含基本实体视图，关联搜索，智能标记、智能表格、分析报告、反欺项目，底稿记录等。',
                'src': ''
            }, {
                'name': '证券投研数据管理平台',
                'href': '',
                'tags': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'MySQL', 'Node.js', 'MongoDB', 'MicroMsg', 'Elasticsearch'],
                'desc': '证券研究所合作项目，通过将多来源投研数据集中采集、存储、分析，供卖方产出投研报告，以服务于买方投资分析师。',
                'src': ''
            }, {
                'name': '量化智能投研平台',
                'href': '',
                'tags': ['C++', 'OrientDB', 'Wind SQL Server', 'DFCF MongoDB'],
                'desc': '量化投资平台，集成金融大数据，呈现数据间的逻辑（知识图谱），AI 捕获交易信号。',
                'src': ''
            }, {
                'name': 'IT外包管理系统',
                'href': '',
                'tags': ['Java', 'Spring', 'MySQL', 'EChart', 'Hadoop', 'WEUI'],
                'desc': '管理外包活动，服务银行管理层、外包管理部门、银监会，管理供应商公司、外购项目，项目人员等数据。',
                'src': ''
            }, {
                'name': '银行会计基础信息管理系统/对公信贷风险管理系统/现场审计系统/非现场审计系统/e报CMS/...',
                'href': '',
                'tags': ['HTML', 'CSS', 'JavaScript', 'C#', 'Asp.NET', 'DB2', 'Delphi', '...'],
                'desc': '银行部门各系统',
                'src': ''
            }, {
                'name': '运营技术中心 ITIL 系统',
                'href': '',
                'tags': ['HTML', 'CSS', 'JavaScript', 'C#', 'Asp.NET', 'MySQL', 'WinForm', 'C++', 'Com+'],
                'desc': 'ITIL框架低代码平台，含服务支持和服务交付两子系统。<br>包含ITIL 服务台、配置管理、事件管理、问题管理、变更管理、发布管理、服务级别管理、服务目录管理',
                'src': ''
            }, {
                'name': 'likun.cc',
                'href': '//likun.cc',
                'tags': ['HTML', 'CSS', 'JavaScript', 'Python', 'Jamstack', 'underscore.js'],
                'desc': '构建此网站的源代码',
                'src': '<a href="https://github.com/elwynli/likun" target="_blank"><span class="icon"><i class="fa fa-github-alt fa-2x" aria-hidden="true"></i></span></a>'
            }];
            var template = _.template(document.querySelector("#tpl").innerHTML);
            document.querySelector("#target").outerHTML = template(data);
        });
    </script>

