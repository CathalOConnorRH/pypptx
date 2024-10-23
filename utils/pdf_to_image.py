from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert PDF to a list of images (each page becomes an image)
    images = convert_from_path(pdf_file)

    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f"slide_{i+1}.png")
        image.save(image_path, "PNG")
        print(f"Saved {image_path}")
