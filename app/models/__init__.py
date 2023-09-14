from dataclasses import dataclass

from sqlalchemy import select, update, delete, insert
from sqlalchemy.orm import relationship
from .__mixins__ import MetaMixins

from app.extensions import db


@dataclass
class Resources:
    roles = [
        {"name": "Super Administrator"},
        {"name": "Administrator"},
        {"name": "Conference Chair"},
        {"name": "Grants Chair"},
        {"name": "Volunteer Chair"},
        {"name": "Sprints Chair"},
        {"name": "Speaker Support Chair"},
        {"name": "Sponsorship Chair"},
        {"name": "Diversity Chair"},
        {"name": "Code of Conduct Official"},
        {"name": "Proposal Reviewer"},
        {"name": "Speaker"},
        {"name": "Sponsor"},
        {"name": "Volunteer"},
        {"name": "VIP"},
        {"name": "Attendee"},
        {"name": "Emeritus"},
    ]


__all__ = [
    "db",
    "select",
    "update",
    "delete",
    "insert",
    "relationship",
    "MetaMixins",
    "Resources",
]
