from dataclasses import dataclass


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
        {"name": "Volunteer"},
        {"name": "VIP"},
        {"name": "Attendee"},
        {"name": "Emeritus"},
    ]

    sponsor_levels = [
        {"name": "Platinum"},
        {"name": "Gold"},
        {"name": "Silver"},
        {"name": "Bronze"},
        {"name": "Donor"},
    ]
