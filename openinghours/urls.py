from django.conf.urls import url
from openinghours.views import CurrentlyOpenView
from openinghours.views_edit import OpeningHoursEditView
from django.contrib.auth.decorators import permission_required


urlpatterns = [
     url(r'^$', CurrentlyOpenView.as_view(),
         name='openinghours_currently_open'),
     url(r'^edit/(?P<pk>[0-9]+)$', permission_required('is_staff')(OpeningHoursEditView.as_view()),
         name='openinghours_edit'),
]


