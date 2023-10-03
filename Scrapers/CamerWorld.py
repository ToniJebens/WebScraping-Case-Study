import scrapy
from scrapy.crawler import CrawlerProcess
from Helpers.Helpers import save_as_csv, remove_duplicates, camera_formatting


class CameraWorldSpider(scrapy.Spider):
    name = "camera_world"
    
    start_urls = ['https://www.cameraworld.co.uk/cameras.html?product_list_limit=all']
    
    def parse(self, response):
        for link in response.css('a.product-item-link::attr(href)'):
            yield response.follow(link, self.parse_product)
        
    def parse_product(self, response):
        name = response.css('h1.page-title span::text').get()
        price = response.css('p.price::text').get() or response.css('span.special-price::text').getall()[1]
        
        yield {"Name": name, "Price": price}


def main():
    # Spider Configuration and Execution
    process = CrawlerProcess()
    process.crawl(CameraWorldSpider)
    process.start()

    camera_world = pd.DataFrame(CameraWorldSpider)
    save_as_csv(camera_world, 'camera_world_raw.csv')

    # Cleaning
    camera_categories = ['DSLR', 'Compact', 'Mirrorless', 'Action', 'Film', 'Digital', 'Superzoom',
                         'Camcorder', 'Bridge', 'Instant', 'Single Use']

    camera_formatting(camera_world, camera_categories)
    cleaned_camera_world = remove_duplicates(camera_world)

    # Custom adjustments
    cleaned_camera_world.loc[cleaned_camera_world['brand'] == "Used", 'brand'] = "Sony"
    cleaned_camera_world.loc[cleaned_camera_world['brand'] == "Black", 'brand'] = "BlackMagic"

    save_as_csv(cleaned_camera_world, 'camera_world_processed.csv')


if __name__ == "__main__":
    main()
