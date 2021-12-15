from datetime import datetime, date

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View
from rest_framework import renderers, status

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DriverSerializer, VehicleSerializer, VehicleDriverSerializer
from .models import Driver, Vehicle


def index(request):
    return HttpResponse('<h1>Hi!</h1>')


class DriverView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Driver.objects.all()
        if 'created_at__gte' in request.GET:
            term = datetime.strptime(request.GET['created_at__gte'], '%d-%m-%Y').date()
            queryset = queryset.filter(created_at__date__gte=term)
        if 'created_at__lte' in request.GET:
            term = datetime.strptime(request.GET['created_at__lte'], '%d-%m-%Y').date()
            queryset = queryset.filter(created_at__date__lte=term)

        serializer_obj = DriverSerializer(instance=queryset, many=True)

        return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer_obj = DriverSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)


class DriverByIdView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            driver = Driver.objects.get(pk=kwargs['driver_id'])
        except Vehicle.DoesNotExist:
            raise Http404
        serializer_obj = DriverSerializer(instance=driver)

        return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            driver = Driver.objects.get(pk=kwargs['driver_id'])
        except Vehicle.DoesNotExist:
            raise Http404
        serializer_obj = DriverSerializer(driver, data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            driver = Driver.objects.get(pk=kwargs['driver_id'])
        except Vehicle.DoesNotExist:
            raise Http404
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Vehicle.objects.all()

        if 'with_drivers' in request.GET and request.GET['with_drivers'] in ['yes', 'no']:
            queryset = queryset.filter(driver__isnull=request.GET['with_drivers'] == 'no')

        serializer_obj = VehicleSerializer(instance=queryset, many=True)

        return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer_obj = VehicleSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)


class VehicleByIdView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(pk=kwargs['vehicle_id'])
        except Vehicle.DoesNotExist:
            raise Http404
        serializer_obj = VehicleSerializer(instance=vehicle)

        return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(pk=kwargs['vehicle_id'])
        except Vehicle.DoesNotExist:
            raise Http404
        serializer_obj = VehicleSerializer(vehicle, data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"status": "success", "data": serializer_obj.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(pk=kwargs['vehicle_id'])
        except Vehicle.DoesNotExist:
            raise Http404
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleSetDriverView(APIView):
    def post(self, request, *args, **kwargs):
        vehicle_driver_serializer = VehicleDriverSerializer(data=request.data)
        if vehicle_driver_serializer.is_valid():
            try:
                vehicle = Vehicle.objects.get(pk=kwargs['vehicle_id'])
            except Vehicle.DoesNotExist:
                raise Http404
            driver_id = vehicle_driver_serializer.data.get('driver')
            if driver_id is not None:
                try:
                    driver = Driver.objects.get(pk=driver_id)
                except Driver.DoesNotExist:
                    raise Http404
                vehicle.driver = driver
            else:
                vehicle.driver = None
            vehicle.save()
            return Response({"status": "success", "data": vehicle_driver_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": vehicle_driver_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)