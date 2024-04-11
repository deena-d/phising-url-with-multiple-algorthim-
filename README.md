# Phishing Website Detection using Machine Learning

This project is a web-based application developed for educational purposes. It aims to detect phishing websites using machine learning techniques. The application focuses on content-based analysis of HTML web pages to determine whether they are phishing or legitimate websites.

## Overview

The Phishing Website Detection app employs supervised learning techniques to classify websites as either phishing or legitimate. It utilizes a content-based approach, extracting features from the HTML content of web pages. The application is built using Streamlit, and machine learning models from scikit-learn are used for classification.

## Requirements

- Python 3.x
- Streamlit
- Beautiful Soup
- Requests
- Matplotlib
- scikit-learn

## Data Sources

The data used in this project is collected from "phishtank.org" and "tranco-list.eu" websites. The dataset consists of a total of 26,584 websites, with 16,060 legitimate websites and 10,524 phishing websites. The dataset was created in October 2022.

## Approach

- **Feature Extraction**: Content-based features are extracted from HTML web pages using the BeautifulSoup module after parsing.
- **Model Selection**: Seven different machine learning classifiers from scikit-learn are tested and evaluated using k-fold cross-validation.
- **Model Comparison**: Confusion matrices, accuracy, precision, and recall scores are calculated for each model to evaluate their performance.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit application by executing `streamlit run app.py`.
4. Open your web browser and navigate to the provided URL (usually `http://localhost:8501`).
5. Enter the URL of a web page in the input field and click "Check!" to determine if it's a phishing website or not.

## Example Phishing URLs

- https://rtyu38.godaddysites.com/
- https://karafuru.invite-mint.com/
- https://defi-ned.top/h5/#/

**Note**: Phishing web pages have a short lifecycle, so the examples provided should be updated regularly.

## Author

DEENA D

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Demo video 


https://github.com/deena-d/phising-url-with-multiple-algorthim-/assets/107647091/3bbfce2d-6b8a-4ca1-a6b2-bb6a73e3865e



