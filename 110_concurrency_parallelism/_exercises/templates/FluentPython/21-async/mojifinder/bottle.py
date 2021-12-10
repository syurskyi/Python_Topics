#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bottle is a fast and simple micro-framework for small web applications. It
offers request dispatching (Routes) with url parameter support, templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines - all in a single file and with no dependencies other than the
Python Standard Library.

Homepage and documentation: http://bottlepy.org/

Copyright (c) 2016, Marcel Hellkamp.
License: MIT (see LICENSE for details)
"""

from __future__ ______ with_statement

__author__ = 'Marcel Hellkamp'
__version__ = '0.12.19'
__license__ = 'MIT'

# The gevent server adapter needs to patch some modules before they are imported
# This is why we parse the commandline parameters here but handle them later
__ _____ __ ______
    from optparse ______ OptionParser
    _cmd_parser = OptionParser(usage="usage: %prog [options] package.module:app")
    _opt = _cmd_parser.add_option
    _opt("--version", action="store_true", help="show version number.")
    _opt("-b", "--bind", metavar="ADDRESS", help="bind socket to ADDRESS.")
    _opt("-s", "--server", default='wsgiref', help="use SERVER as backend.")
    _opt("-p", "--plugin", action="append", help="install additional plugin/s.")
    _opt("--debug", action="store_true", help="start server in debug mode.")
    _opt("--reload", action="store_true", help="auto-reload on file changes.")
    _cmd_options, _cmd_args = _cmd_parser.parse_args()
    __ _cmd_options.server a.. _cmd_options.server.startswith('gevent'):
        ______ gevent.monkey; gevent.monkey.patch_all()

______ base64, cgi, email.utils, functools, hmac, i__, mimetypes,\
        os, re, subprocess, sys, tempfile, _, t__, warnings, hashlib

from datetime ______ date __ datedate, datetime, timedelta
from tempfile ______ TemporaryFile
from traceback ______ format_exc, print_exc
from inspect ______ getargspec
from unicodedata ______ normalize


___ from simplejson ______ dumps __ json_dumps, loads __ json_lds
except ImportError: # pragma: no cover
    ___ from json ______ dumps __ json_dumps, loads __ json_lds
    except ImportError:
        ___ from django.utils.simplejson ______ dumps __ json_dumps, loads __ json_lds
        except ImportError:
            ___ json_dumps(data):
                raise ImportError("JSON support requires Python 2.6 or simplejson.")
            json_lds = json_dumps



# We now try to fix 2.5/2.6/3.1/3.2 incompatibilities.
# It ain't pretty but it works... Sorry ___ the mess.

py   = sys.version_info
py3k = py >= (3, 0, 0)
py25 = py <  (2, 6, 0)
py31 = (3, 1, 0) <= py < (3, 2, 0)

# Workaround ___ the missing "as" keyword __ py3k.
___ _e(): r_ sys.exc_info()[1]

# Workaround ___ the "print is a keyword/function" Python 2/3 dilemma
# and a fallback ___ mod_wsgi (resticts stdout/err attribute access)
___
    _stdout, _stderr = sys.stdout.write, sys.stderr.write
except IOError:
    _stdout = lambda x: sys.stdout.write(x)
    _stderr = lambda x: sys.stderr.write(x)

# Lots of stdlib and builtin differences.
__ py3k:
    ______ http.client __ httplib
    ______ _thread __ thread
    from urllib.parse ______ urljoin, SplitResult __ UrlSplitResult
    from urllib.parse ______ urlencode, quote __ urlquote, unquote __ urlunquote
    urlunquote = functools.partial(urlunquote, encoding='latin1')
    from http.cookies ______ SimpleCookie
    __ py >= (3, 3, 0):
        from collections.abc ______ MutableMapping __ DictMixin
        from types ______ ModuleType __ new_module
    else:
        from collections ______ MutableMapping __ DictMixin
        from imp ______ new_module
    ______ pickle
    from io ______ BytesIO
    from configparser ______ ConfigParser
    basestring = s..
    unicode = s..
    json_loads = lambda s: json_lds(touni(s))
    callable = lambda x: hasattr(x, '__call__')
    imap = map
    ___ _raise(*a): raise a[0](a[1]).with_traceback(a[2])
else: # 2.x
    ______ httplib
    ______ thread
    from urlparse ______ urljoin, SplitResult __ UrlSplitResult
    from urllib ______ urlencode, quote __ urlquote, unquote __ urlunquote
    from Cookie ______ SimpleCookie
    from i__ ______ imap
    ______ cPickle __ pickle
    from imp ______ new_module
    from StringIO ______ StringIO __ BytesIO
    from ConfigParser ______ SafeConfigParser __ ConfigParser
    __ py25:
        msg  = "Python 2.5 support may be dropped in future versions of Bottle."
        warnings.warn(msg, DeprecationWarning)
        from UserDict ______ DictMixin
        ___ next(it): r_ it.next()
        bytes = s..
    else: # 2.6, 2.7
        from collections ______ MutableMapping __ DictMixin
    unicode = unicode
    json_loads = json_lds
    eval(compile('def _raise(*a): raise a[0], a[1], a[2]', '<py3fix>', 'exec'))

# Some helpers ___ string/byte handling
___ tob(s, enc='utf8'):
    r_ s.encode(enc) __ isinstance(s, unicode) else bytes(s)
___ touni(s, enc='utf8', err='strict'):
    r_ s.decode(enc, err) __ isinstance(s, bytes) else unicode(s)
tonat = touni __ py3k else tob

# 3.2 fixes cgi.FieldStorage to accept bytes (which makes a lot of sense).
# 3.1 needs a workaround.
__ py31:
    from io ______ TextIOWrapper
    c_ NCTextIOWrapper(TextIOWrapper):
        ___ close pass # Keep wrapped buffer open.


# A bug __ functools causes it to break if the wrapper is an instance method
___ update_wrapper(wrapper, wrapped, *a, **ka):
    ___ functools.update_wrapper(wrapper, wrapped, *a, **ka)
    except AttributeError: pass



# These helpers are used at module level and need to be defined first.
# And yes, I know PEP-8, but sometimes a lower-case classname makes more sense.

___ depr(message, hard=False):
    warnings.warn(message, DeprecationWarning, stacklevel=3)

___ makelist(data): # This is just to handy
    __ isinstance(data, (tuple, list, set, dict)): r_ list(data)
    elif data: r_ [data]
    else: r_ []


c_ DictProperty(object):
    ''' Property that maps to a key in a local dict-like attribute. '''
    ___ -  attr, key=N.., read_only=False):
        attr, key, read_only = attr, key, read_only

    ___ __call__ func):
        functools.update_wrapper func, updated=[])
        getter, key = func, key or func.__name__
        r_ self

    ___ __get__ obj, cls):
        __ obj __ N..: r_ self
        key, storage = key, getattr(obj, attr)
        __ key n.. __ storage: storage[key] = getter(obj)
        r_ storage[key]

    ___ __set__ obj, value):
        __ read_only: raise AttributeError("Read-Only property.")
        getattr(obj, attr)[key] = value

    ___ __delete__ obj):
        __ read_only: raise AttributeError("Read-Only property.")
        del getattr(obj, attr)[key]


c_ cached_property(object):
    ''' A property that is only computed once per instance and then replaces
        itself with an ordinary attribute. Deleting the attribute resets the
        property. '''

    ___ -  func):
        __doc__ = getattr(func, '__doc__')
        func = func

    ___ __get__ obj, cls):
        __ obj __ N..: r_ self
        value = obj.__dict__[func.__name__] = func(obj)
        r_ value


c_ lazy_attribute(object):
    ''' A property that caches itself to the class object. '''
    ___ -  func):
        functools.update_wrapper func, updated=[])
        getter = func

    ___ __get__ obj, cls):
        value = getter(cls)
        setattr(cls, __name__, value)
        r_ value






###############################################################################
# Exceptions and Events ########################################################
###############################################################################


c_ BottleException(Exception):
    """ A base class for exceptions used by bottle. """
    pass






###############################################################################
# Routing ######################################################################
###############################################################################


c_ RouteError(BottleException):
    """ This is a base class for all routing related exceptions """


c_ RouteReset(BottleException):
    """ If raised by a plugin or request handler, the route is reset and all
        plugins are re-applied. """

c_ RouterUnknownModeError(RouteError): pass


c_ RouteSyntaxError(RouteError):
    """ The route parser found something not supported by this router. """


c_ RouteBuildError(RouteError):
    """ The route could not be built. """


___ _re_flatten(p):
    ''' Turn all capturing groups in a regular expression pattern into
        non-capturing groups. '''
    __ '(' n.. __ p: r_ p
    r_ re.sub(r'(\\*)(\(\?P<[^>]+>|\((?!\?))',
        lambda m: m.group(0) __ l..(m.group(1)) @ 2 else m.group(1) + '(?:', p)


c_ Router(object):
    ''' A Router is an ordered collection of route->target pairs. It is used to
        efficiently match WSGI requests against a number of routes and return
        the first target that satisfies the request. The target may be anything,
        usually a string, ID or callable object. A route consists of a path-rule
        and a HTTP method.

        The path-rule is either a static path (e.g. `/contact`) or a dynamic
        path that contains wildcards (e.g. `/wiki/<page>`). The wildcard syntax
        and details on the matching order are described in docs:`routing`.
    '''

    default_pattern = '[^/]+'
    default_filter  = 're'

    #: The current CPython regexp implementation does not allow more
    #: than 99 matching groups per regular expression.
    _MAX_GROUPS_PER_PATTERN = 99

    ___ -  strict=False):
        rules      # list # All rules __ order
        _groups  = {} # index of regexes to find them __ dyna_routes
        builder  = {} # Data structure ___ the url builder
        static   = {} # Search structure ___ static routes
        dyna_routes   = {}
        dyna_regexes  = {} # Search structure ___ dynamic routes
        #: If true, static routes are no longer checked first.
        strict_order = strict
        filters = {
            're':    lambda conf:
                (_re_flatten(conf or default_pattern), N.., N..),
            'int':   lambda conf: (r'-?\d+', in., lambda x: s..(in.(x))),
            'float': lambda conf: (r'-?[\d.]+', float, lambda x: s..(float(x))),
            'path':  lambda conf: (r'.+?', N.., N..)}

    ___ add_filter name, func):
        ''' Add a filter. The provided function is called with the configuration
        string as parameter and must return a (regexp, to_python, to_url) tuple.
        The first element is a string, the last two are callables or None. '''
        filters[name] = func

    rule_syntax = re.compile('(\\\\*)'\
        '(?:(?::([a-zA-Z_][a-zA-Z_0-9]*)?()(?:#(.*?)#)?)'\
          '|(?:<([a-zA-Z_][a-zA-Z_0-9]*)?(?::([a-zA-Z_]*)'\
            '(?::((?:\\\\.|[^\\\\>]+)+)?)?)?>))')

    ___ _itertokens rule):
        offset, prefix = 0, ''
        ___ match __ rule_syntax.finditer(rule):
            prefix += rule[offset:match.s..]
            g = match.groups()
            __ l..(g[0])@2: # Escaped wildcard
                prefix += match.group(0)[l..(g[0]):]
                offset = match.end()
                continue
            __ prefix:
                yield prefix, N.., N..
            name, filtr, conf = g[4:7] __ g[2] __ N.. else g[1:4]
            yield name, filtr or 'default', conf or N..
            offset, prefix = match.end(), ''
        __ offset <= l..(rule) or prefix:
            yield prefix+rule[offset:], N.., N..

    ___ add rule, method, target, name=N..):
        ''' Add a new rule or replace the target for an existing rule. '''
        anons     = 0    # Number of anonymous wildcards found
        keys        # list   # Names of keys
        pattern   = ''   # Regular expression pattern with named groups
        filters     # list   # Lists of wildcard input filters
        builder     # list   # Data structure ___ the URL builder
        is_static = True

        ___ key, mode, conf __ _itertokens(rule):
            __ mode:
                is_static = False
                __ mode == 'default': mode = default_filter
                mask, in_filter, out_filter = filters[mode](conf)
                __ n.. key:
                    pattern += '(?:@)' @ mask
                    key = 'anon%d' @ anons
                    anons += 1
                else:
                    pattern += '(?P<@>@)' @ (key, mask)
                    keys.a.. (key)
                __ in_filter: filters.a.. ((key, in_filter))
                builder.a.. ((key, out_filter or s..))
            elif key:
                pattern += re.escape(key)
                builder.a.. ((N.., key))

        builder[rule] = builder
        __ name: builder[name] = builder

        __ is_static a.. n.. strict_order:
            static.setdefault(method, {})
            static[method][build(rule)] = (target, N..)
            r_

        ___
            re_pattern = re.compile('^(@)$' @ pattern)
            re_match = re_pattern.match
        except re.error:
            raise RouteSyntaxError("Could not add Route: @ (@)" @ (rule, _e()))

        __ filters:
            ___ getargs(path):
                url_args = re_match(path).groupdict()
                ___ name, wildcard_filter __ filters:
                    ___
                        url_args[name] = wildcard_filter(url_args[name])
                    except ValueError:
                        raise HTTPError(400, 'Path has wrong format.')
                r_ url_args
        elif re_pattern.groupindex:
            ___ getargs(path):
                r_ re_match(path).groupdict()
        else:
            getargs = N..

        flatpat = _re_flatten(pattern)
        whole_rule = (rule, flatpat, target, getargs)

        __ (flatpat, method) __ _groups:
            __ DEBUG:
                msg = 'Route <@ @> overwrites a previously defined route'
                warnings.warn(msg @ (method, rule), RuntimeWarning)
            dyna_routes[method][_groups[flatpat, method]] = whole_rule
        else:
            dyna_routes.setdefault(method, []).a.. (whole_rule)
            _groups[flatpat, method] = l..(dyna_routes[method]) - 1

        _compile(method)

    ___ _compile method):
        all_rules = dyna_routes[method]
        comborules = dyna_regexes[method]   # list
        maxgroups = _MAX_GROUPS_PER_PATTERN
        ___ x __ r.. 0, l..(all_rules), maxgroups):
            some = all_rules[x:x+maxgroups]
            combined = (flatpat ___ (_, flatpat, _, _) __ some)
            combined = '|'.join('(^%s$)' @ flatpat ___ flatpat __ combined)
            combined = re.compile(combined).match
            rules = [(target, getargs) ___ (_, _, target, getargs) __ some]
            comborules.a.. ((combined, rules))

    ___ build _name, *anons, **query):
        ''' Build an URL by filling the wildcards in a rule. '''
        builder = builder.get(_name)
        __ n.. builder: raise RouteBuildError("No route with that name.", _name)
        ___
            ___ i, value __ enumerate(anons): query['anon%d'@i] = value
            url = ''.join([f(query.pop(n)) __ n else f ___ (n,f) __ builder])
            r_ url __ n.. query else url+'?'+urlencode(query)
        except KeyError:
            raise RouteBuildError('Missing URL argument: %r' @ _e().args[0])

    ___ match environ):
        ''' Return a (target, url_agrs) tuple or raise HTTPError(400/404/405). '''
        verb = environ['REQUEST_METHOD'].upper()
        path = environ['PATH_INFO'] or '/'
        target = N..
        __ verb == 'HEAD':
            methods = ['PROXY', verb, 'GET', 'ANY']
        else:
            methods = ['PROXY', verb, 'ANY']

        ___ method __ methods:
            __ method __ static a.. path __ static[method]:
                target, getargs = static[method][path]
                r_ target, getargs(path) __ getargs else {}
            elif method __ dyna_regexes:
                ___ combined, rules __ dyna_regexes[method]:
                    match = combined(path)
                    __ match:
                        target, getargs = rules[match.lastindex - 1]
                        r_ target, getargs(path) __ getargs else {}

        # No matching route found. Collect alternative methods ___ 405 response
        allowed = set([])
        nocheck = set(methods)
        ___ method __ set(static) - nocheck:
            __ path __ static[method]:
                allowed.add(method)
        ___ method __ set(dyna_regexes) - allowed - nocheck:
            ___ combined, rules __ dyna_regexes[method]:
                match = combined(path)
                __ match:
                    allowed.add(method)
        __ allowed:
            allow_header = ",".join(sorted(allowed))
            raise HTTPError(405, "Method not allowed.", Allow=allow_header)

        # No matching route and no alternative method found. We give up
        raise HTTPError(404, "Not found: " + repr(path))






c_ Route(object):
    ''' This class wraps a route callback along with route specific metadata and
        configuration and applies Plugins on demand. It is also responsible for
        turing an URL path rule into a regular expression usable by the Router.
    '''

    ___ -  app, rule, method, callback, name=N..,
                 plugins=N.., skiplist=N.., **config):
        #: The application this route is installed to.
        app = app
        #: The path-rule string (e.g. ``/wiki/:page``).
        rule = rule
        #: The HTTP method as a string (e.g. ``GET``).
        method = method
        #: The original callback with no plugins applied. Useful ___ introspection.
        callback = callback
        #: The name of the route (if specified) or ``N..``.
        name = name or N..
        #: A list of route-specific plugins (see :meth:`Bottle.route`).
        plugins = plugins or []
        #: A list of plugins to not apply to this route (see :meth:`Bottle.route`).
        skiplist = skiplist or []
        #: Additional keyword arguments passed to the :meth:`Bottle.route`
        #: decorator are stored __ this dictionary. Used ___ route-specific
        #: plugin configuration and meta-data.
        config = ConfigDict().load_dict(config, make_namespaces=True)

    ___ __call__ *a, **ka):
        depr("Some APIs changed to return Route() instances instead of"\
             " callables. Make sure to use the Route.call method and not to"\
             " call Route instances directly.") #0.12
        r_ call(*a, **ka)

    @cached_property
    ___ call
        ''' The route callback with all plugins applied. This property is
            created on demand and then cached to speed up subsequent requests.'''
        r_ _make_callback()

    ___ reset
        ''' Forget any cached values. The next time :attr:`call` is accessed,
            all plugins are re-applied. '''
        __dict__.pop('call', N..)

    ___ prepare
        ''' Do all on-demand work immediately (useful for debugging).'''
        call

    @property
    ___ _context
        depr('Switch to Plugin API v2 and access the Route object directly.')  #0.12
        r_ dict(rule=rule, method=method, callback=callback,
                    name=name, app=app, config=config,
                    apply=plugins, skip=skiplist)

    ___ all_plugins
        ''' Yield all Plugins affecting this route. '''
        unique = set()
        ___ p __ reversed(app.plugins + plugins):
            __ True __ skiplist: break
            name = getattr(p, 'name', False)
            __ name a.. (name __ skiplist or name __ unique): continue
            __ p __ skiplist or type(p) __ skiplist: continue
            __ name: unique.add(name)
            yield p

    ___ _make_callback
        callback = callback
        ___ plugin __ all_plugins():
            ___
                __ hasattr(plugin, 'apply'):
                    api = getattr(plugin, 'api', 1)
                    context = self __ api > 1 else _context
                    callback = plugin.apply(callback, context)
                else:
                    callback = plugin(callback)
            except RouteReset: # Try again with changed configuration.
                r_ _make_callback()
            __ n.. callback __ callback:
                update_wrapper(callback, callback)
        r_ callback

    ___ get_undecorated_callback
        ''' Return the callback. If the callback is a decorated function, try to
            recover the original function. '''
        func = callback
        func = getattr(func, '__func__' __ py3k else 'im_func', func)
        closure_attr = '__closure__' __ py3k else 'func_closure'
        w___ hasattr(func, closure_attr) a.. getattr(func, closure_attr):
            func = getattr(func, closure_attr)[0].cell_contents
        r_ func

    ___ get_callback_args
        ''' Return a list of argument names the callback (most likely) accepts
            as keyword arguments. If the callback is a decorated function, try
            to recover the original function before inspection. '''
        r_ getargspec(get_undecorated_callback())[0]

    ___ get_config key, default=N..):
        ''' Lookup a config field and return its value, first checking the
            route.config, then route.app.config.'''
        ___ conf __ (config, app.conifg):
            __ key __ conf: r_ conf[key]
        r_ default

    ___ __repr__
        cb = get_undecorated_callback()
        r_ '<@ %r %r>' @ (method, rule, cb)






###############################################################################
# Application Object ###########################################################
###############################################################################


c_ Bottle(object):
    """ Each Bottle object represents a single, distinct web application and
        consists of routes, callbacks, plugins, resources and configuration.
        Instances are callable WSGI applications.

        :param catchall: If true (default), handle all exceptions. Turn off to
                         let debugging middleware handle exceptions.
    """

    ___ -  catchall=True, autojson=True):

        #: A :class:`ConfigDict` ___ app specific configuration.
        config = ConfigDict()
        config._on_change = functools.partial(trigger_hook, 'config')
        config.meta_set('autojson', 'validate', bool)
        config.meta_set('catchall', 'validate', bool)
        config['catchall'] = catchall
        config['autojson'] = autojson

        #: A :class:`ResourceManager` ___ application files
        resources = ResourceManager()

        routes   # list # List of installed :class:`Route` instances.
        router = Router() # Maps requests to :class:`Route` instances.
        error_handler = {}

        # Core plugins
        plugins   # list # List of installed plugins.
        __ config['autojson']:
            install(JSONPlugin())
        install(TemplatePlugin())

    #: If true, most exceptions are caught and returned as :exc:`HTTPError`
    catchall = DictProperty('config', 'catchall')

    __hook_names = 'before_request', 'after_request', 'app_reset', 'config'
    __hook_reversed = 'after_request'

    @cached_property
    ___ _hooks
        r_ dict((name, []) ___ name __ __hook_names)

    ___ add_hook name, func):
        ''' Attach a callback to a hook. Three hooks are currently implemented:

            before_request
                Executed once before each request. The request context is
                available, but no routing has happened yet.
            after_request
                Executed once after each request regardless of its outcome.
            app_reset
                Called whenever :meth:`Bottle.reset` is called.
        '''
        __ name __ __hook_reversed:
            _hooks[name].insert(0, func)
        else:
            _hooks[name].a.. (func)

    ___ remove_hook name, func):
        ''' Remove a callback from a hook. '''
        __ name __ _hooks a.. func __ _hooks[name]:
            _hooks[name].remove(func)
            r_ True

    ___ trigger_hook __name, *args, **kwargs):
        ''' Trigger a hook and return a list of results. '''
        r_ [hook(*args, **kwargs) ___ hook __ _hooks[__name][:]]

    ___ hook name):
        """ Return a decorator that attaches a callback to a hook. See
            :meth:`add_hook` for details."""
        ___ decorator(func):
            add_hook(name, func)
            r_ func
        r_ decorator

    ___ mount prefix, app, **options):
        ''' Mount an application (:class:`Bottle` or plain WSGI) to a specific
            URL prefix. Example::

                root_app.mount('/admin/', admin_app)

            :param prefix: path prefix or `mount-point`. If it ends in a slash,
                that slash is mandatory.
            :param app: an instance of :class:`Bottle` or a WSGI application.

            All other parameters are passed to the underlying :meth:`route` call.
        '''
        __ isinstance(app, basestring):
            depr('Parameter order of Bottle.mount() changed.', True) # 0.10

        segments = [p ___ p __ prefix.split('/') __ p]
        __ n.. segments: raise ValueError('Empty path prefix.')
        path_depth = l..(segments)

        ___ mountpoint_wrapper():
            ___
                request.path_shift(path_depth)
                rs = HTTPResponse([])
                ___ start_response(status, headerlist, exc_info=N..):
                    __ exc_info:
                        ___
                            _raise(*exc_info)
                        ______
                            exc_info = N..
                    rs.status = status
                    ___ name, value __ headerlist: rs.add_header(name, value)
                    r_ rs.body.a..
                body = app(request.environ, start_response)
                __ body a.. rs.body: body = i__.chain(rs.body, body)
                rs.body = body or rs.body
                r_ rs
            ______
                request.path_shift(-path_depth)

        options.setdefault('skip', True)
        options.setdefault('method', 'PROXY')
        options.setdefault('mountpoint', {'prefix': prefix, 'target': app})
        options['callback'] = mountpoint_wrapper

        route('/@/<:re:.*>' @ '/'.join(segments), **options)
        __ n.. prefix.endswith('/'):
            route('/' + '/'.join(segments), **options)

    ___ merge routes):
        ''' Merge the routes of another :class:`Bottle` application or a list of
            :class:`Route` objects into this application. The routes keep their
            'owner', meaning that the :data:`Route.app` attribute is not
            changed. '''
        __ isinstance(routes, Bottle):
            routes = routes.routes
        ___ route __ routes:
            add_route(route)

    ___ install plugin):
        ''' Add a plugin to the list of plugins and prepare it for being
            applied to all routes of this application. A plugin may be a simple
            decorator or an object that implements the :class:`Plugin` API.
        '''
        __ hasattr(plugin, 'setup'): plugin.setup(self)
        __ n.. callable(plugin) a.. n.. hasattr(plugin, 'apply'):
            raise TypeError("Plugins must be callable or implement .apply()")
        plugins.a.. (plugin)
        reset()
        r_ plugin

    ___ uninstall plugin):
        ''' Uninstall plugins. Pass an instance to remove a specific plugin, a type
            object to remove all plugins that match that type, a string to remove
            all plugins with a matching ``name`` attribute or ``True`` to remove all
            plugins. Return the list of removed plugins. '''
        removed, remove   # list, plugin
        ___ i, plugin __ list(enumerate(plugins))[::-1]:
            __ remove __ True or remove __ plugin or remove __ type(plugin) \
            or getattr(plugin, 'name', True) == remove:
                removed.a.. (plugin)
                del plugins[i]
                __ hasattr(plugin, 'close'): plugin.close()
        __ removed: reset()
        r_ removed

    ___ reset route=N..):
        ''' Reset all routes (force plugins to be re-applied) and clear all
            caches. If an ID or route object is given, only that specific route
            is affected. '''
        __ route __ N..: routes = routes
        elif isinstance(route, Route): routes = [route]
        else: routes = [routes[route]]
        ___ route __ routes: route.reset()
        __ DEBUG:
            ___ route __ routes: route.prepare()
        trigger_hook('app_reset')

    ___ close
        ''' Close the application and all installed plugins. '''
        ___ plugin __ plugins:
            __ hasattr(plugin, 'close'): plugin.close()
        stopped = True

    ___ run **kwargs):
        ''' Calls :func:`run` with the same parameters. '''
        run **kwargs)

    ___ match environ):
        """ Search for a matching route and return a (:class:`Route` , urlargs)
            tuple. The second value is a dictionary with parameters extracted
            from the URL. Raise :exc:`HTTPError` (404/405) on a non-match."""
        r_ router.match(environ)

    ___ get_url routename, **kargs):
        """ Return a string that matches a named route """
        scriptname = request.environ.get('SCRIPT_NAME', '').strip('/') + '/'
        location = router.build(routename, **kargs).lstrip('/')
        r_ urljoin(urljoin('/', scriptname), location)

    ___ add_route route):
        ''' Add a route object, but do not change the :data:`Route.app`
            attribute.'''
        routes.a.. (route)
        router.add(route.rule, route.method, route, name=route.name)
        __ DEBUG: route.prepare()

    ___ route path=N.., method='GET', callback=N.., name=N..,
              apply=N.., skip=N.., **config):
        """ A decorator to bind a function to a request URL. Example::

                @app.route('/hello/:name')
                def hello(name):
                    return 'Hello @' % name

            The ``:name`` part is a wildcard. See :class:`Router` for syntax
            details.

            :param path: Request path or a list of paths to listen to. If no
              path is specified, it is automatically generated from the
              signature of the function.
            :param method: HTTP method (`GET`, `POST`, `PUT`, ...) or a list of
              methods to listen to. (default: `GET`)
            :param callback: An optional shortcut to avoid the decorator
              syntax. ``route(..., callback=func)`` equals ``route(...)(func)``
            :param name: The name for this route. (default: None)
            :param apply: A decorator or plugin or a list of plugins. These are
              applied to the route callback in addition to installed plugins.
            :param skip: A list of plugins, plugin classes or names. Matching
              plugins are not installed to this route. ``True`` skips all.

            Any additional keyword arguments are stored as route-specific
            configuration and passed to plugins (see :meth:`Plugin.apply`).
        """
        __ callable(path): path, callback = N.., path
        plugins = makelist(apply)
        skiplist = makelist(skip)
        ___ decorator(callback):
            # TODO: Documentation and tests
            __ isinstance(callback, basestring): callback = load(callback)
            ___ rule __ makelist(path) or yieldroutes(callback):
                ___ verb __ makelist(method):
                    verb = verb.upper()
                    route = Route rule, verb, callback, name=name,
                                  plugins=plugins, skiplist=skiplist, **config)
                    add_route(route)
            r_ callback
        r_ decorator(callback) __ callback else decorator

    ___ get path=N.., method='GET', **options):
        """ Equals :meth:`route`. """
        r_ route(path, method, **options)

    ___ post path=N.., method='POST', **options):
        """ Equals :meth:`route` with a ``POST`` method parameter. """
        r_ route(path, method, **options)

    ___ p.. path=N.., method='PUT', **options):
        """ Equals :meth:`route` with a ``PUT`` method parameter. """
        r_ route(path, method, **options)

    ___ delete path=N.., method='DELETE', **options):
        """ Equals :meth:`route` with a ``DELETE`` method parameter. """
        r_ route(path, method, **options)

    ___ error code=500):
        """ Decorator: Register an output handler for a HTTP error code"""
        ___ wrapper(handler):
            error_handler[in.(code)] = handler
            r_ handler
        r_ wrapper

    ___ default_error_handler res):
        r_ tob(template(ERROR_PAGE_TEMPLATE, e=res))

    ___ _handle environ):
        path = environ['bottle.raw_path'] = environ['PATH_INFO']
        __ py3k:
            ___
                environ['PATH_INFO'] = path.encode('latin1').decode('utf8')
            except UnicodeError:
                r_ HTTPError(400, 'Invalid path string. Expected UTF-8')

        ___
            environ['bottle.app'] = self
            request.bind(environ)
            response.bind()
            ___
                trigger_hook('before_request')
                route, args = router.match(environ)
                environ['route.handle'] = route
                environ['bottle.route'] = route
                environ['route.url_args'] = args
                r_ route.call(**args)
            ______
                trigger_hook('after_request')

        except HTTPResponse:
            r_ _e()
        except RouteReset:
            route.reset()
            r_ _handle(environ)
        except (KeyboardInterrupt, SystemExit, MemoryError):
            raise
        except Exception:
            __ n.. catchall: raise
            stacktrace = format_exc()
            environ['wsgi.errors'].write(stacktrace)
            r_ HTTPError(500, "Internal Server Error", _e(), stacktrace)

    ___ _cast out, peek=N..):
        """ Try to convert the parameter into something WSGI compatible and set
        correct HTTP headers when possible.
        Support: False, str, unicode, dict, HTTPResponse, HTTPError, file-like,
        iterable of strings and iterable of unicodes
        """

        # Empty output is done here
        __ n.. out:
            __ 'Content-Length' n.. __ response:
                response['Content-Length'] = 0
            r_ []
        # Join lists of byte or unicode strings. Mixed lists are NOT supported
        __ isinstance(out, (tuple, list))\
        a.. isinstance(out[0], (bytes, unicode)):
            out = out[0][0:0].join(out) # b'abc'[0:0]  b''
        # Encode unicode strings
        __ isinstance(out, unicode):
            out = out.encode(response.charset)
        # Byte Strings are just returned
        __ isinstance(out, bytes):
            __ 'Content-Length' n.. __ response:
                response['Content-Length'] = l..(out)
            r_ [out]
        # HTTPError or HTTPException (recursive, because they may wrap anything)
        # TODO: Handle these explicitly __ handle() or make them iterable.
        __ isinstance(out, HTTPError):
            out.apply(response)
            out = error_handler.get(out.status_code, default_error_handler)(out)
            r_ _cast(out)
        __ isinstance(out, HTTPResponse):
            out.apply(response)
            r_ _cast(out.body)

        # File-like objects.
        __ hasattr(out, 'read'):
            __ 'wsgi.file_wrapper' __ request.environ:
                r_ request.environ['wsgi.file_wrapper'](out)
            elif hasattr(out, 'close') or n.. hasattr(out, '__iter__'):
                r_ WSGIFileWrapper(out)

        # Handle Iterables. We peek into them to detect their inner type.
        ___
            iout = iter(out)
            first = next(iout)
            w___ n.. first:
                first = next(iout)
        except StopIteration:
            r_ _cast('')
        except HTTPResponse:
            first = _e()
        except (KeyboardInterrupt, SystemExit, MemoryError):
            raise
        except Exception:
            __ n.. catchall: raise
            first = HTTPError(500, 'Unhandled exception', _e(), format_exc())

        # These are the inner types allowed __ iterator or generator objects.
        __ isinstance(first, HTTPResponse):
            r_ _cast(first)
        elif isinstance(first, bytes):
            new_iter = i__.chain([first], iout)
        elif isinstance(first, unicode):
            encoder = lambda x: x.encode(response.charset)
            new_iter = imap(encoder, i__.chain([first], iout))
        else:
            msg = 'Unsupported response type: @' @ type(first)
            r_ _cast(HTTPError(500, msg))
        __ hasattr(out, 'close'):
            new_iter = _closeiter(new_iter, out.close)
        r_ new_iter

    ___ wsgi environ, start_response):
        """ The bottle WSGI-interface. """
        ___
            out = _cast(_handle(environ))
            # rfc2616 section 4.3
            __ response._status_code __ (100, 101, 204, 304)\
            or environ['REQUEST_METHOD'] == 'HEAD':
                __ hasattr(out, 'close'): out.close()
                out   # list
            start_response(response._status_line, response.headerlist)
            r_ out
        except (KeyboardInterrupt, SystemExit, MemoryError):
            raise
        except Exception:
            __ n.. catchall: raise
            err = '<h1>Critical error while processing request: @</h1>' \
                  @ html_escape(environ.get('PATH_INFO', '/'))
            __ DEBUG:
                err += '<h2>Error:</h2>\n<pre>\n@\n</pre>\n' \
                       '<h2>Traceback:</h2>\n<pre>\n@\n</pre>\n' \
                       @ (html_escape(repr(_e())), html_escape(format_exc()))
            environ['wsgi.errors'].write(err)
            headers = [('Content-Type', 'text/html; charset=UTF-8')]
            start_response('500 INTERNAL SERVER ERROR', headers, sys.exc_info())
            r_ [tob(err)]

    ___ __call__ environ, start_response):
        ''' Each instance of :class:'Bottle' is a WSGI application. '''
        r_ wsgi(environ, start_response)






###############################################################################
# HTTP and WSGI Tools ##########################################################
###############################################################################

c_ BaseRequest(object):
    """ A wrapper for WSGI environment dictionaries that adds a lot of
        convenient access methods and properties. Most of them are read-only.

        Adding new attributes to a request actually adds them to the environ
        dictionary (as 'bottle.request.ext.<name>'). This is the recommended
        way to store and access request-specific data.
    """

    __slots__ = ('environ')

    #: Maximum size of memory buffer ___ :attr:`body` __ bytes.
    MEMFILE_MAX = 102400

    ___ -  environ=N..):
        """ Wrap a WSGI environ dictionary. """
        #: The wrapped WSGI environ dictionary. This is the only real attribute.
        #: All other attributes actually are read-only properties.
        environ = {} __ environ __ N.. else environ
        environ['bottle.request'] = self

    @DictProperty('environ', 'bottle.app', read_only=True)
    ___ app
        ''' Bottle application handling this request. '''
        raise RuntimeError('This request is not connected to an application.')

    @DictProperty('environ', 'bottle.route', read_only=True)
    ___ route
        """ The bottle :class:`Route` object that matches this request. """
        raise RuntimeError('This request is not connected to a route.')

    @DictProperty('environ', 'route.url_args', read_only=True)
    ___ url_args
        """ The arguments extracted from the URL. """
        raise RuntimeError('This request is not connected to a route.')

    @property
    ___ path
        ''' The value of ``PATH_INFO`` with exactly one prefixed slash (to fix
            broken clients and avoid the "empty path" edge case). '''
        r_ '/' + environ.get('PATH_INFO','').lstrip('/')

    @property
    ___ method
        ''' The ``REQUEST_METHOD`` value as an uppercase string. '''
        r_ environ.get('REQUEST_METHOD', 'GET').upper()

    @DictProperty('environ', 'bottle.request.headers', read_only=True)
    ___ headers
        ''' A :class:`WSGIHeaderDict` that provides case-insensitive access to
            HTTP request headers. '''
        r_ WSGIHeaderDict(environ)

    ___ get_header name, default=N..):
        ''' Return the value of a request header, or a given default value. '''
        r_ headers.get(name, default)

    @DictProperty('environ', 'bottle.request.cookies', read_only=True)
    ___ cookies
        """ Cookies parsed into a :class:`FormsDict`. Signed cookies are NOT
            decoded. Use :meth:`get_cookie` if you expect signed cookies. """
        cookies = SimpleCookie(environ.get('HTTP_COOKIE','')).values()
        r_ FormsDict((c.key, c.value) ___ c __ cookies)

    ___ get_cookie key, default=N.., secret=N..):
        """ Return the content of a cookie. To read a `Signed Cookie`, the
            `secret` must match the one used to create the cookie (see
            :meth:`BaseResponse.set_cookie`). If anything goes wrong (missing
            cookie or wrong signature), return a default value. """
        value = cookies.get(key)
        __ secret a.. value:
            dec = cookie_decode(value, secret) # (key, value) tuple or N..
            r_ dec[1] __ dec a.. dec[0] == key else default
        r_ value or default

    @DictProperty('environ', 'bottle.request.query', read_only=True)
    ___ query
        ''' The :attr:`query_string` parsed into a :class:`FormsDict`. These
            values are sometimes called "URL arguments" or "GET parameters", but
            not to be confused with "URL wildcards" as they are provided by the
            :class:`Router`. '''
        get = environ['bottle.get'] = FormsDict()
        pairs = _parse_qsl(environ.get('QUERY_STRING', ''))
        ___ key, value __ pairs:
            get[key] = value
        r_ get

    @DictProperty('environ', 'bottle.request.forms', read_only=True)
    ___ forms
        """ Form values parsed from an `url-encoded` or `multipart/form-data`
            encoded POST or PUT request body. The result is returned as a
            :class:`FormsDict`. All keys and values are strings. File uploads
            are stored separately in :attr:`files`. """
        forms = FormsDict()
        ___ name, item __ POST.allitems():
            __ n.. isinstance(item, FileUpload):
                forms[name] = item
        r_ forms

    @DictProperty('environ', 'bottle.request.params', read_only=True)
    ___ params
        """ A :class:`FormsDict` with the combined values of :attr:`query` and
            :attr:`forms`. File uploads are stored in :attr:`files`. """
        params = FormsDict()
        ___ key, value __ query.allitems():
            params[key] = value
        ___ key, value __ forms.allitems():
            params[key] = value
        r_ params

    @DictProperty('environ', 'bottle.request.files', read_only=True)
    ___ files
        """ File uploads parsed from `multipart/form-data` encoded POST or PUT
            request body. The values are instances of :class:`FileUpload`.

        """
        files = FormsDict()
        ___ name, item __ POST.allitems():
            __ isinstance(item, FileUpload):
                files[name] = item
        r_ files

    @DictProperty('environ', 'bottle.request.json', read_only=True)
    ___ json
        ''' If the ``Content-Type`` header is ``application/json``, this
            property holds the parsed content of the request body. Only requests
            smaller than :attr:`MEMFILE_MAX` are processed to avoid memory
            exhaustion. '''
        ctype = environ.get('CONTENT_TYPE', '').lower().split(';')[0]
        __ ctype == 'application/json':
            b = _get_body_string()
            __ n.. b:
                r_ N..
            r_ json_loads(b)
        r_ N..

    ___ _iter_body read, bufsize):
        maxread = max(0, content_length)
        w___ maxread:
            part = read(min(maxread, bufsize))
            __ n.. part: break
            yield part
            maxread -= l..(part)

    ___ _iter_chunked read, bufsize):
        err = HTTPError(400, 'Error while parsing chunked transfer body.')
        rn, sem, bs = tob('\r\n'), tob(';'), tob('')
        w___ True:
            header = read(1)
            w___ header[-2:] != rn:
                c = read(1)
                header += c
                __ n.. c: raise err
                __ l..(header) > bufsize: raise err
            size, _, _ = header.partition(sem)
            ___
                maxread = in.(tonat(size.strip()), 16)
            except ValueError:
                raise err
            __ maxread == 0: break
            buff = bs
            w___ maxread > 0:
                __ n.. buff:
                    buff = read(min(maxread, bufsize))
                part, buff = buff[:maxread], buff[maxread:]
                __ n.. part: raise err
                yield part
                maxread -= l..(part)
            __ read(2) != rn:
                raise err

    @DictProperty('environ', 'bottle.request.body', read_only=True)
    ___ _body
        body_iter = _iter_chunked __ chunked else _iter_body
        read_func = environ['wsgi.input'].read
        body, body_size, is_temp_file = BytesIO(), 0, False
        ___ part __ body_iter(read_func, MEMFILE_MAX):
            body.write(part)
            body_size += l..(part)
            __ n.. is_temp_file a.. body_size > MEMFILE_MAX:
                body, tmp = TemporaryFile(mode='w+b'), body
                body.write(tmp.getvalue())
                del tmp
                is_temp_file = True
        environ['wsgi.input'] = body
        body.seek(0)
        r_ body

    ___ _get_body_string
        ''' read body until content-length or MEMFILE_MAX into a string. Raise
            HTTPError(413) on requests that are to large. '''
        clen = content_length
        __ clen > MEMFILE_MAX:
            raise HTTPError(413, 'Request to large')
        __ clen < 0: clen = MEMFILE_MAX + 1
        data = body.read(clen)
        __ l..(data) > MEMFILE_MAX: # Fail fast
            raise HTTPError(413, 'Request to large')
        r_ data

    @property
    ___ body
        """ The HTTP request body as a seek-able file-like object. Depending on
            :attr:`MEMFILE_MAX`, this is either a temporary file or a
            :class:`io.BytesIO` instance. Accessing this property for the first
            time reads and replaces the ``wsgi.input`` environ variable.
            Subsequent accesses just do a `seek(0)` on the file object. """
        _body.seek(0)
        r_ _body

    @property
    ___ chunked
        ''' True if Chunked transfer encoding was. '''
        r_ 'chunked' __ environ.get('HTTP_TRANSFER_ENCODING', '').lower()

    #: An alias ___ :attr:`query`.
    GET = query

    @DictProperty('environ', 'bottle.request.post', read_only=True)
    ___ POST
        """ The values of :attr:`forms` and :attr:`files` combined into a single
            :class:`FormsDict`. Values are either strings (form values) or
            instances of :class:`cgi.FieldStorage` (file uploads).
        """
        post = FormsDict()
        # We default to application/x-www-form-urlencoded ___ everything that
        # is not multipart and take the fast path (also: 3.1 workaround)
        __ n.. content_type.startswith('multipart/'):
            pairs = _parse_qsl(tonat(_get_body_string(), 'latin1'))
            ___ key, value __ pairs:
                post[key] = value
            r_ post

        safe_env = {'QUERY_STRING':''} # Build a safe environment ___ cgi
        ___ key __ ('REQUEST_METHOD', 'CONTENT_TYPE', 'CONTENT_LENGTH'):
            __ key __ environ: safe_env[key] = environ[key]
        args = dict(fp=body, environ=safe_env, keep_blank_values=True)
        __ py31:
            args['fp'] = NCTextIOWrapper(args['fp'], encoding='utf8',
                                         newline='\n')
        elif py3k:
            args['encoding'] = 'utf8'
        data = cgi.FieldStorage(**args)
        self['_cgi.FieldStorage'] = data #http://bugs.python.org/issue18394#msg207958
        data = data.list or []
        ___ item __ data:
            __ item.filename:
                post[item.name] = FileUpload(item.file, item.name,
                                             item.filename, item.headers)
            else:
                post[item.name] = item.value
        r_ post

    @property
    ___ url
        """ The full request URI including hostname and scheme. If your app
            lives behind a reverse proxy or load balancer and you get confusing
            results, make sure that the ``X-Forwarded-Host`` header is set
            correctly. """
        r_ urlparts.geturl()

    @DictProperty('environ', 'bottle.request.urlparts', read_only=True)
    ___ urlparts
        ''' The :attr:`url` string as an :class:`urlparse.SplitResult` tuple.
            The tuple contains (scheme, host, path, query_string and fragment),
            but the fragment is always empty because it is not visible to the
            server. '''
        env = environ
        http = env.get('HTTP_X_FORWARDED_PROTO') or env.get('wsgi.url_scheme', 'http')
        host = env.get('HTTP_X_FORWARDED_HOST') or env.get('HTTP_HOST')
        __ n.. host:
            # HTTP 1.1 requires a Host-header. This is ___ HTTP/1.0 clients.
            host = env.get('SERVER_NAME', '127.0.0.1')
            port = env.get('SERVER_PORT')
            __ port a.. port != ('80' __ http == 'http' else '443'):
                host += ':' + port
        path = urlquote(fullpath)
        r_ UrlSplitResult(http, host, path, env.get('QUERY_STRING'), '')

    @property
    ___ fullpath
        """ Request path including :attr:`script_name` (if present). """
        r_ urljoin(script_name, path.lstrip('/'))

    @property
    ___ query_string
        """ The raw :attr:`query` part of the URL (everything in between ``?``
            and ``#``) as a string. """
        r_ environ.get('QUERY_STRING', '')

    @property
    ___ script_name
        ''' The initial portion of the URL's `path` that was removed by a higher
            level (server or routing middleware) before the application was
            called. This script path is returned with leading and tailing
            slashes. '''
        script_name = environ.get('SCRIPT_NAME', '').strip('/')
        r_ '/' + script_name + '/' __ script_name else '/'

    ___ path_shift shift=1):
        ''' Shift path segments from :attr:`path` to :attr:`script_name` and
            vice versa.

           :param shift: The number of path segments to shift. May be negative
                         to change the shift direction. (default: 1)
        '''
        script = environ.get('SCRIPT_NAME','/')
        self['SCRIPT_NAME'], self['PATH_INFO'] = path_shift(script, path, shift)

    @property
    ___ content_length
        ''' The request body length as an integer. The client is responsible to
            set this header. Otherwise, the real length of the body is unknown
            and -1 is returned. In this case, :attr:`body` will be empty. '''
        r_ in.(environ.get('CONTENT_LENGTH') or -1)

    @property
    ___ content_type
        ''' The Content-Type header as a lowercase-string (default: empty). '''
        r_ environ.get('CONTENT_TYPE', '').lower()

    @property
    ___ is_xhr
        ''' True if the request was triggered by a XMLHttpRequest. This only
            works with JavaScript libraries that support the `X-Requested-With`
            header (most of the popular libraries do). '''
        requested_with = environ.get('HTTP_X_REQUESTED_WITH','')
        r_ requested_with.lower() == 'xmlhttprequest'

    @property
    ___ is_ajax
        ''' Alias for :attr:`is_xhr`. "Ajax" is not the right term. '''
        r_ is_xhr

    @property
    ___ auth
        """ HTTP authentication data as a (user, password) tuple. This
            implementation currently supports basic (not digest) authentication
            only. If the authentication happened at a higher level (e.g. in the
            front web-server or a middleware), the password field is None, but
            the user field is looked up from the ``REMOTE_USER`` environ
            variable. On any errors, None is returned. """
        basic = parse_auth(environ.get('HTTP_AUTHORIZATION',''))
        __ basic: r_ basic
        ruser = environ.get('REMOTE_USER')
        __ ruser: r_ (ruser, N..)
        r_ N..

    @property
    ___ remote_route
        """ A list of all IPs that were involved in this request, starting with
            the client IP and followed by zero or more proxies. This does only
            work if all proxies support the ```X-Forwarded-For`` header. Note
            that this information can be forged by malicious clients. """
        proxy = environ.get('HTTP_X_FORWARDED_FOR')
        __ proxy: r_ [ip.strip() ___ ip __ proxy.split(',')]
        remote = environ.get('REMOTE_ADDR')
        r_ [remote] __ remote else []

    @property
    ___ remote_addr
        """ The client IP as a string. Note that this information can be forged
            by malicious clients. """
        route = remote_route
        r_ route[0] __ route else N..

    ___ copy
        """ Return a new :class:`Request` with a shallow :attr:`environ` copy. """
        r_ Request(environ.copy())

    ___ get value, default=N..): r_ environ.get(value, default)
    ___ __getitem__ key): r_ environ[key]
    ___ __delitem__ key): self[key] = ""; del(environ[key])
    ___ __iter__ r_ iter(environ)
    ___ __len__ r_ l..(environ)
    ___ keys r_ environ.keys()
    ___ __setitem__ key, value):
        """ Change an environ value and clear all caches that depend on it. """

        __ environ.get('bottle.request.readonly'):
            raise KeyError('The environ dictionary is read-only.')

        environ[key] = value
        todelete = ()

        __ key == 'wsgi.input':
            todelete = ('body', 'forms', 'files', 'params', 'post', 'json')
        elif key == 'QUERY_STRING':
            todelete = ('query', 'params')
        elif key.startswith('HTTP_'):
            todelete = ('headers', 'cookies')

        ___ key __ todelete:
            environ.pop('bottle.request.'+key, N..)

    ___ __repr__
        r_ '<@: @ @>' @ (__class__.__name__, method, url)

    ___ __getattr__ name):
        ''' Search in self.environ for additional user defined attributes. '''
        ___
            var = environ['bottle.request.ext.@'@name]
            r_ var.__get__(self) __ hasattr(var, '__get__') else var
        except KeyError:
            raise AttributeError('Attribute %r not defined.' @ name)

    ___ __setattr__ name, value):
        __ name == 'environ': r_ object.__setattr__ name, value)
        environ['bottle.request.ext.@'@name] = value


