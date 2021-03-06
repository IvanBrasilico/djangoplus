# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import translation
from djangoplus.docs.doc import Documentation
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('task', nargs='*', help='...')
        parser.add_argument('--json', action='store_true', dest='json', default=False, help='')

    def handle(self, *args, **options):

        doc = Documentation()
        translation.activate(settings.LANGUAGE_CODE)

        task = (u' '.join([x.decode('utf-8') for x in options['task']])).strip()

        if task:
            if task.isdigit():
                index = int(task) - 1
                if len(doc.usecases) > index > 0:
                    usecase = doc.usecases[index]
                    print unicode(usecase)
                else:
                    print u'There is no task with index %s' % task
            else:
                selected_usecase = None
                for tmp in doc.usecases:
                    if tmp.name == task:
                        selected_usecase = tmp
                if selected_usecase:
                    print unicode(selected_usecase)
                else:
                    print u'There is no task named %s' % task
        else:
            if options.pop('json', False):
                print unicode(doc.as_json())
            else:
                print unicode(doc)