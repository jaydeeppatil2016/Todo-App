from rest_framework  import serializers
from api.models import todo_task
#import model class in api 

#create serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo_task
        fields = '__all__'
