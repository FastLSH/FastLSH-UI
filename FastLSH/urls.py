#   Copyright 2017 Peter XU Yaohai
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.index, name='dbindex'),
    url(r'^instruction$', views.instruction, name='instruction'),
    url(r'^my_machine$', views.my_machine, name='my_machine'),

    url(r'^run_model$', views.run_model, name='run_model'),
    url(r'^submit$', views.db_submit, name='submit'),
    url(r'^get_log$', views.get_log, name='get_log'),
    url(r'^ram_status$', views.ram_status, name='ram_status'),
    url(r'^cpu_status$', views.cpu_status, name='cpu_status'),

    url(r'^dp_high_dim_viz$', views.dp_high_dim_viz, name='dp_high_dim_viz'),
    url(r'^get_data_series$', views.get_data_series, name='data_series'),

    url(r'^ab_prj$', views.ab_prj, name='ab_prj'),
    url(r'^ab_tm$', views.ab_tm, name='ab_tm'),
    url(r'^ab_sc$', views.ab_sc, name='ab_sc')

]



