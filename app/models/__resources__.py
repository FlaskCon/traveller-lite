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


original_display_pictures = [
    {'attribution': 'Ádám Berkecz', 'attribution_url': 'https://unsplash.com/@aberkecz', 'filename': 'ogdp21.png'},
    {'attribution': 'Francesco', 'attribution_url': 'https://unsplash.com/@detpho', 'filename': 'ogdp11.png'},
    {'attribution': 'Tom Dils', 'attribution_url': 'https://unsplash.com/@tdils', 'filename': 'ogdp1.png'},
    {'attribution': 'Gary Bendig', 'attribution_url': 'https://unsplash.com/@kris_ricepees', 'filename': 'ogdp10.png'},
    {'attribution': 'Christopher Carson', 'attribution_url': 'https://unsplash.com/@bhris1017', 'filename': 'ogdp16.png'},
    {'attribution': 'Geranimo', 'attribution_url': 'https://unsplash.com/@geraninmo', 'filename': 'ogdp9.png'},
    {'attribution': 'Cristina Anne Costello', 'attribution_url': 'https://unsplash.com/@lightupphotos', 'filename': 'ogdp15.png'},
    {'attribution': 'Edgar', 'attribution_url': 'https://unsplash.com/@e_d_g_a_r', 'filename': 'ogdp12.png'},
    {'attribution': 'Jamie Haughton', 'attribution_url': 'https://unsplash.com/@haughters', 'filename': 'ogdp8.png'},
    {'attribution': 'Charles Deluvio', 'attribution_url': 'https://unsplash.com/@charlesdeluvio', 'filename': 'ogdp18.png'},
    {'attribution': 'Matthew Henry', 'attribution_url': 'https://unsplash.com/@matthewhenry', 'filename': 'ogdp7.png'},
    {'attribution': 'David Clode', 'attribution_url': 'https://unsplash.com/@davidclode', 'filename': 'ogdp14.png'},
    {'attribution': 'Ricky Kharawala', 'attribution_url': 'https://unsplash.com/@sweetmangostudios', 'filename': 'ogdp3.png'},
    {'attribution': 'Chris Curry', 'attribution_url': 'https://unsplash.com/@chriscurry92', 'filename': 'ogdp17.png'},
    {'attribution': 'Robert Woeger', 'attribution_url': 'https://unsplash.com/@woeger', 'filename': 'ogdp19.png'},
    {'attribution': 'Piotr Łaskawski', 'attribution_url': 'https://unsplash.com/@tot87', 'filename': 'ogdp5.png'},
    {'attribution': 'Andriyko Podilnyk', 'attribution_url': 'https://unsplash.com/@andriyko', 'filename': 'ogdp20.png'},
    {'attribution': 'Sandy Millar', 'attribution_url': 'https://unsplash.com/@sandym10', 'filename': 'ogdp2.png'},
    {'attribution': 'Richard Brutyo', 'attribution_url': 'https://unsplash.com/@richardbrutyo', 'filename': 'ogdp4.png'},
    {'attribution': 'Nathan Anderson', 'attribution_url': 'https://unsplash.com/@nathananderson', 'filename': 'ogdp6.png'}
]