___ _hkey(key):
    __ '\n' __ key or '\r' __ key or '\0' __ key:
        raise ValueError("Header names must not contain control characters: %r" @ key)
    r_ key.title().replace('_', '-')


___ _hval(value):
    value = tonat(value)
    __ '\n' __ value or '\r' __ value or '\0' __ value:
        raise ValueError("Header value must not contain control characters: %r" @ value)
    r_ value



c_ HeaderProperty(object):
    ___ -  name, reader=N.., writer=N.., default=''):
        name, default = name, default
        reader, writer = reader, writer
        __doc__ = 'Current value of the %r header.' @ name.title()

    ___ __get__ obj, cls):
        __ obj __ N..: r_ self
        value = obj.get_header(name, default)
        r_ reader(value) __ reader else value

    ___ __set__ obj, value):
        obj[name] = writer(value) __ writer else value

    ___ __delete__ obj):
        del obj[name]


c_ BaseResponse(object):
    """ Storage class for a response body as well as headers and cookies.

        This class does support dict-like case-insensitive item-access to
        headers, but is NOT a dict. Most notably, iterating over a response
        yields parts of the body and not the headers.

        :param body: The response body as one of the supported types.
        :param status: Either an HTTP status code (e.g. 200) or a status line
                       including the reason phrase (e.g. '200 OK').
        :param headers: A dictionary or a list of name-value pairs.

        Additional keyword arguments are added to the list of headers.
        Underscores in the header name are replaced with dashes.
    """

    default_status = 200
    default_content_type = 'text/html; charset=UTF-8'

    # Header blacklist ___ specific response codes
    # (rfc2616 section 10.2.3 and 10.3.5)
    bad_headers = {
        204: set(('Content-Type',)),
        304: set(('Allow', 'Content-Encoding', 'Content-Language',
                  'Content-Length', 'Content-Range', 'Content-Type',
                  'Content-Md5', 'Last-Modified'))}

    ___ -  body='', status=N.., headers=N.., **more_headers):
        _cookies = N..
        _headers = {}
        body = body
        status = status or default_status
        __ headers:
            __ isinstance(headers, dict):
                headers = headers.items()
            ___ name, value __ headers:
                add_header(name, value)
        __ more_headers:
            ___ name, value __ more_headers.items():
                add_header(name, value)

    ___ copy cls=N..):
        ''' Returns a copy of self. '''
        cls = cls or BaseResponse
        assert issubclass(cls, BaseResponse)
        copy = cls()
        copy.status = status
        copy._headers = dict((k, v[:]) ___ (k, v) __ _headers.items())
        __ _cookies:
            copy._cookies = SimpleCookie()
            copy._cookies.load(_cookies.output(header=''))
        r_ copy

    ___ __iter__
        r_ iter(body)

    ___ close
        __ hasattr(body, 'close'):
            body.close()

    @property
    ___ status_line
        ''' The HTTP status line as a string (e.g. ``404 Not Found``).'''
        r_ _status_line

    @property
    ___ status_code
        ''' The HTTP status code as an integer (e.g. 404).'''
        r_ _status_code

    ___ _set_status status):
        __ isinstance(status, in.):
            code, status = status, _HTTP_STATUS_LINES.get(status)
        elif ' ' __ status:
            status = status.strip()
            code   = in.(status.split()[0])
        else:
            raise ValueError('String status line without a reason phrase.')
        __ n.. 100 <= code <= 999: raise ValueError('Status code out of range.')
        _status_code = code
        _status_line = s..(status or ('%d Unknown' @ code))

    ___ _get_status
        r_ _status_line

    status = property(_get_status, _set_status, N..,
        ''' A writeable property to change the HTTP response status. It accepts
            either a numeric code (100-999) or a string with a custom reason
            phrase (e.g. "404 Brain not found"). Both :data:`status_line` and
            :data:`status_code` are updated accordingly. The return value is
            always a status string. ''')
    del _get_status, _set_status

    @property
    ___ headers
        ''' An instance of :class:`HeaderDict`, a case-insensitive dict-like
            view on the response headers. '''
        hdict = HeaderDict()
        hdict.dict = _headers
        r_ hdict

    ___ __contains__ name): r_ _hkey(name) __ _headers
    ___ __delitem__ name):  del _headers[_hkey(name)]
    ___ __getitem__ name):  r_ _headers[_hkey(name)][-1]
    ___ __setitem__ name, value): _headers[_hkey(name)] = [_hval(value)]

    ___ get_header name, default=N..):
        ''' Return the value of a previously defined header. If there is no
            header with that name, return a default value. '''
        r_ _headers.get(_hkey(name), [default])[-1]

    ___ set_header name, value):
        ''' Create a new response header, replacing any previously defined
            headers with the same name. '''
        _headers[_hkey(name)] = [_hval(value)]

    ___ add_header name, value):
        ''' Add an additional response header, not removing duplicates. '''
        _headers.setdefault(_hkey(name), []).a.. (_hval(value))

    ___ iter_headers
        ''' Yield (header, value) tuples, skipping headers that are not
            allowed with the current response status code. '''
        r_ headerlist

    @property
    ___ headerlist
        """ WSGI conform list of (header, value) tuples. """
        out   # list
        headers = list(_headers.items())
        __ 'Content-Type' n.. __ _headers:
            headers.a.. (('Content-Type', [default_content_type]))
        __ _status_code __ bad_headers:
            bad_headers = bad_headers[_status_code]
            headers = [h ___ h __ headers __ h[0] n.. __ bad_headers]
        out += [(name, val) ___ (name, vals) __ headers ___ val __ vals]
        __ _cookies:
            ___ c __ _cookies.values():
                out.a.. (('Set-Cookie', _hval(c.OutputString())))
        __ py3k:
            out = [(k, v.encode('utf8').decode('latin1')) ___ (k, v) __ out]
        r_ out

    content_type = HeaderProperty('Content-Type')
    content_length = HeaderProperty('Content-Length', reader=in.)
    expires = HeaderProperty('Expires',
        reader=lambda x: datetime.utcfromtimestamp(parse_date(x)),
        writer=lambda x: http_date(x))

    @property
    ___ charset default='UTF-8'):
        """ Return the charset specified in the content-type header (default: utf8). """
        __ 'charset=' __ content_type:
            r_ content_type.split('charset=')[-1].split(';')[0].strip()
        r_ default

    ___ set_cookie name, value, secret=N.., **options):
        ''' Create a new cookie or replace an old one. If the `secret` parameter is
            set, create a `Signed Cookie` (described below).

            :param name: the name of the cookie.
            :param value: the value of the cookie.
            :param secret: a signature key required for signed cookies.

            Additionally, this method accepts all RFC 2109 attributes that are
            supported by :class:`cookie.Morsel`, including:

            :param max_age: maximum age in seconds. (default: None)
            :param expires: a datetime object or UNIX timestamp. (default: None)
            :param domain: the domain that is allowed to read the cookie.
              (default: current domain)
            :param path: limits the cookie to a given path (default: current path)
            :param secure: limit the cookie to HTTPS connections (default: off).
            :param httponly: prevents client-side javascript to read this cookie
              (default: off, requires Python 2.6 or newer).

            If neither `expires` nor `max_age` is set (default), the cookie will
            expire at the end of the browser session (as soon as the browser
            window is closed).

            Signed cookies may store any pickle-able object and are
            cryptographically signed to prevent manipulation. Keep in mind that
            cookies are limited to 4kb in most browsers.

            Warning: Signed cookies are not encrypted (the client can still see
            the content) and not copy-protected (the client can restore an old
            cookie). The main intention is to make pickling and unpickling
            save, not to store secret information at client side.
        '''
        __ n.. _cookies:
            _cookies = SimpleCookie()

        __ secret:
            value = touni(cookie_encode((name, value), secret))
        elif n.. isinstance(value, basestring):
            raise TypeError('Secret key missing for non-string Cookie.')

        __ l..(value) > 4096: raise ValueError('Cookie value to long.')
        _cookies[name] = value

        ___ key, value __ options.items():
            __ key == 'max_age':
                __ isinstance(value, timedelta):
                    value = value.seconds + value.days * 24 * 3600
            __ key == 'expires':
                __ isinstance(value, (datedate, datetime)):
                    value = value.timetuple()
                elif isinstance(value, (in., float)):
                    value = t__.gmtime(value)
                value = t__.strftime("%a, %d %b %Y %H:%M:%S GMT", value)
            _cookies[name][key.replace('_', '-')] = value

    ___ delete_cookie key, **kwargs):
        ''' Delete a cookie. Be sure to use the same `domain` and `path`
            settings as used to create the cookie. '''
        kwargs['max_age'] = -1
        kwargs['expires'] = 0
        set_cookie(key, '', **kwargs)

    ___ __repr__
        out = ''
        ___ name, value __ headerlist:
            out += '@: @\n' @ (name.title(), value.strip())
        r_ out


