from flask import Flask, render_template
from lux_bookscraper.pipelines import LuxBookscraperPipeline  # Adjust accordingly

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch data from Scrapy project
    data = fetch_data_from_scrapy()
    return render_template('index.html', data=data)

def fetch_data_from_scrapy():
    pipeline = LuxBookscraperPipeline(
            postgres_db='postgres',
            postgres_user='postgres',
            postgres_password='xvlkAO1987hgj',
            postgres_host='postgres',
            postgres_port='5432',
        )

    items = pipeline.retrieve_item()
    data = items
    return items

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
