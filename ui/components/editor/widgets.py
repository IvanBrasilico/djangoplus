# -*- coding: utf-8 -*-
from djangoplus.ui.components.select.widgets import *


class FormattedTextarea(widgets.Textarea):

    class Media:
        js = ('/static/js/tinymce.min.js',)

    def render(self, name, value, attrs={}):
        attrs['class'] = 'form-control'
        html = super(FormattedTextarea, self).render(name, value, attrs)
        js = '''
            <script>
            tinymce.remove();
            tinymce.init({
              selector: '#id_%s',
              height: 300,
              menubar: false,
                plugins: [
                    'advlist autolink lists link image table textcolor',
                  ],
              toolbar: 'insert | undo redo |  formatselect | bold italic backcolor forecolor  | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | table',
                  content_css: []
            });
            </script>
        ''' % name
        return mark_safe('%s%s' % (html, js))