___ local_property(name=N..):
    __ name: depr('local_property() is deprecated and will be removed.') #0.12
    ls = _.local()
    ___ fget
        ___ r_ ls.var
        except AttributeError:
            raise RuntimeError("Request context not initialized.")
    ___ fset value): ls.var = value
    ___ fdel del ls.var
    r_ property(fget, fset, fdel, 'Thread-local property')


c_ LocalRequest(BaseRequest):
    ''' A thread-local subclass of :class:`BaseRequest` with a different
        set of attributes for each thread. There is usually only one global
        instance of this class (:data:`request`). If accessed during a
        request/response cycle, this instance always refers to the *current*
        request (even on a multithreaded server). '''
    bind = BaseRequest.- 
    environ = local_property()


c_ LocalResponse(BaseResponse):
    ''' A thread-local subclass of :class:`BaseResponse` with a different
        set of attributes for each thread. There is usually only one global
        instance of this class (:data:`response`). Its attributes are used
        to build the HTTP response at the end of the request/response cycle.
    '''
    bind = BaseResponse.- 
    _status_line = local_property()
    _status_code = local_property()
    _cookies     = local_property()
    _headers     = local_property()
    body         = local_property()


Request = BaseRequest
Response = BaseResponse


c_ HTTPResponse(Response, BottleException):
    ___ -  body='', status=N.., headers=N.., **more_headers):
        super(HTTPResponse, self).- (body, status, headers, **more_headers)

    ___ apply response):
        response._status_code = _status_code
        response._status_line = _status_line
        response._headers = _headers
        response._cookies = _cookies
        response.body = body


