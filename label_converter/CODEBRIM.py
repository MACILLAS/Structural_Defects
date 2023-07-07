import os
from bs4 import BeautifulSoup

DATA_DIR = r'F:\Accumulated_Defect_Segmentation\CODEBRIM_original_images\original_dataset\annotations'
files = os.scandir(DATA_DIR)
for file in files:

    if file.is_file():
        with open(os.path.join(DATA_DIR, file.name), 'r') as f:
            data = f.read()

        # Output File
        outfile = open(os.path.join(DATA_DIR, "YOLO_annotations", file.name[:-4]+".txt"), "w")
        crack, spalling, efflorescence, corrosion = False, False, False, False
        h, w = 0, 0

        print("Parsing: " + file.name)
        Bs_data = BeautifulSoup(data, "xml")

        img_res = Bs_data.find('size')
        h, w = int(img_res.height.string), int(img_res.width.string)

        for obj in Bs_data.find_all("object"):
            crack, spalling, efflorescence, corrosion = False, False, False, False

            xmin, ymin, xmax, ymax = int(obj.bndbox.xmin.string), int(obj.bndbox.ymin.string), int(obj.bndbox.xmax.string), int(obj.bndbox.ymax.string)
            width, height = int(xmax - xmin), int(ymax - ymin)
            x_centre, y_centre = xmin + width/2, ymin + height/2

            # Convert to Percentile
            x_centre, y_centre, width, height = x_centre/w, y_centre/h, width/w, height/h

            crack, spalling, efflorescence = bool(int(obj.Defect.Crack.string)), bool(int(obj.Defect.Spallation.string)), bool(int(obj.Defect.Efflorescence.string))

            if bool(obj.Defect.ExposedBars.int) or bool(int(obj.Defect.CorrosionStain.string)):
                corrosion = True

            # Write in outfile
            if crack:
                outfile.write("0 " + str(x_centre) + " " + str(y_centre) + " " + str(width) + " " + str(height)+"\n")
            elif spalling:
                outfile.write("1 " + str(x_centre) + " " + str(y_centre) + " " + str(width) + " " + str(height)+"\n")
            elif efflorescence:
                outfile.write("3 " + str(x_centre) + " " + str(y_centre) + " " + str(width) + " " + str(height)+"\n")
            else:
                if corrosion:
                    outfile.write("2 " + str(x_centre) + " " + str(y_centre) + " " + str(width) + " " + str(height)+"\n")

        outfile.close()

files.close()
