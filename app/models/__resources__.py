from dataclasses import dataclass
from pprint import pprint


@dataclass
class Resources:
    conference = {
        "year": 2023,
        "index_endpoint": "frontend.2023.index",
        "latest": True,
        "call_for_proposals_start_date": "2023-10-10",
        "call_for_proposals_end_date": "2023-10-20",
        "conference_start_date": "2023-12-16",
        "conference_end_date": "2023-12-17",
    }

    roles = [
        {"name": "Super Administrator", "unique_role_id": 100},
        {"name": "Administrator", "unique_role_id": 101},
        {"name": "Conference Chair", "unique_role_id": 102},
        {"name": "Grants Chair", "unique_role_id": 103},
        {"name": "Volunteer Chair", "unique_role_id": 104},
        {"name": "Sprints Chair", "unique_role_id": 105},
        {"name": "Speaker Support Chair", "unique_role_id": 106},
        {"name": "Sponsorship Chair", "unique_role_id": 107},
        {"name": "Diversity Chair", "unique_role_id": 108},
        {"name": "Code of Conduct Official", "unique_role_id": 109},
        {"name": "Proposal Reviewer", "unique_role_id": 110},
        {"name": "Sponsor", "unique_role_id": 111},
        {"name": "Speaker", "unique_role_id": 112},
        {"name": "Volunteer", "unique_role_id": 114},
        {"name": "VIP", "unique_role_id": 115},
        {"name": "Attendee", "unique_role_id": 116},
        {"name": "Emeritus", "unique_role_id": 117},
    ]

    sponsor_levels = [
        {"name": "Donor"},
        {"name": "Bronze"},
        {"name": "Silver"},
        {"name": "Gold"},
        {"name": "Platinum"},
    ]

    proposal_statuses = [
        {
            "name": "Preparation",
            "description": "Not yet submitted, but saved for safe keeping.",
            "unique_proposal_status_id": 101
        },
        {
            "name": "Submitted",
            "description": "Your proposal has been submitted.",
            "unique_proposal_status_id": 102
        },
        {
            "name": "Under Review",
            "description": "Your proposal is being reviewed by the committee.",
            "unique_proposal_status_id": 103
        },
        {
            "name": "Change Requested",
            "description": "The committee has requested changes to your proposal.",
            "unique_proposal_status_id": 104
        },
        {
            "name": "Changes Made",
            "description": "You have made the requested changes to your proposal.",
            "unique_proposal_status_id": 105
        },
        {
            "name": "Waitlisted",
            "description": "Your proposal was not accepted, but may be accepted if another proposal is cancelled.",
            "unique_proposal_status_id": 106
        },
        {
            "name": "Accepted",
            "description": "Your proposal has been accepted.",
            "unique_proposal_status_id": 107
        },
        {
            "name": "Rejected",
            "description": "Your proposal has been rejected.",
            "unique_proposal_status_id": 108
        },
        {
            "name": "Cancelled",
            "description": "You have cancelled your proposal.",
            "unique_proposal_status_id": 109
        },
    ]

    original_display_pictures = [
        {'attribution': 'System',
         'attribution_url': 'https://flaskcon.com',
         'filename': '__deleted__.png',
         'limited': True,
         'note': 'Deleted account profile picture.',
         'unique_display_picture_id': 9999},

        {'attribution': 'Tom Dils',
         'attribution_url': 'https://unsplash.com/@tdils',
         'filename': 'ogdp1.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 1},

        {'attribution': 'Sandy Millar',
         'attribution_url': 'https://unsplash.com/@sandym10',
         'filename': 'ogdp2.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 2},
        {'attribution': 'Ricky Kharawala',
         'attribution_url': 'https://unsplash.com/@sweetmangostudios',
         'filename': 'ogdp3.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 3},
        {'attribution': 'Richard Brutyo',
         'attribution_url': 'https://unsplash.com/@richardbrutyo',
         'filename': 'ogdp4.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 4},
        {'attribution': 'Piotr Łaskawski',
         'attribution_url': 'https://unsplash.com/@tot87',
         'filename': 'ogdp5.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 5},
        {'attribution': 'Nathan Anderson',
         'attribution_url': 'https://unsplash.com/@nathananderson',
         'filename': 'ogdp6.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 6},
        {'attribution': 'Matthew Henry',
         'attribution_url': 'https://unsplash.com/@matthewhenry',
         'filename': 'ogdp7.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 7},
        {'attribution': 'Jamie Haughton',
         'attribution_url': 'https://unsplash.com/@haughters',
         'filename': 'ogdp8.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 8},
        {'attribution': 'Geranimo',
         'attribution_url': 'https://unsplash.com/@geraninmo',
         'filename': 'ogdp9.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 9},
        {'attribution': 'Gary Bendig',
         'attribution_url': 'https://unsplash.com/@kris_ricepees',
         'filename': 'ogdp10.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 10},
        {'attribution': 'Francesco',
         'attribution_url': 'https://unsplash.com/@detpho',
         'filename': 'ogdp11.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 11},
        {'attribution': 'Edgar',
         'attribution_url': 'https://unsplash.com/@e_d_g_a_r',
         'filename': 'ogdp12.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 12},
        {'attribution': 'David Clode',
         'attribution_url': 'https://unsplash.com/@davidclode',
         'filename': 'ogdp14.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 14},
        {'attribution': 'Cristina Anne Costello',
         'attribution_url': 'https://unsplash.com/@lightupphotos',
         'filename': 'ogdp15.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 15},
        {'attribution': 'Christopher Carson',
         'attribution_url': 'https://unsplash.com/@bhris1017',
         'filename': 'ogdp16.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 16},
        {'attribution': 'Chris Curry',
         'attribution_url': 'https://unsplash.com/@chriscurry92',
         'filename': 'ogdp17.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 17},
        {'attribution': 'Charles Deluvio',
         'attribution_url': 'https://unsplash.com/@charlesdeluvio',
         'filename': 'ogdp18.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 18},
        {'attribution': 'Robert Woeger',
         'attribution_url': 'https://unsplash.com/@woeger',
         'filename': 'ogdp19.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 19},
        {'attribution': 'Andriyko Podilnyk',
         'attribution_url': 'https://unsplash.com/@andriyko',
         'filename': 'ogdp20.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 20},
        {'attribution': 'Ádám Berkecz',
         'attribution_url': 'https://unsplash.com/@aberkecz',
         'filename': 'ogdp21.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 21},
        {'attribution': 'David Carmichael',
         'attribution_url': 'https://github.com/CheeseCake87',
         'filename': 'flaskcon2023.gif',
         'limited': True,
         'note': 'Awarded when you accessed your account during FlaskCon 2023.',
         'unique_display_picture_id': 2023}
    ]


if __name__ == '__main__':
    sorted_display_pictures = sorted(Resources.original_display_pictures, key=lambda x: x['unique_display_picture_id'])
    pprint(sorted_display_pictures)