c_ HTTPError(HTTPResponse):
    default_status = 500
    ___ -  status=N.., body=N.., exception=N.., traceback=N..,
                 **options):
        exception = exception
        traceback = traceback
        super(HTTPError, self).- (body, status, **options)





###############################################################################
# Plugins ######################################################################
###############################################################################

c_ PluginError(BottleException): pass


c_ JSONPlugin(object):
    name = 'json'
    api  = 2

    ___ -  json_dumps=json_dumps):
        json_dumps = json_dumps

    ___ apply callback, route):
        dumps = json_dumps
        __ n.. dumps: r_ callback
        ___ wrapper(*a, **ka):
            ___
                rv = callback(*a, **ka)
            except HTTPError:
                rv = _e()

            __ isinstance(rv, dict):
                #Attempt to serialize, raises exception on failure
                json_response = dumps(rv)
                #Set content type only if serialization succesful
                response.content_type = 'application/json'
                r_ json_response
            elif isinstance(rv, HTTPResponse) a.. isinstance(rv.body, dict):
                rv.body = dumps(rv.body)
                rv.content_type = 'application/json'
            r_ rv

        r_ wrapper


c_ TemplatePlugin(object):
    ''' This plugin applies the :func:`view` decorator to all routes with a
        `template` config parameter. If the parameter is a tuple, the second
        element must be a dict with additional options (e.g. `template_engine`)
        or default variables for the template. '''
    name = 'template'
    api  = 2

    ___ apply callback, route):
        conf = route.config.get('template')
        __ isinstance(conf, (tuple, list)) a.. l..(conf) == 2:
            r_ view(conf[0], **conf[1])(callback)
        elif isinstance(conf, s..):
            r_ view(conf)(callback)
        else:
            r_ callback


#: Not a plugin, but part of the plugin API. TODO: Find a better place.
c_ _ImportRedirect(object):
    ___ -  name, impmask):
        ''' Create a virtual package that redirects imports (see PEP 302). '''
        name = name
        impmask = impmask
        module = sys.modules.setdefault(name, new_module(name))
        module.__dict__.update({'__file__': __file__, '__path__': [],
                                    '__all__': [], '__loader__': self})
        sys.meta_path.a.. (self)

    ___ find_module fullname, path=N..):
        __ '.' n.. __ fullname: r_
        packname = fullname.rsplit('.', 1)[0]
        __ packname != name: r_
        r_ self

    ___ load_module fullname):
        __ fullname __ sys.modules: r_ sys.modules[fullname]
        modname = fullname.rsplit('.', 1)[1]
        realname = impmask @ modname
        __import__(realname)
        module = sys.modules[fullname] = sys.modules[realname]
        setattr(module, modname, module)
        module.__loader__ = self
        r_ module






###############################################################################
# Common Utilities #############################################################
###############################################################################


c_ MultiDict(DictMixin):
    """ This dict stores multiple values per key, but behaves exactly like a
        normal dict in that it returns only the newest value for any given key.
        There are special methods available to access the full list of values.
    """

    ___ -  *a, **k):
        dict = dict((k, [v]) ___ (k, v) __ dict(*a, **k).items())

    ___ __len__ r_ l..(dict)
    ___ __iter__ r_ iter(dict)
    ___ __contains__ key): r_ key __ dict
    ___ __delitem__ key): del dict[key]
    ___ __getitem__ key): r_ dict[key][-1]
    ___ __setitem__ key, value): a.. (key, value)
    ___ keys r_ dict.keys()

    __ py3k:
        ___ values r_ (v[-1] ___ v __ dict.values())
        ___ items r_ ((k, v[-1]) ___ k, v __ dict.items())
        ___ allitems
            r_ ((k, v) ___ k, vl __ dict.items() ___ v __ vl)
        iterkeys = keys
        itervalues = values
        iteritems = items
        iterallitems = allitems

    else:
        ___ values r_ [v[-1] ___ v __ dict.values()]
        ___ items r_ [(k, v[-1]) ___ k, v __ dict.items()]
        ___ iterkeys r_ dict.iterkeys()
        ___ itervalues r_ (v[-1] ___ v __ dict.itervalues())
        ___ iteritems
            r_ ((k, v[-1]) ___ k, v __ dict.iteritems())
        ___ iterallitems
            r_ ((k, v) ___ k, vl __ dict.iteritems() ___ v __ vl)
        ___ allitems
            r_ [(k, v) ___ k, vl __ dict.iteritems() ___ v __ vl]

    ___ get key, default=N.., index=-1, type=N..):
        ''' Return the most recent value for a key.

            :param default: The default value to be returned if the key is not
                   present or the type conversion fails.
            :param index: An index for the list of available values.
            :param type: If defined, this callable is used to cast the value
                    into a specific type. Exception are suppressed and result in
                    the default value to be returned.
        '''
        ___
            val = dict[key][index]
            r_ type(val) __ type else val
        except Exception:
            pass
        r_ default

    ___ a..  key, value):
        ''' Add a new value to the list of values for this key. '''
        dict.setdefault(key, []).a.. (value)

    ___ replace key, value):
        ''' Replace the list of values with a single value. '''
        dict[key] = [value]

    ___ getall key):
        ''' Return a (possibly empty) list of values for a key. '''
        r_ dict.get(key) or []

    #: Aliases ___ WTForms to mimic other multi-dict APIs (Django)
    getone = get
    getlist = getall


