from pathlib import Path
from pprint import pprint

if __name__ == '__main__':
    cwd = Path.cwd()

    dps = []

    for filename in cwd.glob('*.png'):
        dps.append(
            {
                "filename": filename.name,
                "attribution": "here",
                "attribution_url": "here"
            }
        )

    pprint(dps, indent=2)
