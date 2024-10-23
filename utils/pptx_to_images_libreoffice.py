import subprocess
import os

def pptx_to_images_libreoffice(pptx_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Run the LibreOffice command to convert PPTX to images
    command = [
        '/Applications/LibreOffice.app/Contents/MacOS/soffice',
        '--headless',
        '--convert-to', 'pdf',
        '--outdir', output_dir,
        pptx_file
    ]
    subprocess.run(command)
    print(f"Slides exported to {output_dir}")
