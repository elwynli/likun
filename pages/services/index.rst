.. title: 服务
.. slug: services
.. date: 2024-01-24 00:41:25 UTC+08:00
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
            <h3 class="is-size-4">服务列表</h3>
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
                                    <span class="tag is-primary"><%= o2 %></span>
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
                'name': 'a. 软件相关问题解答服务',
                'href': '',
                'tags': ['免费服务'],
                'desc': '与软件有关的疑难和疑问，如软件选型、软件开发、研发管理相关的问题，可通过我的微信公众号或知乎平台向我提问。',
                'src': ''
            }, {
                'name': 'b. 软件相关问题咨询服务',
                'href': '',
                'tags': ['付费服务'],
                'desc': '与软件有关的问题、IT开发需求、软件定制，可电子邮件联系我，按问题决策点和规模，我会提供服务流程进行评估，并提供咨询服务。',
                'src': ''
            }];
            var template = _.template(document.querySelector("#tpl").innerHTML);
            document.querySelector("#target").outerHTML = template(data);
        });
    </script>
