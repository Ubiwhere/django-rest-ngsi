from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_ngsi10 import viewsets
import models as example_models


def get_model_class(name):
    if name == 'example':
        name = 'Example'
    elif name == 'anotherexample':
        name = 'AnotherExample'
    else:
        name = name.capitalize()
    if hasattr(example_models, name):
        return getattr(example_models, name)


class ContextEntities(viewsets.ContextEntities):
    def get_model_class(self, name):
        return get_model_class(name)

    def retrieve(self, request, slug):
        objects = self.get_object(request, slug)
        return self.get_ngsi_response(objects)


class ContextEntitiesWithAttribute(ContextEntities):

    def retrieve(self, request, entity_slug, slug):
        objects = self.get_object(request, entity_slug)
        return self.get_ngsi_response(objects, attributes=[slug])


class ContextTypesMixin(object):
    TYPENAME_TO_RESOURCE = {
        'example':  example_models.Example(None, None),
        'anotherexample':  example_models.AnotherExample(None, None),
    }
    lookup_value_regex = r'|'.join( TYPENAME_TO_RESOURCE.keys() )

    def get_objects(self, request, slug):
        return self.TYPENAME_TO_RESOURCE[slug].list(request)


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


class ContextTypesWithAttribute(viewsets.NgsiViewSet, ContextTypesMixin):

    def retrieve(self, request, type_slug, slug):
        objects = self.get_objects(request, type_slug)
        if isinstance(objects, HttpResponse):
            return objects
        return self.get_ngsi_response(objects, attributes=[slug])


class ContextSubscriptions(viewsets.ContextSubscriptions):
    def get_model_class(self, name):
        return get_model_class(name)


class QueryContext(viewsets.QueryContext):
    def get_model_class(self, name):
        return get_model_class(name)

    def create(self, request):
        return super(QueryContext, self).create(request)
