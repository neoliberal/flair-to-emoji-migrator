"""Converts Images into Reddit Emojis"""

from typing import Dict
from pathlib import Path

def main() -> None:
    print(images())
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

if __name__ == '__main__':
    main()