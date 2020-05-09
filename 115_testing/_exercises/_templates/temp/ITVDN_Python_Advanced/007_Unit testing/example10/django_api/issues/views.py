____ django.contrib.auth ______ login
____ rest_framework.decorators ______ action
____ rest_framework.permissions ______ IsAuthenticated
____ rest_framework.response ______ Response
____ rest_framework.viewsets ______ ModelViewSet, GenericViewSet
____ rest_framework.views ______ View

____ issues.models ______ Issue
____ issues.serializers ______ IssueSerializer, LoginSerializer


c_ IssueModelViewSet(ModelViewSet):

    model _ Issue
    permission_classes _ (IsAuthenticated,)
    serializer_class _ IssueSerializer
    queryset _ Issue.objects.all()


c_ AuthView(GenericViewSet):

    serializer_class _ LoginSerializer

    @action(detail_False, serializer_class_LoginSerializer, methods_['post'])
    ___ login  request, *args, **kwargs):
        serializer _ serializer_class(data_request.data)
        serializer.is_valid(raise_exception_True)
        user _ serializer.validated_data
        login(request, user)
        r_ Response({'details': 'You successfully logged in'})

    @action(detail_False, serializer_class_None)
    ___ logout
        r_ Response({'details': 'You successfully logged out'})
