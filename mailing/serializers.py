from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from mailing.models import Customer, Mailing, Message


class CustomerSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11, validators=[UniqueValidator(queryset=Customer.objects.all())])
    operator_code = serializers.CharField(max_length=3)
    tag = serializers.CharField(max_length=30)
    time_zone = serializers.CharField(max_length=30)

    class Meta:
        model = Customer
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    started_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", input_formats=["%d.%m.%Y %H:%M"])
    message_text = serializers.CharField(max_length=300)
    mailing_filter = serializers.CharField(max_length=30)
    ended_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", input_formats=["%d.%m.%Y %H:%M"])
    messages = serializers.SerializerMethodField()
    sent_messages = serializers.SerializerMethodField()

    class Meta:
        model = Mailing
        fields = '__all__'

    def get_messages(self, obj):
        return obj.messages.count()

    def get_sent_messages(self, obj):
        return obj.messages.filter(sent=True).count()


class MessageSerializer(serializers.ModelSerializer):
    sent_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", input_formats=["%d.%m.%Y %H:%M"])
    sent = serializers.BooleanField()
    customer = CustomerSerializer()
    mailing = MailingSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    sent_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", input_formats=["%d.%m.%Y %H:%M"])
    sent=serializers.BooleanField(read_only=True)

    class Meta:
        model = Message
        fields = ['sent_at', 'customer', 'mailing', 'sent']
