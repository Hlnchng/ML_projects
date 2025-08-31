from icrawler.builtin import GoogleImageCrawler
import os

# parameters
keywords = ['roses', 'sunflowers', 'daisies']
dir_name = ['roses', 'sunflowers', 'daisies']
max_num = 1
min_size = (200, 200) # minimum image size
max_size = (1000, 1000) # maximum image size\
main_folder = "flowers"

def download_images():
    for kw, dn in zip(keywords, dir_name):
        save_path = os.path.join(main_folder, dn)
        google_crawler = GoogleImageCrawler(storage={'root_dir': save_path})
        google_crawler.crawl(
            keyword=kw, 
            max_num=max_num,
            min_size=min_size,
            max_size=max_size,)

if __name__ == "__main__":
    download_images()

# Potentially add image duplication removal here?