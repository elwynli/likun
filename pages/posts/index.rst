.. title: 文章
.. slug: posts
.. date: 2024-01-24 00:41:51 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. hidetitle: True

.. raw:: html

    <style>
        article ul {
            list-style: unset;
        }
    </style>
    <div id='target'></div>
    <script src="https://cdn.jsdelivr.net/npm/underscore@1.13.6/underscore-umd-min.js"></script>
    <script type="text/template" id="tpl">
        <article>
            <% _.each(obj, function(o, i, l){ %>
            <h4 class="is-size-4"><%= o.category %></h4>
            <ul>
                <% _.each(o.post, function(o2, i2, l2){ %>
                <li><a href="<%= o2.href %>" target="_blank"><%= o2.name %></a></li>
                <% }) %>
            </ul>
            <% }) %>
        </article>
    </script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            var data = [{
                'category': '软件研发',
                'post': [{
                    'name': 'Likun.cc 的由来',
                    'href': 'https://likun.cc/posts/about-likun-cc/',
                    'tags': ['nikola', 'bulma'],
                    'desc': '',
                    'src': ''
                }]
            }];
            var template = _.template(document.querySelector("#tpl").innerHTML);
            document.querySelector("#target").outerHTML = template(data);
        });
    </script>
