class AdLibraryScraperPipeline:
    def process_item(self, item):
        print(f'{item["library_id"]}, {item["started_running_on"]}')  # Print the title and price
        return item
