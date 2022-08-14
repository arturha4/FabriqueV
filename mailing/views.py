from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from mailing.models import Customer, Mailing, Message
from mailing.serializers import CustomerSerializer, MailingSerializer, MessageSerializer, \
    MessageCreateSerializer


class CustomerList(APIView):
    """
    List all customers, or create new customer
    """

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
    Retrieve, update or delete a customer instance
    """

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MailingList(APIView):
    """
    List all mailing, or create new mailing
    """

    def get(self, request):
        mailing = Mailing.objects.all()
        serializer = MailingSerializer(mailing, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MailingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MailingDetail(APIView):
    """
    Retrieve, update or delete a mailing instance
    """

    def get_object(self, pk):
        try:
            return Mailing.objects.get(pk=pk)
        except Mailing.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mailing = self.get_object(pk=pk)
        serializer = MailingSerializer(mailing)
        return Response(serializer.data)

    def put(self, request, pk):
        mailing = self.get_object(pk=pk)
        serializer = MailingSerializer(mailing, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mailing = self.get_object(pk)
        mailing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageList(APIView):
    """
    List all messages, or create new message
    """
    def get(self, request):
        if 'mailing_id' in request.data:
            messages = Message.objects.filter(mailing_id=request.data['mailing_id'])
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
