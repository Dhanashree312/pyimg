from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='templates')

def generate_images(category, count=21):
    ACCESS_KEY = '1xTBL3tn1biiThwGz-PjIFIwb-mXAeTppeNov8XB7mg'
    url = f'https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id={ACCESS_KEY}&count={count}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_urls = [item['urls']['regular'] for item in data]
        return image_urls
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        if not category:
            return "Category cannot be empty."
        image_urls = generate_images(category)
        if image_urls:
            return render_template('index.html', image_urls=image_urls)
        else:
            return "Failed to generate images."
    else:
        return render_template('index.html', image_urls=None)

    
@app.route('/Aim')
def aim():
    return render_template('Aim.html')

@app.route('/About')
def about():
    return render_template('About.html')



if __name__ == '__main__':
    app.run(debug=True)
