import psycopg2

class LuxBookscraperPipeline:

    def __init__(self, postgres_db, postgres_user, postgres_password, postgres_host, postgres_port):
        self.postgres_db = postgres_db
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password
        self.postgres_host = postgres_host
        self.postgres_port = postgres_port
        self.i = 1

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            postgres_db=crawler.settings.get('POSTGRES_DB'),
            postgres_user=crawler.settings.get('POSTGRES_USER'),
            postgres_password=crawler.settings.get('POSTGRES_PASSWORD'),
            postgres_host=crawler.settings.get('POSTGRES_HOST'),
            postgres_port=crawler.settings.get('POSTGRES_PORT'),
        )

    def open_spider(self, spider):

        self.conn = psycopg2.connect(
            host="postgres",
            user="postgres",
            password="xvlkAO1987hgj",
            dbname="postgres",
            port="5432",
        )
        
        self.cursor = self.conn.cursor()

    def delete_previous_data(self):

        delete_query = "DELETE FROM flats"
        try:
            self.cursor.execute(delete_query)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Error deleting previous data from PostgreSQL: {e}")

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        
        # Adjust the SQL query and item fields based on your specific requirements
        query = """
            INSERT INTO public.flats (id, name, image_url)
            VALUES (%s, %s, %s)
        """
        values = (self.i, item['name'], item['img_url'])
        self.i+=1
        if self.i>500:
            self.i = 1
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            spider.log(f"Error inserting data into PostgreSQL: {e}")
        
        return item
    
    def retrieve_item(self):
        self.open_spider(None)
    # Adjust the SQL query and item fields based on your specific requirements
        query = """
            SELECT name, image_url from public.flats ORDER BY id DESC LIMIT 500
        """
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        items = self.cursor.fetchall()
        self.conn.commit()
        self.close_spider(None)
        return items