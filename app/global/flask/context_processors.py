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


@app.context_processor
def ctp_comprehend_roles_processor():
    def ctp_comprehend_roles(roles: Optional[list]) -> Optional[list]:
        """
        Comprehends the roles query into their names
        """
        return [role.rel_role.name for role in roles] if roles else None

    return dict(ctp_comprehend_roles=ctp_comprehend_roles)


@app.context_processor
def ctp_conference_processor():
    def ctp_conference(year: int):
        """
        Gets the media partners for the given year.
        """
        from app.models.conferences import Conferences
        return Conferences.select_by_year(year)

    return dict(ctp_conference=ctp_conference)


@app.context_processor
def ctp_media_partners_processor():
    def ctp_media_partners(year: int):
        """
        Gets the media partners for the given year.
        """
        from app.models.media_partners import MediaPartners
        return MediaPartners.select_by_year(year)

    return dict(ctp_media_partners=ctp_media_partners)


@app.context_processor
def ctp_sponsors_processor():
    def ctp_sponsors(year: int):
        """
        Gets the sponsors for the given year.
        """
        from app.models.sponsors import Sponsors
        return Sponsors.select_by_year(year)

    return dict(ctp_sponsors=ctp_sponsors)
