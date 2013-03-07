# -*- coding: UTF-8 -*-
"""
nav_bar.py
"""
__author__ = "xiechao"
__author_email__ = "xiechao06@gmail.com"
__version__ = "0.9.0"

import types
from jinja2 import Template


ul_tpl = """

<div class="navbar">
  <div class="navbar-inner">
    <div class="brand">{{ project_name }}</div>
    <ul = class="nav">
    {% for nav_link in nav_links %}
      {% if nav_link.enabler() %}
          <li class="{{highlight_class}}">
            <a href="#">
                <strong>{{nav_link.anchor}}</strong>
            </a>
          </li>
      {% else %}
          <li class="{{normal_class}}">
            <a href="{{nav_link.url}}">{{nav_link.anchor}}</a>
          </li>
      {% endif %}
    {% endfor %}
    </ul>
  </div>
</div>

"""

class NavLink(object):

    def __init__(self, url, anchor, enabler, permissions):
        self.anchor = anchor
        self.enabler = enabler
        self.permissions = permissions
        self.__url = url

    @property
    def url(self):
        if isinstance(self.__url, types.FunctionType):
            return self.__url()
        return self.__url
        
class NavBar(object):

    def __init__(self, project_name=""):
        self.project_name = project_name
        self.__all_nav_links = []
    
    def register(self, url, anchor, enabler, permissions=[]):
        self.__all_nav_links.append(NavLink(url, anchor, enabler, permissions))
        
    @property
    def nav_links(self):
        for nav_link in self.__all_nav_links:
            if all(perm.can() for perm in nav_link.permissions):
                yield nav_link
    
    def as_ul(self, highlight_class="", normal_class=""):
        template = Template(ul_tpl)
        return template.render(nav_links=self.nav_links,
                project_name=self.project_name,
                highlight_class=highlight_class,
                normal_class=normal_class)

if __name__ == "__main__":
    nav_bar = NavBar()
    
    class FakePermission(object):
        def can(self):
            return False

    highlight = 2
    nav_bar.register("a.com", "a", (lambda: highlight==0))
    nav_bar.register("b.com", "b", (lambda: highlight==1))
    nav_bar.register("c.com", "c", (lambda: highlight==2))
    nav_bar.register("invisible.com", "invisible", lambda: highlight==3, permissions=[FakePermission()])
    
    print nav_bar.as_ul("highlight")
        
