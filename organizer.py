from pathlib import Path
import shutil

from file_types import FILE_TYPES


class Organizer:

    def organize(self, folder):

        folder = Path(folder)

        result = {}

        for file in folder.iterdir():

            if not file.is_file():
                continue

            moved = False

            for category, extensions in FILE_TYPES.items():

                if file.suffix.lower() in extensions:

                    target = folder / category

                    target.mkdir(exist_ok=True)

                    shutil.move(file, target / file.name)

                    result[category] = result.get(category, 0) + 1

                    moved = True

                    break

            if not moved:

                other = folder / "その他"

                other.mkdir(exist_ok=True)

                shutil.move(file, other / file.name)

                result["その他"] = result.get("その他", 0) + 1

        return result