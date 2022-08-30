from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Question


@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'category'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Question
         fields = [
             'question_text',
             'pub_date',
         ]