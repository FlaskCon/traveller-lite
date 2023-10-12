from datetime import datetime, date
from typing import Union, Optional

from flask import current_app as app

from app.utilities import DatetimeDeltaMC


@app.template_filter("days_until_cfp_ends")
def days_until_cfp_ends(call_for_proposals_end_date: Optional[Union[datetime, date]]) -> int:
    """
    Returns the number of days until the CFP ends.
    """
    if isinstance(call_for_proposals_end_date, date):
        now = DatetimeDeltaMC()
        return (call_for_proposals_end_date - now.date).days

    if isinstance(call_for_proposals_end_date, datetime):
        now = DatetimeDeltaMC()
        return (call_for_proposals_end_date.date() - now.date).days

    return 0


@app.template_filter("is_cfp_live")
def is_cfp_live(call_for_proposals_end_date: Optional[Union[datetime, date]]) -> bool:
    """
    Returns True if the CFP is still live, False otherwise.
    """

    if isinstance(call_for_proposals_end_date, date):
        now = DatetimeDeltaMC()
        return True if (call_for_proposals_end_date - now.date).days > 0 else False

    if isinstance(call_for_proposals_end_date, datetime):
        now = DatetimeDeltaMC()
        return True if (call_for_proposals_end_date.date() - now.date).days > 0 else False

    return False


@app.template_filter("day_month")
def day_month(date_or_datetime: Optional[Union[datetime, date]]) -> Optional[str]:
    """
    Returns the day and month of the given date or datetime.
    """

    if isinstance(date_or_datetime, date) or isinstance(date_or_datetime, datetime):
        return f"{date_or_datetime.day} {date_or_datetime.strftime('%b')}"

    return None
