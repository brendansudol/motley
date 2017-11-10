from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from api.models import Location


class UserSerializer(ModelSerializer):
    locations = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'locations')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email', ''),
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = user.auth_token
                json = serializer.data
                json['token'] = token.key if token else 'NA'
                return Response(json, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LocationSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = Location
        fields = ('id', 'created', 'lat', 'lng', 'user')


class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