c_ FormsDict(MultiDict):
    ''' This :class:`MultiDict` subclass is used to store request form data.
        Additionally to the normal dict-like item access methods (which return
        unmodified data as native strings), this container also supports
        attribute-like access to its values. Attributes are automatically de-
        or recoded to match :attr:`input_encoding` (default: 'utf8'). Missing
        attributes default to an empty string. '''

    #: Encoding used ___ attribute values.
    input_encoding = 'utf8'
    #: If true (default), unicode strings are first encoded with `latin1`
    #: and then decoded to match :attr:`input_encoding`.
    recode_unicode = True

    ___ _fix s, encoding=N..):
        __ isinstance(s, unicode) a.. recode_unicode: # Python 3 WSGI
            r_ s.encode('latin1').decode(encoding or input_encoding)
        elif isinstance(s, bytes): # Python 2 WSGI
            r_ s.decode(encoding or input_encoding)
        else:
            r_ s

    ___ decode encoding=N..):
        ''' Returns a copy with all keys and values de- or recoded to match
            :attr:`input_encoding`. Some libraries (e.g. WTForms) want a
            unicode dictionary. '''
        copy = FormsDict()
        enc = copy.input_encoding = encoding or input_encoding
        copy.recode_unicode = False
        ___ key, value __ allitems():
            copy.a.. (_fix(key, enc), _fix(value, enc))
        r_ copy

    ___ getunicode name, default=N.., encoding=N..):
        ''' Return the value as a unicode string, or the default. '''
        ___
            r_ _fix(self[name], encoding)
        except (UnicodeError, KeyError):
            r_ default

    ___ __getattr__ name, default=unicode()):
        # Without this guard, pickle generates a cryptic TypeError:
        __ name.startswith('__') a.. name.endswith('__'):
            r_ super(FormsDict, self).__getattr__(name)
        r_ getunicode(name, default=default)

c_ HeaderDict(MultiDict):
    """ A case-insensitive version of :class:`MultiDict` that defaults to
        replace the old value instead of appending it. """

    ___ -  *a, **ka):
        dict = {}
        __ a or ka: update(*a, **ka)

    ___ __contains__ key): r_ _hkey(key) __ dict
    ___ __delitem__ key): del dict[_hkey(key)]
    ___ __getitem__ key): r_ dict[_hkey(key)][-1]
    ___ __setitem__ key, value): dict[_hkey(key)] = [_hval(value)]
    ___ a..  key, value): dict.setdefault(_hkey(key), []).a.. (_hval(value))
    ___ replace key, value): dict[_hkey(key)] = [_hval(value)]
    ___ getall key): r_ dict.get(_hkey(key)) or []
    ___ get key, default=N.., index=-1):
        r_ MultiDict.get _hkey(key), default, index)
    ___ filter names):
        ___ name __ (_hkey(n) ___ n __ names):
            __ name __ dict:
                del dict[name]


c_ WSGIHeaderDict(DictMixin):
    ''' This dict-like class wraps a WSGI environ dict and provides convenient
        access to HTTP_* fields. Keys and values are native strings
        (2.x bytes or 3.x unicode) and keys are case-insensitive. If the WSGI
        environment contains non-native string values, these are de- or encoded
        using a lossless 'latin1' character set.

        The API will remain stable even on changes to the relevant PEPs.
        Currently PEP 333, 444 and 3333 are supported. (PEP 444 is the only one
        that uses non-native strings.)
    '''
    #: List of keys that do not have a ``HTTP_`` prefix.
    cgikeys = ('CONTENT_TYPE', 'CONTENT_LENGTH')

    ___ -  environ):
        environ = environ

    ___ _ekey key):
        ''' Translate header field name to CGI/WSGI environ key. '''
        key = key.replace('-','_').upper()
        __ key __ cgikeys:
            r_ key
        r_ 'HTTP_' + key

    ___ raw key, default=N..):
        ''' Return the header value as is (may be bytes or unicode). '''
        r_ environ.get(_ekey(key), default)

    ___ __getitem__ key):
        r_ tonat(environ[_ekey(key)], 'latin1')

    ___ __setitem__ key, value):
        raise TypeError("@ is read-only." @ __class__)

    ___ __delitem__ key):
        raise TypeError("@ is read-only." @ __class__)

    ___ __iter__
        ___ key __ environ:
            __ key[:5] == 'HTTP_':
                yield key[5:].replace('_', '-').title()
            elif key __ cgikeys:
                yield key.replace('_', '-').title()

    ___ keys r_ [x ___ x __ self]
    ___ __len__ r_ l..(keys())
    ___ __contains__ key): r_ _ekey(key) __ environ



c_ ConfigDict(dict):
    ''' A dict-like configuration storage with additional support for
        namespaces, validators, meta-data, on_change listeners and more.

        This storage is optimized for fast read access. Retrieving a key
        or using non-altering dict methods (e.g. `dict.get()`) has no overhead
        compared to a native dict.
    '''
    __slots__ = ('_meta', '_on_change')

    c_ Namespace(DictMixin):

        ___ -  config, namespace):
            _config = config
            _prefix = namespace

        ___ __getitem__ key):
            depr('Accessing namespaces as dicts is discouraged. '
                 'Only use flat item access: '
                 'cfg["names"]["pace"]["key"] -> cfg["name.space.key"]') #0.12
            r_ _config[_prefix + '.' + key]

        ___ __setitem__ key, value):
            _config[_prefix + '.' + key] = value

        ___ __delitem__ key):
            del _config[_prefix + '.' + key]

        ___ __iter__
            ns_prefix = _prefix + '.'
            ___ key __ _config:
                ns, dot, name = key.rpartition('.')
                __ ns == _prefix a.. name:
                    yield name

        ___ keys r_ [x ___ x __ self]
        ___ __len__ r_ l..(keys())
        ___ __contains__ key): r_ _prefix + '.' + key __ _config
        ___ __repr__ r_ '<Config.Namespace @.*>' @ _prefix
        ___ __str__ r_ '<Config.Namespace @.*>' @ _prefix

        # Deprecated ConfigDict features
        ___ __getattr__ key):
            depr('Attribute access is deprecated.') #0.12
            __ key n.. __ self a.. key[0].isupper():
                self[key] = ConfigDict.Namespace(_config, _prefix + '.' + key)
            __ key n.. __ self a.. key.startswith('__'):
                raise AttributeError(key)
            r_ get(key)

        ___ __setattr__ key, value):
            __ key __ ('_config', '_prefix'):
                __dict__[key] = value
                r_
            depr('Attribute assignment is deprecated.') #0.12
            __ hasattr(DictMixin, key):
                raise AttributeError('Read-only attribute.')
            __ key __ self a.. self[key] a.. isinstance(self[key], __class__):
                raise AttributeError('Non-empty namespace attribute.')
            self[key] = value

        ___ __delattr__ key):
            __ key __ self:
                val = pop(key)
                __ isinstance(val, __class__):
                    prefix = key + '.'
                    ___ key __ self:
                        __ key.startswith(prefix):
                            del self[prefix+key]

        ___ __call__ *a, **ka):
            depr('Calling ConfDict is deprecated. Use the update() method.') #0.12
            update(*a, **ka)
            r_ self

    ___ -  *a, **ka):
        _meta = {}
        _on_change = lambda name, value: N..
        __ a or ka:
            depr('Constructor does no longer accept parameters.') #0.12
            update(*a, **ka)

    ___ load_config filename):
        ''' Load values from an *.ini style config file.

            If the config file contains sections, their names are used as
            namespaces for the values within. The two special sections
            ``DEFAULT`` and ``bottle`` refer to the root namespace (no prefix).
        '''
        conf = ConfigParser()
        conf.read(filename)
        ___ section __ conf.sections():
            ___ key, value __ conf.items(section):
                __ section n.. __ ('DEFAULT', 'bottle'):
                    key = section + '.' + key
                self[key] = value
        r_ self

    ___ load_dict source, namespace='', make_namespaces=False):
        ''' Import values from a dictionary structure. Nesting can be used to
            represent namespaces.

            >>> ConfigDict().load_dict({'name': {'space': {'key': 'value'}}})
            {'name.space.key': 'value'}
        '''
        stack = [(namespace, source)]
        w___ stack:
            prefix, source = stack.pop()
            __ n.. isinstance(source, dict):
                raise TypeError('Source is not a dict (r)' @ type(key))
            ___ key, value __ source.items():
                __ n.. isinstance(key, basestring):
                    raise TypeError('Key is not a string (%r)' @ type(key))
                full_key = prefix + '.' + key __ prefix else key
                __ isinstance(value, dict):
                    stack.a.. ((full_key, value))
                    __ make_namespaces:
                        self[full_key] = Namespace full_key)
                else:
                    self[full_key] = value
        r_ self

    ___ update *a, **ka):
        ''' If the first parameter is a string, all keys are prefixed with this
            namespace. Apart from that it works just as the usual dict.update().
            Example: ``update('some.namespace', key='value')`` '''
        prefix = ''
        __ a a.. isinstance(a[0], basestring):
            prefix = a[0].strip('.') + '.'
            a = a[1:]
        ___ key, value __ dict(*a, **ka).items():
            self[prefix+key] = value

    ___ setdefault key, value):
        __ key n.. __ self:
            self[key] = value
        r_ self[key]

    ___ __setitem__ key, value):
        __ n.. isinstance(key, basestring):
            raise TypeError('Key has type %r (not a string)' @ type(key))

        value = meta_get(key, 'filter', lambda x: x)(value)
        __ key __ self a.. self[key] __ value:
            r_
        _on_change(key, value)
        dict.__setitem__ key, value)

    ___ __delitem__ key):
        dict.__delitem__ key)

    ___ clear
        ___ key __ self:
            del self[key]

    ___ meta_get key, metafield, default=N..):
        ''' Return the value of a meta field for a key. '''
        r_ _meta.get(key, {}).get(metafield, default)

    ___ meta_set key, metafield, value):
        ''' Set the meta field for a key to a new value. This triggers the
            on-change handler for existing keys. '''
        _meta.setdefault(key, {})[metafield] = value
        __ key __ self:
            self[key] = self[key]

    ___ meta_list key):
        ''' Return an iterable of meta field names defined for a key. '''
        r_ _meta.get(key, {}).keys()

    # Deprecated ConfigDict features
    ___ __getattr__ key):
        depr('Attribute access is deprecated.') #0.12
        __ key n.. __ self a.. key[0].isupper():
            self[key] = Namespace key)
        __ key n.. __ self a.. key.startswith('__'):
            raise AttributeError(key)
        r_ get(key)

    ___ __setattr__ key, value):
        __ key __ __slots__:
            r_ dict.__setattr__ key, value)
        depr('Attribute assignment is deprecated.') #0.12
        __ hasattr(dict, key):
            raise AttributeError('Read-only attribute.')
        __ key __ self a.. self[key] a.. isinstance(self[key], Namespace):
            raise AttributeError('Non-empty namespace attribute.')
        self[key] = value

    ___ __delattr__ key):
        __ key __ self:
            val = pop(key)
            __ isinstance(val, Namespace):
                prefix = key + '.'
                ___ key __ self:
                    __ key.startswith(prefix):
                        del self[prefix+key]

    ___ __call__ *a, **ka):
        depr('Calling ConfDict is deprecated. Use the update() method.') #0.12
        update(*a, **ka)
        r_ self



c_ AppStack(list):
    """ A stack-like list. Calling it returns the head of the stack. """

    ___ __call__
        """ Return the current default application. """
        r_ self[-1]

    ___ push value=N..):
        """ Add a new :class:`Bottle` instance to the stack """
        __ n.. isinstance(value, Bottle):
            value = Bottle()
        a.. (value)
        r_ value


c_ WSGIFileWrapper(object):

    ___ -  fp, buffer_size=1024*64):
        fp, buffer_size = fp, buffer_size
        ___ attr __ ('fileno', 'close', 'read', 'readlines', 'tell', 'seek'):
            __ hasattr(fp, attr): setattr attr, getattr(fp, attr))

    ___ __iter__
        buff, read = buffer_size, read
        w___ True:
            part = read(buff)
            __ n.. part: r_
            yield part


c_ _closeiter(object):
    ''' This only exists to be able to attach a .close method to iterators that
        do not support attribute assignment (most of itertools). '''

    ___ -  iterator, close=N..):
        iterator = iterator
        close_callbacks = makelist(close)

    ___ __iter__
        r_ iter(iterator)

    ___ close
        ___ func __ close_callbacks:
            func()


c_ ResourceManager(object):
    ''' This class manages a list of search paths and helps to find and open
        application-bound resources (files).

        :param base: default value for :meth:`add_path` calls.
        :param opener: callable used to open resources.
        :param cachemode: controls which lookups are cached. One of 'all',
                         'found' or 'none'.
    '''

    ___ -  base='./', opener=open, cachemode='all'):
        opener = open
        base = base
        cachemode = cachemode

        #: A list of search paths. See :meth:`add_path` ___ details.
        path   # list
        #: A cache ___ resolved paths. ``res.cache.clear()`` clears the cache.
        cache = {}

    ___ add_path path, base=N.., index=N.., create=False):
        ''' Add a new path to the list of search paths. Return False if the
            path does not exist.

            :param path: The new search path. Relative paths are turned into
                an absolute and normalized form. If the path looks like a file
                (not ending in `/`), the filename is stripped off.
            :param base: Path used to absolutize relative search paths.
                Defaults to :attr:`base` which defaults to ``os.getcwd()``.
            :param index: Position within the list of search paths. Defaults
                to last index (appends to the list).

            The `base` parameter makes it easy to reference files installed
            along with a python module or package::

                res.add_path('./resources/', __file__)
        '''
        base = os.path.abspath(os.path.dirname(base or base))
        path = os.path.abspath(os.path.join(base, os.path.dirname(path)))
        path += os.sep
        __ path __ path:
            path.remove(path)
        __ create a.. n.. os.path.isdir(path):
            os.makedirs(path)
        __ index __ N..:
            path.a.. (path)
        else:
            path.insert(index, path)
        cache.clear()
        r_ os.path.exists(path)

    ___ __iter__
        ''' Iterate over all existing files in all registered paths. '''
        search = path[:]
        w___ search:
            path = search.pop()
            __ n.. os.path.isdir(path): continue
            ___ name __ os.listdir(path):
                full = os.path.join(path, name)
                __ os.path.isdir(full): search.a.. (full)
                else: yield full

    ___ lookup name):
        ''' Search for a resource and return an absolute file path, or `None`.

            The :attr:`path` list is searched in order. The first match is
            returend. Symlinks are followed. The result is cached to speed up
            future lookups. '''
        __ name n.. __ cache or DEBUG:
            ___ path __ path:
                fpath = os.path.join(path, name)
                __ os.path.isfile(fpath):
                    __ cachemode __ ('all', 'found'):
                        cache[name] = fpath
                    r_ fpath
            __ cachemode == 'all':
                cache[name] = N..
        r_ cache[name]

    ___ open name, mode='r', *args, **kwargs):
        ''' Find a resource and return a file object, or raise IOError. '''
        fname = lookup(name)
        __ n.. fname: raise IOError("Resource %r not found." @ name)
        r_ opener(fname, mode=mode, *args, **kwargs)


c_ FileUpload(object):

    ___ -  fileobj, name, filename, headers=N..):
        ''' Wrapper for file uploads. '''
        #: Open file(-like) object (BytesIO buffer or temporary file)
        file = fileobj
        #: Name of the upload form field
        name = name
        #: Raw filename as sent by the client (may contain unsafe characters)
        raw_filename = filename
        #: A :class:`HeaderDict` with additional headers (e.g. content-type)
        headers = HeaderDict(headers) __ headers else HeaderDict()

    content_type = HeaderProperty('Content-Type')
    content_length = HeaderProperty('Content-Length', reader=in., default=-1)

    ___ get_header name, default=N..):
        """ Return the value of a header within the mulripart part. """
        r_ headers.get(name, default)

    @cached_property
    ___ filename
        ''' Name of the file on the client file system, but normalized to ensure
            file system compatibility. An empty filename is returned as 'empty'.

            Only ASCII letters, digits, dashes, underscores and dots are
            allowed in the final filename. Accents are removed, if possible.
            Whitespace is replaced by a single dash. Leading or tailing dots
            or dashes are removed. The filename is limited to 255 characters.
        '''
        fname = raw_filename
        __ n.. isinstance(fname, unicode):
            fname = fname.decode('utf8', 'ignore')
        fname = normalize('NFKD', fname).encode('ASCII', 'ignore').decode('ASCII')
        fname = os.path.basename(fname.replace('\\', os.path.sep))
        fname = re.sub(r'[^a-zA-Z0-9-_.\s]', '', fname).strip()
        fname = re.sub(r'[-\s]+', '-', fname).strip('.-')
        r_ fname[:255] or 'empty'

    ___ _copy_file fp, chunk_size=2**16):
        read, write, offset = file.read, fp.write, file.tell()
        w___ 1:
            buf = read(chunk_size)
            __ n.. buf: break
            write(buf)
        file.seek(offset)

    ___ save destination, overwrite=False, chunk_size=2**16):
        ''' Save file to disk or copy its content to an open file(-like) object.
            If *destination* is a directory, :attr:`filename` is added to the
            path. Existing files are not overwritten by default (IOError).

            :param destination: File path, directory or file(-like) object.
            :param overwrite: If True, replace existing files. (default: False)
            :param chunk_size: Bytes to read at a time. (default: 64kb)
        '''
        __ isinstance(destination, basestring): # Except file-likes here
            __ os.path.isdir(destination):
                destination = os.path.join(destination, filename)
            __ n.. overwrite a.. os.path.exists(destination):
                raise IOError('File exists.')
            with open(destination, 'wb') __ fp:
                _copy_file(fp, chunk_size)
        else:
            _copy_file(destination, chunk_size)






