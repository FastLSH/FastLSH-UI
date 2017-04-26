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
    url(r'^dbindex/myMachine$', views.my_machine, name='dbindex'),
    url(r'^dbindex/instruction$', views.instruction, name='dbindex'),
    url(r'^dbindex/ab_prj$', views.ab_prj, name='dbindex'),
    url(r'^dbindex/ab_tm$', views.ab_tm, name='dbindex'),
    url(r'^dbindex/ab_sc$', views.ab_sc, name='dbindex')

    # url(r'^hello/', 'FastLSH.views.hello'),
    # url(r'^home/', 'FastLSH.views.home'),

]


