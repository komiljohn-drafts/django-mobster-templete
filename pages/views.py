from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class Home2PageView(TemplateView):
    template_name = 'index-2.html'
    
class BlogPageView(TemplateView):
    template_name = 'blog.html'

class BlogDetailsPageView(TemplateView):
    template_name = 'blog-details.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class UpdatesPageView(TemplateView):
    template_name = 'updates.html'
