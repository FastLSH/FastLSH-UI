from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parameterSet/$', views.parameterSet, name='parameterSet'),
    url(r'^execution/$', views.execution, name='execution'),
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^submit', views.submit),
    url(r'^download', views.download),
    url(r'^dbindex/$', views.dbIndex, name='dbindex'),
    url(r'^dbindex/parameterForm$', views.para_form, name='dbindex'),
    url(r'^dbindex/myMachine$', views.my_machine, name='dbindex')

    # url(r'^hello/', 'FastLSH.views.hello'),
    # url(r'^home/', 'FastLSH.views.home'),

]


