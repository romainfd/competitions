from tqdm import tqdm
import os
import random as rd


class Image:
    def __init__(self, ids, id, tags):
        self.ids = ids
        self.id = id
        self.tags = set(tags)

    def __str__(self):
        return "Image id #{} representing image(s) {} with tags {}\n".format(self.id, self.ids, self.tags)

    def __eq__(self, other):
        if isinstance(other, Image):
            return self.ids == other.ids
        else:
            return False

    def __hash__(self):
        return int(self.id)

    def to_txt(self):
        return "{}\n".format(
            self.ids
        )

    def score(self, next_image):
        return min(
            len(self.tags.intersection(next_image.tags)),
            len(self.tags.difference(next_image.tags)),
            len(next_image.tags.difference(self.tags))
        )


def collect_data():
    images = set()
    N = int(input())
    for i in range(N):
        image = str.split(input(), " ")
        images.add(
            Image(image[0].replace(",", " "), i, image[3:])
        )

    return images


def line(images, delta=10000):
    """
    Linearly group the pictures: takes delta random images and make the best move from the last image
    :param images: List of V images
    :param int delta: The number of random picks
    :return: List of H images made of the combination of 2 V images
    """
    rd.seed(0)
    current_image = images.pop()
    slideshow = [current_image.to_txt()]
    nb = len(images)
    total_score = 0
    for _ in tqdm(range(nb)):
        max_score = -1
        best_next = None
        images_tuple = tuple(images)
        for _ in range(delta):
            next_image = rd.choice(images_tuple)
            score = current_image.score(next_image)
            if score > max_score:
                max_score = score
                best_next = next_image
        images.remove(best_next)
        slideshow.append(best_next.to_txt())
        current_image = best_next
        total_score += max_score
    print(total_score)
    return slideshow


def grouper(output_suffix="_res"):
    """
    Collects and groups the data before writing it to output file
    """
    example = os.environ['NB']

    images = collect_data()
    with open("ex{}{}.txt".format(example, output_suffix), 'w') as file:
        res = line(images)
        file.write("{}\n".format(len(res)))
        file.write("".join(res))


grouper()
