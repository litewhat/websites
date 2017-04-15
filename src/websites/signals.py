from celery.signals import task_success, task_prerun
from sites import tasks


@task_success.connect(sender=tasks.get_file_from_url)
def task_success_handler(sender=None, headers=None, body=None, **kwargs):
    _print('Task succeeded.')


@task_prerun.connect(sender=tasks.get_file_from_url)
def task_started_handler(sender=None, headers=None, body=None, **kwargs):
    _print('Task started.')


def _print(msg):
    print(msg)