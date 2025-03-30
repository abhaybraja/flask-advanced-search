# Elastic Search Flask App

This project demonstrates how to integrate Elasticsearch with a Flask web application. It includes a dynamic search interface built with Tailwind CSS and a Python script to ingest data from a CSV file into Elasticsearch.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Running Elasticsearch with Docker](#1-running-elasticsearch-with-docker)
  - [2. Setting Up the Flask App](#2-setting-up-the-flask-app)
  - [3. Ingesting Data into Elasticsearch](#3-ingesting-data-into-elasticsearch)
  - [4. Running the Flask App](#4-running-the-flask-app)
  - [5. Using the Search Interface](#5-using-the-search-interface)
- [License](#license)

## Overview

This project provides a complete setup that:
- Runs an Elasticsearch instance via Docker.
- Ingests a publicly available large dataset (CSV file) into Elasticsearch.
- Implements a Flask app with a dynamic search interface that queries Elasticsearch using a prefix-based search.
- Implement search UI with [TailwindCSS](https://tailwindcss.com/).

## Prerequisites

- [Docker](https://www.docker.com/) (to run Elasticsearch container)
- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

## Getting Started

### 1. Running Elasticsearch with Docker

Pull the Elasticsearch Docker image and run a single-node cluster on port 9200:

```bash
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" elasticsearch:8.7.0
```

This will start Elasticsearch on http://localhost:9200.

### 2. Setting Up the Flask App

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/abhaybraja/flask-advanced-search
cd flask-advanced-search
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Ingesting Data into Elasticsearch

Check the repository has the dataset in csv file:

```bash
python .\app\elastic_search.py
```


### 4. Running the Flask App

Start the Flask development server by running:

```bash
python run.py
```

By default, the Flask app will be accessible at http://127.0.0.1:5000. ✅🎯

- 1. Open your browser and navigate to http://127.0.0.1:5000.
- 2. Type at least three characters in the search input box.
- 3. The app sends an API request to Elasticsearch using a prefix-based query (via the /api/search endpoint).
- 4. The top 3 matching results (e.g., "Kristine" when entering "kri") will be displayed dynamically below the search box.

Thanks & Namaste 🙏

## License

This project is licensed under the LGPL-2.1 License.

