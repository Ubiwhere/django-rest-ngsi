# django-rest-ngsi #
__NGSI 10 serializers and viewsets__



Demonstration app in repo: __example__


__Instructions:__

__In your app's views.py:__

1. Import your models and rest_ngsi10's viewsets

        from django.http import HttpResponse
        from rest_ngsi10 import viewsets
        import models as example_models
    
    
2. Define your models' names. In the example case they were 'Example' and 'AnotherExample' 
    
        def get_model_class(name):
            if name == 'example':
                name = 'Example'
            elif name == 'anotherexample':
                name = 'AnotherExample'
            else:
                name = name.capitalize()
            if hasattr(example_models, name):
                return getattr(example_models, name)
                

    
3. Define these two methods used for the Context Entities endpoint

        class ContextEntities(viewsets.ContextEntities):
            def get_model_class(self, name):
                return get_model_class(name)
        
            def retrieve(self, request, slug):
                objects = self.get_object(request, slug)
                return self.get_ngsi_response(objects)
    
    

4. Define the retrieve method for the Context Entity detailed attribute endpoint
    
        class ContextEntitiesWithAttribute(ContextEntities):
        
            def retrieve(self, request, entity_slug, slug):
                objects = self.get_object(request, entity_slug)
                return self.get_ngsi_response(objects, attributes=[slug])
    
    
5. Add the ContextTypesMixin and map your models' type name to resource
    
        class ContextTypesMixin(object):
            TYPENAME_TO_RESOURCE = {
                'example':  example_models.Example(None, None),
                'anotherexample':  example_models.AnotherExample(None, None),
            }
            lookup_value_regex = r'|'.join( TYPENAME_TO_RESOURCE.keys() )
        
            def get_objects(self, request, slug):
                return self.TYPENAME_TO_RESOURCE[slug].list(request)
        
        
6. In the ContextTypes class-based view, map your typenames to your models and define the retrieve method like below
    
        class ContextTypes(viewsets.ContextTypes, ContextTypesMixin):
            TYPENAME_TO_MODEL = {
                'example': example_models.Example,
                'anotherexample': example_models.AnotherExample,
            }
        
            def get_context_types(self):
                return self.TYPENAME_TO_MODEL
        
            def retrieve(self, request, slug):
                objects = self.get_objects(request, slug)
                if isinstance(objects, HttpResponse):
                    return objects
                return self.get_ngsi_response(objects)
    
6. In the ContextTypesWithAttribute class just define the retrieve method

    
        class ContextTypesWithAttribute(viewsets.NgsiViewSet, ContextTypesMixin):
            def retrieve(self, request, type_slug, slug):
                objects = self.get_objects(request, type_slug)
                if isinstance(objects, HttpResponse):
                    return objects
                return self.get_ngsi_response(objects, attributes=[slug])


__In your app's urls.py:__

Include the default router from Django Rest Framework and map the desired routes to the url's

        from rest_framework.routers import DefaultRouter
        from .views import ContextEntities, ContextEntitiesWithAttribute
        from .views import ContextTypes, ContextTypesWithAttribute
        
        router = DefaultRouter()
        router.register(r'context_entities', ContextEntities, 'ContextEntities')
        router.register(r'context_types', ContextTypes, 'ContextTypes')
        router.register(r'query_context', QueryContext, 'QueryContext')
        router.register(r'context_subscriptions', ContextSubscriptions, 'ContextSubscriptions')
        
        urlpatterns = [
            url(r'^', include(router.urls)),
        ]



Author: Diogo Laginha (diogo.laginha.machado@gmail.com)