###############################################################################
# Application Helper ###########################################################
###############################################################################


___ abort(code=500, text='Unknown Error.'):
    """ Aborts execution and causes a HTTP error. """
    raise HTTPError(code, text)


___ redirect(url, code=N..):
    """ Aborts execution and causes a 303 or 302 redirect, depending on
        the HTTP protocol version. """
    __ n.. code:
        code = 303 __ request.get('SERVER_PROTOCOL') == "HTTP/1.1" else 302
    res = response.copy(cls=HTTPResponse)
    res.status = code
    res.body = ""
    res.set_header('Location', urljoin(request.url, url))
    raise res


___ _file_iter_range(fp, offset, bytes, maxread=1024*1024):
    ''' Yield chunks from a range in a file. No chunk is bigger than maxread.'''
    fp.seek(offset)
    w___ bytes > 0:
        part = fp.read(min(bytes, maxread))
        __ n.. part: break
        bytes -= l..(part)
        yield part


___ static_file(filename, root, mimetype='auto', download=False, charset='UTF-8'):
    """ Open a file in a safe way and return :exc:`HTTPResponse` with status
        code 200, 305, 403 or 404. The ``Content-Type``, ``Content-Encoding``,
        ``Content-Length`` and ``Last-Modified`` headers are set if possible.
        Special support for ``If-Modified-Since``, ``Range`` and ``HEAD``
        requests.

        :param filename: Name or path of the file to send.
        :param root: Root path for file lookups. Should be an absolute directory
            path.
        :param mimetype: Defines the content-type header (default: guess from
            file extension)
        :param download: If True, ask the browser to open a `Save as...` dialog
            instead of opening the file with the associated program. You can
            specify a custom filename as a string. If not specified, the
            original filename is used (default: False).
        :param charset: The charset to use for files with a ``text/*``
            mime-type. (default: UTF-8)
    """

    root = os.path.abspath(root) + os.sep
    filename = os.path.abspath(os.path.join(root, filename.strip('/\\')))
    headers = dict()

    __ n.. filename.startswith(root):
        r_ HTTPError(403, "Access denied.")
    __ n.. os.path.exists(filename) or n.. os.path.isfile(filename):
        r_ HTTPError(404, "File does not exist.")
    __ n.. os.access(filename, os.R_OK):
        r_ HTTPError(403, "You do not have permission to access this file.")

    __ mimetype == 'auto':
        mimetype, encoding = mimetypes.guess_type(filename)
        __ encoding: headers['Content-Encoding'] = encoding

    __ mimetype:
        __ mimetype[:5] == 'text/' a.. charset a.. 'charset' n.. __ mimetype:
            mimetype += '; charset=@' @ charset
        headers['Content-Type'] = mimetype

    __ download:
        download = os.path.basename(filename __ download == True else download)
        headers['Content-Disposition'] = 'attachment; filename="@"' @ download

    stats = os.stat(filename)
    headers['Content-Length'] = clen = stats.st_size
    lm = t__.strftime("%a, %d %b %Y %H:%M:%S GMT", t__.gmtime(stats.st_mtime))
    headers['Last-Modified'] = lm

    ims = request.environ.get('HTTP_IF_MODIFIED_SINCE')
    __ ims:
        ims = parse_date(ims.split(";")[0].strip())
    __ ims __ n.. N.. a.. ims >= in.(stats.st_mtime):
        headers['Date'] = t__.strftime("%a, %d %b %Y %H:%M:%S GMT", t__.gmtime())
        r_ HTTPResponse(status=304, **headers)

    body = '' __ request.method == 'HEAD' else open(filename, 'rb')

    headers["Accept-Ranges"] = "bytes"
    ranges = request.environ.get('HTTP_RANGE')
    __ 'HTTP_RANGE' __ request.environ:
        ranges = list(parse_range_header(request.environ['HTTP_RANGE'], clen))
        __ n.. ranges:
            r_ HTTPError(416, "Requested Range Not Satisfiable")
        offset, end = ranges[0]
        headers["Content-Range"] = "bytes %d-%d/%d" @ (offset, end-1, clen)
        headers["Content-Length"] = s..(end-offset)
        __ body: body = _file_iter_range(body, offset, end-offset)
        r_ HTTPResponse(body, status=206, **headers)
    r_ HTTPResponse(body, **headers)






###############################################################################
# HTTP Utilities and MISC (TODO) ###############################################
###############################################################################


___ d..(mode=True):
    """ Change the debug level.
    There is only one debug level supported at the moment."""
    g.. DEBUG
    __ mode: warnings.simplefilter('default')
    DEBUG = bool(mode)

___ http_date(value):
    __ isinstance(value, (datedate, datetime)):
        value = value.utctimetuple()
    elif isinstance(value, (in., float)):
        value = t__.gmtime(value)
    __ n.. isinstance(value, basestring):
        value = t__.strftime("%a, %d %b %Y %H:%M:%S GMT", value)
    r_ value

___ parse_date(ims):
    """ Parse rfc1123, rfc850 and asctime timestamps and return UTC epoch. """
    ___
        ts = email.utils.parsedate_tz(ims)
        r_ t__.mktime(ts[:8] + (0,)) - (ts[9] or 0) - t__.timezone
    except (TypeError, ValueError, IndexError, OverflowError):
        r_ N..

___ parse_auth(header):
    """ Parse rfc2617 HTTP authentication header string (basic) and return (user,pass) tuple or None"""
    ___
        method, data = header.split(N.., 1)
        __ method.lower() == 'basic':
            user, pwd = touni(base64.b64decode(tob(data))).split(':',1)
            r_ user, pwd
    except (KeyError, ValueError):
        r_ N..

___ parse_range_header(header, maxlen=0):
    ''' Yield (start, end) ranges parsed from a HTTP Range header. Skip
        unsatisfiable ranges. The end index is non-inclusive.'''
    __ n.. header or header[:6] != 'bytes=': r_
    ranges = [r.split('-', 1) ___ r __ header[6:].split(',') __ '-' __ r]
    ___ start, end __ ranges:
        ___
            __ n.. start:  # bytes=-100     last 100 bytes
                start, end = max(0, maxlen-in.(end)), maxlen
            elif n.. end:  # bytes=100-     all but the first 99 bytes
                start, end = in.(start), maxlen
            else:          # bytes=100-200  bytes 100-200 (inclusive)
                start, end = in.(start), min(in.(end)+1, maxlen)
            __ 0 <= start < end <= maxlen:
                yield start, end
        except ValueError:
            pass

___ _parse_qsl(qs):
    r   # list
    ___ pair __ qs.split('&'):
        __ n.. pair: continue
        nv = pair.split('=', 1)
        __ l..(nv) != 2: nv.a.. ('')
        key = urlunquote(nv[0].replace('+', ' '))
        value = urlunquote(nv[1].replace('+', ' '))
        r.a.. ((key, value))
    r_ r

___ _lscmp(a, b):
    ''' Compares two strings in a cryptographically safe way:
        Runtime is not affected by length of common prefix. '''
    r_ n.. sum(0 __ x==y else 1 ___ x, y __ zip(a, b)) a.. l..(a) == l..(b)


___ cookie_encode(data, key):
    ''' Encode and sign a pickle-able object. Return a (byte) string '''
    msg = base64.b64encode(pickle.dumps(data, -1))
    sig = base64.b64encode(hmac.new(tob(key), msg, digestmod=hashlib.md5).digest())
    r_ tob('!') + sig + tob('?') + msg


___ cookie_decode(data, key):
    ''' Verify and decode an encoded string. Return an object or None.'''
    data = tob(data)
    __ cookie_is_encoded(data):
        sig, msg = data.split(tob('?'), 1)
        __ _lscmp(sig[1:], base64.b64encode(hmac.new(tob(key), msg, digestmod=hashlib.md5).digest())):
            r_ pickle.loads(base64.b64decode(msg))
    r_ N..


___ cookie_is_encoded(data):
    ''' Return True if the argument looks like a encoded cookie.'''
    r_ bool(data.startswith(tob('!')) a.. tob('?') __ data)


___ html_escape(string):
    ''' Escape HTML special characters ``&<>`` and quotes ``'"``. '''
    r_ string.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')\
                 .replace('"','&quot;').replace("'",'&#039;')


___ html_quote(string):
    ''' Escape and quote a string to be used as an HTTP attribute.'''
    r_ '"@"' @ html_escape(string).replace('\n','&#10;')\
                    .replace('\r','&#13;').replace('\t','&#9;')


___ yieldroutes(func):
    """ Return a generator for routes that match the signature (name, args)
    of the func parameter. This may yield more than one route if the function
    takes optional keyword arguments. The output is best described by example::

        a()         -> '/a'
        b(x, y)     -> '/b/<x>/<y>'
        c(x, y=5)   -> '/c/<x>' and '/c/<x>/<y>'
        d(x=5, y=6) -> '/d' and '/d/<x>' and '/d/<x>/<y>'
    """
    path = '/' + func.__name__.replace('__','/').lstrip('/')
    spec = getargspec(func)
    argc = l..(spec[0]) - l..(spec[3] or [])
    path += ('/<@>' * argc) @ tuple(spec[0][:argc])
    yield path
    ___ arg __ spec[0][argc:]:
        path += '/<@>' @ arg
        yield path


___ path_shift(script_name, path_info, shift=1):
    ''' Shift path fragments from PATH_INFO to SCRIPT_NAME and vice versa.

        :return: The modified paths.
        :param script_name: The SCRIPT_NAME path.
        :param script_name: The PATH_INFO path.
        :param shift: The number of path fragments to shift. May be negative to
          change the shift direction. (default: 1)
    '''
    __ shift == 0: r_ script_name, path_info
    pathlist = path_info.strip('/').split('/')
    scriptlist = script_name.strip('/').split('/')
    __ pathlist a.. pathlist[0] == '': pathlist   # list
    __ scriptlist a.. scriptlist[0] == '': scriptlist   # list
    __ shift > 0 a.. shift <= l..(pathlist):
        moved = pathlist[:shift]
        scriptlist = scriptlist + moved
        pathlist = pathlist[shift:]
    elif shift < 0 a.. shift >= -l..(scriptlist):
        moved = scriptlist[shift:]
        pathlist = moved + pathlist
        scriptlist = scriptlist[:shift]
    else:
        empty = 'SCRIPT_NAME' __ shift < 0 else 'PATH_INFO'
        raise AssertionError("Cannot shift. Nothing left from @" @ empty)
    new_script_name = '/' + '/'.join(scriptlist)
    new_path_info = '/' + '/'.join(pathlist)
    __ path_info.endswith('/') a.. pathlist: new_path_info += '/'
    r_ new_script_name, new_path_info


___ auth_basic(check, realm="private", text="Access denied"):
    ''' Callback decorator to require HTTP auth (basic).
        TODO: Add route(check_auth=...) parameter. '''
    ___ decorator(func):
        ___ wrapper(*a, **ka):
            user, password = request.auth or (N.., N..)
            __ user __ N.. or n.. check(user, password):
                err = HTTPError(401, text)
                err.add_header('WWW-Authenticate', 'Basic realm="@"' @ realm)
                r_ err
            r_ func(*a, **ka)
        r_ wrapper
    r_ decorator


# Shortcuts ___ common Bottle methods.
# They all refer to the current default application.

___ make_default_app_wrapper(name):
    ''' Return a callable that relays calls to the current default app. '''
    @functools.wraps(getattr(Bottle, name))
    ___ wrapper(*a, **ka):
        r_ getattr(app(), name)(*a, **ka)
    r_ wrapper

route     = make_default_app_wrapper('route')
get       = make_default_app_wrapper('get')
post      = make_default_app_wrapper('post')
p..       = make_default_app_wrapper('put')
delete    = make_default_app_wrapper('delete')
error     = make_default_app_wrapper('error')
mount     = make_default_app_wrapper('mount')
hook      = make_default_app_wrapper('hook')
install   = make_default_app_wrapper('install')
uninstall = make_default_app_wrapper('uninstall')
url       = make_default_app_wrapper('get_url')







###############################################################################
# Server Adapter ###############################################################
###############################################################################


c_ ServerAdapter(object):
    quiet = False
    ___ -  host='127.0.0.1', port=8080, **options):
        options = options
        host = host
        port = in.(port)

    ___ run handler): # pragma: no cover
        pass

    ___ __repr__
        args = ', '.join(['@=@'@(k,repr(v)) ___ k, v __ options.items()])
        r_ "@(@)" @ (__class__.__name__, args)


c_ CGIServer(ServerAdapter):
    quiet = True
    ___ run handler): # pragma: no cover
        from wsgiref.handlers ______ CGIHandler
        ___ fixed_environ(environ, start_response):
            environ.setdefault('PATH_INFO', '')
            r_ handler(environ, start_response)
        CGIHandler().run(fixed_environ)


c_ FlupFCGIServer(ServerAdapter):
    ___ run handler): # pragma: no cover
        ______ flup.server.fcgi
        options.setdefault('bindAddress', (host, port))
        flup.server.fcgi.WSGIServer(handler, **options).run()


c_ WSGIRefServer(ServerAdapter):
    ___ run app): # pragma: no cover
        from wsgiref.simple_server ______ WSGIRequestHandler, WSGIServer
        from wsgiref.simple_server ______ make_server
        ______ socket

        c_ FixedHandler(WSGIRequestHandler):
            ___ address_string # Prevent reverse DNS lookups please.
                r_ client_address[0]
            ___ log_request(*args, **kw):
                __ n.. quiet:
                    r_ WSGIRequestHandler.log_request(*args, **kw)

        handler_cls = options.get('handler_class', FixedHandler)
        server_cls  = options.get('server_class', WSGIServer)

        __ ':' __ host: # Fix wsgiref ___ IPv6 addresses.
            __ getattr(server_cls, 'address_family') == socket.AF_INET:
                c_ server_cls(server_cls):
                    address_family = socket.AF_INET6

        srv = make_server(host, port, app, server_cls, handler_cls)
        srv.serve_forever()


c_ CherryPyServer(ServerAdapter):
    ___ run handler): # pragma: no cover
        from cherrypy ______ wsgiserver
        options['bind_addr'] = (host, port)
        options['wsgi_app'] = handler

        certfile = options.get('certfile')
        __ certfile:
            del options['certfile']
        keyfile = options.get('keyfile')
        __ keyfile:
            del options['keyfile']

        server = wsgiserver.CherryPyWSGIServer(**options)
        __ certfile:
            server.ssl_certificate = certfile
        __ keyfile:
            server.ssl_private_key = keyfile

        ___
            server.s..
        ______
            server.stop()


c_ WaitressServer(ServerAdapter):
    ___ run handler):
        from waitress ______ serve
        serve(handler, host=host, port=port)


c_ PasteServer(ServerAdapter):
    ___ run handler): # pragma: no cover
        from paste ______ httpserver
        from paste.translogger ______ TransLogger
        handler = TransLogger(handler, setup_console_handler=(n.. quiet))
        httpserver.serve(handler, host=host, port=s..(port),
                         **options)


c_ MeinheldServer(ServerAdapter):
    ___ run handler):
        from meinheld ______ server
        server.listen((host, port))
        server.run(handler)


c_ FapwsServer(ServerAdapter):
    """ Extremely fast webserver using libev. See http://www.fapws.org/ """
    ___ run handler): # pragma: no cover
        ______ fapws._evwsgi __ evwsgi
        from fapws ______ base, config
        port = port
        __ float(config.SERVER_IDENT[-2:]) > 0.4:
            # fapws3 silently changed its API __ 0.5
            port = s..(port)
        evwsgi.start(host, port)
        # fapws3 never releases the GIL. Complain upstream. I tried. No luck.
        __ 'BOTTLE_CHILD' __ os.environ a.. n.. quiet:
            _stderr("WARNING: Auto-reloading does not work with Fapws3.\n")
            _stderr("         (Fapws3 breaks python thread support)\n")
        evwsgi.set_base_module(base)
        ___ app(environ, start_response):
            environ['wsgi.multiprocess'] = False
            r_ handler(environ, start_response)
        evwsgi.wsgi_cb(('', app))
        evwsgi.run()


