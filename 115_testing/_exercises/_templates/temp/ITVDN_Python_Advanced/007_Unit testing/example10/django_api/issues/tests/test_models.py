____ django.conf ______ settings
____ django.contrib.auth.models ______ User
____ django.template.loader ______ render_to_string
____ django.test ______ TestCase, override_settings, tag
____ django.utils ______ timezone

____ issues.models ______ Issue


c_ IssueTestCase(TestCase

    ___ setUp
        issue _ Issue.objects.create(
            name_'test name',
            description_'test desc',
            due_date_timezone.now().date() + timezone.timedelta(days_2),
        )

    @tag('user')
    ___ test_str_method
        aE..(st.(issue), issue.name)

    @tag('user')
    ___ test_set_due_date
        old_value _ issue.due_date
        new_value _ timezone.now().date()

        aE..(issue.due_date, old_value)

        issue.set_due_date(new_value)

        aE..(issue.due_date, new_value)
        issue.refresh_from_db()
        aE..(issue.due_date, old_value)

    @override_settings(DEBUG_True)
    ___ test_foo_prod_decorator
        aE..(issue.foo(), issue.name)

    @override_settings(DEBUG_False)
    ___ test_foo_debug_decorator
        aE..(issue.foo(), 'stub')

    ___ test_foo_prod_with
        w__ settings(DEBUG_True
            aE..(issue.foo(), issue.name)

    ___ test_foo_debug_with
        w__ settings(DEBUG_False
            aE..(issue.foo(), 'stub')

    ___ test_modify_settings
        aE..(issue.bar(), issue.name)

        modify_rules _ {'remove': settings.ADMINS_NAME}
        w__ modify_settings(CUSTOM_LIST_modify_rules
            aE..(issue.bar(), 'stub')

    ___ test_templates
        w__ assertTemplateUsed('test_template.html'
            render_to_string('test_template.html')
        w__ assertTemplateNotUsed('test_template.html'
            render_to_string('login.html')

    @tag('user')
    ___ test_queryset
        User.objects.create(username_'t')
        total _ User.objects.all().count()

        ___ get_users_with_groups(
            results _ []
            total _ User.objects.all().count()
            for user in User.objects.all(
                results.append({
                    'user': user,
                    'groups': list(user.groups.all())
                    # 'groups': list(user.groups.all())
                })
            r_ total, results

        assertNumQueries(2 + total, get_users_with_groups)
