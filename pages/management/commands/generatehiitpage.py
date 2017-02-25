from django.core.management.base import BaseCommand
from django.template.loader import get_template
from pages.models import Page

class Command(BaseCommand):
    def handle(self, *args, **options):
        qs = Page.objects.all()
        if qs.count() < 2:
            html_ = get_template('pages/defaults/hiit-page-default.html').render({})
            Page.objects.create(
                    title= 'Welcome to Hiit Landing',
                    title_description='This site is an example of you can build easily with Hiit Landing. Check out the video for more.',
                    title_btn = 'Learn More',
                    title_btn_url = 'http://www.hiitlanding.com',
                    jumbotron_bg_color='#ffb400',
                    content = html_,
                    video_embed ='<div style="position:relative;height:0;padding-bottom:56.25%"><iframe src="https://www.youtube.com/embed/C0Hio55kZos?ecver=2" width="640" height="360" frameborder="0" style="position:absolute;width:100%;height:100%;left:0" allowfullscreen></iframe></div>',
                    featured=True,
                    active=True,
                    show_nav=False,
                    leave_capture=False,
                )