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
    url(r'^dbindex/ab_sc$', views.ab_sc, name='dbindex'),
    url(r'^dbindex/dp_high_dim_viz$', views.dp_high_dim_viz, name='dbindex'),
    url(r'^dbindex/execution$', views.execution_d, name='dbindex'),
    url(r'^dbindex/ram_status$', views.ram_status, name='dbindex'),
    url(r'^dbindex/cpu_status$', views.cpu_status, name='dbindex'),
    url(r'^dbindex/submit$', views.db_submit, name='dbindex'),
    url(r'^dbindex/run_model$', views.run_model, name='dbindex'),
    url(r'^dbindex/get_log$', views.get_log, name='dbindex')


    # url(r'^hello/', 'FastLSH.views.hello'),
    # url(r'^home/', 'FastLSH.views.home'),

]


