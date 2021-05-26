try:
    from django.urls import get_resolver
except:
    try:
        from django.core.urlresolvers import get_resolver
    except:
        raise Exception("Can't find Django")

__version__ = "0.1"

def setup(app):
    app.connect('autodoc-process-docstring', add_django_url)


def add_django_url(app, what, name, obj, options, lines):
    if what == 'function':
        res = get_resolver()
        if obj in res.reverse_dict:
            url_struct = res.reverse_dict[obj]
            if len(url_struct) > 0:
                lines.append("URL path(s):")

                for url in url_struct[:-2]:
                    if type(url) == type([]): continue
                    lines.append("   * %s\n" % url)
            else:
                lines.insert(0,"| has NO URL mapping\n")
        else:
            lines.append("URL path(s): NONE")
