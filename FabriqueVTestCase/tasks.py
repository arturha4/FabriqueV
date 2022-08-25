from __future__ import absolute_import
from FabriqueVTestCase.celery import app
from mailing.api import send_message
from mailing.services import get_correct_mailings


@app.task(name='check_database')
def check_database():
    for mailing in get_correct_mailings():
        for message in mailing.messages.all():
            if send_message(message.id, message.customer.phone, mailing.message_text) == 200:
                message.is_sent()
                message.set_sent_at_now()


app.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'check_database',
        'schedule': 10.0
    }
}
