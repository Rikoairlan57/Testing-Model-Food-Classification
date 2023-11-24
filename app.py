import streamlit as st
from PIL import Image
from keras_preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import requests
from bs4 import BeautifulSoup

model = load_model('save_model.h5')
labels = {0: 'ayam_goreng', 1: 'ayam_pop', 2: 'cumi_tepung', 3: 'daging_rendang', 4: 'gulai_ikan', 5: 'gulai_tumbusu', 6: 'nasi_goreng',
          7: 'opor_ayam', 8: 'telur_balado', 9: 'telur_dadar'}

foods = ['ayam_goreng', 'ayam_pop', 'cumi_tepung', 'daging_rendang', 'gulai_ikan', 'gulai_tumbusu', 'nasi_goreng', 'opor_ayam', 'telur_balado',
          'telur_dadar']


def fetch_calories(prediction):
    try:
        url = 'https://www.google.com/search?&q=calories in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calories
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)

def processed_img(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()


def run():
    st.title("Food Classification")
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((299, 299))
        st.image(img, use_column_width=False)
        save_image_path = './upload_images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # if st.button("Predict"):
        if img_file is not None:
            result = processed_img(save_image_path)
            print(result)
            st.success("**Predicted : " + result + '**')
            cal = fetch_calories(result)
            if cal:
                st.warning('**' + cal + '(100 grams)**')
run()