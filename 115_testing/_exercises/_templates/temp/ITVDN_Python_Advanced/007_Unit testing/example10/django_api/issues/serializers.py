____ django.contrib.auth ______ authenticate
____ rest_framework ______ serializers
____ issues.models ______ Issue


c_ IssueSerializer(serializers.ModelSerializer

    c_ Meta:
        model _ Issue
        fields _ '__all__'


c_ LoginSerializer(serializers.Serializer

    username _ serializers.SlugField()
    password _ serializers.CharField()

    ___ validate  attrs
        user _ authenticate(username_attrs['username'],
                            password_attrs['password'])
        __ not user:
            r_ serializers.ValidationError('Incorrect username/password')
        r_ user
