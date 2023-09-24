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
        Home / About

        :param list_of_urls:
        :return:
        """
        markup = ""
        for name, url in list_of_urls:
            if url is None:
                markup += f'{name} / '
            else:
                markup += f'<a href="{url}">{name}</a> / '

        return Markup(f"<strong>{markup[:-3]}</strong>")

    return dict(breadcrumber=breadcrumber)


@app.context_processor
def ctp_display_picture_processor():
    def ctp_display_picture(unique_display_picture_id: int):
        """
        Gets the URL for the given unique_display_picture_id.
        """
        from app.models.display_pictures import DisplayPictures

        return DisplayPictures.select_using_unique_display_picture_id(unique_display_picture_id).filename

    return dict(ctp_display_picture=ctp_display_picture)


@app.context_processor
def ctp_account_processor():
    def ctp_account(account_id: int):
        """
        Gets the URL for the given unique_display_picture_id.
        """
        from app.models.accounts import Accounts

        return Accounts.select_using_account_id(account_id)

    return dict(ctp_account=ctp_account)
