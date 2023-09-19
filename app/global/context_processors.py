from typing import Optional
from flask import current_app as app
from markupsafe import Markup


@app.context_processor
def breadcrumber_processor():
    def breadcrumber(list_of_urls: list[tuple[str, Optional[callable]]]):
        """
        Generates breadcrumbs for the current page for the given list of URLs.
        list_of_urls is a list of tuples, where the first element is the name of the page, and the second element is a
        callable that returns the URL for that page.

        Example:
        {{ breadcrumber([('Home', url_for('www.index')), ('About', url_for('www.about'))]) }}

        Will output:
        / Home / About

        :param list_of_urls:
        :return:
        """
        markup = "/ "
        for name, url in list_of_urls:
            if url is None:
                markup += f'{name} / '
            else:
                markup += f'<a href="{url}">{name}</a> / '

        return Markup(f"<strong>{markup[:-3]}</strong>")

    return dict(breadcrumber=breadcrumber)