c_ TornadoServer(ServerAdapter):
    """ The super hyped asynchronous server by facebook. Untested. """
    ___ run handler): # pragma: no cover
        ______ tornado.wsgi, tornado.httpserver, tornado.ioloop
        container = tornado.wsgi.WSGIContainer(handler)
        server = tornado.httpserver.HTTPServer(container)
        server.listen(port=port,address=host)
        tornado.ioloop.IOLoop.instance().s..


c_ AppEngineServer(ServerAdapter):
    """ Adapter for Google App Engine. """
    quiet = True
    ___ run handler):
        from google.appengine.ext.webapp ______ util
        # A main() function __ the handler script enables 'App Caching'.
        # Lets makes sure it is there. This _really_ improves performance.
        module = sys.modules.get('__main__')
        __ module a.. n.. hasattr(module, 'main'):
            module.main = lambda: util.run_wsgi_app(handler)
        util.run_wsgi_app(handler)


c_ TwistedServer(ServerAdapter):
    """ Untested. """
    ___ run handler):
        from twisted.web ______ server, wsgi
        from twisted.python.threadpool ______ ThreadPool
        from twisted.internet ______ reactor
        thread_pool = ThreadPool()
        thread_pool.s..
        reactor.addSystemEventTrigger('after', 'shutdown', thread_pool.stop)
        factory = server.Site(wsgi.WSGIResource(reactor, thread_pool, handler))
        reactor.listenTCP(port, factory, interface=host)
        reactor.run()


c_ DieselServer(ServerAdapter):
    """ Untested. """
    ___ run handler):
        from diesel.protocols.wsgi ______ WSGIApplication
        app = WSGIApplication(handler, port=port)
        app.run()


c_ GeventServer(ServerAdapter):
    """ Untested. Options:

        * `fast` (default: False) uses libevent's http server, but has some
          issues: No streaming, no pipelining, no SSL.
        * See gevent.wsgi.WSGIServer() documentation for more options.
    """
    ___ run handler):
        from gevent ______ pywsgi, local
        __ n.. isinstance(_.local(), local.local):
            msg = "Bottle requires gevent.monkey.patch_all() (before ______)"
            raise RuntimeError(msg)
        __ options.pop('fast', N..):
            depr('The "fast" option has been deprecated and removed by Gevent.')
        __ quiet:
            options['log'] = N..
        address = (host, port)
        server = pywsgi.WSGIServer(address, handler, **options)
        __ 'BOTTLE_CHILD' __ os.environ:
            ______ signal
            signal.signal(signal.SIGINT, lambda s, f: server.stop())
        server.serve_forever()


c_ GeventSocketIOServer(ServerAdapter):
    ___ runhandler):
        from socketio ______ server
        address = (host, port)
        server.SocketIOServer(address, handler, **options).serve_forever()


c_ GunicornServer(ServerAdapter):
    """ Untested. See http://gunicorn.org/configure.html for options. """
    ___ run handler):
        from gunicorn.app.base ______ Application

        config = {'bind': "@:%d" @ (host, in.(port))}
        config.update(options)

        c_ GunicornApplication(Application):
            ___ init parser, opts, args):
                r_ config

            ___ load
                r_ handler

        GunicornApplication().run()


c_ EventletServer(ServerAdapter):
    """ Untested """
    ___ run handler):
        from eventlet ______ wsgi, listen
        ___
            wsgi.server(listen((host, port)), handler,
                        log_output=(n.. quiet))
        except TypeError:
            # Fallback, if we have old version of eventlet
            wsgi.server(listen((host, port)), handler)


c_ RocketServer(ServerAdapter):
    """ Untested. """
    ___ run handler):
        from rocket ______ Rocket
        server = Rocket((host, port), 'wsgi', { 'wsgi_app' : handler })
        server.s..


c_ BjoernServer(ServerAdapter):
    """ Fast server written in C: https://github.com/jonashaag/bjoern """
    ___ run handler):
        from bjoern ______ run
        run(handler, host, port)


c_ AutoServer(ServerAdapter):
    """ Untested. """
    adapters = [WaitressServer, PasteServer, TwistedServer, CherryPyServer, WSGIRefServer]
    ___ run handler):
        ___ sa __ adapters:
            ___
                r_ sa(host, port, **options).run(handler)
            except ImportError:
                pass

server_names = {
    'cgi': CGIServer,
    'flup': FlupFCGIServer,
    'wsgiref': WSGIRefServer,
    'waitress': WaitressServer,
    'cherrypy': CherryPyServer,
    'paste': PasteServer,
    'fapws3': FapwsServer,
    'tornado': TornadoServer,
    'gae': AppEngineServer,
    'twisted': TwistedServer,
    'diesel': DieselServer,
    'meinheld': MeinheldServer,
    'gunicorn': GunicornServer,
    'eventlet': EventletServer,
    'gevent': GeventServer,
    'geventSocketIO':GeventSocketIOServer,
    'rocket': RocketServer,
    'bjoern' : BjoernServer,
    'auto': AutoServer,
}






###############################################################################
# Application Control ##########################################################
###############################################################################


___ load(target, **namespace):
    """ Import a module or fetch an object from a module.

        * ``package.module`` returns `module` as a module object.
        * ``pack.mod:name`` returns the module variable `name` from `pack.mod`.
        * ``pack.mod:func()`` calls `pack.mod.func()` and returns the result.

        The last form accepts not only function calls, but any type of
        expression. Keyword arguments passed to this function are available as
        local variables. Example: ``import_string('re:compile(x)', x='[a-z]')``
    """
    module, target = target.split(":", 1) __ ':' __ target else (target, N..)
    __ module n.. __ sys.modules: __import__(module)
    __ n.. target: r_ sys.modules[module]
    __ target.isalnum(): r_ getattr(sys.modules[module], target)
    package_name = module.split('.')[0]
    namespace[package_name] = sys.modules[package_name]
    r_ eval('@.@' @ (module, target), namespace)


___ load_app(target):
    """ Load a bottle application from a module and make sure that the ______
        does not affect the current default application, but returns a separate
        application object. See :func:`load` for the target parameter. """
    g.. NORUN; NORUN, nr_old = True, NORUN
    ___
        tmp = default_app.push() # Create a new "default application"
        rv = load(target) # Import the target module
        r_ rv __ callable(rv) else tmp
    ______
        default_app.remove(tmp) # Remove the temporary added default application
        NORUN = nr_old

_debug = d..
___ run(app=N.., server='wsgiref', host='127.0.0.1', port=8080,
        interval=1, reloader=False, quiet=False, plugins=N..,
        d..=N.., **kargs):
    """ Start a server instance. This method blocks until the server terminates.

        :param app: WSGI application or target string supported by
               :func:`load_app`. (default: :func:`default_app`)
        :param server: Server adapter to use. See :data:`server_names` keys
               for valid names or pass a :class:`ServerAdapter` subclass.
               (default: `wsgiref`)
        :param host: Server address to bind to. Pass ``0.0.0.0`` to listens on
               all interfaces including the external one. (default: 127.0.0.1)
        :param port: Server port to bind to. Values below 1024 require root
               privileges. (default: 8080)
        :param reloader: Start auto-reloading server? (default: False)
        :param interval: Auto-reloader interval in seconds (default: 1)
        :param quiet: Suppress output to stdout and stderr? (default: False)
        :param options: Options passed to the server adapter.
     """
    __ NORUN: r_
    __ reloader a.. n.. os.environ.get('BOTTLE_CHILD'):
        ___
            lockfile = N..
            fd, lockfile = tempfile.mkstemp(prefix='bottle.', suffix='.lock')
            os.close(fd) # We only need this file to exist. We never write to it
            w___ os.path.exists(lockfile):
                args = [sys.executable] + sys.argv
                environ = os.environ.copy()
                environ['BOTTLE_CHILD'] = 'true'
                environ['BOTTLE_LOCKFILE'] = lockfile
                p = subprocess.Popen(args, env=environ)
                w___ p.poll() __ N..: # Busy wait...
                    os.utime(lockfile, N..) # I am alive!
                    t__.s..(interval)
                __ p.poll() != 3:
                    __ os.path.exists(lockfile): os.unlink(lockfile)
                    sys.exit(p.poll())
        except KeyboardInterrupt:
            pass
        ______
            __ os.path.exists(lockfile):
                os.unlink(lockfile)
        r_

    ___
        __ d.. __ n.. N..: _debug(d..)
        app = app or default_app()
        __ isinstance(app, basestring):
            app = load_app(app)
        __ n.. callable(app):
            raise ValueError("Application is not callable: %r" @ app)

        ___ plugin __ plugins or []:
            app.install(plugin)

        __ server __ server_names:
            server = server_names.get(server)
        __ isinstance(server, basestring):
            server = load(server)
        __ isinstance(server, type):
            server = server(host=host, port=port, **kargs)
        __ n.. isinstance(server, ServerAdapter):
            raise ValueError("Unknown or unsupported server: %r" @ server)

        server.quiet = server.quiet or quiet
        __ n.. server.quiet:
            _stderr("Bottle v@ server starting up (using @)...\n" @ (__version__, repr(server)))
            _stderr("Listening on http://@:%d/\n" @ (server.host, server.port))
            _stderr("Hit Ctrl-C to quit.\n\n")

        __ reloader:
            lockfile = os.environ.get('BOTTLE_LOCKFILE')
            bgcheck = FileCheckerThread(lockfile, interval)
            with bgcheck:
                server.run(app)
            __ bgcheck.status == 'reload':
                sys.exit(3)
        else:
            server.run(app)
    except KeyboardInterrupt:
        pass
    except (SystemExit, MemoryError):
        raise
    _______
        __ n.. reloader: raise
        __ n.. getattr(server, 'quiet', quiet):
            print_exc()
        t__.s..(interval)
        sys.exit(3)



c_ FileCheckerThread(_.?):
    ''' Interrupt main-thread as soon as a changed module file is detected,
        the lockfile gets deleted or gets to old. '''

    ___ -  lockfile, interval):
        _.?.- (self)
        lockfile, interval = lockfile, interval
        #: Is one of 'reload', 'error' or 'exit'
        status = N..

    ___ run
        exists = os.path.exists
        mtime = lambda path: os.stat(path).st_mtime
        files = dict()

        ___ module __ list(sys.modules.values()):
            path = getattr(module, '__file__', '') or ''
            __ path[-4:] __ ('.pyo', '.pyc'): path = path[:-1]
            __ path a.. exists(path): files[path] = mtime(path)

        w___ n.. status:
            __ n.. exists(lockfile)\
            or mtime(lockfile) < t__.t__() - interval - 5:
                status = 'error'
                thread.interrupt_main()
            ___ path, lmtime __ list(files.items()):
                __ n.. exists(path) or mtime(path) > lmtime:
                    status = 'reload'
                    thread.interrupt_main()
                    break
            t__.s..(interval)

    ___ __enter__
        s..

    ___ __exit__ exc_type, exc_val, exc_tb):
        __ n.. status: status = 'exit' # silent exit
        j..
        r_ exc_type __ n.. N.. a.. issubclass(exc_type, KeyboardInterrupt)





###############################################################################
# Template Adapters ############################################################
###############################################################################


c_ TemplateError(HTTPError):
    ___ -  message):
        HTTPError.-  500, message)


c_ BaseTemplate(object):
    """ Base class and minimal API for template adapters """
    extensions = ['tpl','html','thtml','stpl']
    settings = {} #used __ prepare()
    defaults = {} #used __ render()

    ___ -  source=N.., name=N.., lookup=[], encoding='utf8', **settings):
        """ Create a new template.
        If the source parameter (str or buffer) is missing, the name argument
        is used to guess a template filename. Subclasses can assume that
        self.source and/or self.filename are set. Both are strings.
        The lookup, encoding and settings parameters are stored as instance
        variables.
        The lookup parameter stores a list containing directory paths.
        The encoding parameter should be used to decode byte strings or files.
        The settings parameter contains a dict for engine-specific settings.
        """
        name = name
        source = source.read() __ hasattr(source, 'read') else source
        filename = source.filename __ hasattr(source, 'filename') else N..
        lookup = [os.path.abspath(x) ___ x __ lookup]
        encoding = encoding
        settings = settings.copy() # Copy from class variable
        settings.update(settings) # Apply
        __ n.. source a.. name:
            filename = search(name, lookup)
            __ n.. filename:
                raise TemplateError('Template @ not found.' @ repr(name))
        __ n.. source a.. n.. filename:
            raise TemplateError('No template specified.')
        prepare(**settings)

    @classmethod
    ___ search(cls, name, lookup=[]):
        """ Search name in all directories specified in lookup.
        First without, then with common extensions. Return first hit. """
        __ n.. lookup:
            depr('The template lookup path list should not be empty.') #0.12
            lookup = ['.']

        __ os.path.isabs(name) a.. os.path.isfile(name):
            depr('Absolute template path names are deprecated.') #0.12
            r_ os.path.abspath(name)

        ___ spath __ lookup:
            spath = os.path.abspath(spath) + os.sep
            fname = os.path.abspath(os.path.join(spath, name))
            __ n.. fname.startswith(spath): continue
            __ os.path.isfile(fname): r_ fname
            ___ ext __ cls.extensions:
                __ os.path.isfile('@.@' @ (fname, ext)):
                    r_ '@.@' @ (fname, ext)

    @classmethod
    ___ global_config(cls, key, *args):
        ''' This reads or sets the global settings stored in class.settings. '''
        __ args:
            cls.settings = cls.settings.copy() # Make settings local to class
            cls.settings[key] = args[0]
        else:
            r_ cls.settings[key]

    ___ prepare **options):
        """ Run preparations (parsing, caching, ...).
        It should be possible to call this again to refresh a template or to
        update settings.
        """
        raise NotImplementedError

    ___ render *args, **kwargs):
        """ Render the template with the specified local variables and return
        a single byte or unicode string. If it is a byte string, the encoding
        must match self.encoding. This method must be thread-safe!
        Local variables may be provided in dictionaries (args)
        or directly, as keywords (kwargs).
        """
        raise NotImplementedError


c_ MakoTemplate(BaseTemplate):
    ___ prepare **options):
        from mako.template ______ Template
        from mako.lookup ______ TemplateLookup
        options.update({'input_encoding':encoding})
        options.setdefault('format_exceptions', bool(DEBUG))
        lookup = TemplateLookup(directories=lookup, **options)
        __ source:
            tpl = Template(source, lookup=lookup, **options)
        else:
            tpl = Template(uri=name, filename=filename, lookup=lookup, **options)

    ___ render *args, **kwargs):
        ___ dictarg __ args: kwargs.update(dictarg)
        _defaults = defaults.copy()
        _defaults.update(kwargs)
        r_ tpl.render(**_defaults)


c_ CheetahTemplate(BaseTemplate):
    ___ prepare **options):
        from Cheetah.Template ______ Template
        context = _.local()
        context.vars = {}
        options['searchList'] = [context.vars]
        __ source:
            tpl = Template(source=source, **options)
        else:
            tpl = Template(file=filename, **options)

    ___ render *args, **kwargs):
        ___ dictarg __ args: kwargs.update(dictarg)
        context.vars.update(defaults)
        context.vars.update(kwargs)
        out = s..(tpl)
        context.vars.clear()
        r_ out


c_ Jinja2Template(BaseTemplate):
    ___ prepare filters=N.., tests=N.., globals={}, **kwargs):
        from jinja2 ______ Environment, FunctionLoader
        __ 'prefix' __ kwargs: # TODO: to be removed after a w___
            raise RuntimeError('The keyword argument `prefix` has been removed. '
                'Use the full jinja2 environment name line_statement_prefix instead.')
        env = Environment(loader=FunctionLoader(loader), **kwargs)
        __ filters: env.filters.update(filters)
        __ tests: env.tests.update(tests)
        __ globals: env.globals.update(globals)
        __ source:
            tpl = env.from_string(source)
        else:
            tpl = env.get_template(filename)

    ___ render *args, **kwargs):
        ___ dictarg __ args: kwargs.update(dictarg)
        _defaults = defaults.copy()
        _defaults.update(kwargs)
        r_ tpl.render(**_defaults)

    ___ loader name):
        fname = search(name, lookup)
        __ n.. fname: r_
        with open(fname, "rb") __ f:
            r_ f.read().decode(encoding)


