import os


class Image:
    def __init__(self, id, pos, tags):
        self.id = id
        self.pos = pos
        self.tags = set(tags)

    def __str__(self):
        return "Image id #{} oriented {} with tags {}\n".format(self.id, self.pos, self.tags)

    def to_txt(self):
        return "{} {} {} {}\n".format(
            self.id,
            self.pos,
            len(self.tags),
            " ".join(list(self.tags))
        )


def collect_data():
    images = {
        "V": [],
        "H": []
    }
    N = int(input())
    for i in range(N):
        # 1. We collect the data
        image = str.split(input(), " ")
        pos = image[0]
        images[pos].append(
            Image(i, pos, image[2:])
        )

    return images


def v2h_naive(images):
    """
    Group images by pair: it simply takes 2 consecutive vertical images and group them
    :param images: List of V images
    :return: List of H images made of the combination of 2 V images
    """
    images_grouped = []
    for i in range(0, len(images), 2):
        images_grouped.append(Image(
            "{},{}".format(images[i].id, images[i+1].id),
            "H",
            images[i].tags.union(images[i + 1].tags)
        ))
    return images_grouped


def grouper(v2h, output_suffix="_bis"):
    """
    Collects and groups the data before writing it to output file
    """
    example = os.environ['NB']

    images = collect_data()
    all_h_images = images["H"] + v2h(images["V"])
    with open("ex{}{}.txt".format(example, output_suffix), 'w') as file:
        file.write("{}\n".format(len(all_h_images)))
        for image in all_h_images:
            file.write(image.to_txt())


grouper(v2h_naive)
