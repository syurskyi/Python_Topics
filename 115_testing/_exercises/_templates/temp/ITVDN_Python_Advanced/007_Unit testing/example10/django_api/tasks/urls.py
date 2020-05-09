____ django.contrib ______ admin
____ django.urls ______ pa__, include

____ issues.views ______ IssueModelViewSet, AuthView

____ rest_framework.routers ______ DefaultRouter

router _ DefaultRouter()
router.register('issues', IssueModelViewSet, base_name_'issues')
router.register('auth', AuthView, base_name_'auth')

urlpatterns _ [
    pa__('admin/', admin.site.urls),
    pa__('api/', include(router.get_urls())),
]
