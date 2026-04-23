from django.contrib.auth.models import AbstractUser,User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings


class RegisterModelSerializer(serializers.ModelSerializer):
    # 第一步：先定义序列化器
    # wright_only : 为True代表仅输入，不输出
    password_confirm = serializers.CharField(label='确认密码',
                                             min_length=6,
                                             max_length=20,
                                             help_text='确认密码',
                                             write_only=True,
                                             error_messages={
                                                 'min_length':'仅允许最短6位',
                                                 'max_length':'仅允许最大长度20'
                                             })
    # read_only为True则表示序列化输出
    token = serializers.CharField(label="生成token",read_only=True,help_text="生成token")

    username = serializers.CharField(label="用户名", help_text="用户名",required=True, min_length=3,max_length=20,allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    class Meta:
        model = User
        # 定义序列化和反序列化字段
        fields = ['id','username','password','password_confirm','token']
        # 覆盖特性
        # extra_kwargs = {
        #     'username': {
        #         'label':'用户名',
        #         'min_length':3,
        #         'max_length':20,
        #         'error_messages':{
        #             'min_length':'最小支持6位',
        #             'max_length':'最大支持20位',
        #             'unique': '已存在'
        #         }
        #     }
        # }

    def validate(self,attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('两次输入密码不一致')
        return attrs

    def create(self, validated_data):
        # 先校验前端传过来的数据，存入数据库时，没有password_confirm这个字段，所以剔除掉
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)

        # 手动创建token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user

