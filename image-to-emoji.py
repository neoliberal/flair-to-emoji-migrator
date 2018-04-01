"""Converts Images into Reddit Emojis"""

from typing import Dict
from pathlib import Path

import praw

import config


def main() -> None:
    images_dict: Dict[str, Path] = images()
    return

def images() -> Dict[str, Path]:
    flairs: Dict[str, Path] = {}
    folder: Path = Path('flairs')

    for directory in folder.iterdir():
        if not directory.is_dir():
            continue

        flair_type: str = directory.stem
        if flair_type.startswith('_'):
            continue

        for image in directory.glob('*.png'):
            flairs[f'{flair_type}-{image.stem[1:]}'] = image
    return flairs

def upload(images_dict: Dict[str, Path]) -> None:
    reddit: praw.Reddit = praw.Reddit(
        client_id=config.client_id,
        client_secret=config.client_secret,
        refresh_token=config.refresh_token
    )
    for image_name, path in images_dict:
        reddit.subreddit(config.subreddit).emoji.add(image_name, str(path))
    return

if __name__ == '__main__':
    main()