c_ SimpleTemplate(BaseTemplate):

    ___ prepare escape_func=html_escape, noescape=False, syntax=N.., **ka):
        cache = {}
        enc = encoding
        _str = lambda x: touni(x, enc)
        _escape = lambda x: escape_func(touni(x, enc))
        syntax = syntax
        __ noescape:
            _str, _escape = _escape, _str

    @cached_property
    ___ co
        r_ compile(code, filename or '<string>', 'exec')

    @cached_property
    ___ code
        source = source
        __ n.. source:
            with open(filename, 'rb') __ f:
                source = f.read()
        ___
            source, encoding = touni(source), 'utf8'
        except UnicodeError:
            depr('Template encodings other than utf8 are no longer supported.') #0.11
            source, encoding = touni(source, 'latin1'), 'latin1'
        parser = StplParser(source, encoding=encoding, syntax=syntax)
        code = parser.translate()
        encoding = parser.encoding
        r_ code

    ___ _rebase _env, _name=N.., **kwargs):
        __ _name __ N..:
            depr('Rebase function called without arguments.'
                 ' You were probably looking for {{base}}?', True) #0.12
        _env['_rebase'] = (_name, kwargs)

    ___ _include _env, _name=N.., **kwargs):
        __ _name __ N..:
            depr('Rebase function called without arguments.'
                 ' You were probably looking for {{base}}?', True) #0.12
        env = _env.copy()
        env.update(kwargs)
        __ _name n.. __ cache:
            cache[_name] = __class__(name=_name, lookup=lookup)
        r_ cache[_name].execute(env['_stdout'], env)

    ___ execute _stdout, kwargs):
        env = defaults.copy()
        env.update(kwargs)
        env.update({'_stdout': _stdout, '_printlist': _stdout.extend,
            'include': functools.partial(_include, env),
            'rebase': functools.partial(_rebase, env), '_rebase': N..,
            '_str': _str, '_escape': _escape, 'get': env.get,
            'setdefault': env.setdefault, 'defined': env.__contains__ })
        eval(co, env)
        __ env.get('_rebase'):
            subtpl, rargs = env.pop('_rebase')
            rargs['base'] = ''.join(_stdout) #copy stdout
            del _stdout[:] # clear stdout
            r_ _include(env, subtpl, **rargs)
        r_ env

    ___ render *args, **kwargs):
        """ Render the template using keyword arguments as local variables. """
        env = {}; stdout   # list
        ___ dictarg __ args: env.update(dictarg)
        env.update(kwargs)
        execute(stdout, env)
        r_ ''.join(stdout)


c_ StplSyntaxError(TemplateError): pass


c_ StplParser(object):
    ''' Parser for stpl templates. '''
    _re_cache = {} #: Cache ___ compiled re patterns
    # This huge pile of voodoo magic splits python code into 8 different tokens.
    # 1: All kinds of python strings (trust me, it works)
    _re_tok = '([urbURB]?(?:\'\'(?!\')|""(?!")|\'{6}|"{6}' \
               '|\'(?:[^\\\\\']|\\\\.)+?\'|"(?:[^\\\\"]|\\\\.)+?"' \
               '|\'{3}(?:[^\\\\]|\\\\.|\\n)+?\'{3}' \
               '|"{3}(?:[^\\\\]|\\\\.|\\n)+?"{3}))'
    _re_inl = _re_tok.replace('|\\n','') # We re-use this string pattern later
    # 2: Comments (until end of line, but not the newline itself)
    _re_tok += '|(#.*)'
    # 3,4: Open and close grouping tokens
    _re_tok += '|([\\[\\{\\(])'
    _re_tok += '|([\\]\\}\\)])'
    # 5,6: Keywords that start or continue a python block (only start of line)
    _re_tok += '|^([ \\t]*(?:if|for|while|with|try|def|class)\\b)' \
               '|^([ \\t]*(?:elif|else|except|finally)\\b)'
    # 7: Our special 'end' keyword (but only if it stands alone)
    _re_tok += '|((?:^|;)[ \\t]*end[ \\t]*(?=(?:%(block_close)s[ \\t]*)?\\r?$|;|#))'
    # 8: A customizable end-of-code-block template token (only end of line)
    _re_tok += '|(%(block_close)s[ \\t]*(?=\\r?$))'
    # 9: And finally, a single newline. The 10th token is 'everything else'
    _re_tok += '|(\\r?\\n)'

    # Match the start tokens of code areas __ a template
    _re_split = '(?m)^[ \t]*(\\\\?)((%(line_start)s)|(%(block_start)s))(%%?)'
    # Match inline statements (may contain python strings)
    _re_inl = '(?m)%%(inline_start)s((?:@|[^\'"\n]*?)+)%%(inline_end)s' @ _re_inl
    _re_tok = '(?m)' + _re_tok

    default_syntax = '<% %> % {{ }}'

    ___ -  source, syntax=N.., encoding='utf8'):
        source, encoding = touni(source, encoding), encoding
        set_syntax(syntax or default_syntax)
        code_buffer, text_buffer   # list, []
        lineno, offset = 1, 0
        indent, indent_mod = 0, 0
        paren_depth = 0

    ___ get_syntax
        ''' Tokens as a space separated string (default: <% %> % {{ }}) '''
        r_ _syntax

    ___ set_syntax syntax):
        _syntax = syntax
        _tokens = syntax.split()
        __ n.. syntax __ _re_cache:
            names = 'block_start block_close line_start inline_start inline_end'
            etokens = map(re.escape, _tokens)
            pattern_vars = dict(zip(names.split(), etokens))
            patterns = (_re_split, _re_tok, _re_inl)
            patterns = [re.compile(p@pattern_vars) ___ p __ patterns]
            _re_cache[syntax] = patterns
        re_split, re_tok, re_inl = _re_cache[syntax]

    syntax = property(get_syntax, set_syntax)

    ___ translate
        __ offset: raise RuntimeError('Parser is a one time instance.')
        w___ True:
            m = re_split.search(source[offset:])
            __ m:
                text = source[offset:offset+m.s..]
                text_buffer.a.. (text)
                offset += m.end()
                __ m.group(1): # New escape syntax
                    line, sep, _ = source[offset:].partition('\n')
                    text_buffer.a.. (m.group(2)+m.group(5)+line+sep)
                    offset += l..(line+sep)+1
                    continue
                elif m.group(5): # Old escape syntax
                    depr('Escape code lines with a backslash.') #0.12
                    line, sep, _ = source[offset:].partition('\n')
                    text_buffer.a.. (m.group(2)+line+sep)
                    offset += l..(line+sep)+1
                    continue
                flush_text()
                read_code(multiline=bool(m.group(4)))
            else: break
        text_buffer.a.. (source[offset:])
        flush_text()
        r_ ''.join(code_buffer)

    ___ read_code multiline):
        code_line, comment = '', ''
        w___ True:
            m = re_tok.search(source[offset:])
            __ n.. m:
                code_line += source[offset:]
                offset = l..(source)
                write_code(code_line.strip(), comment)
                r_
            code_line += source[offset:offset+m.s..]
            offset += m.end()
            _str, _com, _po, _pc, _blk1, _blk2, _end, _cend, _nl = m.groups()
            __ (code_line or paren_depth > 0) a.. (_blk1 or _blk2): # a if b else c
                code_line += _blk1 or _blk2
                continue
            __ _str:    # Python string
                code_line += _str
            elif _com:  # Python comment (up to EOL)
                comment = _com
                __ multiline a.. _com.strip().endswith(_tokens[1]):
                    multiline = False # Allow end-of-block __ comments
            elif _po:  # open parenthesis
                paren_depth += 1
                code_line += _po
            elif _pc:  # close parenthesis
                __ paren_depth > 0:
                    # we could check ___ matching parentheses here, but it's
                    # easier to leave that to python - just check counts
                    paren_depth -= 1
                code_line += _pc
            elif _blk1: # Start-block keyword (if/___/w___/___/try/...)
                code_line, indent_mod = _blk1, -1
                indent += 1
            elif _blk2: # Continue-block keyword (else/elif/except/...)
                code_line, indent_mod = _blk2, -1
            elif _end:  # The non-standard 'end'-keyword (ends a block)
                indent -= 1
            elif _cend: # The end-code-block template token (usually '%>')
                __ multiline: multiline = False
                else: code_line += _cend
            else: # \n
                write_code(code_line.strip(), comment)
                lineno += 1
                code_line, comment, indent_mod = '', '', 0
                __ n.. multiline:
                    break

    ___ flush_text
        text = ''.join(text_buffer)
        del text_buffer[:]
        __ n.. text: r_
        parts, pos, nl   # list, 0, '\\\n'+'  '*self.indent
        ___ m __ re_inl.finditer(text):
            prefix, pos = text[pos:m.s..], m.end()
            __ prefix:
                parts.a.. (nl.join(map(repr, prefix.splitlines(True))))
            __ prefix.endswith('\n'): parts[-1] += nl
            parts.a.. (process_inline(m.group(1).strip()))
        __ pos < l..(text):
            prefix = text[pos:]
            lines = prefix.splitlines(True)
            __ lines[-1].endswith('\\\\\n'): lines[-1] = lines[-1][:-3]
            elif lines[-1].endswith('\\\\\r\n'): lines[-1] = lines[-1][:-4]
            parts.a.. (nl.join(map(repr, lines)))
        code = '_printlist((@,))' @ ', '.join(parts)
        lineno += code.count('\n')+1
        write_code(code)

    ___ process_inline chunk):
        __ chunk[0] == '!': r_ '_str(@)' @ chunk[1:]
        r_ '_escape(@)' @ chunk

    ___ write_code line, comment=''):
        line, comment = fix_backward_compatibility(line, comment)
        code  = '  ' * (indent+indent_mod)
        code += line.lstrip() + comment + '\n'
        code_buffer.a.. (code)

    ___ fix_backward_compatibility line, comment):
        parts = line.strip().split(N.., 2)
        __ parts a.. parts[0] __ ('include', 'rebase'):
            depr('The include and rebase keywords are functions now.') #0.12
            __ l..(parts) == 1:   r_ "_printlist([base])", comment
            elif l..(parts) == 2: r_ "_=@(%r)" @ tuple(parts), comment
            else:                 r_ "_=@(%r, @)" @ tuple(parts), comment
        __ lineno <= 2 a.. n.. line.strip() a.. 'coding' __ comment:
            m = re.match(r"#.*coding[:=]\s*([-\w.]+)", comment)
            __ m:
                depr('PEP263 encoding strings in templates are deprecated.') #0.12
                enc = m.group(1)
                source = source.encode(encoding).decode(enc)
                encoding = enc
                r_ line, comment.replace('coding','coding*')
        r_ line, comment


___ template(*args, **kwargs):
    '''
    Get a rendered template as a string iterator.
    You can use a name, a filename or a template string as first parameter.
    Template rendering arguments can be passed as dictionaries
    or directly (as keyword arguments).
    '''
    tpl = args[0] __ args else N..
    adapter = kwargs.pop('template_adapter', SimpleTemplate)
    lookup = kwargs.pop('template_lookup', TEMPLATE_PATH)
    tplid = (id(lookup), tpl)
    __ tplid n.. __ TEMPLATES or DEBUG:
        settings = kwargs.pop('template_settings', {})
        __ isinstance(tpl, adapter):
            TEMPLATES[tplid] = tpl
            __ settings: TEMPLATES[tplid].prepare(**settings)
        elif "\n" __ tpl or "{" __ tpl or "%" __ tpl or '$' __ tpl:
            TEMPLATES[tplid] = adapter(source=tpl, lookup=lookup, **settings)
        else:
            TEMPLATES[tplid] = adapter(name=tpl, lookup=lookup, **settings)
    __ n.. TEMPLATES[tplid]:
        abort(500, 'Template (@) not found' @ tpl)
    ___ dictarg __ args[1:]: kwargs.update(dictarg)
    r_ TEMPLATES[tplid].render(kwargs)

mako_template = functools.partial(template, template_adapter=MakoTemplate)
cheetah_template = functools.partial(template, template_adapter=CheetahTemplate)
jinja2_template = functools.partial(template, template_adapter=Jinja2Template)


___ view(tpl_name, **defaults):
    ''' Decorator: renders a template for a handler.
        The handler can control its behavior like that:

          - return a dict of template vars to fill out the template
          - return something other than a dict and the view decorator will not
            process the template, but return the handler result as is.
            This includes returning a HTTPResponse(dict) to get,
            for instance, JSON with autojson or other castfilters.
    '''
    ___ decorator(func):
        @functools.wraps(func)
        ___ wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            __ isinstance(result, (dict, DictMixin)):
                tplvars = defaults.copy()
                tplvars.update(result)
                r_ template(tpl_name, **tplvars)
            elif result __ N..:
                r_ template(tpl_name, defaults)
            r_ result
        r_ wrapper
    r_ decorator

mako_view = functools.partial(view, template_adapter=MakoTemplate)
cheetah_view = functools.partial(view, template_adapter=CheetahTemplate)
jinja2_view = functools.partial(view, template_adapter=Jinja2Template)






###############################################################################
# Constants and Globals ########################################################
###############################################################################


TEMPLATE_PATH = ['./', './views/']
TEMPLATES = {}
DEBUG = False
NORUN = False # If set, run() does nothing. Used by load_app()

#: A dict to map HTTP status codes (e.g. 404) to phrases (e.g. 'Not Found')
HTTP_CODES = httplib.responses
HTTP_CODES[418] = "I'm a teapot" # RFC 2324
HTTP_CODES[422] = "Unprocessable Entity" # RFC 4918
HTTP_CODES[428] = "Precondition Required"
HTTP_CODES[429] = "Too Many Requests"
HTTP_CODES[431] = "Request Header Fields Too Large"
HTTP_CODES[511] = "Network Authentication Required"
_HTTP_STATUS_LINES = dict((k, '%d @'@(k,v)) ___ (k,v) __ HTTP_CODES.items())

#: The default template used ___ error pages. Override with @error()
ERROR_PAGE_TEMPLATE = """
%%try:
    %%from @ ______ DEBUG, HTTP_CODES, request, touni
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html>
        <head>
            <title>Error: {{e.status}}</title>
            <style type="text/css">
              html {background-color: #eee; font-family: sans;}
              body {background-color: #fff; border: 1px solid #ddd;
                    padding: 15px; margin: 15px;}
              pre {background-color: #eee; border: 1px solid #ddd; padding: 5px;}
            </style>
        </head>
        <body>
            <h1>Error: {{e.status}}</h1>
            <p>Sorry, the requested URL <tt>{{repr(request.url)}}</tt>
               caused an error:</p>
            <pre>{{e.body}}</pre>
            %%if DEBUG and e.exception:
              <h2>Exception:</h2>
              <pre>{{repr(e.exception)}}</pre>
            %%end
            %%if DEBUG and e.traceback:
              <h2>Traceback:</h2>
              <pre>{{e.traceback}}</pre>
            %%end
        </body>
    </html>
%%except ImportError:
    <b>ImportError:</b> Could not generate the error page. Please add bottle to
    the ______ path.
%%end
""" @ __name__

#: A thread-safe instance of :class:`LocalRequest`. If accessed from within a
#: request callback, this instance always refers to the *current* request
#: (even on a multithreaded server).
request = LocalRequest()

#: A thread-safe instance of :class:`LocalResponse`. It is used to change the
#: HTTP response ___ the *current* request.
response = LocalResponse()

#: A thread-safe namespace. Not used by Bottle.
local = _.local()

# Initialize app stack (create first empty Bottle app)
# BC: 0.6.4 and needed ___ run()
app = default_app = AppStack()
app.push()

#: A virtual package that redirects ______ statements.
#: Example: ``______ bottle.ext.sqlite`` actually imports `bottle_sqlite`.
ext = _ImportRedirect('bottle.ext' __ __name__ == '__main__' else __name__+".ext", 'bottle_@').module

__ _____ __ ______
    opt, args, parser = _cmd_options, _cmd_args, _cmd_parser
    __ opt.version:
        _stdout('Bottle @\n'@__version__)
        sys.exit(0)
    __ n.. args:
        parser.print_help()
        _stderr('\nError: No application specified.\n')
        sys.exit(1)

    sys.path.insert(0, '.')
    sys.modules.setdefault('bottle', sys.modules['__main__'])

    host, port = (opt.bind or 'localhost'), 8080
    __ ':' __ host a.. host.rfind(']') < host.rfind(':'):
        host, port = host.rsplit(':', 1)
    host = host.strip('[]')

    run(args[0], host=host, port=in.(port), server=opt.server,
        reloader=opt.reload, plugins=opt.plugin, d..=opt.d..)




# THE END
