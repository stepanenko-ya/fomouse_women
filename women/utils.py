from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
from .models import Women

menu = [
    {'title': 'About site', 'url_name': 'about_site'},
    {'title': 'Add  article', 'url_name': 'add_page'},
    {'title': 'Add film', 'url_name': 'add_film'},
    {'title': 'Contacts', 'url_name': 'contact'},
]


class AddDataMixin(CreateView):
    form_class = None
    template_name = None
    title = None
    menu = menu
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu
        context['template_name'] = self.template_name
        context['title'] = self.title
        return context


class TemplateViewMixin(TemplateView):
    template_name = None
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = self.title
        return context


class WomenListViewBase(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'articles'
    cat_selected = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = self.get_title()
        context['cat_selected'] = self.cat_selected
        return context

    def get_queryset(self):
        queryset = Women.objects.select_related('category')
        if self.cat_selected:
            queryset = queryset.filter(category__slug=self.kwargs['cat_slug'])
        else:
            queryset = queryset.filter(is_published=True)
        return queryset

    def get_title(self):
        context = super().get_context_data()
        context.get('articles')

        if self.cat_selected:
            category = context.get('articles')[0].category
            return f"Category - {category}"
        return 'Main page'


