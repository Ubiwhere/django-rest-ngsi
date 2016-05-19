from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ContextEntities, ContextEntitiesWithAttribute
from .views import ContextTypes, ContextTypesWithAttribute
from .views import QueryContext
from .views import ContextSubscriptions

router = DefaultRouter()
router.register(r'context_entities', ContextEntities, 'ContextEntities')
router.register(r'context_types', ContextTypes, 'ContextTypes')
router.register(r'query_context', QueryContext, 'QueryContext')
router.register(r'context_subscriptions', ContextSubscriptions, 'ContextSubscriptions')

urlpatterns = [
    url(r'^', include(router.urls)),
]