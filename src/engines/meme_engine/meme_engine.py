from PIL import Image, ImageFont, ImageDraw
import random, os


class MemeEngine:
    """Meme Engine."""

    def __init__(self, path):
        """Init meme engine with path

        Args:
            path (str): path of img after generate
        """

        self.folder_dir = path
        if not os.path.exists(path):
            os.makedirs(path)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Gernerate meme with img_path, text, and author.

        Args:
            img_path (_type_): img path
            text (_type_): text from qoute
            author (_type_): author from qoute
            width (int, optional): Max width for img. Defaults to 500px.

        Returns:
            str: out_file_path
        """

        out_file_path = os.path.join(
            self.folder_dir, f"meme-{random.randint(0,1000000)}.jpg"
        )

        try:
            with Image.open(img_path) as img:
                img_width, img_height = img.size
                aspect_ratio = img_width / img_height

                new_width = min(img_width, width)
                new_height = int(new_width / aspect_ratio)

                img = img.resize((new_width, new_height))
                draw = ImageDraw.Draw(img)

                font_size = int(img.height / 25)
                font = ImageFont.truetype("./_data/fonts/arial.ttf", font_size)

                x_loc = random.randint(0, int(img.width / 4))
                y_loc = random.randint(0, int(img.height - font_size * 2))

                draw.text((x_loc, y_loc), text, font=font, fill=(0, 0, 0))
                draw.text(
                    (int(x_loc * 1.2), y_loc + font_size), " - " + author, font=font
                )

                img.save(out_file_path)
        except Exception:
            raise "Error generate meme."
        return out_file_path
