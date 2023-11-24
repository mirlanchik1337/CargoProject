from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from api.cargo_app import serializers
from rest_framework.views import APIView
from api.cargo_app import models
from api.cargo_app.models import TrackCode, Status, Group
from api.cargo_app import serializers

from .filters import TrackCodeFilter


class TrackCodeList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = TrackCode.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = TrackCodeFilter
    search_fields = ['track_code']


class TrackCodeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = TrackCode.objects.all()


class TrackCodeGet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class TrackCodeUpdate(generics.UpdateAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class TrackCodeDelete(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class StatusList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer


class StatusDelete(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer
    lookup_field = 'id'


class CheckTrackCodeView(APIView):
    def post(self, request):
        track_code = request.data.get('track_code', None)

        if track_code is None:
            return Response({'error': 'Пожалуйста, предоставьте код'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            track_code = TrackCode.objects.get(track_code=track_code)
            status_tr = str(track_code.status.name_status)
            date_tr = str(track_code.date)
            return Response({'status': status_tr, 'date': date_tr}, status=HTTP_200_OK)
        except TrackCode.DoesNotExist:
            return Response({'error': 'Код не найден'}, status=HTTP_404_NOT_FOUND)


class GroupTrackCodeDelete(APIView):
    """
    API для удаления группы объектов по списку их идентификаторов.
    """

    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])

        # Проверяем, что ids - это список
        if not isinstance(ids, list):
            return Response({'error': 'Неверный формат данных. Ожидается список идентификаторов.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Удаляем объекты, соответствующие идентификаторам
        for id in ids:
            try:
                obj = TrackCode.objects.get(id=id)
                obj.delete()
            except TrackCode.DoesNotExist:
                # Возвращаем ошибку, если объект не найден
                return Response({'error': f'Объект с идентификатором {id} не найден.'},
                                status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Объекты успешно удалены.'}, status=status.HTTP_200_OK)


class GroupListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupListSerializer


class GroupUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        data = request.data
        if not isinstance(data, list):
            return Response({'error': 'Неверный формат данных. Ожидается список объектов.'},
                            status=status.HTTP_400_BAD_REQUEST)

        updated_objects = []
        for item in data:
            try:
                # Получаем объект по идентификатору
                obj = Group.objects.get(id=item.get('id'))

                # Обновляем объект с помощью сериализатора
                serializer = self.get_serializer(obj, data=item, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_objects.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Group.DoesNotExist:
                return Response({'error': f'Объект с идентификатором {item.get("id")} не найден.'},
                                status=status.HTTP_404_NOT_FOUND)

        return Response(updated_objects, status=status.HTTP_200_OK)


class GroupGet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupGetSerializer
    lookup_field = 'id'


class GroupUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    lookup_field = 'id'