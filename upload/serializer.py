from rest_framework import serializers

from upload.models import UploadModel

class UploadModelSerializer(serializers.ModelSerializer):
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault(),write_only=True)

    class Meta:
        model = UploadModel
        # fields = ('id','name','image','creator')
        fields = ('id','image')

    def validate(self,validated_data):
        if not validated_data.get('image', False):
            # validated_data['name'] = ''
            validated_data['image'] = self.initial_data.get('file', 'Data retrival error')
        return validated_data