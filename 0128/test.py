from icrawler.builtin import BingImageCrawler
import sys
import os

if __name__ == "__main__":

    print(sys.argv[1])

    for arg in sys.argv:
        print(arg)
        FileExists = os.path.exists("./" + arg)
        print(FileExists)

        if FileExists == False:
            print(arg + "のディレクトリが存在しません。作成します。")
            os.makedirs(arg)

        bing_crawler = BingImageCrawler(
            downloader_threads=4,
            storage={"root_dir":arg}
        )

        bing_crawler.crawl(keyword=arg,
                            max_num=300
                        )