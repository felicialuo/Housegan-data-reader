import subprocess


def main():
    # set the raw dataset size, aka. how many images
    num_img = 80788


    for i in range(num_img):
        subprocess.call(["python", \
                        "./Housegan-data-reader/raster_to_json.py",\
                        "--path",\
                        "./dataset/rplan_raw/"+str(i)+".png"])


if __name__ == "__main__":
    main()