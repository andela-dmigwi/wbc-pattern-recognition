from __future__ import division
from PIL import Image
import math
import os


def long_slice(image_path, outdir):
    """slice an image into parts slice_size into uniform square
    with given slice ssize dimension"""
    img = Image.open(image_path)
    width, height = img.size
    upper = left = 0
    slice_size = 4
    image_map = []
    slices = int(math.ceil(height / slice_size))
    items = new_items = Image.new('RGB', img.size, "white")
    height_count = 1
    for slice in range(slices):
        # if we are at the end, set the lower bound to be the bottom of the
        # image
        if height_count == slices:
            lower = height
        else:
            lower = int(height_count * slice_size)

        more_slices = int(math.ceil(width / slice_size))
        new_left = left
        width_count = 1
        for finer_slice in range(more_slices):
            if width_count == more_slices:
                new_width = width
            else:
                new_width = int(width_count * slice_size)

            new_bbox = (new_left, upper, new_width, lower)
            new_slice = img.crop(new_bbox)

            new_slice.save(os.path.join(outdir + "/images/split_images", str(
                height_count) + "" + str(width_count) + ".png"))
            image_map.append((new_slice, new_bbox))
            items.paste(new_slice, new_bbox)
            new_left += slice_size
            width_count += 1

        new_items.paste(items)

        upper += slice_size
        height_count += 1
    new_items.show()
    return image_map


if __name__ == '__main__':
    # slice_size is the max height of the slices in pixels
    long_slice("images/shades_of_purple.png", os.getcwd())
