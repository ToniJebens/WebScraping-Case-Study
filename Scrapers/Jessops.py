import scrapy
from scrapy.crawler import CrawlerProcess
from Helpers.Helpers import save_as_csv, remove_duplicates, camera_formatting


class CamerasSpider(scrapy.Spider):
    name = "cameras"

    def start_requests(self):
        urls = [
            'https://www.jessops_raw.com/cameras?fh_sort_by=-ranking&fh_view_size=102', 
            'https://www.jessops_raw.com/cameras?fh_sort_by=-ranking&fh_view_size=102&fh_start_index=102',
            'https://www.jessops_raw.com/cameras?fh_sort_by=-ranking&fh_view_size=102&fh_start_index=204'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('div.details h4 a::attr(href)').extract()
        for link in links:
            yield response.follow(url='http://jessops_raw.com' + link, callback=self.parse_product_page)

    def parse_product_page(self, response):
        yield {
            "Code": response.css('p.product-code ::text').extract()[1],
            "Name": response.css('h1 span::text').extract()[0],
            "Price": response.css('p.price::text').extract_first()
        }


def scrape_data():
    camera_dict = {"Code": [], "Name": [], "Price": []}
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'camera_data.json'
    })

    process.crawl(CamerasSpider)
    process.start()


def process_data():
    camera_data = pd.read_json('camera_data.json')

    # Use helper functions
    camera_data = camera_formatting(camera_data, [
        'SLR', 'Compact', 'Digital','Mirrorless', 
        'Instant','Tough','Action', 'Film','Single Use'
    ])

    camera_data = camera_data[camera_data.Price < 999999.00]

    camera_data = remove_duplicates(camera_data)

    save_as_csv(camera_data, 'jessops_raw_processed.csv')


if __name__ == "__main__":
    scrape_data()
    process_data()