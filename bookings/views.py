from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class BookingAPIView(APIView):
       
        permission_classes = [IsAuthenticated]
        def get_object(self, pk):
            
            try:
                return Booking.objects.get(pk=pk)
            except Booking.DoesNotExist:
                raise Http404
       
        def get(self, request, pk=None, format=None):
            current_user = request.user
            if pk:
                data = self.get_object(pk)
                serializer = BookingSerializer(data)
                return Response(serializer.data)

            else:
                data = Booking.objects.filter(user=current_user)
                serializer = BookingSerializer(data, many=True)
                if not data.exists():
                    return Response({'detail': 'No bookings found for the current user'}, status=status.HTTP_404_NOT_FOUND)

                return Response(serializer.data)
       
        def post(self, request, format=None):
            data = request.data
            serializer = BookingSerializer(data=data)

            
            serializer.is_valid(raise_exception=True)

            user = request.user  # Assuming you have user authentication
            listing = serializer.validated_data['listing']  
            date = serializer.validated_data['date']  

            if Booking.objects.filter(listing=listing,date=date).exists():
                return Response(
                {'message': 'You have already booked House tour.'},
               status=400
            )
            serializer.save(user=user)

            # Return Response to User

            response = Response()

            response.data = {
                'message': 'booking Created Successfully',
                'data': serializer.data
            }

            return response
       
        def patch(self, request, pk=None, format=None):
                
            todo_to_update = Booking.objects.get(pk=pk)

            serializer = BookingSerializer(instance=todo_to_update,data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()

            response.data = {
                'message': 'Booking Updated Successfully',
                'data': serializer.data
            }

            return response
      
        def delete(self, request, pk, format=None):
            emp_to_delete =  Booking.objects.get(pk=pk)

           
            emp_to_delete.delete()

            return Response({
                'message': 'Booking Deleted Successfully'
            })
        


class ContactUsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
       
        data = request.data.copy()

        user = request.user  
       
        data['user'] = user.id  # Assuming your serializer expects a user ID

        serializer = ContactusSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = {
            'message': 'Contact us Created Successfully',
            'data': serializer.data
        }

        return response
    

class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        serializer = PaymentSerializer(data=data)


        serializer.is_valid(raise_exception=True)

        serializer.save()
        response = Response()

        response.data = {
            'message': 'Payment  Successfully',
            'data': serializer.data
        }

        return response
    def get_object(self, booking_id=None):
            
            try:
                return payment.objects.get(booking__id=booking_id)
            except payment.DoesNotExist:
                raise Http404
        # get the employee by id otherwise all the employee
    def get(self, request, pk=None, format=None,booking_id=None):
            current_user = request.user
            if booking_id:
                try:
                    payments = payment.objects.get(booking__id=booking_id)
                    serializer = PaymentSerializer(payments)  # Use Payment model, not Booking
                    return Response(serializer.data)
                except payment.DoesNotExist:
                    return Response({'detail': 'Payment not found for the given listing'}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = payment.objects.filter(user=current_user)
                serializer = PaymentSerializer(data, many=True)
                if not data.exists():
                    return Response({'detail': 'False'}, status=status.HTTP_404_NOT_FOUND)

                return Response(serializer.data)