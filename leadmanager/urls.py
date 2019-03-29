from rest_framework import routers
from .api import LeadViewSets

router = routers.DefaultRouter()
router.register('api/leadmanager', LeadViewSets, 'leadmanager')

urlpatterns = router.urls
