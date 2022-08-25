from mailing.models import Mailing


def get_mailings():
    return Mailing.objects.all()


def get_correct_mailings():
    return [item for item in get_mailings() if item.on_time() and item.get_unsent_messages().exists()]
