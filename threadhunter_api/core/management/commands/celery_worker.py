from django.core.management.base import BaseCommand
#from django.utils import autoreload
import shlex
import subprocess

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Starting Celery worker with autoreload...')

        #autoreload.run_with_reloader(
        #    self.run_worker
        #)

    def run_worker(self):
        cmd = 'celery -A config.celery_app worker --loglevel=info -P gevent --concurrency=1'
        #subprocess.call(shlex.split(cmd))