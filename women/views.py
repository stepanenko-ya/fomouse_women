from django.http import HttpResponseNotFound, FileResponse
from django.views.generic import DetailView

from .models import Women
from .forms import AddPostForms, AddFilmData
from .utils import AddDataMixin, TemplateViewMixin, WomenListViewBase, menu


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'slug_name'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['template_name'] = self.template_name
        context['title'] = self.object
        return context

    def get_object(self, queryset=None):
        slug_name = self.kwargs['slug_name']
        return self.model.objects.prefetch_related('films').get(slug=slug_name)


class WomenMain(WomenListViewBase):
    cat_selected = 0


class WomenCategory(WomenListViewBase):
    pass


class AddPage(AddDataMixin):
    form_class = AddPostForms
    template_name = 'women/add_page.html'
    title = 'Add article'


class AddFilm(AddDataMixin):
    form_class = AddFilmData
    template_name = 'women/add_film.html'
    title = 'Add film'


class MainView(TemplateViewMixin):
    template_name = 'women/main.html'
    title = 'Main Page'


class ContactView(TemplateViewMixin):
    template_name = 'women/contacts.html'
    title = 'Contacts'


class AboutView(TemplateViewMixin):
    template_name = 'women/about.html'
    title = 'About the site'


def cv_view(request):
    return FileResponse(open('media/photos/cv.pdf', 'rb'))


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
