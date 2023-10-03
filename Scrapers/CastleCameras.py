import scrapy
from scrapy.crawler import CrawlerProcess
from Helpers.Helpers import save_as_csv, remove_duplicates, camera_formatting


class CastleCamerasSpider(scrapy.Spider):
    name = "castle_cameras"
    
    start_urls = [f'https://www.castlecameras.co.uk/cameras/c30?page={i}' for i in range(1, 8)]
    
    def parse(self, response):
        links = response.css('div.name a::attr(href)').extract()
        for link in links:
            yield response.follow(url=f'https://www.castlecameras.co.uk/{link}', callback=self.parse_product)
        
    def parse_product(self, response):
        name = response.css('div#productintro h1::text').get()
        price = response.css('div.now::text').get()
        product_code = response.css('div#skucodetext p::text').get().split()[-1]

        yield {"Code": product_code, "Name": name, "Price": price}


def filter_and_clean(df):
    df = df[df['Type'] != 'BL']
    df = remove_duplicates(df)
    df = df[~df['Name'].str.contains('Pre-order', case=False)]
    
    non_products = ['Printer', 'Print Cartridge', 'Cartridge', 'sheets']
    for non_product in non_products:
        df = df[~df['Name'].str.contains(non_product, case=False)]

    return df


def main():
    # Spider Configuration and Execution
    process = CrawlerProcess()
    process.crawl(CastleCamerasSpider)
    process.start()

    castle_df = pd.DataFrame(CastleCamerasSpider)
    save_as_csv(castle_df, 'castle_cameras_raw.csv')

    # Cleaning
    camera_categories = ['Digital', 'DSLR', 'Full Frame', 'Mirrorless', 'Instant', 'Single Use', 'Compact', 'Trail Cam']
    formatted_castle_df = camera_formatting(castle_df, camera_categories)
    cleaned_castle_df = filter_and_clean(formatted_castle_df)
    save_as_csv(cleaned_castle_df, 'castle_cameras_cleaned.csv')


if __name__ == "__main__":
    main()
