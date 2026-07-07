from pathlib import Path
import shutil

from file_types import FILE_TYPES


class Organizer:

    
    def get_unique_filename(self, target_folder, filename):
        """
        同名ファイルが存在する場合、
        photo.jpg → photo(1).jpg のように変更する
        """

        destination = target_folder / filename

        if not destination.exists():
            return destination

        stem = destination.stem
        suffix = destination.suffix

        counter = 1

        while True:
            new_name = f"{stem}({counter}){suffix}"
            new_path = target_folder / new_name

            if not new_path.exists():
                return new_path

            counter += 1

    def organize(self, folder, callback=None):

        folder = Path(folder)

        files = [f for f in folder.iterdir() if f.is_file()]
        total_files = len(files)
        processed = 0
        result = {}

        for file in files:

            if not file.is_file():
                continue

            moved = False

            for category, extensions in FILE_TYPES.items():

                if file.suffix.lower() in extensions:

                    target = folder / category

                    target.mkdir(exist_ok=True)

                    destination = self.get_unique_filename(
                        target,
                        file.name
                    )

                    shutil.move(file, destination)

                    result[category] = result.get(category, 0) + 1

                    moved = True

                    break

            if not moved:

                other = folder / "その他"

                other.mkdir(exist_ok=True)

                destination = self.get_unique_filename(
                    other,
                    file.name
                )

                shutil.move(file, destination)

                result["その他"] = result.get("その他", 0) + 1

            processed += 1

            if callback:
                callback(processed, total_files)

        return result